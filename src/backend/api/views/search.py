from django.http import JsonResponse
from django.db.models import Q
from .models import Server, Invoice, Ticket

def global_search_view(request):
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse({"results": []})
    
    server_results = Server.objects.filter(Q(name__icontains=query) | Q(ip_address__icontains=query))
    invoice_results = Invoice.objects.filter(reference__icontains=query)
    ticket_results = Ticket.objects.filter(subject__icontains=query)

    results = {
        "servers": [{"id": s.id, "name": s.name} for s in server_results],
        "invoices": [{"id": i.id, "reference": i.reference} for i in invoice_results],
        "tickets": [{"id": t.id, "subject": t.subject} for t in ticket_results],
    }
    return JsonResponse({"results": results})
