from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        
        (
            "MentorLink Information", {
                "fields": ("role", "phone_number", "gender", "date_of_birth",)
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Personal Information", {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "email",)
            }
        ),
        (
            "MentorLink Information", {
                "fields": ("role", "phone_number", "gender", "date_of_birth",)
            }
        ),
    )