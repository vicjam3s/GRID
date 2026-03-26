from django.contrib import admin
from .models import ExamAttempt, FailedQuestion


class FailedQuestionInline(admin.TabularInline):
    model = FailedQuestion
    extra = 0


@admin.register(ExamAttempt)
class ExamAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "subject", "score", "total_questions", "created_at")
    inlines = [FailedQuestionInline]


@admin.register(FailedQuestion)
class FailedQuestionAdmin(admin.ModelAdmin):
    list_display = ("attempt", "question", "selected_option")