from django.urls import path
from .views import ExamHistoryView

urlpatterns = [
    path("history/", ExamHistoryView.as_view(), name="exam_history"),
]