from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'status', 'image')  
    search_fields = ('name', 'category__name')  
    list_filter = ('status', 'category')  
    list_editable = ('price', 'stock_quantity', 'status')  

admin.site.register(Product, ProductAdmin)