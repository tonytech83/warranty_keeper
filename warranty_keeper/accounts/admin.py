from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from warranty_keeper.accounts.models import Profile

# Unregister the default User model
admin.site.unregister(User)

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "is_staff",
        "is_superuser",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
    )

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )

    search_fields = ("email",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
    )
    ordering = (
        "first_name",
        "last_name",
    )
    search_fields = (
        "first_name",
        "last_name",
    )
