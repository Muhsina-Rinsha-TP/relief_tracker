from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    assigned_area = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Delivery(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    delivery_status = models.CharField(max_length=50, default='Collected')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.volunteer.name} ({self.delivery_status})"
