# src/backend/app/server_management/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ServerInstance

class CreateServerView(APIView):
    def post(self, request):
        # Logic to create a server
        server = ServerInstance.objects.create(name=request.data.get('name'), status='stopped')
        return Response({"message": "Server created", "id": server.id}, status=status.HTTP_201_CREATED)

class StartServerView(APIView):
    def post(self, request, pk):
        # Logic to start a server
        server = ServerInstance.objects.get(pk=pk)
        server.status = 'running'
        server.save()
        return Response({"message": "Server started"}, status=status.HTTP_200_OK)

class StopServerView(APIView):
    def post(self, request, pk):
        # Logic to stop a server
        server = ServerInstance.objects.get(pk=pk)
        server.status = 'stopped'
        server.save()
        return Response({"message": "Server stopped"}, status=status.HTTP_200_OK)

class DeleteServerView(APIView):
    def delete(self, request, pk):
        # Logic to delete a server
        server = ServerInstance.objects.get(pk=pk)
        server.delete()
        return Response({"message": "Server deleted"}, status=status.HTTP_204_NO_CONTENT)
