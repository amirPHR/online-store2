from rest_framework import serializers 
from .models import Cart 
from user.serializers import UserCreateSerializer

# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = ['id', 'user', 'status']
        model = Cart

class CountOfCartUserSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    class Meta:
        fields = '__all__' 
        model = Cart