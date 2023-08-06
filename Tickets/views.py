from django.shortcuts import render, get_object_or_404
from .models import Race, Order

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
    if request.method == 'POST':
        races = Race.objects.all()

        # Get the race name from the query parameters if it exists
        race_name = request.GET.get('race_name', None)
        context = {
            'races': races,
            'default_race': race_name,  # Pass the race name as context variable
        }

        return render(request, 'buy_tickets.html', context)

    races = Race.objects.all()
    default_race = races.first() if races.exists() else None
    context = {
        'races': races,
        'default_race': default_race,
    }

    return render(request, 'buy_tickets.html', context)


def contact(request):
    return render(request, 'contact.html')
