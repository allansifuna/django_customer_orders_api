import africastalking

from django.conf import settings
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .serializers import OrdersSerializer
from .models import Order
from .utils import Util


# Initialize Africastalking
username = settings.AFRICASTALKING_USERNAME
api_key = settings.AFRICASTALKING_API_KEY

africastalking.initialize(username, api_key)
sms = africastalking.SMS


class OrderListAPIView(ListCreateAPIView):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        instance = serializer.save()

        message = "Your order has been created. Thank you for shopping with us!"

        customer_phone = [instance.customer.phone_number]

        Util.send_sms(sms, message, customer_phone)
        return instance

    def get_queryset(self):
        return self.queryset.all()


class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter()
