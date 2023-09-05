from django.test import TestCase
from .models import Race, Order
from django.contrib.auth.models import User


class RaceModelTest(TestCase):
    def setUp(self):
        self.race = Race.objects.create(
            name='Test Race',
            date='2023-08-19',
            location='Test Location'
        )

    def test_race_name(self):
        self.assertEqual(str(self.race), 'Test Race')

    def test_race_date(self):
        self.assertEqual(str(self.race.date), '2023-08-19')

    def test_race_location(self):
        self.assertEqual(str(self.race.location), 'Test Location')


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.race = Race.objects.create(
            name='Test Race',
            date='2023-08-19',
            location='Test Location'
        )
        self.order = Order.objects.create(
            user=self.user,
            race=self.race,
            ticket_type='friday',
            ticket_category='general',
            quantity=2,
            total_price=2000,  # Adjust this as needed
            paid=True,
        )

    def test_order_user(self):
        self.assertEqual(str(self.order.user), 'testuser')

    def test_order_race(self):
        self.assertEqual(str(self.order.race), 'Test Race')

    def test_order_ticket_type(self):
        self.assertEqual(str(self.order.ticket_type), 'friday')

    def test_order_ticket_category(self):
        self.assertEqual(str(self.order.ticket_category), 'general')

    def test_order_quantity(self):
        self.assertEqual(self.order.quantity, 2)

    def test_order_total_price(self):
        self.assertEqual(self.order.total_price, 2000)

    def test_order_paid(self):
        self.assertEqual(self.order.paid, True)
