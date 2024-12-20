from django.core.management.base import BaseCommand
from app.models import Role, Permission

class Command(BaseCommand):
    help = "Seed initial roles and permissions"

    def handle(self, *args, **kwargs):
        roles = [
            {"name": "Admin", "description": "Full access to all system resources."},
            {"name": "Developer", "description": "Access to development-related resources."},
            {"name": "End-User", "description": "Basic access to use the system."},
        ]

        permissions = [
            {"name": "manage_users", "description": "Manage user accounts."},
            {"name": "view_reports", "description": "View system reports."},
            {"name": "access_developer_tools", "description": "Access developer-specific tools."},
        ]

        for role in roles:
            Role.objects.get_or_create(**role)

        for permission in permissions:
            perm, _ = Permission.objects.get_or_create(**permission)
            if permission["name"] == "manage_users":
                perm.roles.add(Role.objects.get(name="Admin"))
            if permission["name"] == "access_developer_tools":
                perm.roles.add(Role.objects.get(name="Developer"))
            perm.save()

        self.stdout.write(self.style.SUCCESS("Roles and permissions seeded successfully!"))
