from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
        extra_kwargs = {'shelter': {'read_only': True}}

    def create(self, validated_data):
        user = self.context['request'].user
        if not user.is_seeker:
            validated_data['shelter'] = user
        else:
            raise serializers.ValidationError("Only shelters can create pets.")
        return super().create(validated_data)
