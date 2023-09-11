from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'created_at']


admin.site.register(User, UserAdmin)
