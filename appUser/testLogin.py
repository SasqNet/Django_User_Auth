import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class AuthTestCase(TestCase):
    def setUp(self):
        # Create a client instance to make requests
        self.client = Client()

        # Create a test user
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_login(self):
        # Make a POST request to the login endpoint
        response = self.client.post(reverse('dj_rest_auth:rest_login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains a token
        self.assertIn('key', response.json())

    def test_logout(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Make a POST request to the logout endpoint
        response = self.client.post(reverse('dj_rest_auth:rest_logout'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_user(self):
        # Log in the test user and get the token
        response = self.client.post(reverse('dj_rest_auth:rest_login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        token = response.json()['key']

        # Make a GET request to the user details endpoint with the token in the header
        response = self.client.get(reverse('dj_rest_auth:rest_user_details'), HTTP_AUTHORIZATION=f'Token {token}')

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the user details
        self.assertEqual(response.json()['username'], 'testuser')

    def test_password_change(self):
        # Log in the test user and get the token
        response = self.client.post(reverse('dj_rest_auth:rest_login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        token = response.json()['key']

        # Make a POST request to the password change endpoint with the token in the header
        response = self.client.post(reverse('dj_rest_auth:rest_password_change'), {
            'new_password1': 'newtestpassword',
            'new_password2': 'newtestpassword',
        }, HTTP_AUTHORIZATION=f'Token {token}')

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)