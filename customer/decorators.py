from django.shortcuts import redirect


def sign_in_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            func(request, *args, **kwargs)
            return func(request, *args, **kwargs)
        else:
            return redirect("signin")
    return wrapper

