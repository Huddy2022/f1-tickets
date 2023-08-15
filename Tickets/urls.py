from django.contrib import admin
from django.urls import path, include
from Tickets import views

# Define the URL patterns for booking app
urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.home, name='home'),
    path('calendar', views.calendar, name='calendar'),
    path('teams', views.teams, name='teams'),
    path('drivers', views.drivers, name='drivers'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
    path('basket/', views.basket, name='basket'),
    path('remove_from_basket/<int:index>/',
         views.remove_from_basket, name='remove_from_basket'),
]
