from django.db import models
from syllabus.models import Course, Subject


class Question(models.Model):

    QUESTION_SOURCE = (
        ("INTERNAL", "Internal"),
        ("CASSOA", "CASSOA"),
        ("JAA", "JAA"),
        ("TM_EDITOR", "TM Editor"),
        ("TURKISH", "Turkish"),
        ("ECQB", "ECQB"),
        ("GREENBANK", "Greenbank"),
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    question_source = models.CharField(
        max_length=20,
        choices=QUESTION_SOURCE,
        default="INTERNAL",
        db_index=True
    )

    question_text = models.TextField(unique=True)

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_option = models.CharField(
        max_length=1,
        choices=(("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")),
    )

    explanation = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=["subject", "question_source"]),
        ]
    
    def __str__(self):
        return f"[{self.question_source}] {self.question_text[:80]}"
    