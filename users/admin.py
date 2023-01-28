from django.contrib import admin

from .models import CustomerUsers
# Register your models here.
@admin.register(CustomerUsers)
class UserManager(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'password')
