from django.urls import path, include
from .api import ProductListAPI, ProductDetailAPI, CreateProductAPI

urlpatterns = [
    path('products/', ProductListAPI.as_view()),
    path('product/<str:pk>', ProductDetailAPI.as_view()),
    path('product/', CreateProductAPI.as_view()),
]
