from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('facility_list/', views.facility_list, name='facility_list'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('member_list/', views.member_list, name='member_list'),
    path('member_list/add/', views.member_create, name='member_create'),
    path('member_list/edit/<int:pk>/', views.member_update, name='member_update'),
    path('member_list/delete/<int:pk>/', views.member_delete, name='member_delete'),
    
]