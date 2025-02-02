from django.urls import path 
from .views import FullProfileOfUsersView

urlpatterns = [
    path('fullprofile/', FullProfileOfUsersView.as_view(), name='FullProfileOfUsersView')
]