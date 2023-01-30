from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from .data import initial_data
from urllib.parse import urlencode, urlparse
from urllib.parse import  parse_qs
import random
from django.contrib.auth.hashers import make_password

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

class Change_Password(View):
    def get(self, request):
        data = initial_data
        customer_id = int(request.GET.get('customer_id'))
        customer_verification_token = request.GET.get('customer_verification_token')
        customer = Customer.objects.get(id=customer_id)
        if customer:
            data['customer_id']=customer.id
            data['customer_verification_token']=customer.verification_token
            data['customer_name']=customer.first_name
            data['title']='Change Password - Secure Your Account'
            data['meta_description']='Ensure the security of your account by updating your password. Seth Sares change password page is for verified users to easily update their password for added protection.'
            data['meta_tags']='Change password, secure account, verified user, password'
           
            return render(request, 'change_password.html', data)
        else:
            url='/forgot-password'
            return redirect(modify_url(url,'forgot_password_is_error','Error'))        
        
    def post(self, request):
        data = initial_data
        customer = Customer.objects.get(id=request.POST.get('customer_id'))
        if customer.verification_token ==request.POST.get('customer_verification_token'):
            customer.password=request.POST.get('password')
            customer.password=make_password(customer.password)
            verification_token=random.randint(100000, 999999)
            customer.verification_token=verification_token
            customer.save()
            request.session['customer'] = customer.id
            request.session['customer_first_name'] = customer.first_name
            request.session['customer_last_name'] = customer.last_name
            request.session['customer_phone_number'] = customer.phone_number
            request.session['customer_email'] = customer.email
            request.session['customer_country_code'] = customer.country_code
          
            return redirect('/')
        else :
            url='/forgot-password'
            return redirect(modify_url(url,'forgot_password_is_error','Error'))
        