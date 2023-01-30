from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='',upload_to='uploads/category_img/')
    description = models.TextField( default='' , null=True , blank=True)
    alt_text = models.CharField(max_length=100, default='', null=True, blank=True)
    meta_title = models.CharField(max_length=255, default='', null=True, blank=True) 
    meta_tags = models.CharField(max_length=255, default='', null=True, blank=True) 
    meta_description = models.TextField(default='', null=True, blank=True) 
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    def get_absolute_url(self):
        #/store/category/1/sarees
        return '/store/category/'+str(self.id)+'/sarees'
    
    def __str__(self):
        return self.name