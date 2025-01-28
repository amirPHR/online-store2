from rest_framework import serializers 
from .models import Order 

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['user', 'cart', 'status', 'payment_status', 'total_price']
        model = Order 