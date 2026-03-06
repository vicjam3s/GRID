from django.conf import settings
from django.db import models
from syllabus.models import Subject, Topic, Subtopic

# Create your models here.

class ContentSource(models.Model):
    SOURCE_TYPE_CHOICES = (
        ("INTERNAL", "Internal"),
        ("USER_UPLOAD", "User Upload"),
        ("EXTERNAL_REF", "External Reference"),
    )

    title = models.CharField(max_length=255)
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPE_CHOICES)
    source_url = models.URLField(blank=True)
    license_info = models.CharField(max_length=255, blank=True)
    attribution = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContentDocument(models.Model):
    source = models.ForeignKey(ContentSource, on_delete=models.CASCADE, related_name="documents")
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    file = models.FileField(upload_to="content/")
    extracted_text = models.TextField(blank=True)
    processed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


class ContentChunk(models.Model):
    document = models.ForeignKey(ContentDocument, on_delete=models.CASCADE, related_name="chunks")

    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.SET_NULL, null=True, blank=True)

    text = models.TextField()

    def __str__(self):
        return self.text[:60]