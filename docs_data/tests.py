from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Subdivision
from factory import django, Faker


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = Subdivision
    subdivision_name = Faker('name', locale='ru_RU')


class SubdivisionTests(APITestCase):
    def test_create_subdivision(self):
        for _ in range(100):
            print('fake', UserFactory())

        """
        Ensure we can create a new Subdivision object.
        """
        url = "http://localhost:8000/api/subdivisions/"
        data = {'subdivision_name': 'Subdivision1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)