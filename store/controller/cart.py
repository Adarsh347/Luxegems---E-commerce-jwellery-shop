from django.shortcuts import render,redirect
from django.contrib import  messages
from store.models import Product,Cart
from django.http import JsonResponse


def index(request):
    cart_items = []
    total = 0
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            item.subtotal = item.product.selling_price * item.product_qty
        total = sum(item.subtotal for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request,'store/cart.html', context)

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            product_id = request.POST.get('product_id')
            product_qty = request.POST.get('product_qty')
            try:
                product_check = Product.objects.get(id=int(product_id))
            except (Product.DoesNotExist, ValueError, TypeError):
                return JsonResponse({'status': 'No such product found'})

            if Cart.objects.filter(user=request.user, product_id=product_check.id).exists():
                return JsonResponse({'status': 'Product already in cart'})

            qty = 1
            try:
                qty = int(product_qty)
            except (TypeError, ValueError):
                qty = 1

            if qty <= 0:
                qty = 1

            if qty > product_check.quantity:
                return JsonResponse({'status': f'Only {product_check.quantity} quantity available'})

            Cart.objects.create(user=request.user, product=product_check, product_qty=qty)
            return JsonResponse({'status': 'Product added to cart'})
        else:
            return JsonResponse({'status': 'Login to continue'})
    return redirect('/')


def update_cart(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'Login to continue'})

        cart_ids = request.POST.getlist('cart_id[]')
        qtys = request.POST.getlist('qty[]')
        for cid, q in zip(cart_ids, qtys):
            try:
                cart_obj = Cart.objects.get(id=int(cid), user=request.user)
                qty = int(q)
            except (Cart.DoesNotExist, ValueError, TypeError):
                continue

            if qty <= 0:
                qty = 1
            if qty > cart_obj.product.quantity:
                qty = cart_obj.product.quantity

            cart_obj.product_qty = qty
            cart_obj.save()

        return JsonResponse({'status': 'Cart updated'})
    return JsonResponse({'status': 'Invalid request'})


def delete_cart_item(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'Login to continue'})

        cart_id = request.POST.get('cart_id')
        try:
            cart_obj = Cart.objects.get(id=int(cart_id), user=request.user)
            cart_obj.delete()
            return JsonResponse({'status': 'Item removed'})
        except (Cart.DoesNotExist, ValueError, TypeError):
            return JsonResponse({'status': 'Item not found'})
    return JsonResponse({'status': 'Invalid request'})