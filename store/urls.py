from django.urls import path
from .views.detail import Detail
from store.views.category import show_category
from store.views.category import store

urlpatterns = [
    path('category/<int:category_id>/sarees', show_category, name='category'),
    path('category/<int:category_id>/sarees/<int:product_id>/detail', Detail.as_view(),name="detail"),
    path('',store,name="store")
]