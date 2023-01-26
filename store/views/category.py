
from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from .data import initial_data

def show_category(request):
    data = initial_data
    customer_id = request.session.get('customer')
    data['wishlist_len']=0
    if customer_id:
        customer = Customer.objects.get(id=customer_id)
        data['wishlist_len'] = len(Wishlist.objects.filter(customer=customer_id))
    error_msg=''
    error_msg = request.GET.get('error_msg')
    data['error_msg'] = error_msg

    category_id = request.GET.get('category')
    if category_id:
        products=Product.get_all_products_by_categoryid(category_id)
        category_obj=Category.objects.get(pk=category_id)
        data['category_obj'] = category_obj
        data['title']=category_obj.meta_title
        data['meta_description']=category_obj.meta_description
        data['meta_tags']=category_obj.meta_tags
        data['products'] = products

    else:
        data['title']="Saree Collection - Explore Our Extensive Range of Luxurious Silk and Banarasi Sarees - Wholesale and Retail"
        data['meta_description']='Discover a wide range of luxurious and unique Silk and Banarasi Sarees in Varanasi at wholesale and retail prices. Visit our showroom or shop online now.'
        data['meta_tags']='Banarasi Sarees, Silk Sarees, Varanasi, Wholesale, Retail,Silk,Saree'
        products = Product.get_all_products()
        data['categories'] = Category.get_all_categories()
    
    for product in products:
            product.in_wishlist = len(Wishlist.objects.filter(customer=customer_id, product=product)) > 0
    for product in products:
            print(product.in_wishlist,' abe hai kya')
    data['products']=products
    return render(request, 'category.html', data)