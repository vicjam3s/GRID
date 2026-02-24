from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import random

from .models import Question
from .serializers import (
    QuestionSerializer,
    ExamGenerateSerializer,
    ExamSubmitSerializer,
)
from progress.models import ExamAttempt, QuestionAttempt
from django.conf import settings


class GenerateExamView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ExamGenerateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course_code = serializer.validated_data["course_code"]
        num_questions = serializer.validated_data["num_questions"]

        questions = Question.objects.filter(
            subtopic__topic__subject__course__code=course_code,
            is_active=True,
        )

        if questions.count() < num_questions:
            return Response(
                {"detail": "Not enough questions available."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        selected = random.sample(list(questions), num_questions)

        return Response(
            {"questions": QuestionSerializer(selected, many=True).data},
            status=status.HTTP_200_OK,
        )


class SubmitExamView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ExamSubmitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        answers = serializer.validated_data["answers"]

        questions = Question.objects.filter(
            id__in=[a["question_id"] for a in answers]
        )

        question_map = {q.id: q for q in questions}

        correct_count = 0
        failed_questions = []

        exam = ExamAttempt.objects.create(
            user=request.user,
            total_questions=len(answers),
            score=0,
            passed=False,
        )

        for answer in answers:
            question = question_map.get(answer["question_id"])
            if not question:
                continue

            is_correct = (
                answer["selected_option"] == question.correct_option
            )

            if is_correct:
                correct_count += 1
            else:
                failed_questions.append({
                    "question_id": question.id,
                    "question_text": question.question_text,
                    "correct_option": question.correct_option,
                    "explanation": question.explanation,
                })

            QuestionAttempt.objects.create(
                exam=exam,
                question=question,
                selected_option=answer["selected_option"],
                is_correct=is_correct,
            )

        score_percent = int((correct_count / len(answers)) * 100)
        passed = score_percent >= settings.EXAM_PASS_MARK_PERCENT

        exam.score = score_percent
        exam.passed = passed
        exam.save()

        return Response(
            {
                "score": score_percent,
                "passed": passed,
                "failed_questions": failed_questions,
            },
            status=status.HTTP_200_OK,
        )