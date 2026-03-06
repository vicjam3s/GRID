from rest_framework import serializers
from .models import ExamAttempt


class ExamHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamAttempt
        fields = (
            "id",
            "total_questions",
            "score",
            "passed",
            "created_at",
        )

class ExamRetakeSerializer(serializers.Serializer):
    exam_id = serializers.IntegerField()
