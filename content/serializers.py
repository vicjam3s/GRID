from rest_framework import serializers
from .models import ContentDocument, ContentChunk
from syllabus.models import Subtopic


class ContentUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    subtopic_id = serializers.IntegerField()

    def validate_subtopic_id(self, value):
        if not Subtopic.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid subtopic.")
        return value


class ContentChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentChunk
        fields = ("id", "text")