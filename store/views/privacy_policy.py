from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from store.models.faqs import Faqs
from .data import initial_data

def show_privacy_policy(request):
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
    faqs=Faqs.objects.all()
    data['faqs']=faqs
    data['title']="Terms and Conditions and Privacy Policy for Seth Sarees"

    return render(request, 'privacy_policy.html', data)
