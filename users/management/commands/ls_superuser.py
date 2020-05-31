from django.core.management.base import BaseCommand
from users.models import CustomUser as User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.filter(is_superuser=True)
        print("### Below show superusers")
        for user in users:
            print(user.email)
