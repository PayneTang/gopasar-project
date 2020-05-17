from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer
from .models import CustomUser
from knox.models import AuthToken

from django.core.mail import EmailMessage


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class CheckUserAPI(APIView):
    def get(self, request):
        email = request.query_params['email']
        user = CustomUser.objects.filter(email=email)
        if user:
            return Response({"email": user[0].email, "fb_login": user[0].fb_login})
        else:
            return Response(status=404)


class UserListAPI(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        # Custom: check if the user logged with FB
        if request.data["fb_login"].lower() == "true":
            request_fb_login = True
        else:
            request_fb_login = False

        if user.fb_login:
            # Pre-process fb_login to boolean
            if not request_fb_login:
                return Response({'message': "This email logged in with Facebook, please try log in with Facebook!"}, status=401)
        else:
            if request_fb_login:
                return Response({"message": "This email has been registered, please log in with the email directly!"}, status=401)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
