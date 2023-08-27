import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Race, Order
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from decimal import Decimal
# Import login_required decorator
from django.contrib.auth.decorators import login_required


stripe.api_key = settings.STRIPE_SECRET_KEY

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


class CreateCheckoutSessionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        basket_data = request.session.get('basket', [])
        YOUR_DOMAIN = "https://8000-huddy2022-f1-tickets-gllzk9garf.us2.codeanyapp.com"

        line_items = []

        created_orders = []
        for item in basket_data:
            # Extract item details
            race_name = item['race']
            ticket_type = item['ticket_type']
            ticket_category = item['ticket_category']
            quantity = item['quantity']
            total_price = item['total_price']

            # Retrieve the Race instance based on the race_name
            race = Race.objects.get(name=race_name)

            line_items.append({
                'price_data': {
                    'currency': 'gbp',
                    'unit_amount': int(total_price * 100),
                    'product_data': {
                        'name': f"{race_name} - {ticket_type} ({ticket_category}) x{quantity}",
                    },
                },
                'quantity': 1,
            })

            # Create and save the Order objects
            order = Order.objects.create(
                user=request.user,
                race=race,  # Use the retrieved Race instance
                ticket_type=ticket_type,
                ticket_category=ticket_category,
                quantity=quantity,
                total_price=total_price,
            )
            created_orders.append(order)

            # Store the order ID in the session
            request.session['paid_order_id'] = order.id

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=YOUR_DOMAIN + '/checkout_success',
            cancel_url=YOUR_DOMAIN + '/basket/',
        )

        request.session['checkout_session_id'] = checkout_session.id

        return JsonResponse({'id': checkout_session.id})


def checkout_success(request):
    paid_order_id = request.session.get('paid_order_id')
    if paid_order_id:
        # Mark the order as paid using the order ID
        order = Order.objects.get(id=paid_order_id)
        order.paid = True
        order.save()

        # Clear the user's basket and paid_order_id after successful payment
        request.session.pop('basket', None)
        request.session.pop('paid_order_id', None)

    return redirect('my_orders')


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

        return redirect('basket')

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

    print(context)

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
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
    }

    return render(request, 'basket.html', context)


@login_required
def edit_basket_item(request, index):
    basket_data = request.session.get('basket', [])

    if 0 <= index < len(basket_data):
        item = basket_data[index]
        original_order = item.copy()

        if request.method == 'POST':
            # Get the form data from request.POST
            race_name = request.POST.get('race')
            ticket_type = request.POST.get('ticket_type')
            ticket_category = request.POST.get('ticket_category')
            quantity = request.POST.get('quantity')

            # Find the original order in the database
            try:
                order_to_edit = Order.objects.get(
                    user=request.user,
                    race__name=original_order['race'],
                    ticket_type=original_order['ticket_type'],
                    ticket_category=original_order['ticket_category'],
                    quantity=original_order['quantity'],
                    total_price=original_order['total_price']
                )

                # Update the order's fields with the new values
                order_to_edit.race = Race.objects.get(name=race_name)
                order_to_edit.ticket_type = ticket_type
                order_to_edit.ticket_category = ticket_category
                order_to_edit.quantity = quantity
                order_to_edit.total_price = ticket_prices.get(
                    f"{ticket_type}-{ticket_category}", 0) * int(quantity)
                order_to_edit.save()

                # Update the basket item in session
                basket_data[index] = {
                    'race': race_name,
                    'ticket_type': ticket_type,
                    'ticket_category': ticket_category,
                    'quantity': quantity,
                    'total_price': order_to_edit.total_price,
                }
                request.session['basket'] = basket_data

                return redirect('basket')
            except Order.DoesNotExist:
                # Handle the case where the order doesn't exist (optional)
                pass

    # Get all races and the default race based on the query parameters
    races = Race.objects.all()
    selected_race_name = request.GET.get('race_name', '')
    default_race = get_object_or_404(
        Race, name=selected_race_name) if selected_race_name else races.first()

    context = {
        'basket': basket_data,
        'original_order': original_order,
        'races': races,
        'selected_race_name': selected_race_name,
        'item_index': index,
    }

    return render(request, 'edit_basket_item.html', context)


def remove_from_basket(request, index):
    basket = request.session.get('basket', [])

    if 0 <= index < len(basket):
        # Get the removed item
        removed_item = basket.pop(index)
        request.session['basket'] = basket

        # Get the corresponding order's ID from the removed item
        order_race = removed_item['race']
        order_ticket_type = removed_item['ticket_type']
        order_ticket_category = removed_item['ticket_category']
        order_quantity = removed_item['quantity']
        order_total_price = removed_item['total_price']

        # Find and delete the corresponding order from the database
        try:
            order_to_delete = Order.objects.get(
                user=request.user,
                race__name=order_race,
                ticket_type=order_ticket_type,
                ticket_category=order_ticket_category,
                quantity=order_quantity,
                total_price=order_total_price
            )
            order_to_delete.delete()
        except Order.DoesNotExist:
            # Handle the case where the order doesn't exist (optional)
            pass

    return redirect('basket')
