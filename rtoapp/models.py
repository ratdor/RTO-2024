from django.db import models

class Vehicle(models.Model):
    vehicle_no = models.CharField(max_length=100)
    registration_year = models.IntegerField()
    chassis_no = models.CharField(max_length=100)
    engine_no = models.CharField(max_length=100)
    rto = models.CharField(max_length=100,null=True)
    vehicle_make = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100,null=True)
    manufacturer_name = models.CharField(max_length=100,null=True)
    mobile_no = models.CharField(max_length=15,null=True)
    distributor_name = models.CharField(max_length=100,null=True)
    owner_address = models.CharField(max_length=100,null=True)
    distributor_address = models.CharField(max_length=100,null=True)
    camera_serial_number_primary = models.CharField(max_length=100,null=True)
    model_number_primary = models.CharField(max_length=100,null=True)
    camera_serial_number_secondary = models.CharField(max_length=100,null=True)
    model_number_secondary = models.CharField(max_length=100,null=True)
    Vehicle_number_plate_view = models.ImageField(upload_to='vehicle_images/',null=True)
    Camera_image = models.ImageField(upload_to='vehicle_images/',null=True)
    Sensor_image = models.ImageField(upload_to='vehicle_images/',null=True)
    Display_image = models.ImageField(upload_to='vehicle_images/',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.vehicle_no


class cameraVehicle(models.Model):
    vehicle_no = models.CharField(max_length=100)
    registration_year = models.IntegerField()
    chassis_no = models.CharField(max_length=100)
    engine_no = models.CharField(max_length=100)
    rto = models.CharField(max_length=100,null=True)
    vehicle_make = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100,null=True)
    manufacturer_name = models.CharField(max_length=100,null=True)
    mobile_no = models.CharField(max_length=15,null=True)
    distributor_name = models.CharField(max_length=100,null=True)
    owner_address = models.CharField(max_length=100,null=True)
    distributor_address = models.CharField(max_length=100,null=True)
    camera_serial_number_primary = models.CharField(max_length=100,null=True)
    camera_serial_number_secondary = models.CharField(max_length=100,null=True)
    camera_serial_number_tertiary = models.CharField(max_length=100,null=True)
    model_number_primary = models.CharField(max_length=100,null=True)
    model_number_secondary = models.CharField(max_length=100,null=True)
    model_number_tertiary= models.CharField(max_length=100,null=True)
    model_number_quaternary  = models.CharField(max_length=100,null=True)
    part_number = models.CharField(max_length=100,null=True)
    drawing_number = models.CharField(max_length=100,null=True)
    imei_no = models.CharField(max_length=100,blank=True,null=True)
    did_no_primary = models.CharField(max_length=100,blank=True,null=True)
    did_no_secondary = models.CharField(max_length=100,blank=True,null=True)
    did_no_tertiary = models.CharField(max_length=100,blank=True,null=True)
    sim_no = models.CharField(max_length=100,blank=True,null=True)
    mobile_network = models.CharField(max_length=100,blank=True,null=True)
    Vehicle_number_plate_view = models.ImageField(upload_to='vehicle_images/',null=True)
    Camera_image = models.ImageField(upload_to='vehicle_images/',null=True)
    Sensor_image = models.ImageField(upload_to='vehicle_images/',null=True)
    Display_image = models.ImageField(upload_to='vehicle_images/',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __self__(self):
        return self.vehicle_no

class gpsVehicle(models.Model):
    invoice_no = models.CharField(max_length=100)
    gps_serial_no = models.CharField(max_length=100,null=True)
    gps_model = models.CharField(max_length=100,null=True)
    registration_date = models.IntegerField()
    engine_no = models.CharField(max_length=100,null=True)
    network = models.CharField(max_length=100,null=True)
    vehicle_make = models.CharField(max_length=100,null=True)
    vehicle_model = models.CharField(max_length=100,null=True)
    registration_no = models.CharField(max_length=100,null=True)
    chassis_no = models.CharField(max_length=100,null=True)
    dealer = models.CharField(max_length=100,null=True)
    location_primary = models.CharField(max_length=100,null=True)
    customer_name = models.CharField(max_length=100,null=True)
    customer_address = models.CharField(max_length=100,null=True)
    location_secondary = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15,null=True)
    time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.gps_serial_no












