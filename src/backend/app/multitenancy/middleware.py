from django.utils.deprecation import MiddlewareMixin
from .models import Tenant

class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tenant_id = request.META.get('HTTP_TENANT_ID')
        if tenant_id:
            request.tenant = Tenant.objects.get(id=tenant_id)
        else:
            request.tenant = None
