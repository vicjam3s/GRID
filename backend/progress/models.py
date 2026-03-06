from django.conf import settings
from django.db import models
from assessments.models import Question

# Create your models here.

class ExamAttempt(models.Model):
    """
    Represents one exam sitting by a user.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="exam_attempts",
    )

    total_questions = models.PositiveIntegerField()
    score = models.PositiveIntegerField()
    passed = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ExamAttempt #{self.id} - {self.user.email}"


class QuestionAttempt(models.Model):
    """
    Represents a user's answer to a single question in an exam.
    """

    exam = models.ForeignKey(
        ExamAttempt,
        on_delete=models.CASCADE,
        related_name="question_attempts",
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )

    selected_option = models.CharField(
        max_length=1,
        choices=(("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")),
    )

    is_correct = models.BooleanField()

    def __str__(self):
        return f"Q{self.question.id} → {self.selected_option}"