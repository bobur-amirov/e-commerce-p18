from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, UpdateAPIView

from .serializers import UserCreateSerializer, UserUpdateSerializers


User = get_user_model()

class SignUp(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializers