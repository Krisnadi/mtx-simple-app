from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return f'Bearer {str(refresh.access_token)}'


class AccountTests(APITestCase):

    def setUp(self):
        url = reverse('rest_register')
        data = {
            'email': 'test@example.com',
            'password1': '#Heihachi15',
            'password2': '#Heihachi15',
        }
        self.client.post(url, data, format='json')
        user = User.objects.get(email='test@example.com')
        self.token = get_tokens_for_user(user)

    def test_register_success(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('rest_register')
        data = {
            'email': 'alexanderkrisnadi@gmail.com',
            'password1': '#Heihachi15',
            'password2': '#Heihachi15',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.last().email, 'alexanderkrisnadi@gmail.com')

    def test_register_failed(self):
        """
        Registration with simple password should be failed.
        """
        url = reverse('rest_register')
        data = {
            'email': 'alexanderkrisnadi@gmail.com',
            'password1': 'testing',
            'password2': 'testing',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_register_existing(self):
        """
        Registration with existing email should be failed.
        """
        url = reverse('rest_register')
        data = {
            'email': 'test@example.com',
            'password1': '#Heihachi15',
            'password2': '#Heihachi15',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_resend_email_verification(self):
        """
        Ensure we can resend an email verification.
        """
        url = reverse('rest_resend_email')
        data = {
            'email': 'test@example.com',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_wrong_password(self):
        """
        Login with wrong password should be rejected.
        """
        url = reverse('rest_login')
        data = {
            'email': 'test@example.com',
            'password': 'testing',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_unverified(self):
        """
        Login with unverified email should be rejected.
        """
        url = reverse('rest_login')
        data = {
            'email': 'test@example.com',
            'password': '#Heihachi15',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_verified(self):
        """
        Login with verified email should be allowed.
        """
        EmailAddress.objects.filter(email='test@example.com').update(verified=True)
        url = reverse('rest_login')
        data = {
            'email': 'test@example.com',
            'password': '#Heihachi15',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profile_unauthorized(self):
        """
        Get user profile without token should be rejected.
        """
        url = reverse('rest_user_details')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_profile(self):
        """
        Get user profile.
        """
        url = reverse('rest_user_details')
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('email', response.data)
        self.assertIn('first_name', response.data)
        self.assertIn('last_name', response.data)

    def test_update_profile(self):
        """
        Update user profile first_name and last_name.
        """
        url = reverse('rest_user_details')
        data = {
            'first_name': 'first',
            'last_name': 'last',
        }
        response = self.client.patch(url, data, HTTP_AUTHORIZATION=self.token, format='json')
        user = User.objects.get(email='test@example.com')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.first_name, 'first')
        self.assertEqual(user.last_name, 'last')

    def test_change_password_wrong_old_password(self):
        """
        Change password with wrong old password should be rejected.
        """
        url = reverse('rest_password_change')
        data = {
            'old_password': 'testing',
            'new_password1': 'testing',
            'new_password2': 'testing',
        }
        response = self.client.post(url, data, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_password_simple_password(self):
        """
        Change password with simple old password should be rejected.
        """
        url = reverse('rest_password_change')
        data = {
            'old_password': '#Heihachi15',
            'new_password1': 'testing',
            'new_password2': 'testing',
        }
        response = self.client.post(url, data, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_password_success(self):
        """
        User can change password.
        """
        url = reverse('rest_password_change')
        data = {
            'old_password': '#Heihachi15',
            'new_password1': '#Heihachi1515',
            'new_password2': '#Heihachi1515',
        }
        response = self.client.post(url, data, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        """
        User can logout.
        """
        url = reverse('rest_logout')
        response = self.client.post(url, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
