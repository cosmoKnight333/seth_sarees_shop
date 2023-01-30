from django.db import models
from .category import Category
import random

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField( default='' , null=True , blank=True)
    short_description= models.TextField( default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    image1 = models.ImageField(upload_to='uploads/products/')
    image2 = models.ImageField(upload_to='uploads/products/')
    alt_text1 = models.CharField(max_length=100, default='', null=True, blank=True)
    alt_text2 = models.CharField(max_length=100, default='', null=True, blank=True)
    alt_text3 = models.CharField(max_length=100, default='', null=True, blank=True)
    meta_title = models.CharField(max_length=255, default='', null=True, blank=True) 
    meta_tags = models.CharField(max_length=255, default='', null=True, blank=True) 
    meta_description = models.TextField(default='', null=True, blank=True) 
    def __str__(self):
        return self.name 
    def get_absolute_url(self):
        return '/'+str(self.category.id)+'/'+str(self.id)+''
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_product_by_id(id):
        return Product.objects.get(id=id)
        

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid_random(category_id, product_id):
        if category_id:
            items = Product.objects.filter(category=category_id).exclude(id=product_id)
            return random.sample(list(items), min(10, len(items)))
        else:
            Product.objects.exclude(id=product_id)
