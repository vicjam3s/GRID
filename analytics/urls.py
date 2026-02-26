from django.urls import path
from .views import *

urlpatterns = [
    path("subjects/", SubjectAnalyticsView.as_view(), name="subject_analytics"),
    path("topics/", TopicAnalyticsView.as_view(), name="topic_analytics"),
    path("subtopics/", SubtopicAnalyticsView.as_view(), name="subtopic_analytics"),
]