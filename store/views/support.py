from django.shortcuts import render
from django.views import View
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from store.models.faqs import Faqs
from .data import initial_data

def show_support(request):
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
    data['title']="Saree Shopping Support - Schedule Video Calls, Create Wishlists, In-Store Assistance & More"
    data['meta_description']='We are here to help you find the perfect saree for your occasion. You can schedule a video call with one of our reps through our website, visit our store in person or create a wishlist on our website to find the perfect sarees. If you need assistance, you can call us and one of our reps will be happy to help you out. Our store also provides a custom color and border feature for our sarees.'
    data['meta_tags']='Support, find perfect saree, occasion, video call, reps, website, visit store, wishlist, assistance, custom color, border feature'
    return render(request, 'support.html', data)
