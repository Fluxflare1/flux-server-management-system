from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import subprocess

@require_http_methods(["POST"])
def create_server(request):
    # Logic to create a new server instance
    return JsonResponse({"message": "Server created successfully"})

@require_http_methods(["POST"])
def start_server(request, server_id):
    # Logic to start the server instance with the given ID
    return JsonResponse({"message": f"Server {server_id} started successfully"})

@require_http_methods(["POST"])
def stop_server(request, server_id):
    # Logic to stop the server instance with the given ID
    return JsonResponse({"message": f"Server {server_id} stopped successfully"})

@require_http_methods(["DELETE"])
def delete_server(request, server_id):
    # Logic to delete the server instance with the given ID
    return JsonResponse({"message": f"Server {server_id} deleted successfully"})
