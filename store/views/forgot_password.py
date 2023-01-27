from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from .data import initial_data
from urllib.parse import urlencode, urlparse 
from urllib.parse import  parse_qs
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_otp_email(user_email, otp):
    subject = 'Welcome to Seth Sarees'
    message = render_to_string('otp_email.html', {'otp': otp})
    send_mail(subject, '', 'sethsarees@gmail.com', [user_email], html_message=message)

 
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

class Forgot_Password(View):
    def get(self, request):
        data = initial_data
        email=request.GET.get('email')
        data['customer_email']=email
        data['meta_tags']='Forgot password, reset account, email, phone number, OTP'
        data['meta_description']='Forgot your password? No problem. Enter your email or phone number and we will send you an OTP to verify your identity and reset your account.'
        data['title']='Forgot Password - Reset Your Account'
        return render(request, 'forgot_password.html', data)

    def post(self, request):
        data = initial_data
        email = request.POST.get('customer_email')
        customer = Customer.get_customer_by_email(email) or Customer.get_customer_by_phone_number(email)
        is_error=''
        if customer:
            url='/forgot-password'
            url=modify_url(url,'hidden_email',hide_email(customer.email))
            url=modify_url(url,'email',email)
            customer_id=customer.id
            link =str(request.build_absolute_uri('/'))
            link=link+'change_password?customer_id='+str(customer.id)+'&customer_verification_token='+customer.verification_token            
            phone_number='+'+customer.country_code+customer.phone_number
            url=modify_url(url,'customer_id',customer.id)
            send_otp_email(customer.email,customer.verification_token)
            return redirect(modify_url(url,'forgot_password_is_error','Success'))
        else:
            url='/forgot-password'
            url=modify_url(url,'email',email)
            return redirect(modify_url(url,'forgot_password_is_error','Error'))