from django.urls import path
from .views import *

urlpatterns = [
    path("upload/", ContentUploadView.as_view()),
    path("notes/", TopicNotesView.as_view()),
]