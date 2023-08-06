from django.shortcuts import render, get_object_or_404
from .models import Race, Order
# Import login_required decorator
from django.contrib.auth.decorators import login_required

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
    ticket_prices = {
        'friday-general': 70,
        'friday-grandstand': 150,
        'saturday-general': 100,
        'saturday-grandstand': 200,
        'sunday-general': 120,
        'sunday-grandstand': 250,
        'all-general': 250,
        'all-grandstand': 500,
    }

    if request.method == 'POST':
        # Get the form data from request.POST
        race_name = request.POST.get('race')
        ticket_type = request.POST.get('ticket_type')
        ticket_category = request.POST.get('ticket_category')
        quantity = request.POST.get('quantity')

        # Get the Race object based on the selected race name
        race = Race.objects.get(name=race_name)

        # Calculate the total price based on the selected options
        option_key = f"{ticket_type}-{ticket_category}"
        total_price = ticket_prices.get(option_key, 0) * int(quantity)

        # Save the ticket booking information with the user information
        Order.objects.create(
            user=request.user,
            race=race,
            ticket_type=ticket_type,
            ticket_category=ticket_category,
            quantity=quantity,
            total_price=total_price,
        )

    races = Race.objects.all()
    default_race = races.first() if races.exists() else None
    context = {
        'races': races,
        'default_race': default_race,
    }

    return render(request, 'buy_tickets.html', context)


def contact(request):
    return render(request, 'contact.html')


@login_required
def my_orders(request):
    # Get all orders related to the currently logged-in user
    orders = Order.objects.filter(user=request.user)

    context = {
        'orders': orders,
    }

    return render(request, 'my_orders.html', context)
