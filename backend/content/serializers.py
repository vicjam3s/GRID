from rest_framework import serializers
from .models import ContentDocument, ContentChunk
from syllabus.models import Subject, Topic


class ContentUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    subject_id = serializers.IntegerField(required=False)
    topic_id = serializers.IntegerField(required=False)

    def validate_subject_id(self, value):
        if not Subject.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid subject.")
        return value

    def validate_topic_id(self, value):
        if not Topic.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid topic.")
        return value


class ContentChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentChunk
        fields = ("id", "text", "subject", "topic")