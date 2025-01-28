from rest_framework import serializers 
from .models import CartItem 

# CartItem Serializer
class CartItemSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = ['id', 'cart', 'product', 'quantity', 'total_price'] 
        model = CartItem