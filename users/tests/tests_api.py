from rest_framework.test import APITestCase
from ..models import CustomUser


class APITests(APITestCase):

    def run_test(self, method, url, body, **kwargs):
        headers = {}
        if kwargs:
            if kwargs['headers']:
                headers = kwargs['headers'].copy()

        if method == 'GET':
            resp = self.client.get(url, body, headers=headers)
        if method == 'POST':
            resp = self.client.post(url, body, headers=headers)
        return (resp.data, resp.status_code)

    def test_user_api(self):
        # test create user
        url = 'https://localhost:8000/api/user/register'
        body = {"email": "paynetestapi@gmail.com",
                "password": "paynetestapi@gmail.com",
                "fb_login": "true",
                "first_name": "Payne",
                "last_name": "Tang"}
        (resp, status) = self.run_test('POST', url, body)
        self.assertEqual(resp["user"]["email"], body["email"])
        self.assertEqual(resp["user"]["first_name"],
                         body["first_name"])
        self.assertEqual(resp["user"]["last_name"], body["last_name"])
        self.assertEqual(status, 200)

        # test login
        url = 'https://localhost:8000/api/user/login'
        body = {"email": "paynetestapi@gmail.com",
                "password": "paynetestapi@gmail.com",
                "fb_login": "true"}
        (resp, status) = self.run_test('POST', url, body)
        self.assertEqual(status, 200)

        # test get user info
        url = 'https://localhost:8000/api/user/'
        token = resp['token']
        resp = self.client.get(
            url, HTTP_AUTHORIZATION='Token {}'.format(token))
        self.assertEqual(resp.data['email'], body['email'])
        self.assertEqual(resp.data['fb_login'], True)

        # test failed login
        url = 'https://localhost:8000/api/user/login'
        body = {"email": "paynetestapi@gmail.com",
                "password": "paynetestapi@gmail.com",
                "fb_login": "false"}
        (resp, status) = self.run_test('POST', url, body)
        self.assertEqual(status, 401)
        self.assertEqual(
            resp['message'], 'This email logged in with Facebook, please try log in with Facebook!')

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
