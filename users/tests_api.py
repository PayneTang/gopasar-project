from rest_framework.test import APITestCase
from .models import CustomUser


class APITests(APITestCase):

    def test_user_api(self):
        # test create user
        data = {"email": "paynetestapi@gmail.com",
                "password": "12345678", "fb_login": "true"}
        response = self.client.post(
            'https://localhost:8000/api/user/register', data)
        self.assertEqual(response.data["user"]["email"], data["email"])
        self.assertEqual(response.status_code, 200)

        # test login
        response = self.client.post(
            'https://localhost:8000/api/user/login', data)
        self.assertEqual(response.status_code, 200)

        # check existing email
        response = self.client.get(
            'https://localhost:8000/api/user/check?email=paynetestapi@gmail.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data, {"email": "paynetestapi@gmail.com", "fb_login": True})

        # check email that does not exist
        response = self.client.get(
            'https://localhost:8000/api/user/check?email=paynetestapi2@gmail.com')
        self.assertEqual(response.status_code, 404)
        self.assertNotEqual(response.data, "paynetestapi@gmail.com")
