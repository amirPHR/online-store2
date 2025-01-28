from rest_framework import serializers 
from .models import Category

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        fields = ['id', 'name', 'parent_category', 'slug']
        model = Category