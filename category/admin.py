from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')  
    search_fields = ('name',)  
    list_filter = ('parent_category',)  
    list_per_page = 50

admin.site.register(Category, CategoryAdmin)
