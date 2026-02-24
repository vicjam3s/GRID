from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import ExamAttempt, QuestionAttempt
from .serializers import ExamRetakeSerializer, ExamHistorySerializer
from assessments.serializers import QuestionSerializer

from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Create your views here.

class ExamHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        exams = ExamAttempt.objects.filter(
            user=request.user
        ).order_by("-created_at")

        serializer = ExamHistorySerializer(exams, many=True)
        return Response(serializer.data)

class RetakeExamView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ExamRetakeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        exam_id = serializer.validated_data["exam_id"]

        try:
            exam = ExamAttempt.objects.get(
                id=exam_id,
                user=request.user,
            )
        except ExamAttempt.DoesNotExist:
            return Response(
                {"detail": "Exam not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        failed_attempts = QuestionAttempt.objects.filter(
            exam=exam,
            is_correct=False,
        ).select_related("question")

        if not failed_attempts.exists():
            return Response(
                {"detail": "No failed questions to retake."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        questions = [qa.question for qa in failed_attempts]

        return Response(
            {
                "questions": QuestionSerializer(questions, many=True).data,
                "retake_of_exam": exam.id,
            },
            status=status.HTTP_200_OK,
        )   




class ExamResultPDFView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, exam_id):
        try:
            exam = ExamAttempt.objects.get(
                id=exam_id,
                user=request.user,
            )
        except ExamAttempt.DoesNotExist:
            return Response(
                {"detail": "Exam not found."},
                status=404,
            )

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="exam_{exam.id}.pdf"'

        doc = SimpleDocTemplate(response)
        styles = getSampleStyleSheet()
        elements = []

        elements.append(Paragraph(f"<b>GRID Exam Result</b>", styles["Title"]))
        elements.append(Spacer(1, 12))

        elements.append(Paragraph(f"Score: {exam.score}%", styles["Normal"]))
        elements.append(Paragraph(f"Passed: {'Yes' if exam.passed else 'No'}", styles["Normal"]))
        elements.append(Paragraph(f"Date: {exam.created_at}", styles["Normal"]))
        elements.append(Spacer(1, 20))

        attempts = exam.question_attempts.select_related("question")

        for qa in attempts:
            q = qa.question
            elements.append(Paragraph(f"<b>Q:</b> {q.question_text}", styles["Normal"]))
            elements.append(Paragraph(
                f"Your answer: {qa.selected_option} | Correct: {q.correct_option}",
                styles["Normal"],
            ))
            if q.explanation:
                elements.append(Paragraph(f"Explanation: {q.explanation}", styles["Italic"]))
            elements.append(Spacer(1, 12))

        doc.build(elements)
        return response