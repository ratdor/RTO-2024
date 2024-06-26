# forms.py
from django import forms
from . models import Vehicle,cameraVehicle,gpsVehicle


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        
        
        
class cameraVehicleForm(forms.ModelForm):
    class Meta:
        model = cameraVehicle
        fields = '__all__'
        


class GpsVehicleForm(forms.ModelForm):
    class Meta:
        model = gpsVehicle
        fields = [
            'invoice_no', 'gps_serial_no', 'gps_model', 'registration_date',
            'engine_no', 'network', 'vehicle_make', 'vehicle_model',
            'registration_no', 'chassis_no', 'dealer', 'location_primary',
            'customer_name', 'customer_address', 'location_secondary', 'mobile_no'
        ]





