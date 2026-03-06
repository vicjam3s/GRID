from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models


class ExportRecord(models.Model):
    EXPORT_TYPE_CHOICES = (
        ("EXAM_RESULT", "Exam Result"),
        ("NOTES", "Notes"),
        ("NAVLOG", "Navlog"),
        ("LOGBOOK", "Logbook"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    export_type = models.CharField(max_length=20, choices=EXPORT_TYPE_CHOICES)
    file_path = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)