from django.db import models
from syllabus.models import Course, Subject


class Question(models.Model):

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

    def __str__(self):
        return self.question_text[:80]