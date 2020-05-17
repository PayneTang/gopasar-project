from django.contrib.auth.backends import BaseBackend
from .models import CustomUser


class ModelBackend(BaseBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(CustomUser.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = CustomUser._default_manager.get_by_natural_key(username)
        except CustomUser.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            CustomUser().set_password(password)
        else:
            if user.check_password(password):
                return user
