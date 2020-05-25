from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserManagerTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com', password='foo', first_name="payne", last_name="tang")

        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.first_name, 'payne')
        self.assertEqual(user.last_name, 'tang')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(TypeError):
            User.objects.create_user(email='')

        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='foo')

    def test_create_superuser(self):
        User = get_user_model()
        super_user = User.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(super_user.email, 'super@user.com')
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(super_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)
