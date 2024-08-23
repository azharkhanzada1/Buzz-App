#
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
# class UserTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user_data = {
#             'username': 'testuser',
#             'email': 'testuser@example.com',
#             'password': 'testpassword123',
#             'phone_number': '1234567890'
#         }
#
#     def test_user_registration(self):
#         response = self.client.post(reverse('register'), self.user_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(User.objects.count(), 1)
#         self.assertEqual(User.objects.get().username, 'testuser')
#
#     def test_user_details(self):
#         user = User.objects.create_user(**self.user_data)
#         self.client.force_authenticate(user=user)
#         response = self.client.get(reverse('user-detail', kwargs={'username': user.username}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['username'], 'testuser')
#
#     def test_token_obtain(self):
#         user = User.objects.create_user(**self.user_data)
#         self.client.force_authenticate(user=user)
#         response = self.client.post(reverse('token_obtain_pair'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('refresh', response.data)
#         self.assertIn('access', response.data)