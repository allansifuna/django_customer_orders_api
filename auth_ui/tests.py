from django.test import TestCase
from django.urls import reverse


class LoginViewTestCase(TestCase):
    def test_login_view_returns_200_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'auth_ui/google_login.html')
