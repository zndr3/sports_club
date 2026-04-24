from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('facility_list/', views.facility_list, name='facility_list'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('member_list/', views.member_list, name='member_list'),
    
]