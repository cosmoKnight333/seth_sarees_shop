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
from store.views.category import show_category
from store.views.about import show_about
from store.views.home import index
from store.views.support import show_support
from store.views.privacy_policy import show_privacy_policy
from store.views.contact import Contact_Page
from store.views.detail import Detail
from store.views.robots import robots

sitemaps={
    '':IndexSitemap,
    'category':CategorySitemap,
    'about':AboutSitemap,
    'contact':ContactSitemap,
    'privacy_policy':PrivacyPolicySitemap,
    'support':SupportSitemap,
    'detail':ProductSitemap
    
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('<int:category_id>/',show_category,name='category'),
    path('about',show_about,name='about'),
    path('',index,name='index'),
    path('privacy_policy',show_privacy_policy,name='privacy_policy'),
    path('support',show_support,name='support'),
    path('about',show_about,name='about'),
    path('contact',Contact_Page.as_view(),name='contact'),
    path('<int:category_id>/<int:product_id>/', Detail.as_view(),name="detail"),
    path('robots.txt', robots),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

