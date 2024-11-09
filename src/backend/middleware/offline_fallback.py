# offline_fallback.py - Django middleware for offline request handling

from django.http import JsonResponse
import json

class OfflineFallbackMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 502:  # Bad gateway/offline
            # Offline fallback response
            fallback_data = {
                "error": "Server is currently offline. Data may be stale."
            }
            return JsonResponse(fallback_data, status=200)
        
        return response
