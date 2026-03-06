from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer used when SENDING questions to the user (exam generation).
    Does NOT expose the correct answer.
    """

    class Meta:
        model = Question
        fields = (
            "id",
            "question_text",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
        )


class ExamGenerateSerializer(serializers.Serializer):
    course_code = serializers.CharField()
    num_questions = serializers.IntegerField(min_value=1, max_value=100)


class AnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    selected_option = serializers.ChoiceField(
        choices=["A", "B", "C", "D"]
    )


class ExamSubmitSerializer(serializers.Serializer):
    answers = AnswerSerializer(many=True)