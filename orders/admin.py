from django.contrib import admin
from .models import Order, OrderedItem


# Register your models here.
# @admin.register(OrderedItem) While using TabularInline don't use the @admin decorators.
# throws an error as the Wrapped class must subclass ModelAdmin
class OrderItemInline(admin.TabularInline):
    model = OrderedItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'city', 'postal_code', 'paid', 'created_at',
                    'updated_at']
    list_filter = ['paid', 'created_at', 'updated_at']

    inlines = [OrderItemInline]
