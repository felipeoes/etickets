from rest_framework.response import Response

def error_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)})
    return wrapper