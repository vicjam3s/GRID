from django.db import models
from syllabus.models import Subtopic

# Create your models here.

class Question(models.Model):
    DIFFICULTY_CHOICES = (
        ("EASY", "Easy"),
        ("MEDIUM", "Medium"),
        ("HARD", "Hard"),
    )

    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, related_name="questions")

    question_text = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_option = models.CharField(
        max_length=1,
        choices=(("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")),
    )

    explanation = models.TextField(blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text[:80]