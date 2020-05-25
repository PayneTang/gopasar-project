from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Product, ProductImage
from users.serializers import UserSerializer


class ProductDetailSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class UpdateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = ('price',)
        fields = ('name', 'price', 'description')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.save()
        return instance


class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = '__all__'

    def get_url(self, obj):
        request = self.context.get('request')
        url = obj.image.url
        return request.build_absolute_uri(url)


class ProductImageRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'
