from django.contrib import admin
from .models import Course, Subject, Topic


class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    inlines = [SubjectInline]


class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "course")
    list_filter = ("course",)
    inlines = [TopicInline]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "subject")
    list_filter = ("subject",)