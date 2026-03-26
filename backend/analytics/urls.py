from django.urls import path
from .views import *

urlpatterns = [
    path("subjects/", SubjectAnalyticsView.as_view(), name="subject_analytics"),
    path("topics/", TopicAnalyticsView.as_view(), name="topic_analytics"),
    path("weak-areas/", WeakAreasView.as_view(), name="weak_areas"),
]