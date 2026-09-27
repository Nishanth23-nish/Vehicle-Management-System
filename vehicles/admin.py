from django.contrib import admin

from .models import ContactMessage, Driver, Vehicle


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'phone', 'experience_years', 'is_available')
    list_filter = ('is_available', 'experience_years')
    search_fields = ('name', 'license_number', 'phone')


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'make', 'model', 'year', 'vehicle_type', 'owner_name', 'driver', 'status', 'next_service_date')
    list_filter = ('status', 'vehicle_type', 'year', 'driver')
    search_fields = ('vehicle_number', 'make', 'model', 'owner_name', 'driver__name')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
