from django.conf import settings
from django.db import models
from syllabus.models import Course, Subject
from assessments.models import Question


class ExamAttempt(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="exam_attempts"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="exam_attempts",
        null=True,
        blank=True
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="exam_attempts"
    )

    score = models.IntegerField()
    total_questions = models.IntegerField()

    percentage = models.FloatField(default=0)
    passed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.subject.code} ({self.score}/{self.total_questions})"


class FailedQuestion(models.Model):
    attempt = models.ForeignKey(
        ExamAttempt,
        on_delete=models.CASCADE,
        related_name="failed_questions"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    selected_option = models.CharField(max_length=1)

    def __str__(self):
        return f"Failed: {self.question.id}"