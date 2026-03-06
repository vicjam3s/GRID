from django.contrib import admin
from .models import Question

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "subtopic")
    list_filter = ("subtopic__topic__subject__course",)