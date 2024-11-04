

from .utils.validation import validate_positive_integer, validate_email

def create_invoice(request):
    amount = request.POST.get('amount')
    user_email = request.POST.get('user_email')

    try:
        validate_positive_integer(amount, "Amount")
        validate_email(user_email)
        # Proceed with invoice creation
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)






from django.shortcuts import render
from django.http import JsonResponse
from .models import ReportSchedule

def create_report_schedule(request):
    if request.method == 'POST':
        # Parse and save report scheduling preferences
        # e.g., frequency, report_type, etc.
        data = json.loads(request.body)
        new_schedule = ReportSchedule.objects.create(
            user=request.user,
            report_type=data['report_type'],
            frequency=data['frequency']
        )
        return JsonResponse({'status': 'success', 'schedule_id': new_schedule.id})

def fetch_scheduled_reports(request):
    # Return a list of scheduled reports based on the user's settings
    reports = ReportSchedule.objects.filter(user=request.user)
    return JsonResponse(list(reports.values()), safe=False)




from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    # Logic to create a new user
    return JsonResponse({"message": "User created successfully"})

@csrf_exempt
@require_http_methods(["GET"])
def get_user(request, user_id):
    # Logic to retrieve a specific user by ID
    return JsonResponse({"message": f"User {user_id} details retrieved"})

@csrf_exempt
@require_http_methods(["PUT"])
def update_user(request, user_id):
    # Logic to update user details
    return JsonResponse({"message": f"User {user_id} updated successfully"})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    # Logic to delete a user by ID
    return JsonResponse({"message": f"User {user_id} deleted successfully"})




import psutil

@require_http_methods(["GET"])
def get_system_metrics(request):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()._asdict()
    storage_info = psutil.disk_usage('/')._asdict()

    metrics = {
        "cpu_usage": cpu_usage,
        "memory_info": memory_info,
        "storage_info": storage_info,
    }

    return JsonResponse(metrics)





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
