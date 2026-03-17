from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = ("short_question", "correct_option", "is_active")

    search_fields = ("question_text",)

    list_filter = ("is_active",)

    fieldsets = (

        ("Question", {
            "fields": ("question_text",)
        }),

        ("Choices", {
            "fields": (
                "option_a",
                "option_b",
                "option_c",
                "option_d",
                "correct_option",
            )
        }),

        ("Explanation", {
            "fields": ("explanation",)
        }),

        ("Status", {
            "fields": ("is_active",)
        }),

    )

    def short_question(self, obj):
        return obj.question_text[:60]