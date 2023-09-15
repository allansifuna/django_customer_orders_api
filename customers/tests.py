from django.test import TestCase
from users.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Customer
from .serializers import CustomersSerializer


class CustomerListAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username="test_user", password="test_password")
        self.token, created = Token.objects.get_or_create(user=self.user)

    def test_list_customers(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/customers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_customer(self):
        data = {
            "username": "Test Customer",
            "phone_number": "+25413812939"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/customers/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CustomerDetailAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(
            username="Test Customer",
            phone_number="+25413812939"
        )
        self.user = User.objects.create(
            username="test_user", password="test_password")
        self.token, created = Token.objects.get_or_create(user=self.user)

    def test_retrieve_customer(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/customers/{self.customer.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_customer(self):
        data = {
            "username": "Updated Customer",
            "phone_number": "+25413812939"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            f'/api/customers/{self.customer.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_customer(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/customers/{self.customer.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
