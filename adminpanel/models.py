from django.db import models

class RequiredItem(models.Model):
    item_name = models.CharField(max_length=100)
    required_quantity = models.PositiveIntegerField()
    received_quantity = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
