from django.urls import path
from .views import SupportTicketView

urlpatterns = [
    path('support_tickets/', SupportTicketView.as_view(), name="support_tickets_list")
]
