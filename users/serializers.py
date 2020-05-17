from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import authenticate

from django.core.mail import EmailMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ('id', 'email')
        # note: fields all and exclude cannot be set together


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password',
                  'fb_login', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Remove 3 fields for special handling
        clone_validated_data = validated_data.copy()
        for key in ['email', 'password', 'fb_login']:
            try:
                del clone_validated_data[key]
            except KeyError:
                pass
        try:
            if validated_data['fb_login']:
                fb_login = True
            else:
                fb_login = False
        except KeyError:
            fb_login = False
        user = CustomUser.objects.create_user(
            validated_data['email'],
            validated_data['password'],
            fb_login=fb_login, **clone_validated_data)
        registered_user = CustomUser.objects.get(email=validated_data['email'])
        to_email = registered_user.get_email()
        email_content = EmailMessage(
            'Thanks for signing up with GoPasar!', 'Welcome!', to=[to_email], cc=['payne0107@gmail.com'])
        email_content.send()
        return user


class LoginSerializer(serializers.Serializer):
    # Get fields needed for authentication
    # Pending learn authenticate using email and password
    email = serializers.CharField()
    password = serializers.CharField()
    fb_login = serializers.BooleanField()

    def validate(self, data):
        print(data)
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
