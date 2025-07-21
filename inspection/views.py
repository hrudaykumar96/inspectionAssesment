from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import InspectionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Inspections
from django.shortcuts import get_object_or_404


class InspectionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = InspectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(inspected_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        inspections = Inspections.objects.filter(inspected_by=request.user)
        serializer = InspectionSerializer(inspections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailedInspectionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        inspection = get_object_or_404(Inspections, pk=pk)
        if inspection.inspected_by != request.user:
            return Response({"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN)
        serializer = InspectionSerializer(inspection)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        inspection = get_object_or_404(Inspections, pk=pk)
        if inspection.inspected_by != request.user:
            return Response({"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN)
        serializer = InspectionSerializer(inspection, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inspection = get_object_or_404(Inspections, pk=pk)
        if inspection.inspected_by != request.user:
            return Response({"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN)
        inspection.delete()
        return Response(
            {"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class GetInspectViewByStatus(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, inspectionStatus):
        valid_statuses = ["pending", "reviewed", "completed"]
        if inspectionStatus not in valid_statuses:
            return Response(
                {
                    "error": f"Invalid status. Must be one of {', '.join(valid_statuses)}."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        inspection = Inspections.objects.filter(status=inspectionStatus)
        serializer = InspectionSerializer(inspection, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
