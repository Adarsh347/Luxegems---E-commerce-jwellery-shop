from django.urls import path
from .import views
from store.controller import authview,wishlist,cart

urlpatterns = [
    path('',views.home,name='home'),
    path('products',views.products,name='products'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('wishlist',wishlist.index,name='wishlist'),
    path('cart',cart.index,name='cart'),

    path('login/',authview.loginpage,name='loginpage'),
    path('register',authview.register,name='register'),
    path('logout/',authview.logoutpage,name='logoutpage'),

    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),

    path('add-to-cart',cart.addtocart,name='/add-to-cart'),
    path('add-to-wishlist',wishlist.addtowishlist,name='add-to-wishlist'),
    path('update-cart', cart.update_cart, name='update-cart'),
    path('delete-cart-item', cart.delete_cart_item, name='delete-cart-item'),

    path('delete-wishlist-item', wishlist.delete_wishlist_item, name='delete_wishlist_item'),

]