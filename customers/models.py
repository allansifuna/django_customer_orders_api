from django.db import models


class Customer(models.Model):

    username = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ['-created_at']
