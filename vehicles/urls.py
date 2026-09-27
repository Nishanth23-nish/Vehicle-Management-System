from django.urls import path

from .views import (
    ContactView,
    DriverCreateView,
    DriverDeleteView,
    DriverListView,
    DriverUpdateView,
    DashboardView,
    MaintenanceView,
    VehicleCreateView,
    VehicleCSVExportView,
    VehicleDeleteView,
    VehicleDetailView,
    VehicleExcelExportView,
    VehicleListView,
    VehiclePDFExportView,
    VehicleUpdateView,
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('vehicles/', VehicleListView.as_view(), name='vehicle-list'),
    path('drivers/', DriverListView.as_view(), name='driver-list'),
    path('drivers/new/', DriverCreateView.as_view(), name='driver-create'),
    path('drivers/<int:pk>/edit/', DriverUpdateView.as_view(), name='driver-update'),
    path('drivers/<int:pk>/delete/', DriverDeleteView.as_view(), name='driver-delete'),
    path('maintenance/', MaintenanceView.as_view(), name='maintenance'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('export/csv/', VehicleCSVExportView.as_view(), name='vehicle-export-csv'),
    path('export/excel/', VehicleExcelExportView.as_view(), name='vehicle-export-excel'),
    path('export/pdf/', VehiclePDFExportView.as_view(), name='vehicle-export-pdf'),
    path('vehicles/new/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicles/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicles/<int:pk>/edit/', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('vehicles/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle-delete'),
]
