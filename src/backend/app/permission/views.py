from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Role, Permission

class RoleView(APIView):
    def get(self, request):
        roles = Role.objects.all()
        return Response(roles)
