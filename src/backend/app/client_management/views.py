from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client

class ClientView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        return Response(clients)
