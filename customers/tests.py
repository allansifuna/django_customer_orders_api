from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Customer
from .serializers import CustomersSerializer


class CustomerListAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_customers(self):
        response = self.client.get('/customers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_customer(self):
        data = {
            "username": "Test Customer",
            "phone_number": "+25413812939"
        }

        response = self.client.post('/customers/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CustomerDetailAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(
            username="Test Customer",
            phone_number="+25413812939"
        )

    def test_retrieve_customer(self):
        response = self.client.get(f'/customers/{self.customer.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_customer(self):
        data = {
            "username": "Updated Customer",
            "phone_number": "+25413812939"
        }

        response = self.client.put(
            f'/customers/{self.customer.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_customer(self):
        response = self.client.delete(f'/customers/{self.customer.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
