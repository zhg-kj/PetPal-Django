from django.db import models
from apps.account.models import CustomUser


class Review(models.Model):
    reviewer = models.ForeignKey(CustomUser, related_name='reviews_given', on_delete=models.CASCADE)
    shelter = models.ForeignKey(CustomUser, related_name='reviews_received', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(6)])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
