from django.contrib import admin
from .models import Featured

# Register your models here.

@admin.register(Featured)
class FeatureAdmin(admin.ModelAdmin):
    pass
