from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Airspace(models.Model):
    AIRSPACE_TYPE_CHOICES = [
        ("CLASS_A", "Class A"),
        ("CLASS_B", "Class B"),
        ("CLASS_C", "Class C"),
        ("CLASS_D", "Class D"),
        ("CLASS_E", "Class E"),
        ("CLASS_G", "Class G"),
        ("RESTRICTED", "Restricted"),
        ("PROHIBITED", "Prohibited"),
        ("DANGER", "Danger Area"),
    ]

    name = models.CharField(max_length=100)
    airspace_type = models.CharField(max_length=20, choices=AIRSPACE_TYPE_CHOICES)

    # Geometry (Polygon)
    boundary = models.PolygonField(geography=True)

    # Vertical limits
    lower_limit_ft = models.IntegerField(help_text="Lower altitude in feet")
    upper_limit_ft = models.IntegerField(help_text="Upper altitude in feet")

    # Optional metadata
    controlling_authority = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.airspace_type})"