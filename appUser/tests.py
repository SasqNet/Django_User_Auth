import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_register(self):
        response = self.client.post(reverse('users-list'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        })
        print("Register Response Data: ", response.json())
        print("Register Response Status Code: ", response.status_code)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(get_user_model().objects.count(), 2)

    def test_retrieve(self):
        response = self.client.get(reverse('users-detail', args=[self.user.id]))
        print("Retrieve Response Data: ", response.json())
        print("Retrieve Response Status Code: ", response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.put(
            reverse('users-detail', args=[self.user.id]),
            data=json.dumps({
                'username': 'newusername',
                'email': 'newemail@example.com',
                'password': 'newpassword'
            }),
            content_type='application/json'
        )
        print("Update Response Data: ", response.json())
        print("Update Response Status Code: ", response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(reverse('users-detail', args=[self.user.id]))
        print("Delete Response Status Code: ", response.status_code)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(get_user_model().objects.count(), 0)