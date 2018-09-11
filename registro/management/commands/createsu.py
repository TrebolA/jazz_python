from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="10music").exists():
            User.objects.create_superuser("10music", "admin@admin.com", "10music")
