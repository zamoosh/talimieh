from django.contrib import admin
from client.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'id', 'is_staff', 'is_superuser', 'is_active']
    list_editable = ['is_staff']


admin.site.register(User, UserAdmin)
