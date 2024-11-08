from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from domain_management.domain_manager import DomainManager

class RegisterDomainView(APIView):
    def post(self, request):
        domain_name = request.data.get('domain_name')
        client_id = request.data.get('client_id')
        manager = DomainManager()
        try:
            result = manager.register_domain(domain_name, client_id)
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateDNSRecordView(APIView):
    def post(self, request):
        domain_name = request.data.get('domain_name')
        record_type = request.data.get('record_type')
        value = request.data.get('value')
        manager = DomainManager()
        try:
            result = manager.update_dns_record(domain_name, record_type, value)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
