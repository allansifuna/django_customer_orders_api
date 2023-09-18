from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from users.models import User
from .service import GoogleLoginFlowService


class GoogleLoginFlowServiceTestCase(TestCase):
    def test_generate_state_session_token(self):
        google_login_service = GoogleLoginFlowService()
        state = google_login_service._generate_state_session_token()
        self.assertEqual(len(state), 30)


class GoogleLoginRedirectApiTestCase(TestCase):
    def test_google_login_redirect(self):
        self.client.session["google_oauth2_state"] = "test_state"

        response = self.client.get(reverse("redirect"))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)


class GoogleLoginApiTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="password")

    def test_google_login_successful(self):
        google_login_service = GoogleLoginFlowService()
        code = "test_code"
        state = "test_state"

        google_login_service.get_tokens = lambda *args, **kwargs: GoogleAccessTokens(
            "test_id_token", "test_access_token")
        google_login_service.get_user_info = lambda *args, **kwargs: {
            "email": "test@example.com"}

        self.client.session["google_oauth2_state"] = state

        response = self.client.get(reverse("callback"), data={
                                   "code": code, "state": state})

        self.assertEqual(self.client.session.get("google_oauth2_state"), None)

    def test_google_login_missing_code_state(self):
        response = self.client.get(reverse("callback"))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        self.user.delete()
