from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('details/', views.details_view, name='details_view'),
    path('search/', views.search_view, name='search_view'),
    path('certificate/<int:vehicle_id>/', views.certificate_view, name='certificate_view'),
    path('certificate-info/<str:unique_identifier>/', views.certificate_info_view, name='certificate_info_view'),
    path('fitment', views.fitment, name='fitment'),
    path('gps_details/', views.gps_details, name='gps_details'),
    path('gps_search/', views.gps_search, name='gps_search'),
    path('gps_certificate/<int:vehicle_id>/<str:current_time>/', views.gps_certificate, name='gps_certificate'),
    path('gps_certificate_info/<str:gps_unique_identifier>/', views.gps_certificate_info, name='gps_certificate_info'),
    path('camera_details/', views.camera_details, name='camera_details'),
    path('camera_search/', views.camera_search, name='camera_search'),
    path('camera_certificate/<int:vehicle_id>/', views.camera_certificate, name='camera_certificate'),
    path('camera_certificate_info/<str:camera_unique_identifier>/', views.camera_certificate_info, name='camera_certificate_info'),

]
