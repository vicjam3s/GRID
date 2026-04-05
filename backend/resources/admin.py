from django.contrib import admin
from .models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):

    list_display = (
        "course",
        "subject",
        "resource_type",
        "question_bank_type",
        "uploaded_at",
        "is_active"
    )

    list_filter = ("course", "subject", "resource_type", "question_bank_type")

    search_fields = ("course__code", "subject__code", "resource_type", "question_bank_type")