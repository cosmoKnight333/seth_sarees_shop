from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views import View
from store.models.product import Product
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from urllib.parse import urlencode, urlparse, parse_qs

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

def addtowishlist(request):
    customer_id=request.session.get('customer')
    next = request.POST.get('next', '/')
    modify_url(next,'change_info_error_msg','')
    next=modify_url(next,'is_in_wishlist','')

    if customer_id:
        product_id=request.POST.get('product')
        wishlist_len=len(Wishlist.objects.filter(customer=customer_id))
        product=Product.objects.get(id=product_id)
        customer=Customer.objects.get(id=customer_id)
        flag=len(Wishlist.objects.filter(customer=customer_id).filter(product=product_id))
        if flag==0:
            wishlist=Wishlist(customer=customer,
                            product=product)
            wishlist.save()
            return redirect(next)
        else :
            modify_url(next,'change_info_error_msg','')
            print("its in wishlist")
            next=modify_url(next,'is_in_wishlist',str(product.id))
            print(next)
            return redirect(next)

    else :
        modify_url(next,'change_info_error_msg','')
        
        error_msg='Add products to your wishlist - Login Now!'
        return redirect(modify_url(next, 'error_msg', error_msg))
        
        

def removeitem(request):
    customer_id=request.session.get('customer')
    next = request.POST.get('next', '/')
    next=modify_url(next,'is_in_wishlist','')
    product_id=request.POST.get('product')
    customer_id=request.session.get('customer')
    customer=Customer.objects.get(id=customer_id)
    wishlist_len=len(Wishlist.objects.filter(customer=customer_id))
    instance=Wishlist.objects.filter(customer=customer_id).filter(product=product_id)
    instance.delete()
    return HttpResponseRedirect(next)

    