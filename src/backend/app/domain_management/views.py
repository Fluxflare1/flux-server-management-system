from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Domain

class DomainView(APIView):
    def get(self, request):
        domains = Domain.objects.all()
        return Response(domains)
