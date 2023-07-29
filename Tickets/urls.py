from django.contrib import admin
from django.urls import path, include
from Tickets import views

# Define the URL patterns for booking app
urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.home, name='home'),
    path('calender', views.menu, name='calender'),
    path('teams', views.reservations, name='teams'),
    path('drivers', views.gallery, name='drivers'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
