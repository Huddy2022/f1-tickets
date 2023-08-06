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
    if request.method == 'POST':
        # Get the selected race, ticket type, and other details from the form
        selected_race = request.POST.get('race')
        selected_ticket_type = request.POST.get('ticket_type')
        # You can add more form fields for other details like user information,
        # payment method, etc.

        # Placeholder logic for handling the ticket purchase
        # You can implement your actual ticket purchase logic here
        # For now, we'll just print the selected options
        print(f"Selected Race: {selected_race}")
        print(f"Selected Ticket Type: {selected_ticket_type}")

        # After processing the purchase, you may redirect to a
        # confirmation page
        # For example, you can create a `confirmation` view function to
        # handle this
        # return redirect('confirmation')

    races = [
        # List of dictionaries, each representing a race with its details
        {
            'name': 'Race 1',
            'date': '2023-08-01',
            'location': 'Sample Location',
        },
        # Add more races here
    ]

    context = {
        'races': races,
    }
    return render(request, 'buy_tickets.html', context)


def contact(request):
    return render(request, 'contact.html')
