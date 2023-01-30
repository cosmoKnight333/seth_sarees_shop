from django.contrib.sitemaps import Sitemap
from store.models.category import Category
from store.models.product import Product
from django.urls import reverse
from store.models.contact import Contact

class CategorySitemap(Sitemap):
    changefreq='weekly'
    priority=0.85
    def items(self):
        return Category.objects.all()
class ProductSitemap(Sitemap):
    changefreq='weekly'
    priority=0.70
    def items(self):
        return Product.objects.all()

class AboutSitemap(Sitemap):
    changefreq='weekly'
    priority=0.75
    def items(self):
        return ['about']
    def location(self, item):
        return reverse(item)
    
class IndexSitemap(Sitemap):
    changefreq='weekly'
    priority=1 
    def items(self):
        return ['']
    def location(self, item):
        return (item)

class ContactSitemap(Sitemap):
    changefreq='weekly'
    priority=0.51

    def items(self):
        return ['contact']
    def location(self, item):
        return reverse(item)

class PrivacyPolicySitemap(Sitemap):
    def items(self):
        return ['privacy_policy']
    def location(self, item):
        return reverse(item)
    
class SupportSitemap(Sitemap):
    changefreq='weekly'
    priority=0.75
    def items(self):
        return ['support']
    def location(self, item):
        return reverse(item)