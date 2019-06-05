from django.urls import reverse
from django.test import TestCase
from rest_framework import status

from .fibonacci_calculator import fibonnaci_calculator


class FibonacciCalculatorTests(TestCase):

    def setUp(self):
        self.result1 = fibonnaci_calculator(0)
        self.result2 = fibonnaci_calculator(1)
        self.result3 = fibonnaci_calculator(5)

    def test_calculated_fibonacci_sequences(self):
        self.assertTrue(self.result1, [0])
        self.assertEqual(self.result2, [0, 1])
        self.assertEqual(self.result3, [0, 1, 1, 2, 3])


class FibonacciApiViewTests(TestCase):

    def tests_are_not_working(self):
        url = reverse('fibonacci_api')
        data = {'number': 'not a numeric value'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

