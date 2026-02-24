from django.urls import path
from .views import GenerateExamView, SubmitExamView

urlpatterns = [
    path("generate/", GenerateExamView.as_view(), name="generate_exam"),
    path("submit/", SubmitExamView.as_view(), name="submit_exam"),
]