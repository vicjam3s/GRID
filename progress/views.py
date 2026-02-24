from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import ExamAttempt
from .serializers import ExamHistorySerializer

# Create your views here.

class ExamHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        exams = ExamAttempt.objects.filter(
            user=request.user
        ).order_by("-created_at")

        serializer = ExamHistorySerializer(exams, many=True)
        return Response(serializer.data)