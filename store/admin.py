from django.contrib import admin
from .models import Category, Product,Wishlist,Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)