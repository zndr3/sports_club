from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('facilities/', views.facilities, name='facilities'),
]