import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Race, Order
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
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
        YOUR_DOMAIN = (
            "https://f1-tickets-e355687b93ca.herokuapp.com/"
        )

        created_order_ids = request.session.get('created_orders', [])

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
                        'name': f"{race_name} - {ticket_type}"
                                f"({ticket_category}) x{quantity}",
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

        # Clear previously created orders and their IDs
        for order_id in created_order_ids:
            try:
                order = Order.objects.get(id=order_id)
                order.delete()
            except Order.DoesNotExist:
                pass

        # Update session to reflect the cleared created orders
        request.session['created_orders'] = []

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=YOUR_DOMAIN + '/checkout_success',
            cancel_url=YOUR_DOMAIN + '/basket/',
        )

        request.session['checkout_session_id'] = checkout_session.id
        request.session['created_orders'] = [o.id for o in created_orders]

        return JsonResponse({'id': checkout_session.id})


def checkout_success(request):
    created_order_ids = request.session.get('created_orders', [])

    if created_order_ids:
        # Mark all created orders as paid
        Order.objects.filter(id__in=created_order_ids).update(paid=True)

        # Clear the user's basket and created_orders after successful payment
        request.session.pop('basket', None)
        request.session.pop('created_orders', None)

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

    return render(request, 'my_orders.html', context)


def basket(request):
    basket_data = request.session.get('basket', [])

    basket = [(index, item) for index, item in enumerate(basket_data)]

    context = {
        'basket': basket,
        'race_name_to_id': race_name_to_id,
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
    }

    return render(request, 'basket.html', context)


def edit_basket_item(request, index):
    basket_data = request.session.get('basket', [])
    created_order_ids = request.session.get('created_orders', [])

    if 0 <= index < len(basket_data):
        item = basket_data[index]
        original_order = item.copy()

        if request.method == 'POST':
            # Get the form data from request.POST
            race_name = request.POST.get('race')
            ticket_type = request.POST.get('ticket_type')
            ticket_category = request.POST.get('ticket_category')
            # Ensure quantity is an integer
            quantity = int(request.POST.get('quantity'))

            # Calculate the total price based on the selected options
            option_key = f"{ticket_type}-{ticket_category}"
            total_price = ticket_prices.get(option_key, 0) * quantity

            # Get the original order ID from created_order_ids
            if 0 <= index < len(created_order_ids):
                order_id = created_order_ids[index]

                try:
                    order = Order.objects.get(id=order_id)

                    # Update the order with the new information
                    order.race = Race.objects.get(name=race_name)
                    order.ticket_type = ticket_type
                    order.ticket_category = ticket_category
                    order.quantity = quantity
                    order.total_price = total_price  # Update the total_price

                    # Update the original_order with the edited data
                    original_order = {
                        'race': race_name,
                        'ticket_type': ticket_type,
                        'ticket_category': ticket_category,
                        'quantity': quantity,
                        'total_price': total_price,
                    }

                    # Update the basket_data with the edited order
                    basket_data[index] = original_order
                    request.session['basket'] = basket_data

                    order.save()  # Save the order with updated total_price
                except Order.DoesNotExist:
                    pass

            else:
                # Remove the original order from the basket
                basket_data.remove(original_order)

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
    basket_data = request.session.get('basket', [])
    created_order_ids = request.session.get('created_orders', [])

    if 0 <= index < len(basket_data):
        # Remove the item at the specified index
        removed_item = basket_data.pop(index)
        request.session['basket'] = basket_data

        # Remove the associated order from the database and created_orders
        if 0 <= index < len(created_order_ids):
            order_id = created_order_ids[index]
            try:
                order = Order.objects.get(id=order_id)
                order.delete()
                # Remove the order ID from created_orders
                created_order_ids.pop(index)
                # Update session
                request.session['created_orders'] = created_order_ids

            except Order.DoesNotExist:
                pass

    return redirect('basket')
