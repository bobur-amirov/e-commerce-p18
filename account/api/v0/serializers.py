from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    # password1 = serializers.CharField(max_length=100, write_only=True)
    password2 = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {

            'password': {'write_only': True}
        }

    def validate(self, data):
        password = data.get('password')
        password2 = data.pop('password2')
        if password != password2:
            raise serializers.ValidationError("password1 does not match password2")
        return data

    def create(self, data):
        user = User(
            username=data['username'],
            email=data['email']
        )
        user.set_password(data['password'])
        user.save()
        return user


class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone']


