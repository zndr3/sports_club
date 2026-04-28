from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    
    path('booking_list/', views.booking_list, name='booking_list'),
    path('booking_list/facility/<int:facid>/', views.booking_by_facility, name='booking_by_facility'),
    path('booking_list/create/', views.booking_create, name='booking_create'),
    path('booking_list/update/<int:pk>/', views.booking_update, name='booking_update'),
    path('booking_list/delete/<int:pk>/', views.booking_delete, name='booking_delete'),


    path('members/', views.member_list, name='member_list'),
    path('members/add/', views.member_create, name='member_create'),
    path('members/edit/<int:pk>/', views.member_update, name='member_update'),
    path('members/delete/<int:pk>/', views.member_delete, name='member_delete'),

    path('facilities/', views.facility_list, name='facility_list'),
    path('facilities/add/', views.facility_create, name='facility_create'),
    path('facilities/edit/<int:pk>/', views.facility_update, name='facility_update'),
    path('facilities/delete/<int:pk>/', views.facility_delete, name='facility_delete'),



    
]