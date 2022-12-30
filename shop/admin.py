from django.contrib import admin
from .models import FeaturedProducts, Contact

# Register your models here.


@admin.register(FeaturedProducts)
class FeatureProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', )