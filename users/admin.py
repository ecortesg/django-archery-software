from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # Fields to be used in displaying a user
    list_display = ["email", "is_staff", "is_superuser", "is_active"]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        (
            "Permissions",
            {
                "fields": [
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "user_permissions",
                ]
            },
        ),
        ("Important dates", {"fields": ["created_at", "updated_at", "last_login"]}),
    ]
    readonly_fields = ["created_at", "updated_at", "last_login"]

    # Fields to be used in creating a user
    add_fieldsets = [
        (None, {"classes": ["wide"], "fields": ["email", "password1", "password2"]})
    ]

    search_fields = ["email"]
    ordering = ["email"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
