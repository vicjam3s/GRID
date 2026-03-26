from django.urls import path
from .views import *

urlpatterns = [
    path("courses/", CourseListView.as_view()),
    path("subjects/", SubjectListView.as_view()),
    path("topics/", TopicListView.as_view()),
]