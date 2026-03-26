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
from progress.models import ExamAttempt, FailedQuestion
from django.conf import settings
from syllabus.models import Course, Subject


class GenerateExamView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ExamGenerateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course_code = serializer.validated_data["course_code"]
        num_questions = serializer.validated_data["num_questions"]

        questions = Question.objects.filter(
            subject__course__code=course_code,
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
        course_id = serializer.validated_data["course_id"]
        subject_id = serializer.validated_data["subject_id"]

        questions = Question.objects.filter(
            id__in=[a["question_id"] for a in answers]
        )

        question_map = {q.id: q for q in questions}

        correct_count = 0
        failed_questions = []

        exam = ExamAttempt.objects.create(
            user=request.user,
            course_id=course_id,
            subject_id=subject_id,
            total_questions=len(answers),
            score=0,
            percentage=0,
            passed=False,
        )

        for answer in answers:
            question = question_map.get(answer["question_id"])
            if not question:
                continue

            selected = answer["selected_option"]
            is_correct = selected == question.correct_option

            if is_correct:
                correct_count += 1
            else:
                failed_questions.append({
                    "question_id": question.id,
                    "question_text": question.question_text,
                    "correct_option": question.correct_option,
                    "explanation": question.explanation,
                })

                FailedQuestion.objects.create(
                    attempt=exam,
                    question=question,
                    selected_option=selected,
                )

        total = len(answers)
        percentage = (correct_count / total) * 100 if total > 0 else 0
        passed = percentage >= settings.EXAM_PASS_MARK_PERCENT

        exam.score = correct_count
        exam.percentage = percentage
        exam.passed = passed
        exam.save()

        return Response(
            {
                "score": correct_count,
                "total": total,
                "percentage": round(percentage, 2),
                "passed": passed,
                "failed_questions": failed_questions,
            },
            status=status.HTTP_200_OK,
        )