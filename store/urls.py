from django.urls import path
from .views.home import index,logout
from .views.category import show_category
from .views.search import search
from .views.search import search_suggestions
from .views.about import show_about
from .views.support import show_support
from .views.privacy_policy import show_privacy_policy
from .views.contact import Contact_Page
from .views.forgot_password import Forgot_Password
from .views.change_password import Change_Password
from .views.login import Login
from .views.signup import Signup
from .views.change_info import Change_Info
from .views.detail import Detail
from .views.addtowishlist import addtowishlist
from .views.addtowishlist import removeitem
from .views.wishlist import show_wishlist
from .views.show_sent_list import show_sent_list
from .views.take_to_change_password import Take_To_Change_Password


urlpatterns = [
    path('',index,name='homepage'),
    path('category',show_category),
    path('search',search),
    path('search-suggestions',search_suggestions),
    
    path('logout',logout),
    path('wishlist',show_wishlist),
    path('add-to-wishlist',addtowishlist),
    path('remove-item',removeitem),
    path('contact',Contact_Page.as_view()),
    path('forgot-password',Forgot_Password.as_view()),
    path('change_password',Change_Password.as_view()),
    path('take-to-change-password',Take_To_Change_Password.as_view()),
    path('about',show_about),
    path('support',show_support),
    path('privacy_policy',show_privacy_policy),
    path('detail',Detail.as_view(),name="detail"),
    path('login',Login.as_view(),name='login'),
    path('signup',Signup.as_view(),name='signup'),
    path('change_info',Change_Info.as_view(),name='change_info'),
    path('show-sent-list',show_sent_list),

]