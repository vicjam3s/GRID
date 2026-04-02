from django.contrib.gis.db import models


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

    # ==============================
    # VERTICAL LIMITS (ENHANCED)
    # ==============================
    lower_limit_ft = models.IntegerField(help_text="Lower altitude in feet", blank=True, null=True)
    upper_limit_ft = models.IntegerField(help_text="Upper altitude in feet", blank=True, null=True)

    lower_limit_type = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="GND / AMSL / AGL / FL"
    )

    upper_limit_type = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="AMSL / FL / UNL"
    )

    # ==============================
    # AIP OPERATIONAL DATA
    # ==============================
    airspace_class = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="AIP Airspace Class (A, B, C, D, E, G)"
    )

    unit_providing_service = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    call_sign = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    frequency_primary_mhz = models.FloatField(blank=True, null=True)
    frequency_secondary_mhz = models.FloatField(blank=True, null=True)

    hours_of_service = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="e.g. H24 or 0330-1800 UTC"
    )

    remarks = models.TextField(blank=True, null=True)


    controlling_authority = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.airspace_type})"