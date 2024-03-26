# inventory/serializers.py

# class InventoryItemSerializer(serializers.ModelSerializer):  # Rename the class here
#     class Meta:
#         model = InventoryItem
#         fields = '__all__'

# class InventorySerializer(serializers.Serializer):
#     instance_name = serializers.CharField(max_length=100)
#     host_ip = serializers.IPAddressField()
#     user = serializers.CharField(max_length=100)
#     ssh_key_path = serializers.CharField(max_length=200)
#     python_interpreter = serializers.CharField(max_length=200)

from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['instance_name', 'host_ip', 'user', 'ssh_key_path', 'python_interpreter']



