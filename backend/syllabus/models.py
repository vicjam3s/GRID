from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.code


class Subject(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ("course", "code")

    def __str__(self):
        return f"{self.course.code} - {self.code}"


class Topic(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="topics"
    )

    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.subject.code} - {self.title}"