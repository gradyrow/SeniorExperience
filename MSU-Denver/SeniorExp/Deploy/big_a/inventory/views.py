from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import InventorySerializer
from django.conf import settings
import os

# Create your views here.
# inventory/views.py


class InventoryAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            # You can now use the validated data from the serializer
            inventory_entry = f"""[aws_instances]
{data['instance_name']} ansible_host={data['host_ip']} ansible_user={data['user']} ansible_ssh_private_key_file={data['ssh_key_path']} ansible_python_interpreter={data['python_interpreter']}
"""
            # file_name = "/path/to/your/inventory_directory/ansible_inventory.ini"  # Specify the path where you want to save the file
            # os.makedirs(os.path.dirname(file_name), exist_ok=True)
            # with open(file_name, "w") as file:
            #     file.write(inventory_entry)

            file_name = os.path.join(settings.MEDIA_ROOT, "ansible_inventory.ini")
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
            with open(file_name, "w") as file:
                file.write(inventory_entry)
            
            return Response({"message": "Inventory file created successfully.", "file_name": file_name}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
