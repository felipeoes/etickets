from rest_framework.response import Response
from rest_framework.views import APIView

from etickets.models import User
from django.shortcuts import render

def error_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)})
    return wrapper


class Index(APIView):
    @error_decorator
    def get(self, request):
        return render(request, 'teste/teste.html')  