from rest_framework import serializers 
from .models import Cart 

# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = ['id', 'user', 'status']
        model = Cart