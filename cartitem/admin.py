from django.contrib import admin
from .models import CartItem

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'total_price')  
    search_fields = ('product__name', 'cart__user__username')  
    list_filter = ('cart__status',)  
    raw_id_fields = ('product',)  

admin.site.register(CartItem, CartItemAdmin)
