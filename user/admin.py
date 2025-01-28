from django.contrib import admin
from .models import UserProfile, User 

# UserAdmin 
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone_number'] 
    search_fields = ('username', 'first_name', 'last_name', 'phone_number') 
    ordering = ('username',)

admin.site.register(User, UserAdmin) 

# UserProfileAdmin 
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'national_code', 'birth_date', 'job')  
    search_fields = ('user__username', 'national_code')  
    list_filter = ('birth_date', 'job')  
    ordering = ('user',)  

admin.site.register(UserProfile, UserProfileAdmin)