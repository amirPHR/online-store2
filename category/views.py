# Import Rest Framework libraries 
from rest_framework.viewsets import ModelViewSet 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter 
from rest_framework.permissions import IsAuthenticatedOrReadOnly 

# Import serializer and model 
from .models import Category 
from .serializers import CategorySerializer 

# Import Permission class and Pagination class from core app  
from core.pagination import DefaultPagination
from core.permissions import IsCreateOrAdmin 

# Filter Backend list 
FILTER_BACKEND = [DjangoFilterBackend, SearchFilter, OrderingFilter] 

# Constants for Searching and Ordering  
SEARCH_FIELDS = ['name'] 
DEFAULT_ORDERING = ['name'] 

# Category ViewSet
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer 
    pagination_class = DefaultPagination
    filter_backends = FILTER_BACKEND 
    search_fields = SEARCH_FIELDS
    ordering = DEFAULT_ORDERING
    permission_classes = [IsCreateOrAdmin, IsAuthenticatedOrReadOnly]