from django.db import models
from adminpanel.models import RequiredItem

class Donor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    item = models.ForeignKey(RequiredItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    donation_method = models.CharField(
        max_length=20,
        choices=[('Direct', 'Direct'), ('Pickup', 'Pickup')]
    )
    status = models.CharField(max_length=30, default='Pending')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.name} - {self.item.item_name}"
