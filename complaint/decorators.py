from django.shortcuts import redirect
from .models import Profile

def user_approved_by_admin(function):
    def wrap(request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

        if profile.approved:
            return function(request, *args, **kwargs)
        else:
            return redirect('not-approved')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__

    return wrap