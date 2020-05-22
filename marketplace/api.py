from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import ProductSerializer
from .models import Product


@api_view(['GET', ])
@permission_classes([permissions.AllowAny])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    # users = CustomUser.object.all()
    # serializer = UserSerializer(users, )


@api_view(['POST', ])
@permission_classes([permissions.IsAuthenticated])
def create_product(request):

    print(request.user)
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(seller=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
