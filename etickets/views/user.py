from rest_framework.response import Response
from rest_framework.views import APIView

from etickets.models import User


def error_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)})
    return wrapper


# retrieve all user nodes
class UserList(APIView):
    @error_decorator
    def get(self, request):
        users = [user.to_dict() for user in User.nodes.all()]
        return Response(users)

# class for User CRUD operations
class UserDetail(APIView):
    @error_decorator
    def get(self, request, email):
        user = User.nodes.get(email=email)
        return Response(user.to_dict())

    @error_decorator
    def post(self, request):
        user = User(**request.data)
        user.save()
        return Response(user.to_dict())

    @error_decorator
    def put(self, request, email):
        user = User.nodes.get(email=email)
        user.__dict__.update(request.data)
        user.save()
        return Response(user.to_dict())

    @error_decorator
    def delete(self, request, email):
        user = User.nodes.get(email=email)
        user.delete()
        return Response(user.to_dict())
