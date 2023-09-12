from django.db import models
from customers.models import Customer


class Order(models.Model):

    item = models.CharField(max_length=255, blank=False)
    amount = models.IntegerField()
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ['-created_at']

    def __str__(self):
        return str(self.customer) + 's order'
