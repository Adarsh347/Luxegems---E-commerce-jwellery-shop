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
]