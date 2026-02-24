from django.contrib import admin
from .models import ExamAttempt, QuestionAttempt

# Register your models here.

@admin.register(ExamAttempt)
class ExamAttemptAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "score", "passed", "created_at")
    list_filter = ("passed", "created_at")


@admin.register(QuestionAttempt)
class QuestionAttemptAdmin(admin.ModelAdmin):
    list_display = ("exam", "question", "selected_option", "is_correct")
    list_filter = ("is_correct",)