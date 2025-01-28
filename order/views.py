# Import RestFramework libraries 
from rest_framework.viewsets import ModelViewSet 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

# Import Model and Serializer 
from .serializers import OrderSerializer 
from .models import Order 

# Import Permission class from order app 
from .permissions import IsUserOrAnonymousUser 

# Filter Backend 
FILTER_BACKEND = [DjangoFilterBackend, SearchFilter, OrderingFilter] 

# Constants for Searching and ordering 
SEARCHING_FIELD = ['user__username', 'user__first_name', 'user__last_name']
ORDERING_FIELD = ['status', 'payment_status']
DEFAULT_ORDERING = ['user__username']

# OrderViewSet
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all() 
    filter_backends = FILTER_BACKEND 
    search_fields = SEARCHING_FIELD 
    ordering_fields = ORDERING_FIELD 
    ordering = DEFAULT_ORDERING 
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsUserOrAnonymousUser] 

    def get_queryset(self):
        """
        Only Users can see their order
        """
        user = self.request.user
        if not user.is_staff:
            return Order.objects.filter(user=user)
        return  Order.objects.all()