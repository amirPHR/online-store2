# Import RestFramework libraries 
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated 
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter

# Import Serializer and Model 
from .serializers import ReviewSerializer 
from .models import Review

# Import Permission class from review app 
from .permissions import IsUser 

# Review Filter 
class ReviewFilter(filters.FilterSet):
    score = filters.CharFilter(field_name='score', lookup_expr='icontains') 

    class Meta:
        fields = ['score'] 
        model = Review 

# Filter Backend 
FILTER_BACKEND = [DjangoFilterBackend, SearchFilter, OrderingFilter] 

# Constants for Ordering  
ORDERING_FIELDS = ['score', 'product']
DEFAULT_ORDERING = ['score']  

# Review ViewSet 
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer
    ordering_fields = ORDERING_FIELDS 
    ordering = DEFAULT_ORDERING
    permission_classes = [IsAuthenticated, IsUser] 
    filterset_class = ReviewFilter