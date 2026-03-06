from django.urls import path
from .views import *

urlpatterns = [
    path("history/", ExamHistoryView.as_view(), name="exam_history"),
    path("retake/", RetakeExamView.as_view(), name="exam_retake"),
    path("export/<int:exam_id>/", ExamResultPDFView.as_view(), name="exam_pdf"),
]