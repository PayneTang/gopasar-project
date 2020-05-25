import os
from rest_framework.test import APITestCase, APIClient
from ..models import Product
from ..serializers import ProductDetailSerializer
from users.models import CustomUser
from knox.models import AuthToken


class ProductTestCase(APITestCase):

    def setUp(self):
        self.seller = CustomUser.objects.create(
            email="paynetestapi@gmail.com", password="paynetestapi",
            fb_login=True,
            first_name="Payne",
            last_name="tester"
        )
        token = AuthToken.objects.create(self.seller)[1]
        self.client = APIClient(HTTP_AUTHORIZATION='Token ' + token)

        Product.objects.create(
            name="Setup product",
            description="This is a setup product for testing",
            price="15",
            seller=self.seller
        )

        Product.objects.create(
            name="Setup product 2",
            description="This is a second setup product for testing",
            price="12",
            seller=self.seller
        )

        products = Product.objects.all()
        serializer = ProductDetailSerializer(products, many=True)
        self.products = serializer.data

    def test_create_product(self):
        # , "image": open(os.path.join(os.path.dirname(__file__), 'test_data', 'IMG_2927.jpeg'), "rb")
        body = {"description": "Test product",
                "name": "Test product X", "price": "12"}
        resp = self.client.post(
            "https://localhost:8000/api/marketplace/product/", body, format="multipart")
        self.assertEqual(201, resp.status_code)
        self.assertEqual(resp.data['name'], body['name'])
        self.assertEqual(resp.data['description'], body['description'])

    def test_get_all_products(self):
        resp = self.client.get(
            "https://localhost:8000/api/marketplace/products/")
        self.assertEqual(resp.data, self.products)

    # def test_update_product(self):
