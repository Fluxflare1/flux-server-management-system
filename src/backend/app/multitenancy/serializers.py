from rest_framework import serializers
from .models import Tenant, TenantResource

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class TenantResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantResource
        fields = '__all__'
