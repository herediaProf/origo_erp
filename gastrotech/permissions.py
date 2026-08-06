from django.core.exceptions import PermissionDenied


def role_required(allowed_roles=[]):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("/admin/login/")
            if request.user.role in allowed_roles or request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied("Você não tem permissão para acessar este setor.")

        return _wrapped_view

    return decorator
