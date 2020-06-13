import sys
import os
from io import BytesIO
from django.db import models
from users.models import CustomUser
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from common.utils import get_product_upload_destination

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    seller = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    order_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE)
    # product = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(
        upload_to=get_product_upload_destination)

    def __str__(self):
        return str(self.image.url)

    def save(self, *args, **kwargs):
        self.image = self.resize_image(self.image)
        super().save(*args, **kwargs)

    def resize_image(self, uploaded_image):
        img = Image.open(self.image)
        output_io_stream = BytesIO()
        resized_img = img.thumbnail((1000, 1000), Image.ANTIALIAS)
        img.save(output_io_stream, "JPEG", quality=90)
        output_io_stream.seek(0)
        uploaded_image = InMemoryUploadedFile(
            output_io_stream,
            'ImageField',
            '%s.jpg' % uploaded_image.name.split('.')[0],
            'image/jpeg',
            output_io_stream.getbuffer().nbytes,
            None)
        return uploaded_image
