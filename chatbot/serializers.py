from rest_framework import serializers

class ChatSerializer(serializers.Serializer):
    message = serializers.CharField(required=True)
    model = serializers.CharField(default="llama3.1:8b")