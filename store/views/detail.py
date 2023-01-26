from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from .data import initial_data

class Detail(View):
    def get(self, request):
        data = initial_data
        customer_id = request.session.get('customer')
        data['wishlist_len']=0
        if customer_id:
            customer = Customer.objects.get(id=customer_id)
            data['wishlist_len'] = len(Wishlist.objects.filter(customer=customer_id))
        error_msg=None
        error_msg = request.GET.get('error_msg')
        data['error_msg'] = error_msg

        product_id = request.GET.get('product') 
        product_obj=Product.get_product_by_id(product_id)
        product_obj.in_wishlist = len(Wishlist.objects.filter(customer=customer_id, product=product_obj)) > 0
        data['product_obj'] = product_obj
        products = Product.get_all_products_by_categoryid_random(product_obj.category.id,product_id)
        for product in products:
            product.in_wishlist = len(Wishlist.objects.filter(customer=customer_id, product=product)) > 0
        for product in products:
                print(product.in_wishlist,' abe hai kya')
        data['products']=products
        
        data['title']=product_obj.meta_title
        data['meta_description']=product_obj.meta_description
        data['meta_tags']=product_obj.meta_tags

        return render(request, 'detail.html', data)
    
    def post(self, request):
        print(request.build_absolute_uri)
        return redirect('detail')