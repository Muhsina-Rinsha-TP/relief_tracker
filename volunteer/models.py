# Create your models here.
from django.db import models

class RequiredItem(models.Model):
    item_name = models.CharField(max_length=100)
    quantity_required = models.IntegerField()
    quantity_received = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
    
class Delivery(models.Model):
    volunteer_name = models.CharField(max_length=100)
    delivery_status = models.CharField(max_length=30, default='Collected')
    updated_at = models.DateTimeField(auto_now=True)

