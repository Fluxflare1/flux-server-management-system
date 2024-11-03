from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tenant

class TenantView(APIView):
    def get(self, request):
        tenants = Tenant.objects.all()
        return Response(tenants)
