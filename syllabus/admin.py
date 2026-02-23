from django.contrib import admin
from .models import Course, Subject, Topic, Subtopic


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "authority")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "order")
    list_filter = ("course",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "order")
    list_filter = ("subject__course", "subject")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subject" and request.GET.get("course"):
            kwargs["queryset"] = Subject.objects.filter(
                course_id=request.GET.get("course")
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ("title", "topic", "order")
    list_filter = ("topic__subject__course", "topic__subject")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "topic" and request.GET.get("subject"):
            kwargs["queryset"] = Topic.objects.filter(
                subject_id=request.GET.get("subject")
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)