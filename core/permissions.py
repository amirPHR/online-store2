from rest_framework.permissions import BasePermission 

class IsCreateOrAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user 
        if view.action in ['create', 'delete', 'update', 'partial_update']:
            if not user.is_staff:
                return False
        return True 