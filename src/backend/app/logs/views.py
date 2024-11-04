from django.core.paginator import Paginator
from django.db.models import Q

def get_activity_logs(request):
    page = request.GET.get('page', 1)
    filters = Q()

    # Apply filters based on request params
    if request.GET.get('action_type'):
        filters &= Q(action_type=request.GET.get('action_type'))
    if request.GET.get('user_id'):
        filters &= Q(user_id=request.GET.get('user_id'))

    logs = ActivityLog.objects.filter(filters).order_by('-timestamp')
    paginator = Paginator(logs, 10)  # 10 logs per page
    return paginator.get_page(page)
