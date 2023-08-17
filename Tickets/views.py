from django.shortcuts import render, get_object_or_404, redirect
from .models import Race, Order
# Import login_required decorator
from django.contrib.auth.decorators import login_required

# Dictionary to map race names to their IDs
race_name_to_id = {
    'Abu Dhabi Grand Prix': 1,
    'Australian Grand Prix': 2,
    'Austrian Grand Prix': 3,
    'Azerbaijan Grand Prix': 4,
    'Bahrain Grand Prix': 5,
    'Belgian Grand Prix': 6,
    'Brazilian Grand Prix': 7,
    'British Grand Prix': 8,
    'Canadian Grand Prix': 9,
    'Dutch Grand Prix': 10,
    'Emilia Romagna Grand Prix': 11,
    'Hungarian Grand Prix': 12,
    'Italian Grand Prix (Monza)': 13,
    'Japanese Grand Prix': 14,
    'Las Vegas Grand Prix': 15,
    'Mexican Grand Prix': 16,
    'Miami Grand Prix': 17,
    'Monaco Grand Prix': 18,
    'Qatar Grand Prix': 19,
    'Saudi Arabia Grand Prix': 20,
    'Singapore Grand Prix': 21,
    'Spanish Grand Prix': 22,
    'United States Grand Prix': 23,
}
# Dictionary to map ticket prices to their cost
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


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


def calendar(request):
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

        # Save the selected ticket information in session
        basket_item = {
            'race': race_name,
            'ticket_type': ticket_type,
            'ticket_category': ticket_category,
            'quantity': quantity,
            'total_price': total_price,
        }
        basket = request.session.get('basket', [])
        basket.append(basket_item)
        request.session['basket'] = basket

    # Get all races and the default race based on the query parameters
    races = Race.objects.all()
    race_name = request.GET.get('race_name')
    default_race = get_object_or_404(
        Race, name=race_name) if race_name else races.first()

    context = {
        'races': races,
        'default_race': default_race,
    }
    return render(request, 'calendar.html', context)


def teams(request):
    return render(request, 'teams.html')


def drivers(request):
    return render(request, 'drivers.html')


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


def basket(request):
    basket_data = request.session.get('basket', [])

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add_to_basket':
            race_id = int(request.POST.get('race'))
            ticket_type = request.POST.get('ticket_type')
            ticket_category = request.POST.get('ticket_category')
            quantity = int(request.POST.get('quantity'))  # Convert to integer

            # Get the Race object based on the provided race_id
            try:
                race = Race.objects.get(id=race_id)
            except Race.DoesNotExist:
                # Handle the case where the race does not exist
                return redirect('calendar')  # Redirect back to the calendar

            # Calculate the total price based on the selected options
            option_key = f"{ticket_type}-{ticket_category}"
            total_price = ticket_prices.get(option_key, 0) * quantity

            # Save the ticket booking information with the user information
            Order.objects.create(
                user=request.user,
                race=race,
                ticket_type=ticket_type,
                ticket_category=ticket_category,
                quantity=quantity,
                total_price=total_price,
            )

            # Add the selected tickets to the basket
            basket_data.append({
                'race': race.display_name,
                'ticket_type': ticket_type,
                'ticket_category': ticket_category,
                'quantity': quantity,
                'total_price': total_price,
            })

            # Save the updated basket to the session
            request.session['basket'] = basket_data

            return redirect('calendar')  # Redirect back to the calendar

        elif action == 'buy_tickets':
            for item in basket_data:
                race_name = item['race']
                ticket_type = item['ticket_type']
                ticket_category = item['ticket_category']
                quantity = item['quantity']
                total_price = item['total_price']

                # Get the Race object based on the race name
                race = Race.objects.get(name=race_name)

                # Create and save the Order object
                Order.objects.create(
                    user=request.user,
                    race=race,
                    ticket_type=ticket_type,
                    ticket_category=ticket_category,
                    quantity=quantity,
                    total_price=total_price,
                )

            # Clear the session basket after completing the order
            request.session['basket'] = []

            return redirect('my_orders')

    basket = [(index, item) for index, item in enumerate(basket_data)]

    context = {
        'basket': basket,
        'race_name_to_id': race_name_to_id,
    }

    return render(request, 'basket.html', context)


def remove_from_basket(request, index):
    basket = request.session.get('basket', [])

    if 0 <= index < len(basket):
        # Remove the item at the specified index
        removed_item = basket.pop(index)
        request.session['basket'] = basket

    return redirect('basket')
