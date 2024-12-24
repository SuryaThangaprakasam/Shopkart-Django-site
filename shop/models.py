from django.db import models
from django.contrib.auth.models import User

import datetime
import os

def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_filename = '%s%s' %(now_time,filename)
    return os.path.join('uploads', new_filename)

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)     #getFileName is a function
    description = models.TextField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-Show, 1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    # class Meta:
    #     db_table = 'category'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=True)
    vendor = models.CharField(max_length=100, null=False, blank=True)
    product_image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description = models.TextField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-Show, 1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-Trending, 1-no")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    # class Meta:
    #     db_table = 'product'

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.user.username,self.product.name

    @property
    def total_price(self):
        return self.product_qty * self.product.selling_price
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)