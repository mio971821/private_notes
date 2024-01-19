from django.contrib.auth.backends import BaseBackend
from .models import User_Account


class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User_Account.objects.get(email=email)
            if user.password == password:
                return user
        except User_Account.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User_Account.objects.get(pk=user_id)
        except User_Account.DoesNotExist:
            return None
