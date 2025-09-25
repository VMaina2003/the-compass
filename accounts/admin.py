from django.contrib import admin
from .models import CustomUser, Profile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)       
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("get_user_display", "phone", "location")
    search_fields = ("user__username", "user__email", "phone", "location")
    ordering = ("user__email",)  # fallback ordering, since username may not exist

    def get_user_display(self, obj):
        """Show username if available, otherwise email"""
        if hasattr(obj.user, "username") and obj.user.username:
            return obj.user.username
        return obj.user.email

    get_user_display.short_description = "User"
    get_user_display.admin_order_field = "user__username"
    
    