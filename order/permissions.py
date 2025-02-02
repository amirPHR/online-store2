from rest_framework.permissions import BasePermission 
from cart.models import Cart 

class IsUserOrAnonymousUser(BasePermission):
    """
    This Permission checks:
    - Just Users can create Order for themselves
    - Each Users with there own card can create Order
    """
    def has_permission(self, request, view):
        user = request.user 
        data = request.data 

        if view.action in ['create', 'destroy', 'update', 'partial_update']:
            if not user.is_staff:
                if 'user' in data: 
                    if int(data['user']) != user.id:
                        return False 

                if 'cart' in data:
                    cart_id = data['cart' ]
                    if not Cart.objects.filter(id = cart_id, user=user).exists():
                        return False 
        return True