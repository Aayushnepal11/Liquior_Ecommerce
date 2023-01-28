from django.contrib import admin
from .models import Category, Product, Contact


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'image')



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)
