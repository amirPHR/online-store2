from rest_framework import serializers 
from .models import Review 

# Review Serializer 
class ReviewSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = ['user', 'product', 'score', 'comment'] 
        model = Review