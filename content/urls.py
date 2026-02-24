from django.urls import path
from .views import ContentUploadView, SubtopicNotesView

urlpatterns = [
    path("upload/", ContentUploadView.as_view(), name="content_upload"),
    path("notes/<int:subtopic_id>/", SubtopicNotesView.as_view(), name="subtopic_notes"),
]