from rest_framework import serializers 
from .models import Product 

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'description', 'category', 'price', 'stock_quantity', 'status', 'image']
        model = Product
    
# CheapProduct Serializer 
class CheapProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'price', 'image', 'stock_quantity', 'category']
        model = Product

# DiscountedProduct 
class DiscountProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()

    class Meta:
        fields = ['name', 'discount_price', 'image', 'stock_quantity', 'category'] 
        model = Product 

    def get_discount_price(self, obj):
        return float(obj.price) * 0.70