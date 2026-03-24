from django.contrib import admin
from .models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "course",
        "subject",
        "resource_type",
        "uploaded_at",
        "is_active"
    )

    list_filter = ("course", "subject", "resource_type")

    search_fields = ("title",)