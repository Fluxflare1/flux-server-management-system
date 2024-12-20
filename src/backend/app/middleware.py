

from django.http import JsonResponse

class RBACMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        # Check if user is authenticated
        if not user.is_authenticated:
            return JsonResponse({"error": "Unauthorized"}, status=401)

        # Check permissions based on requested URL
        if request.path.startswith("/admin") and not user.has_permission("manage_users"):
            return JsonResponse({"error": "Forbidden"}, status=403)

        if request.path.startswith("/developer") and not user.has_permission("access_developer_tools"):
            return JsonResponse({"error": "Forbidden"}, status=403)

        return self.get_response(request)




from django.core.cache import cache
from django.http import JsonResponse

class RateLimitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        request_count = cache.get(ip, 0)
        if request_count > 100:  # Limit to 100 requests per minute
            return JsonResponse({'error': 'Rate limit exceeded'}, status=429)
        else:
            cache.set(ip, request_count + 1, timeout=60)





import logging
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class ErrorHandlingMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        logger.error(f"Error: {exception}")
        return JsonResponse({'error': 'Internal Server Error'}, status=500)
