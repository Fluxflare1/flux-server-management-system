from django.urls import path
from .views import DomainView

urlpatterns = [
    path('domains/', DomainView.as_view(), name="domains_list")
]
