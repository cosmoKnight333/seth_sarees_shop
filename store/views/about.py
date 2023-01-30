from django.shortcuts import render
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from .data import initial_data

def show_about(request):
    data = initial_data
    error_msg=None
    error_msg = request.GET.get('error_msg')
    data['error_msg'] = error_msg
    customer_id = request.session.get('customer')
    data['wishlist_len']=0
    if customer_id:
        customer = Customer.objects.get(id=customer_id)
        wishlist_len = len(Wishlist.objects.filter(customer=customer_id))
        data['wishlist_len'] = wishlist_len
   
    data['meta_description']='Discover the beauty and craftsmanship of traditional Banarasi sarees at our store in the historic chauk area of Varanasi. Our collection features a wide range of luxurious and unique sarees to suit all tastes and budgets. Our team of knowledgeable and friendly staff are always on hand to assist customers. Follow us on social media or sign up for our email list for special discounts and promotions. Visit Seth Sarees showroom or shop online now.'
    data['meta_tags']='Seth Sarees,Banarasi sarees,silk sarees, Varanasi, finest quality, luxurious, unique, traditional, hand-woven silk, modern printed styles, wholesaler, retailer, showroom, knowledgeable staff, excellent customer service, social media, email list, special discounts, promotions'
    data['title']="About Seth Sarees Shop - Trusted Silk and Banarasi Saree Wholesaler and Retailer in Varanasi Since 1993"
    return render(request, 'about.html', data)
