from django.contrib import admin
from .models import Course, Subject, Topic, Subtopic, Note


class ReadOnlyAdmin(admin.ModelAdmin):
    """
    Base admin class to make models fully read-only.
    """

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Course)
class CourseAdmin(ReadOnlyAdmin):
    list_display = ("code", "name", "authority", "version")
    ordering = ("code",)


@admin.register(Subject)
class SubjectAdmin(ReadOnlyAdmin):
    list_display = ("name", "course", "order")
    ordering = ("course", "order")
    list_filter = ("course",)


@admin.register(Topic)
class TopicAdmin(ReadOnlyAdmin):
    list_display = ("title", "subject", "order")
    ordering = ("subject", "order")
    list_filter = ("subject__course", "subject")


@admin.register(Subtopic)
class SubtopicAdmin(ReadOnlyAdmin):
    list_display = ("title", "topic", "order")
    ordering = ("topic", "order")
    list_filter = ("topic__subject__course", "topic__subject")


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "subtopic", "created_at")
    search_fields = ("title", "content")
    list_filter = ("subtopic__topic__subject__course", "subtopic__topic__subject", "subtopic")
    readonly_fields = ("created_at",)