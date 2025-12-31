from django.db import models
from volunteer.models import RequiredItem

class Donation(models.Model):
    donor_name = models.CharField(max_length=100)
    item = models.ForeignKey(RequiredItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    donation_method = models.CharField(
        max_length=20,
        choices=[('Direct', 'Direct'), ('Pickup', 'Pickup')]
    )
    status = models.CharField(max_length=30, default='Pending')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.donor_name


