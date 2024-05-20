from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "preferred_contact",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("preferred_contact",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("preferred_contact",)}),)

admin.site.register(CustomUser, CustomUserAdmin)