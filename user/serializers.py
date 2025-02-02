from rest_framework import serializers 
from .models import UserProfile 
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer 

# UserCreate Serializer
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number']
        
# UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['user', 'national_code', 'address', 'birth_date', 'job']
        model = UserProfile

# FullProfile of User
class FullProfileOfUsersSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    class Meta:
        fields = ['user', 'national_code', 'address', 'birth_date', 'job']
        model = UserProfile