from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import VehicleForm,cameraVehicleForm,GpsVehicleForm
from django.urls import reverse
from .forms import LoginForm
from .models import Vehicle,cameraVehicle,gpsVehicle
from django.utils import timezone
from io import BytesIO
import qrcode
import base64
from datetime import datetime

def login_view(request):
    if request.user.is_authenticated:
        return redirect('fitment')
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('fitment')  # Redirect to a success page.
            else:
                form.add_error(None, 'Invalid username or password')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

################################################### Sensor Certificate ################################################


def details_view(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('search_view')
    else:
        form = VehicleForm()
    return render(request, 'details.html',{'form':form})

def search_view(request):
    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        vehicle_no = request.POST.get('vecregno')

        from_date_vehicles = Vehicle.objects.none()
        to_date_vehicles = Vehicle.objects.none()
        between_vehicles = Vehicle.objects.none()
        vehno_vehicles = Vehicle.objects.none()

        if from_date:
            from_date_year = datetime.strptime(from_date, '%Y-%m-%d').year
            from_date_vehicles = Vehicle.objects.filter(created_at__year=from_date_year)

        if to_date:
            to_date_year = datetime.strptime(to_date, '%Y-%m-%d').year
            to_date_vehicles = Vehicle.objects.filter(created_at__year=to_date_year)

        if from_date and to_date:
            from_date_year = datetime.strptime(from_date, '%Y-%m-%d').year
            to_date_year = datetime.strptime(to_date, '%Y-%m-%d').year
            between_vehicles = Vehicle.objects.filter(created_at__year__range=[from_date_year, to_date_year])

        if vehicle_no:
            vehno_vehicles = Vehicle.objects.filter(vehicle_no__icontains=vehicle_no)
            from_date_vehicles = from_date_vehicles.filter(vehicle_no__icontains=vehicle_no)
            to_date_vehicles = to_date_vehicles.filter(vehicle_no__icontains=vehicle_no)
            between_vehicles = between_vehicles.filter(vehicle_no__icontains=vehicle_no)

            vehicles = vehno_vehicles | from_date_vehicles | between_vehicles | to_date_vehicles
        else:
            vehicles = from_date_vehicles | to_date_vehicles | between_vehicles

        return render(request, 'search.html', {'vehicles': vehicles})

    else:
        vehicles = Vehicle.objects.all()
        return render(request, 'search.html', {'vehicles': vehicles})

def certificate_info_view(request, unique_identifier):
    vehicle = get_object_or_404(Vehicle, id=unique_identifier)
    return render(request, 'certificate_info.html', {'vehicle': vehicle})

def certificate_view(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    certificate_info_url = request.build_absolute_uri(reverse('certificate_info_view', kwargs={'unique_identifier': vehicle_id}))

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(certificate_info_url)
    qr.make(fit=True)
    
    qr_code_img = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(qr_code_img)
    
    qr_code_base64 = base64.b64encode(qr_code_img.getvalue()).decode()
    
    return render(request, 'certificate_view.html', {'qr_code_base64': qr_code_base64, 'vehicle': vehicle})

def fitment(request):
    return render(request,'fitment.html')


################################################### End Sensor Certificate ################################################


################################################### GPS Certificate ################################################

def gps_details(request):
    if request.method == 'POST':
        form = GpsVehicleForm(request.POST, request.FILES)
        if form.is_valid():
            current_time = datetime.datetime.now()  
            form.instance.time = current_time  
            form.save()
            
            return redirect('gps_search')
        else:
            print("Form is not valid:")
            print(form.errors) 
    else:
        form = GpsVehicleForm()
    
    context = {
        'form': form,
    }
    return render(request, 'gps_details.html', context)

def gps_search(request):
    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        invoice_no = request.POST.get('vecregno')

        from_date_vehicles = gpsVehicle.objects.none()
        to_date_vehicles = gpsVehicle.objects.none()
        between_vehicles = gpsVehicle.objects.none()
        vehno_vehicles = gpsVehicle.objects.none()

        if from_date:
            from_date_year = datetime.strptime(from_date, '%Y-%m-%d').year
            from_date_vehicles = gpsVehicle.objects.filter(created_at__year=from_date_year)

        if to_date:
            to_date_year = datetime.strptime(to_date, '%Y-%m-%d').year
            to_date_vehicles = gpsVehicle.objects.filter(created_at__year=to_date_year)

        if from_date and to_date:
            from_date_year = datetime.strptime(from_date, '%Y-%m-%d').year
            to_date_year = datetime.strptime(to_date, '%Y-%m-%d').year
            between_vehicles = gpsVehicle.objects.filter(created_at__year__range=[from_date_year, to_date_year])

        if invoice_no:
            vehno_vehicles = gpsVehicle.objects.filter(invoice_no__icontains=invoice_no)
            from_date_vehicles = from_date_vehicles.filter(invoice_no__icontains=invoice_no)
            to_date_vehicles = to_date_vehicles.filter(invoice_no__icontains=invoice_no)
            between_vehicles = between_vehicles.filter(invoice_no__icontains=invoice_no)

            gps_vehicles = vehno_vehicles | from_date_vehicles | between_vehicles | to_date_vehicles
        else:
            gps_vehicles = from_date_vehicles | to_date_vehicles | between_vehicles

        return render(request, 'gps_search.html', {'gps_vehicles': gps_vehicles})

    else:
        gps_vehicles = gpsVehicle.objects.all()
        return render(request, 'gps_search.html', {'gps_vehicles': gps_vehicles})

def gps_certificate_info(request,gps_unique_identifier):
    gps_vehicle = get_object_or_404(gpsVehicle,id=gps_unique_identifier)
    return render(request,'gps_certificate_info.html',{'gps_vehicle': gps_vehicle})


def gps_certificate(request, vehicle_id, current_time):
    # Retrieve the GPS vehicle object using vehicle_id
    gps_vehicle = get_object_or_404(gpsVehicle, id=vehicle_id)

    # Build URL for gps_certificate_info view
    gps_certificate_info_url = request.build_absolute_uri(reverse('gps_certificate_info', kwargs={'gps_unique_identifier': gps_vehicle.id}))

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(gps_certificate_info_url)
    qr.make(fit=True)
    
    qr_code_img = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(qr_code_img)
    
    qr_code_base64 = base64.b64encode(qr_code_img.getvalue()).decode()
    
    return render(request, 'gps_certificate.html', {'qr_code_base64': qr_code_base64, 'gps_vehicle': gps_vehicle})

################################################### End GPS Certificate ################################################


################################################### Camera Certificate ################################################

def camera_details(request):
    if request.method == 'POST':
        form = cameraVehicleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('camera_search')
    else:
        form = cameraVehicleForm()
    return render(request,'camera_details.html',{'form':form})

def camera_search(request):
    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        vehicle_no = request.POST.get('vecregno')

        from_date_vehicles = cameraVehicle.objects.none()
        to_date_vehicles = cameraVehicle.objects.none()
        between_vehicles = cameraVehicle.objects.none()
        vehno_vehicles = cameraVehicle.objects.none()

        if from_date:
            from_date_year = datetime.strptime(from_date, '%Y-%m-%d').year
            from_date_vehicles = cameraVehicle.objects.filter(created_at__year=from_date_year)

        if to_date:
            to_date_year = datetime.strptime(to_date, '%Y-%m-%d').year
            to_date_vehicles = cameraVehicle.objects.filter(created_at__year=to_date_year)

        if from_date and to_date:
            from_date_year = datetime.strptime(from_date, '%Y-%m-%d').year
            to_date_year = datetime.strptime(to_date, '%Y-%m-%d').year
            between_vehicles = cameraVehicle.objects.filter(created_at__year__range=[from_date_year, to_date_year])

        if vehicle_no:
            vehno_vehicles = cameraVehicle.objects.filter(vehicle_no__icontains=vehicle_no)
            from_date_vehicles = from_date_vehicles.filter(vehicle_no__icontains=vehicle_no)
            to_date_vehicles = to_date_vehicles.filter(vehicle_no__icontains=vehicle_no)
            between_vehicles = between_vehicles.filter(vehicle_no__icontains=vehicle_no)

            camera_vehicles = vehno_vehicles | from_date_vehicles | between_vehicles | to_date_vehicles
        else:
            camera_vehicles = from_date_vehicles | to_date_vehicles | between_vehicles

        return render(request, 'camera_search.html', {'camera_vehicles': camera_vehicles})

    else:
        camera_vehicles = cameraVehicle.objects.all()
        return render(request, 'camera_search.html', {'camera_vehicles': camera_vehicles})


    
def camera_certificate_info(request,camera_unique_identifier):
    camera_vehicle = get_object_or_404(cameraVehicle,id=camera_unique_identifier)
    return render(request,'camera_certificate_info.html',{'camera_vehicle': camera_vehicle})


def camera_certificate(request, vehicle_id):
    camera_vehicle = get_object_or_404(cameraVehicle, id=vehicle_id)

    # Build URL for camera_certificate_info view
    camera_certificate_info_url = request.build_absolute_uri(reverse('camera_certificate_info', kwargs={'camera_unique_identifier': vehicle_id}))

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(camera_certificate_info_url)
    qr.make(fit=True)
    
    qr_code_img = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(qr_code_img)
    
    qr_code_base64 = base64.b64encode(qr_code_img.getvalue()).decode()
    
    return render(request, 'camera_certificate.html', {'qr_code_base64': qr_code_base64, 'camera_vehicle': camera_vehicle})

################################################### End Camera Certificate ################################################

