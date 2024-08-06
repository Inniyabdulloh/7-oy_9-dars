from django.shortcuts import redirect


def decorator(func):
    def wrapper(*args, **kwargs):
        ...
        user = args[1].user
        if user.is_staff:
            return func(*args, **kwargs)
        return redirect("users:home")
    return wrapper