from django.shortcuts import render, get_object_or_404

# Define index view


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


def calendar(request):
    return render(request, 'calendar.html')


def teams(request):
    return render(request, 'teams.html')


def drivers(request):
    return render(request, 'drivers.html')


def buy_tickets(request):
    return render(request, 'buy_tickets.html')


def contact(request):
    return render(request, 'contact.html')
