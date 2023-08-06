from django.contrib import admin
from .models import Race, Order

# Registering the Race model with the admin site


@admin.register(Race)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'date', 'location']
    list_filter = ('name', 'date', 'location')


# Registering the Order model with the admin site


@admin.register(Order)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'race', 'ticket_type', 'ticket_category',
                    'quantity', 'total_price', 'order_date')
    search_fields = ['user', 'race']
    list_filter = ('user', 'race')
