from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, UpdateUserSerializer, LoginSerializer, RegisterSerializer
from .models import CustomUser
from knox.models import AuthToken

from django.core.mail import EmailMessage

from common.utils import blob_exists, retrieve_upload_relative_path, delete_blob

# Retrieve user from token
@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticated])
def retrieve_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

# GET
@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticated])
def get_user(request, pk):
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
        return Response({"email": user[0].email, "fb_login": user[0].fb_login, "google_login": user[0].google_login})
    else:
        return Response(status=404)


class UpdateUserAPI(generics.GenericAPIView):
    parser_classes = [FormParser, MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        """
        When there is image upload in request data, and user already has avatar image
        will remove existing image before upload the new one
        """
        user = request.user
        if request.data['avatar'] and user.avatar:
            blob_path = retrieve_upload_relative_path(user.avatar.url)
            if blob_exists(blob_path):
                delete_blob(blob_path)
        serializer = UpdateUserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            output = UserSerializer(user)
            return Response(output.data)
        else:
            return Response(serializer.errors)
# @api_view(['PUT'])
# def update_user(request):
#     user = request.user
#     # try:
#     #     user = CustomUser.objects.get(id=pk)
#     # except CustomUser.DoesNotExist:
#     #     return Response({"error": "user not found"})

#     serializer = UpdateUserSerializer(user, data=request.data)
#     # print(serializer.instance)
#     if serializer.is_valid():
#         serializer.save()
#         output = UserSerializer(user)
#         return Response(output.data)  # return updated
#     else:
#         return Response(serializer.errors)


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

        # Custom: Check FB and Google login status, return unauthorized if invalid
        social_login = {'fb_login': False, 'google_login': False}

        for method in social_login.keys():
            try:
                if request.data[method]:
                    social_login[method] = True
            except KeyError:
                pass

        if user.fb_login:
            if not social_login['fb_login']:
                return Response({'message': "This email logged in with Facebook, please try log in with Facebook!"}, status=401)

        if user.google_login:
            if not social_login['google_login']:
                return Response({'message': "This email logged in with Google, please try log in with Google!"}, status=401)

        if any(social_login.values()):
            if not user.fb_login and not user.google_login:
                return Response({"message": "This email has been registered, please log in with the email directly!"}, status=401)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
