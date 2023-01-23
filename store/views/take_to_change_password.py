from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from store.models.contact import Contact
from store.models.wishlist import Wishlist
from .data import initial_data
from urllib.parse import urlencode, urlparse 
from urllib.parse import  parse_qs
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.urls import reverse
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
import os
import urllib



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

def hide_email(email):
    email_parts = email.split("@")
    email_name = email_parts[0]
    email_domain = email_parts[1]
    if len(email_name) > 4:
        email_name = email_name[0:2] + "***" + email_name[-2:]
    else:
        email_name = email_name[0] + "***"

    hidden_email = email_name + "@" + email_domain
    return hidden_email

class Take_To_Change_Password(View):
    def post(self, request):
        data = initial_data
        email = request.POST.get('customer_email')
        customer_id = request.POST.get('customer_id')
        otp = request.POST.get('otp')
        customer = Customer.objects.get(id=request.POST.get('customer_id'))
        print(type(otp),type(customer.verification_token))
        if customer.verification_token==otp:
            url='/change_password?customer_id='+str(customer.id)+'&customer_verification_token'+customer.verification_token
            return redirect(url)
        else:
            url='/forgot-password'
            url=modify_url(url,'email',email)
            url=modify_url(url,'customer_id',customer.id)
            url=modify_url(url,'hidden_email',hide_email(customer.email))
            return redirect(modify_url(url,'wrong_otp_error','Error'))