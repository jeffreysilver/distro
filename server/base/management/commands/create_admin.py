from django.contrib.auth.models import User as DjangoUser
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("CREATING ADMIN")
        admin, created = DjangoUser.objects.get_or_create(username="admin")
        if created:
            admin.set_password("admin")
            admin.is_superuser = True
            admin.is_staff = True
            admin.save()
