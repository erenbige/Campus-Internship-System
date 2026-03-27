from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
   
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {'fields': ('is_student', 'is_company')}),
        ('ATS Profile (CV)', {'fields': ('skills', 'languages', 'experience_years')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)