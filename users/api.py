from rest_framework.decorators import api_view, permission_classes

from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, UpdateUserSerializer, LoginSerializer, RegisterSerializer
from .models import CustomUser
from knox.models import AuthToken

from django.core.mail import EmailMessage


# Retrieve user from token
@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticated])
def retrieve_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

# GET
@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticated])
def get_user(request):
    try:
        user = CustomUser.objects.get(id=pk)
    except CustomUser.DoesNotExist:
        return Response({"error": "user not found"})

    serializer = UserSerializer(user)
    return Response(serializer.data)


# GET ALL
@api_view(['GET'])
def list_all_users(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def check_user(request):
    email = request.query_params['email']
    user = CustomUser.objects.filter(email=email)
    # print(user)
    if user:
        return Response({"email": user[0].email, "fb_login": user[0].fb_login})
    else:
        return Response(status=404)


# UPDATE
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_user(request):
    user = request.user
    # try:
    #     user = CustomUser.objects.get(id=pk)
    # except CustomUser.DoesNotExist:
    #     return Response({"error": "user not found"})

    serializer = UpdateUserSerializer(user, data=request.data)
    # print(serializer.instance)
    if serializer.is_valid():
        serializer.save()
        output = UserSerializer(user)
        return Response(output.data)  # return updated
    else:
        return Response(serializer.errors)


# REGISTER
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


# LOGIN
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
