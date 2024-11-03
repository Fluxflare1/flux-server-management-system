# src/backend/app/views/server_management.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ServerInstance
from .serializers import ServerInstanceSerializer
from .tasks import create_vps, delete_vps, start_vps, stop_vps

class ServerManagementView(APIView):
    def post(self, request):
        """Create a new VPS instance."""
        serializer = ServerInstanceSerializer(data=request.data)
        if serializer.is_valid():
            instance = create_vps(serializer.validated_data)
            return Response({"message": "VPS created", "instance": instance}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a VPS instance."""
        delete_vps(pk)
        return Response({"message": "VPS deleted"}, status=status.HTTP_204_NO_CONTENT)

    def post_start(self, request, pk):
        """Start a VPS instance."""
        start_vps(pk)
        return Response({"message": "VPS started"}, status=status.HTTP_200_OK)

    def post_stop(self, request, pk):
        """Stop a VPS instance."""
        stop_vps(pk)
        return Response({"message": "VPS stopped"}, status=status.HTTP_200_OK)
