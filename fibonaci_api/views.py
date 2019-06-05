from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class FibonacciView(APIView):

    def get(self, request):
        return Response({"test_field: Velcome to Fibonacci API app", status.HTTP_200_OK})

    def post(self, request):
        data = request.data.get('number')
        return Response({"success: you posted {}".format(data), status.HTTP_200_OK})
