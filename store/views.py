from django.shortcuts import render
from . models import *
from django.contrib import  messages

# Create your views here.
def home(request):
    category = Category.objects.filter(status=0)
    trendy_collections = Product.objects.filter(trending=1)
    context = {'category':category,'trendy_collections':trendy_collections}
    return render(request,'store/home.html',context)

def products(request):
    products = Product.objects.filter(status=0)
    context = {'products':products}
    return render(request,"store/products/home.html",context)

def aboutus(request):
    return render(request,"store/aboutus.html")

def contactus(request):
    return render(request,"store/contactus.html")

def register(request):
    return render(request,"store/auth/register.html")


def productview(request,cate_slug,prod_slug):
    if Category.objects.filter(slug=cate_slug,status = 0).exists():
        if Product.objects.filter(slug=prod_slug,status=0).exists():
            products=Product.objects.filter(slug=prod_slug,status=0).first()
            context={'products':products}
        else:
            messages.error(request,"No such product found")
            return redirect("collections")
    else:
        messages.error(request,"No such category found")
        return redirect('collections')
    return render(request,"store/products/view.html",context)