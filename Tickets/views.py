from django.shortcuts import render


def home(request):
    return render(request, 'f1_tickets/home.html')


def calendar(request):
    return render(request, 'f1_tickets/calendar.html')


def teams(request):
    return render(request, 'f1_tickets/teams.html')


def drivers(request):
    return render(request, 'f1_tickets/drivers.html')


def contact(request):
    return render(request, 'f1_tickets/contact.html')
