from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('email', 'full_name', 'telephone', 'national_id', 'family_funds_box_number', 'family_funds_regulations')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'full_name', 'is_staff', 'is_active')
    search_fields = ('email', 'full_name', 'telephone', 'national_id', 'family_funds_box_number', 'family_funds_regulations')
    ordering = ('email',) 


admin.site.register(CustomUser, CustomUserAdmin)
