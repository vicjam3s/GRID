from django.urls import path
from .views import *

urlpatterns = [
    path("submit/", SubmitExamView.as_view()),
    path("performance/", SubjectPerformanceView.as_view()),
]