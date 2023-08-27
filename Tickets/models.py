from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Race(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    TICKET_TYPES = [
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
        ('all', 'All 3 Days'),
    ]

    TICKET_CATEGORIES = [
        ('general', 'General Admission'),
        ('grandstand', 'Grandstand Seat'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=10, choices=TICKET_TYPES)
    ticket_category = models.CharField(
        max_length=10, choices=TICKET_CATEGORIES)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    # Add the total_price field
    total_price = models.IntegerField(default=0)  # cents

    # Add new field to track payment status
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.race.name}"
        f" - {self.ticket_type} ({self.ticket_category})"
