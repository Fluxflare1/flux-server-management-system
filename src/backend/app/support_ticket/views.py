from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SupportTicket

class SupportTicketView(APIView):
    def get(self, request):
        tickets = SupportTicket.objects.all()
        return Response(tickets)
