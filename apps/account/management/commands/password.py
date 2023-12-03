from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Generates hashed passwords'

    def handle(self, *args, **kwargs):
        password = input("Enter the password to hash: ")
        hashed_password = make_password(password)
        print(f"Hashed Password: {hashed_password}")
