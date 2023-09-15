from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class UserManagerTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username="adminuser",
            email="admin@example.com",
            password="adminpassword"
        )
        self.assertEqual(admin_user.username, "adminuser")
        self.assertEqual(admin_user.email, "admin@example.com")
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class UserModelTestCase(TestCase):
    def test_user_str(self):
        user = User(username="testuser", email="test@example.com")
        self.assertEqual(str(user), "test@example.com")


class UserTokensTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )

    def test_user_tokens_generation(self):
        tokens = self.user.tokens()

        self.assertTrue('refresh' in tokens)
        self.assertTrue('access' in tokens)

        self.assertIsNotNone(tokens['refresh'])
        self.assertIsNotNone(tokens['access'])
