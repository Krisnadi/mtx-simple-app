from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountTests(APITestCase):

    def test_user_statistic(self):
        """
        Ensure we can get user statistic.
        """
        url = reverse('user_statistic')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_signup', response.data)
        self.assertIn('today_active_session', response.data)
        self.assertIn('average_active_session', response.data)

    def test_user_list(self):
        """
        Ensure we can get user list.
        """
        url = reverse('user-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
