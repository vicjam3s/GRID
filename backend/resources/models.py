from django.db import models
from syllabus.models import Course, Subject


class Resource(models.Model):

    RESOURCE_TYPE = (
        ("NOTES", "Notes"),
        ("QBANK", "Question Bank"),
    )

    QBANK_TYPE = (
        ("TURKISH", "Turkish"),
        ("TM_EDITOR", "TM Editor"),
        ("GREENBANK", "Greenbank"),
        ("CASSOA", "CASSOA"),
        ("ECQB", "ECQB"),
        ("JAA", "JAA"),
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

    question_bank_type = models.CharField(
        max_length=20,
        choices=QBANK_TYPE,
        blank=True,
        null=True,
        help_text="Only applicable if resource_type is QBANK"
    )

    file = models.FileField(upload_to="resources/pdfs/")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["course", "subject", "resource_type"]

    def __str__(self):
        base = f"{self.course.code} - {self.subject.code} - {self.resource_type}"

        if self.resource_type == "QBANK" and self.question_bank_type:
            base += f" ({self.question_bank_type})"

        return base

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.resource_type == "QBANK" and not self.question_bank_type:
            raise ValidationError("Question bank type is required for QBANK resources.")

        if self.resource_type != "QBANK" and self.question_bank_type:
            raise ValidationError("Question bank type should only be set for QBANK resources.")