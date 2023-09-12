from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch
from .models import Order
from .utils import Util
from customers.models import Customer


class OrderListAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(
            username="Test Customer",
            phone_number="+254713812939",
        )

    def test_create_order(self):
        data = {
            "customer": self.customer.id,
            "item": "Laptop",
            "amount": "10000"
        }

        response = self.client.post(
            '/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_orders(self):
        response = self.client.get('/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OrderDetailAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(
            username="Test Customer",
            phone_number="+254713812939",
        )
        self.order = Order.objects.create(
            customer=self.customer,
            item="Laptop",
            amount="10000"
        )

    def test_retrieve_order(self):
        response = self.client.get(
            f'/orders/{self.order.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_order(self):
        data = {
            "item": "Updated Laptop",
            "customer": self.customer.id,
            "amount": "10000"
        }

        response = self.client.put(
            f'/orders/{self.order.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        response = self.client.delete(f'/orders/{self.order.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class UtilTest(TestCase):
    @patch('africastalking.SMS')
    def test_send_sms(self, mock_sms):
        message = "Test SMS Message"
        phone_numbers = ["+254713812939"]

        Util.send_sms(mock_sms, message, phone_numbers)

        mock_sms.send.assert_called_once_with(message, phone_numbers)
