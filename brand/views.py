# Import DRF libraries 
from rest_framework.viewsets import ModelViewSet  
from rest_framework.permissions import IsAdminUser 


# Import Serializer and Model
from .models import Brand 
from .serializers import BrandSerializer 

# Brand ViewSet 
class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all() 
    serializer_class = BrandSerializer 
    permission_classes=[IsAdminUser]