from django.urls import path
from .views import InspectionView, DetailedInspectionView, GetInspectViewByStatus

urlpatterns = [
    path('inspections/', InspectionView.as_view(), name='inspection-list-create'),
    path('inspection/id/<int:pk>/', DetailedInspectionView.as_view(), name='inspection-details'),
    path('inspection/status/<str:inspectionStatus>/', GetInspectViewByStatus.as_view(), name='inspection-details-by-status'),
]
