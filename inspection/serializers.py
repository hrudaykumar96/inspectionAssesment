from rest_framework import serializers
from .models import Inspections


class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspections
        fields = "__all__"
        read_only_fields = ['inspected_by', 'created_at']

    def validate_vehicle_number(self, value):
        if not value:
            raise serializers.ValidationError("Vehicle number is required.")
        return value

    def validate_damage_report(self, value):
        if not value:
            raise serializers.ValidationError("Damage report is required.")
        return value

    def validate_status(self, value):
        valid_statuses = ["pending", "reviewed", "completed"]
        if value not in valid_statuses:
            raise serializers.ValidationError(
                f"Status must be one of: {', '.join(valid_statuses)}."
            )
        return value

    def validate_image_url(self, value):
        valid_extensions = ["jpg", "jpeg", "png"]
        ext = value.name.split(".")[-1].lower()
        if ext not in valid_extensions:
            raise serializers.ValidationError(
                "Only .jpg, .jpeg, .png files are allowed."
            )
        return value
