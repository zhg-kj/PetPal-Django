from django.utils import timezone
from rest_framework import serializers
from .models import Application, Message


class ApplicationSerializer(serializers.ModelSerializer):
    seeker_name = serializers.SerializerMethodField()
    shelter_name = serializers.SerializerMethodField()
    pet_name = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ('seeker', 'shelter', 'created_at', 'updated_at', 'seeker_name', 'shelter_name', 'pet_name')

    def get_seeker_name(self, obj):
        return obj.seeker.name if obj.seeker else None

    def get_shelter_name(self, obj):
        return obj.shelter.name if obj.shelter else None

    def get_pet_name(self, obj):
        return obj.pet.name if obj.pet else None

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
    sender_name = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('sender', 'time', 'sender_name',)

    def get_sender_name(self, obj):
        return obj.sender.name if obj.sender else None

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['sender'] = user
        return super().create(validated_data)
