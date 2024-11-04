from functools import wraps
from django.http import HttpResponseForbidden

def role_required(roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role not in roles:
                return HttpResponseForbidden("You do not have permission to perform this action.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
