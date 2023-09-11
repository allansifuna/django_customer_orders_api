from rest_framework import serializers
from .models import Order


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'item', 'amount']
