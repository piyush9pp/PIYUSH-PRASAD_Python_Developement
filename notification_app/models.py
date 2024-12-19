# notification_app/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
