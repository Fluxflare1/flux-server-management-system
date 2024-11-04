from django.test import TestCase
from django.contrib.auth.models import User

class RBACPermissionsTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin', role='admin')
        self.regular_user = User.objects.create_user(username='user', role='user')

    def test_tenant_management_access(self):
        self.client.force_login(self.regular_user)
        response = self.client.get('/manage-tenant/')
        self.assertEqual(response.status_code, 403)
