from django.urls import path
from .views import InventoryAPIView

urlpatterns = [
    path('create_inventory/', InventoryAPIView.as_view(), name='create_inventory'),
]
