from django.urls import path
from .views import NotesBySubjectView

urlpatterns = [
    path("notes/", NotesBySubjectView.as_view()),
]