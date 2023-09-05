import stripe
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch
from .models import Race, Order


class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

        # Create some sample races
        self.race1 = Race.objects.create(
            name='Test Race 1',
            date='2023-08-19',
            location='Test Location 1'
        )
        self.race2 = Race.objects.create(
            name='Test Race 2',
            date='2023-08-20',
            location='Test Location 2'
        )

        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_calendar_view(self):
        response = self.client.get(reverse('calendar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendar.html')

        # Test POST request to add items to the basket
        response = self.client.post(reverse('calendar'), {
            'race': self.race1.name,
            'ticket_type': 'friday',
            'ticket_category': 'general',
            'quantity': 2,
        })
        # Should redirect to basket
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('basket'))

    def test_teams_view(self):
        response = self.client.get(reverse('teams'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teams.html')

    def test_drivers_view(self):
        response = self.client.get(reverse('drivers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drivers.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_my_orders_view(self):
        response = self.client.get(reverse('my_orders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_orders.html')

    def test_basket_view(self):
        response = self.client.get(reverse('basket'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket.html')

    def test_checkout_success_view(self):
        response = self.client.get(reverse('checkout_success'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('my_orders'))

    @patch('stripe.checkout.Session.create')
    def test_create_checkout_session_view(self, stripe_create_mock):
        # Mock the Stripe API call
        mock_checkout_session = {
            'id': 'mocked-checkout-session-id',
            'payment_status': 'unpaid',  # Adjust this as needed
            # Add other required fields here as needed for your test
        }

        # Create a Stripe session object using the same structure as the mock
        stripe_session = stripe.checkout.Session.construct_from(
            mock_checkout_session, stripe.api_key
        ) 

        stripe_create_mock.return_value = stripe_session

        # Prepare the data to be sent in the POST request
        data = {
            'race': 'Test Race',
            'ticket_type': 'friday',
            'ticket_category': 'general',
            'quantity': 2,
        }

        response = self.client.post(reverse('create-checkout-session'), data)
        self.assertEqual(response.status_code, 200)

        # Ensure that the Stripe API was called with the expected data
        stripe_create_mock.assert_called_once_with(
            payment_method_types=['card'],
            line_items=[],  # Updated to match the actual implementation
            mode='payment',
            # Adjust this as needed
            success_url='https://f1-tickets-e355687b93ca.herokuapp.com/checkout_success',
            # Adjust this as needed
            cancel_url='https://f1-tickets-e355687b93ca.herokuapp.com/basket/',
        )

        # Check that the checkout session ID is stored in the session
        self.assertEqual(
            self.client.session['checkout_session_id'],
            stripe_session.id
        )

    def test_remove_from_basket_view(self):
        # Add an item to the basket
        response = self.client.post(reverse('calendar'), {
            'race': self.race1.name,
            'ticket_type': 'friday',
            'ticket_category': 'general',
            'quantity': 2,
        })
        # Should redirect to basket
        self.assertEqual(response.status_code, 302)

        # Get the item index from the session
        basket_data = self.client.session.get('basket', [])
        item_index = 0
        self.assertTrue(0 <= item_index < len(basket_data))

        # Remove the item from the basket
        response = self.client.get(
            reverse('remove_from_basket', args=[item_index]))
        # Should redirect to basket
        self.assertEqual(response.status_code, 302)

        # Ensure the item has been removed from the session
        basket_data = self.client.session.get('basket', [])
        self.assertEqual(len(basket_data), 0)

    def test_edit_basket_item_view(self):
        # Add an item to the basket
        response = self.client.post(reverse('calendar'), {
            'race': self.race1.name,
            'ticket_type': 'friday',
            'ticket_category': 'general',
            'quantity': 2,
        })
        # Should redirect to basket
        self.assertEqual(response.status_code, 302)

        # Get the item index from the session
        basket_data = self.client.session.get('basket', [])
        item_index = 0
        self.assertTrue(0 <= item_index < len(basket_data))

        # Edit the item in the basket
        response = self.client.post(reverse('edit_basket_item', args=[item_index]), {
            'race': self.race2.name,
            'ticket_type': 'sunday',
            'ticket_category': 'grandstand',
            'quantity': 3,
        })
        # Should redirect to basket
        self.assertEqual(response.status_code, 302)

        # Ensure the item in the basket has been updated
        basket_data = self.client.session.get('basket', [])
        self.assertEqual(len(basket_data), 1)
        updated_item = basket_data[0]
        self.assertEqual(updated_item['race'], self.race2.name)
        self.assertEqual(updated_item['ticket_type'], 'sunday')
        self.assertEqual(updated_item['ticket_category'], 'grandstand')
        self.assertEqual(updated_item['quantity'], 3)
