from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('reviewer', 'created_at', 'reviewer_name')

    def get_reviewer_name(self, obj):
        return obj.reviewer.name if obj.reviewer else None

    def create(self, validated_data):
        user = self.context['request'].user
        if not user.is_seeker:
            raise serializers.ValidationError("Only seekers can review shelters.")
        validated_data['reviewer'] = user
        return super().create(validated_data)
