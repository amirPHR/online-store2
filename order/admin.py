from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'cart', 'status', 'payment_status', 'total_price', 'created_at')  
    search_fields = ('user__username', 'cart__status')  
    list_filter = ('status', 'payment_status')  
    date_hierarchy = 'created_at'  

admin.site.register(Order, OrderAdmin)
