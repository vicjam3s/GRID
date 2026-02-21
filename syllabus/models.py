from django.db import models

# Create your models here.

class Course(models.Model):
    COURSE_CHOICES = (
        ("PPL", "Private Pilot Licence"),
        ("CPL", "Commercial Pilot Licence"),
    )

    code = models.CharField(max_length=10, choices=COURSE_CHOICES, unique=True)
    name = models.CharField(max_length=100)
    authority = models.CharField(max_length=50, default="KCAA")
    version = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.code


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]
        unique_together = ("course", "name")

    def __str__(self):
        return f"{self.course.code} - {self.name}"


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=150)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]
        unique_together = ("subject", "title")

    def __str__(self):
        return self.title


class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="subtopics")
    title = models.CharField(max_length=150)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]
        unique_together = ("topic", "title")

    def __str__(self):
        return self.title