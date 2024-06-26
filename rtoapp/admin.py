from django.contrib import admin
from . models import Vehicle

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_no','owner_name','mobile_no','owner_address','created_at']

admin.site.register(Vehicle,VehicleAdmin)
