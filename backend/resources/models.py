from django.db import models
from syllabus.models import Course, Subject


class Resource(models.Model):

    RESOURCE_TYPE = (
        ("NOTES", "Notes"),
        ("QBANK", "Question Bank"),
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="resources"
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="resources"
    )

    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPE)

    title = models.CharField(max_length=255)

    file = models.FileField(upload_to="resources/pdfs/")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["course", "subject", "resource_type"]

    def __str__(self):
        return f"{self.course.code} - {self.subject.code} - {self.resource_type} - {self.title}"