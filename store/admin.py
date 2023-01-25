from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.corousel import Corousel
from .models.banarasphoto import BanarasPhoto
from .models.customer import Customer
from .models.contact import Contact
from .models.review import Review
from .models.wishlist import Wishlist
from .models.faqs import Faqs

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','meta_tags','meta_description']

class AdminCorousel(admin.ModelAdmin):
    list_display = ['name','heading','subheading']
class AdminWishlist(admin.ModelAdmin):
    list_display = ['customer','product']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name','meta_tags','meta_title','alt_text']
class AdminFaws(admin.ModelAdmin):
    list_display = ['question']
    
class AdminProduct(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone_number','email']

class AdminBanarasPhoto(admin.ModelAdmin):
    list_display = ['name']

class AdminContact(admin.ModelAdmin):
    list_display = ['name','subject','message']

class AdminReview(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Corousel,AdminCorousel)
admin.site.register(BanarasPhoto,AdminBanarasPhoto)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Contact,AdminContact)
admin.site.register(Review)
admin.site.register(Wishlist,AdminWishlist)
admin.site.register(Faqs)

