from django.db import models


class NotePDF(models.Model):

    SUBJECT_CHOICES = (
        ("HP", "Human Performance"),
        ("NAV", "Navigation"),
        ("MET", "Meteorology"),
        ("AL", "Air Law"),
        ("OPS", "Operational Procedures"),
        ("RNAV", "Radio Navigation"),
    )

    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICES)

    title = models.CharField(max_length=255)

    file = models.FileField(upload_to="notes/pdfs/")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.title}"