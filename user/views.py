# Import Restframework libraries 
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import status 
from rest_framework.response import Response 

# Import Model and serializer
from .models import UserProfile, User 
from .serializers import UserProfileSerializer, UserCreateSerializer

# Import Pagination class from core app
from core.pagination import DefaultPagination

# Filter Backend list
FILTER_BACKEND = [DjangoFilterBackend, SearchFilter, OrderingFilter]

# User ViewSet
class UserViewSet(ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserCreateSerializer
    filter_backends = FILTER_BACKEND
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['username']
    pagination_class = DefaultPagination
    
    def get_queryset(self):
        """
        Just admins can see all users
        """
        user = self.request.user 
        if user.is_authenticated:
            if not user.is_staff:
                return User.objects.filter(id = user.id)
            return User.objects.all()
        return User.objects.none()

# Constants for searching and ordering (for UserProfile)
SEARCH_FIELDS = ['user__username', 'user__first_name', 'user__last_name', 'user__phone_number', 'national_code']
ORDERING = ['user__username']

# UserProfile ViewSet 
class UserProfileViewSet(ModelViewSet): 
    queryset = UserProfile.objects.select_related('user').all() 
    serializer_class = UserProfileSerializer
    filter_backends = FILTER_BACKEND
    search_fields = SEARCH_FIELDS
    ordering = ORDERING
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        """
        Just admins can see all Users Profiles
        """
        user = self.request.user 
        if not user.is_staff:
            return UserProfile.objects.filter(user = user) 
        return UserProfile.objects.all()

    def create(self, request, *args, **kwargs):
        user = request.user 
        if not user.is_staff:
            if 'user' in request.data and int(request.data['user']) != user.id:
                return Response(
                    {'detail':'You are not allowed to create profile for other.'},
                    status=status.HTTP_403_FORBIDDEN 
                )
        return super().create(request, *args, **kwargs)