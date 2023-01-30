from django.shortcuts import render,redirect
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from .data import initial_data 
from urllib.parse import urlencode, urlparse
from urllib.parse import  parse_qs

def modify_url(url, param, value):
    # Parse the URL and retrieve the query string
    parsed_url = urlparse(url)
    query_dict = parse_qs(parsed_url.query)
    
    # Update the value of the parameter in the query string
    query_dict[param] = value
    
    # Rebuild the URL with the updated query string
    new_query_string = urlencode(query_dict, doseq=True)
    modified_url = parsed_url._replace(query=new_query_string).geturl()
    
    return modified_url
def show_wishlist(request):
    data=initial_data
    customer_id=request.session.get('customer')
    if(customer_id):
        customer=Customer.objects.get(id=customer_id)
        wishlist=Wishlist.objects.filter(customer=customer_id)
        wishlist_len=len(wishlist)
        data['wishlist']=wishlist
        data['customer_name']=customer.first_name+' '+customer.last_name
        data['wishlist_len']=wishlist_len
        data['title']="My Wishlist - Favorite Silk and Banarasi Sarees from Seth Sarees"
        data['meta_description']='Keep track of your favorite sarees from our collection of traditional Banarasi sarees in Varanasi. Create and manage your own wishlist for easy access and future reference.'
        data['meta_tags']='Wishlist, save favorite sarees, user, Banarasi sarees, silk sarees, printed sarees, Varanasi'

        return render(request,'wishlist.html',data)
    else :
        url = request.GET.get('next', '/')
        url=modify_url(url,'error_msg','')
        url=modify_url(url,'signup_error_msg','')
        url=modify_url(url,'change_info_error_msg','')

        error_msg=None
        error_msg='Get access to your wishlist - Login Now!'
        return redirect(modify_url(url,'error_msg',error_msg))
   
