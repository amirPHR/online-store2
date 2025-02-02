from rest_framework import serializers 
from .models import CartItem 

# CartItem Serializer
class CartItemSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    class Meta: 
        fields = ['id', 'cart', 'product', 'quantity', 'total_price', 'discounted_price'] 
        model = CartItem

    def get_discounted_price(self,obj):
        if obj.quantity >= 10:
            return float(obj.product.price) * 0.60
        return obj.quantity * obj.product.price