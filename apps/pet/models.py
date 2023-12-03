from django.db import models
from apps.account.models import CustomUser


class Pet(models.Model):
    TYPE_CHOICES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
    )
    SIZE_CHOICES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Waitlisted', 'Waitlisted'),
        ('Adopted', 'Adopted'),
    )

    shelter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    age = models.IntegerField()
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    description = models.TextField()
    medical_history = models.TextField()
    behavior = models.TextField()
    needs = models.TextField()
    image1 = models.URLField()
    image2 = models.URLField()
