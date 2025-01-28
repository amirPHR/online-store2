from rest_framework.permissions import BasePermission 

class IsUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user 
        data = request.data 

        if view.action in ['create', 'update', 'partial_update', 'delete']:
            if not user.is_staff:
                if 'user' in data: 
                    if int(data['user']) != user.id:
                        return False
        return True 