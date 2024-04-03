
from django.urls import path

from . import views

urlpatterns = [
    # Main Page

    path('', views.store, name='store'),

    #Individual Product

    path('product/<slug:slug>/', views.product_info, name='product-info'),

    #Individual Category

    path('search/<slug:category_slug>/', views.list_category, name='list-category'),

]