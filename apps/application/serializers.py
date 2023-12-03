from django.utils import timezone
from rest_framework import serializers
from .models import Application, Message


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ('seeker', 'shelter', 'created_at', 'updated_at',)

    def create(self, validated_data):
        user = self.context['request'].user
        if not user.is_seeker:
            raise serializers.ValidationError("Only seekers can create applications.")
        validated_data['seeker'] = user
        validated_data['shelter'] = validated_data['pet'].shelter
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.updated_at = timezone.now()
        instance.save()
        return instance


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('sender', 'time',)

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['sender'] = user
        return super().create(validated_data)
