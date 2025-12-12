from django.contrib import admin
from .models import LaundryOrder


@admin.register(LaundryOrder)
class LaundryOrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'service_type',
        'weight_kg',
        'status',
        'created_at',
    )
    list_filter = ('status', 'service_type')
    search_fields = ('customer__username', 'address', 'note')
