import re
from django.contrib.auth.models import AnonymousUser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .serializers import ProductDetailSerializer, UpdateProductSerializer, ProductImageSerializer, CreateProductSerializer, ProductImageRetrieveSerializer
from .models import Product, ProductImage

from rest_framework.views import APIView


class ProductListAPI(generics.GenericAPIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)


# class ProductImageListAPI(generics.GenericAPIView):

#     def get(self, request):
#         images = ProductImage.objects.all()
#         serializer = ProductImageRetrieveSerializer(images, many=True)
#         return Response(serializer.data)


class ProductDetailAPI(generics.GenericAPIView):

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        product = Product.objects.get(id=pk)
        return product

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductDetailSerializer(product)
        retrieved_product = serializer.data
        # if retrieved_product['seller']:
        #     print(retrieved_product['seller'])
        # else:
        #     print('is None!')
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)

        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        elif request.user.email != product.seller.email:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = UpdateProductSerializer(
            instance=product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class CreateProductAPI(generics.GenericAPIView):

    parser_classes = [FormParser, MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(seller=request.user)
            img_context = []
            for key in request.data:
                if re.match("image", key):
                    img_context.append(
                        {'image': request.data[key],
                         'product': serializer.data['id']})
            img_serializer = ProductImageSerializer(
                data=img_context, many=True)
            if img_serializer.is_valid():
                img_serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST', ])
# @permission_classes([permissions.IsAuthenticated])
# def create_product(request):

#     print(request.user)
#     serializer = CreateProductSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save(seller=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductImageAPI(generics.GenericAPIView):

#     parser_classes = [FormParser, MultiPartParser]

#     def post(self, request):
#         print(request.data)
#         serializer = ProductImageSerializer(data=request.data)
#         if serializer.is_valid():
#             print("valid!")
#             serializer.save()
#         else:
#             print("not valid!")
#         print(serializer.data)
#         return Response({"message": "file upload!"})
