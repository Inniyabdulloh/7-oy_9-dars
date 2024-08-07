from django.shortcuts import redirect
from rest_framework.response import Response

def decorator(func):
    def wrapper(*args, **kwargs):
        user = args[1].user
        if user.is_staff:
            return func(*args, **kwargs)
        return redirect("users:home")
    return wrapper


# decorator for api views
def is_staff(func):
    def wrapper(*args, **kwargs):
        user = args[1].user
        if user.is_staff:
            return func(*args, **kwargs)
        return Response("You are not a staff member", status=403)

    return wrapper