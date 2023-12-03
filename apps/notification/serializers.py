from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ('read', 'time')

    def create(self, validated_data):
        return Notification.objects.create(read=False, **validated_data)
