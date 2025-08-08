from django.shortcuts import redirect


class CheckUserSensorPermissionMixin:
    """
    Mixin to check if the user has permission to access sensor-related views.
    """
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_staff or request.user.is_superuser):
            return redirect('details sensor')  # Redirect to Details Sensor if user is not staff or superuser

        return super().dispatch(request, *args, **kwargs)  # Proceed with the original dispatch method
