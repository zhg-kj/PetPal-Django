from django.db import models
from apps.account.models import CustomUser
from apps.pet.models import Pet


class Application(models.Model):
    STATUS_CHOICES = (
        ('Accepted', 'Accepted'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )

    seeker = models.ForeignKey(CustomUser, related_name='applications', on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, related_name='applications', on_delete=models.CASCADE)
    shelter = models.ForeignKey(CustomUser, related_name='shelter_applications', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    application = models.ForeignKey(Application, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
