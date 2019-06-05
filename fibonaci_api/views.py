from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .fibonacci_calculator import fibonnaci_calculator

class FibonacciView(APIView):

    def get(self, request):
        return Response({"test_field: Velcome to Fibonacci API app", status.HTTP_200_OK})

    def post(self, request):
        number = int(request.data.get('number'))
        result = fibonnaci_calculator(number)
        return Response(result)
