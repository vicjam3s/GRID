from django.contrib import admin
from .models import NotePDF


@admin.register(NotePDF)
class NotePDFAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "uploaded_at")
    list_filter = ("subject",)
    search_fields = ("title",)