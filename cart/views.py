# Import RestFramework libraries 
from rest_framework.viewsets import ModelViewSet 
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated 

# Import Serializer and Model 
from .serializers import CartSerializer 
from .models import Cart 

# Import Pagination class from core app 
from core.pagination import DefaultPagination 

# Filter Backend list 
FILTER_BACKEND = [DjangoFilterBackend]

# FilterSet class 
class CartFilterSet(filters.FilterSet):
    status = filters.CharFilter(field_name='status', lookup_expr='icontains')

    class Meta:
        fields = ['status']
        model = Cart 

# Cart ViewSet 
class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all() 
    serializer_class = CartSerializer 
    pagination_class = DefaultPagination 
    filterset_class = CartFilterSet
    filter_backends = FILTER_BACKEND
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Users Just can see their Cart
        """
        user = self.request.user 
        if not user.is_staff: 
            return Cart.objects.filter(user=user) 
        return Cart.objects.all() 
    
    def create(self, request, *args, **kwargs):
        """
        Users can not create Cart for other
        """
        user = request.user 
        if not user.is_staff:
            if 'user' in request.data:
                if int(request.data['user']) != user.id:
                    return Response(
                        {'detail':'You are not allow to create cart for others'},
                        status = status.HTTP_403_FORBIDDEN 
                    )
        return super().create(request, *args, **kwargs)