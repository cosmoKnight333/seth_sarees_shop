"""sethsarees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import CategorySitemap,AboutSitemap,IndexSitemap,ContactSitemap,SupportSitemap,PrivacyPolicySitemap,ProductSitemap
from store.views.home import index,logout
from store.views.category import show_category
from store.views.search import search
from store.views.robots import robots
from store.views.search import search_suggestions
from store.views.about import show_about
from store.views.support import show_support
from store.views.privacy_policy import show_privacy_policy
from store.views.contact import Contact_Page
from store.views.forgot_password import Forgot_Password
from store.views.change_password import Change_Password
from store.views.login import Login
from store.views.signup import Signup
from store.views.change_info import Change_Info
from store.views.detail import Detail
from store.views.addtowishlist import addtowishlist
from store.views.addtowishlist import removeitem
from store.views.wishlist import show_wishlist
from store.views.show_sent_list import show_sent_list
from store.views.take_to_change_password import Take_To_Change_Password

sitemaps={
    '':IndexSitemap,
    'category':CategorySitemap,
    'about':AboutSitemap,
    'contact':ContactSitemap,
    'privacy_policy':PrivacyPolicySitemap,
    'support':SupportSitemap,
    'detail':ProductSitemap   
}
handler404 = 'store.views.error.error_400'
handler500 = 'store.views.error.error_500'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/',include('store.urls')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('robots.txt', robots),
    path('search',search),
    path('search-suggestions',search_suggestions),
    path('wishlist',show_wishlist),
    path('add-to-wishlist',addtowishlist),
    path('about',show_about,name='about'),
    path('',index,name='index'),
    path('privacy-policy',show_privacy_policy,name='privacy_policy'),
    path('support',show_support,name='support'),
    path('about',show_about,name='about'),
    path('contact',Contact_Page.as_view(),name='contact'),
    path('remove-item',removeitem),
    path('contact',Contact_Page.as_view()),
    path('forgot-password',Forgot_Password.as_view()),
    path('change_password',Change_Password.as_view()),
    path('take-to-change-password',Take_To_Change_Password.as_view()),
    path('login',Login.as_view(),name='login'),
    path('signup',Signup.as_view(),name='signup'),
    path('change-info',Change_Info.as_view(),name='change_info'),
    path('show-sent-list',show_sent_list),
    path('logout',logout),
    path('store/category/<int:category_id>/sarees', show_category, name='category'),
    path('store/category/<int:category_id>/sarees/<int:product_id>/detail', Detail.as_view(),name="detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

