from pyexpat import model
from django.contrib import admin
from .models import FeaturedProducts

# Register your models here.


@admin.register(FeaturedProducts)
class FeatureProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
