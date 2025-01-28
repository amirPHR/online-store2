from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'score', 'comment')  
    search_fields = ('user__username', 'product__name')  
    list_filter = ('score', 'product')  

admin.site.register(Review, ReviewAdmin)