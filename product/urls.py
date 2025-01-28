from django.urls import path, include 
from .views import CheapProductView, DiscountedProductView

urlpatterns = [
    path('cheap_product/', CheapProductView.as_view(), name = 'CheapProduct'),
    path('discounted_product/', DiscountedProductView.as_view(), name = 'DiscountedProduct'),
]