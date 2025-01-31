from django.urls import path 
from .views import CountOfCartUserView

urlpatterns = [
    path('countcart/', CountOfCartUserView.as_view(), name = 'CountOfCartUserView'),
]