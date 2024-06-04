# serializers.py
from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'created_at']  # Exclude 'name' from input fields

    def create(self, validated_data):
        validated_data['name'] = self.context['request'].user  # Set the 'name' field from the request context
        return super().create(validated_data)
