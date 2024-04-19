# from django.contrib.auth.backends import BaseBackend
# from .models import CustomUser

# class CustomUserAuthBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None):
#         try:
#             user = CustomUser.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#         except CustomUser.DoesNotExist:
#             return None



from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import CustomUser

class CustomUserAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = CustomUser.objects.get(username=username)
            if check_password(password, user.password):
                return user
            else:
                return None
        except CustomUser.DoesNotExist:
            return None
