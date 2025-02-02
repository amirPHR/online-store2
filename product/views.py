# Import Django and DRF libraries 
from rest_framework.views import APIView
import django_filters
from django_filters.rest_framework import FilterSet 
from rest_framework.viewsets import ModelViewSet 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Import Model and Serializer 
from .models import Product 
from .serializers import ProductSerializer, CheapProductSerializer, DiscountProductSerializer

# Import Pagination class from core app 
from core.pagination import DefaultPagination 

# Import Permission class from core app 
from core.permissions import IsCreateOrAdmin

# Product FilterSet 
class ProductFilterSet(FilterSet):
    brand = django_filters.CharFilter(field_name='brand') 

    class Meta:
        fields = ['brand'] 
        model = Product 

# Filter Backend list
FILTER_BACKEND = [DjangoFilterBackend, SearchFilter, OrderingFilter] 

# Constants for searching and ordering 
SEARCH_FIELD = ['name', 'description', 'status'] 
ORDERING_FIELD = ['status', 'price', 'category', 'name', 'id'] 
ORDERING = ['name'] 

# Product ViewSet
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    filter_backends = FILTER_BACKEND
    search_fields = SEARCH_FIELD 
    ordering_fields = ORDERING_FIELD 
    ordering = ORDERING 
    filterset_class = ProductFilterSet
    permission_classes = [IsAuthenticatedOrReadOnly, IsCreateOrAdmin]

# Base Filter for CheapProduct and DiscountedProduct 
class BaseFilterProductView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly] 
    serializer_class = None 
    filter_conditions = {} 

    def get_queryset(self):
        queryset = Product.objects.filter(**self.filter_conditions) 
        request = self.request 


        name = request.query_params.get('name') 
        price = request.query_params.get('price') 
        category = request.query_params.get('category') 

        if name:
            queryset = queryset.filter(name__icontains = name) 
        if price:
            queryset = queryset.filter(price = price) 
        if category:
            queryset = queryset.filter(category__name = category)      

        return queryset    

# CheapProduct View
class CheapProductView(BaseFilterProductView):
    """
    If ProductPrice > 300.00.This is a CheapProduct
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CheapProductSerializer 
    filter_conditions = {'price__lte':300.00}
    
# DiscountedProduct View
class DiscountedProductView(BaseFilterProductView):
    """
    If ProductPrice < 5000.00.discounted 30%
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DiscountProductSerializer 
    filter_conditions = {'price__gte':5000.00}