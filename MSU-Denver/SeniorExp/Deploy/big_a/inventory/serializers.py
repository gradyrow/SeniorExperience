# inventory/serializers.py
from rest_framework import serializers

class InventorySerializer(serializers.Serializer):
    instance_name = serializers.CharField(max_length=100)
    host_ip = serializers.IPAddressField()
    user = serializers.CharField(max_length=100)
    ssh_key_path = serializers.CharField(max_length=200)
    python_interpreter = serializers.CharField(max_length=200)
