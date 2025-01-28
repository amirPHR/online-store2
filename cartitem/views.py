# Import RestFramework libraries 
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated

# Import Serializer and Model 
from .serializers import CartItemSerializer 
from .models import CartItem 
from cart.models import Cart 

# Import Pagination class from core app 
from core.pagination import DefaultPagination 

# CartItem Serializer 
class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all() 
    serializer_class = CartItemSerializer 
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Users just can see their CartItem 
        """
        user = self.request.user 
        if not user.is_staff:
            return CartItem.objects.filter(cart__user = user)
        return CartItem.objects.all()            


    def create(self, request, *args, **kwargs):
        """
        Only Users Can create CartItem for themselves
        """
        user = request.user
        cart_id = request.data['cart']
        if not user.is_staff:
            if 'cart' in request.data:
                if not Cart.objects.filter(id=cart_id, user=user).exists():
                    return Response(
                        {'detail': 'You are not allowed to create CartItem for others'},
                        status=status.HTTP_403_FORBIDDEN
                    )
        return super().create(request, *args, **kwargs)