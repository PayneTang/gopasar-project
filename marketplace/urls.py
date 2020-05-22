from django.urls import path, include
from .api import get_products, create_product

urlpatterns = [
    path('products', get_products),
    path('product', create_product),
]
