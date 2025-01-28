# Import Restframework libraries 
from rest_framework.views import APIView 
from rest_framework.response import Response
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

# Filter Backend list
FILTER_BACKEND = [DjangoFilterBackend, SearchFilter, OrderingFilter] 

# Constants for searching and ordering 
SEARCH_FIELD = ['name', 'description', 'status'] 
ORDERING_FIELD = ['status', 'price', 'category', 'name'] 
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
    permission_classes = [IsAuthenticatedOrReadOnly, IsCreateOrAdmin]

# CheapProduct View
class CheapProductView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.filter(price__lte = 100.00) 
        serializer = CheapProductSerializer(queryset, many = True)
        return Response(serializer.data)

# DiscountedProduct View
class DiscountedProductView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.filter(price__gte = 1000.00)
        serializer = DiscountProductSerializer(queryset, many = True)
        return Response(serializer.data)