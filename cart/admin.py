from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at', 'updated_at')  
    search_fields = ('user__username',)  
    list_filter = ('status',)  
    date_hierarchy = 'created_at'  

admin.site.register(Cart, CartAdmin)
