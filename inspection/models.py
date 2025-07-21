from django.db import models
from django.contrib.auth.models import User

class Inspections(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('reviewed', 'reviewed'),
        ('completed', 'completed'),
    ]
    vehicle_number = models.CharField(max_length=100)
    inspected_by = models.ForeignKey(User, on_delete=models.CASCADE)
    damage_report = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    image_url = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)