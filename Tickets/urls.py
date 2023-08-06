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
    path('buy_tickets', views.buy_tickets, name='buy_tickets'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
]
