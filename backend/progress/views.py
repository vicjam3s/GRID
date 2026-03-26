from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import ExamAttempt, FailedQuestion
from syllabus.models import Course, Subject
from assessments.models import Question


PASS_MARK = 80  # percentage


class SubmitExamView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        course_id = request.data.get("course_id")
        subject_id = request.data.get("subject_id")
        answers = request.data.get("answers", [])

        course = Course.objects.get(id=course_id)
        subject = Subject.objects.get(id=subject_id)

        total_questions = len(answers)
        score = 0

        attempt = ExamAttempt.objects.create(
            user=user,
            course=course,
            subject=subject,
            score=0,
            total_questions=total_questions
        )

        for item in answers:
            question = Question.objects.get(id=item["question_id"])
            selected = item["selected_option"]

            if selected == question.correct_option:
                score += 1
            else:
                FailedQuestion.objects.create(
                    attempt=attempt,
                    question=question,
                    selected_option=selected
                )

        # Calculate percentage
        percentage = (score / total_questions) * 100 if total_questions > 0 else 0

        # Determine pass/fail
        passed = percentage >= PASS_MARK

        # Save results
        attempt.score = score
        attempt.percentage = percentage
        attempt.passed = passed
        attempt.save()

        return Response({
            "score": score,
            "total": total_questions,
            "percentage": round(percentage, 2),
            "passed": passed
        }, status=status.HTTP_200_OK)
    
class SubjectPerformanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        attempts = ExamAttempt.objects.filter(user=user)

        data = []

        for attempt in attempts:
            data.append({
                "course": attempt.course.code,
                "subject": attempt.subject.code,
                "score": attempt.score,
                "total": attempt.total_questions,
                "date": attempt.created_at
            })

        return Response(data)    