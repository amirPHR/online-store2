from django.db import models 
from category.models import Category
from brand.models import Brand 

# Product Model
class Product(models.Model):
    name = models.CharField(max_length = 255, verbose_name='Product Name') 
    description = models.TextField(verbose_name='Description') 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category') 
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Product Price', default=0.00) 
    stock_quantity = models.PositiveBigIntegerField(verbose_name='Product Quantity', default=1) 
    STATUS_CHOICES = [
        ('available ', 'Availble') ,
        ('not_available', 'Not Avaiable')
    ]
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='available', verbose_name='Status')  
    image = models.ImageField(upload_to='images/', blank=True) 
    
    def __str__(self):
        return f'{self.name} ({self.status})' 