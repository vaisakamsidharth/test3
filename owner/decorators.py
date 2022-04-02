from django.shortcuts import redirect


def owner_sign_in_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return func(request, *args, **kwargs)
        else:
            return redirect("signin")
    return wrapper
