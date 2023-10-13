from functools import wraps

def skip_authentication(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        request.user = request.user if request.user.is_authenticated else None
        return view_func(request, *args, **kwargs)
    return _wrapped_view
