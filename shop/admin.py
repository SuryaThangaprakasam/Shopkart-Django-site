from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','image','description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','vendor','quantity','original_price','selling_price')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'product_qty')

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Wishlist, WishlistAdmin)