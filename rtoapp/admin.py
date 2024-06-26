from django.contrib import admin
from . models import Vehicle,cameraVehicle,gpsVehicle

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_no','owner_name','mobile_no','owner_address','created_at']

admin.site.register(Vehicle,VehicleAdmin)

class CameraAdmin(admin.ModelAdmin):
    list_display = ['vehicle_no','owner_name','mobile_no','owner_address','created_at']

admin.site.register(cameraVehicle,CameraAdmin)

class GPSAdmin(admin.ModelAdmin):
    list_display = ['invoice_no','customer_name','mobile_no','customer_address','created_at','time']

admin.site.register(gpsVehicle,GPSAdmin)

