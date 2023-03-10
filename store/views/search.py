from django.http import HttpResponse
from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from django.db.models import Q
from .data import initial_data
from fuzzywuzzy import process
from django.http import JsonResponse
def search(request):
    data = initial_data
    customer_id = request.session.get('customer')
    wishlist_len = 0
    data['wishlist_len'] = 0

    if customer_id:
        customer = Customer.objects.get(id=customer_id)
        wishlist_len = len(Wishlist.objects.filter(customer=customer_id))
    data['wishlist_len'] = wishlist_len
    error_msg = None
    error_msg = request.GET.get('error_msg')
    data['error_msg'] = error_msg

    query = request.GET['search']
    categories = Category.get_all_categories()

    # find the closest string matches for the query in the 'name' field of products
    product_names = Product.objects.values_list('name', flat=True)
    product_name_matches = process.extractBests(query, product_names, score_cutoff=85, limit=10)
    product_names = [match[0] for match in product_name_matches]

    # find the closest string matches for the query in the 'name' field of categories
    category_names = Category.objects.values_list('name', flat=True)
    category_name_matches = process.extractBests(query, category_names, score_cutoff=85, limit=10)
    category_names = [match[0] for match in category_name_matches]

    products = Product.objects.filter(name__in=product_names)
    categories = Category.objects.filter(name__in=category_names)

    # calculate the number of similar words between the query and the name of each product and category
    for product in products:
        product.similarity_score = len(set(product.name.lower().split()) & set(query.lower().split()))
    for category in categories:
        category.similarity_score = len(set(category.name.lower().split()) & set(query.lower().split()))

    # sort the products and categories based on the number of similar words in descending order
    products = sorted(products, key=lambda p: p.similarity_score, reverse=True)
    categories = sorted(categories, key=lambda c: c.similarity_score, reverse=True)

    data['query'] =  query
    data['categories'] = Category.get_all_categories()
    data['products'] = products
    data['meta_description']='Find the perfect saree from our extensive collection of traditional Banarasi sarees at our store in the historic chauk area of Varanasi. Seth Sarees collection features a wide range of luxurious and unique sarees to suit all tastes and budgets including traditional hand-woven silk and more modern printed styles. Our showroom is elegantly adorned with an array of stunning options and our team of knowledgeable and friendly staff are always on hand to assist customers in finding the perfect saree for any occasion. Follow us on social media or sign up  special discounts and promotions. Visit our store today!'
    data['meta_tags']='Seth Sarees,Search, results, sarees, Banarasi, Varanasi, traditional, luxurious, unique, hand-woven silk, modern printed styles, wholesaler, retailer, showroom, knowledgeable staff, excellent customer service, social media, email list, special discounts, promotions'
    data['title']="Search Sarees - Results for '"+ query+"'"
    for product in products:
        product.in_wishlist = len(Wishlist.objects.filter(customer=customer_id, product=product)) > 0

    return render(request, 'search.html', data)


def search_suggestions(request):
    search_term = request.GET.get('search', '')
    if(search_term):
        products = Product.objects.filter(name__icontains=search_term)
        categoreis = Category.objects.filter(name__icontains=search_term)
        product_names=[]
        for category in categoreis:
            product_names.append(category.name)
        for product in products:
            product_names.append(product.name)
        return JsonResponse({'suggestions': product_names[:6]})
    else:
        return JsonResponse({'suggestions': []})