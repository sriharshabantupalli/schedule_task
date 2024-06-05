from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Task(models.Model):
    name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    status = models.CharField(max_length=50, default='Pending')
