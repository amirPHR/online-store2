from rest_framework.permissions import BasePermission 

class IsCreateOrAdmin(BasePermission):
    """
    This Permission shows:
    - Just admins can create, delete and update category
    """
    def has_permission(self, request, view):
        user = request.user 
        if view.action in ['create', 'delete', 'update', 'partial_update']:
            if not user.is_staff:
                return False
        return True 