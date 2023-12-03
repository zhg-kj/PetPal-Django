from django.db import models
from apps.account.models import CustomUser


class Notification(models.Model):
    MODEL_CHOICES = (
        ('Application', 'Application'),
        ('Shelter', 'Shelter'),
    )

    user = models.ForeignKey(CustomUser, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    model_type = models.CharField(max_length=50, choices=MODEL_CHOICES)
    model_id = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
