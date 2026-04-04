from django.contrib.gis.db import models

# Create your models here.

# ==============================
# 1. CORE AERODROME (HEADER)
# ==============================
class Aerodrome(models.Model):
    icao_code = models.CharField(max_length=4, unique=True)
    iata_code = models.CharField(max_length=3, blank=True, null=True)

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    elevation_ft = models.IntegerField()

    location = models.PointField(geography=True) #critical for geospatial queries

    magnetic_variation = models.FloatField(help_text="Degrees East (+) / West (-)")
    timezone = models.CharField(max_length=10, default="UTC+3")
    # ==============================
    # OPERATIONAL STATUS (AIP-ALIGNED)
    # ==============================
    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("CLOSED", "Closed"),
        ("RESTRICTED", "Restricted"),
        ("MILITARY", "Military"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN"
    )

    # Controlled vs uncontrolled aerodrome
    is_controlled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.icao_code} - {self.name}"


# ==============================
# 2. RUNWAYS
# ==============================
class Runway(models.Model):
    SURFACE_CHOICES = [
        ("ASPHALT", "Asphalt"),
        ("CONCRETE", "Concrete"),
        ("GRASS", "Grass"),
        ("GRAVEL", "Gravel"),
        ("DIRT", "Dirt"),
        ("CABRO", "Cabro"),
    ]

    TRAFFIC_PATTERN_CHOICES = [
        ("LEFT", "Left"),
        ("RIGHT", "Right"),
    ]

    # ==============================
    # RUNWAY SERVICEABILITY STATUS
    # ==============================
    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("CLOSED", "Closed"),
        ("UNSERVICEABLE", "Unserviceable"),
        ("RESTRICTED", "Restricted"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN"
    )

    aerodrome = models.ForeignKey(
        Aerodrome,
        related_name="runways",
        on_delete=models.CASCADE
    )

    identifier = models.CharField(max_length=10)

    length_ft = models.IntegerField()
    width_ft = models.IntegerField()

    surface_type = models.CharField(max_length=20, choices=SURFACE_CHOICES)
    pcn = models.CharField(max_length=20, blank=True, null=True)

    gradient_percent = models.FloatField(blank=True, null=True)
    displaced_threshold_ft = models.IntegerField(blank=True, null=True)

    # Lighting + approach
    approach_lighting = models.CharField(max_length=50, blank=True, null=True)  # ALSF-2, SSALR
    edge_lighting = models.BooleanField(default=False)

    # Glide systems
    glide_path_type = models.CharField(max_length=10, blank=True, null=True)  # PAPI/VASI
    glide_path_angle = models.FloatField(blank=True, null=True)

    traffic_pattern = models.CharField(
        max_length=10,
        choices=TRAFFIC_PATTERN_CHOICES,
        default="LEFT"
    )

    def __str__(self):
        return f"{self.aerodrome.icao_code} - RWY {self.identifier}"


# ==============================
# 3. COMMUNICATIONS
# ==============================
class Communication(models.Model):
    SERVICE_CHOICES = [
        ("ATIS", "ATIS"),
        ("UNMANNED", "Unmanned Frequency"),
        ("AWOS", "AWOS"),
        ("CLEARANCE", "Clearance Delivery"),
        ("GROUND", "Ground"),
        ("TOWER", "Tower"),
        ("APPROACH", "Approach"),
        ("DEPARTURE", "Departure"),
        ("CENTER", "Center"),
        ("RADAR", "Radar"),

    ]

    aerodrome = models.ForeignKey(
        Aerodrome,
        related_name="communications",
        on_delete=models.CASCADE
    )

    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    frequency_mhz = models.FloatField()

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="e.g. Nairobi Tower"
    )

    def __str__(self):
        return f"{self.aerodrome.icao_code} - {self.service_type} ({self.frequency_mhz})"


# ==============================
# 4. FBO (FUEL / SERVICES)
# ==============================
class FBO(models.Model):
    aerodrome = models.ForeignKey(
        Aerodrome,
        related_name="fbos",
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)  # Shell, Total, etc
    services = models.TextField(blank=True)

    def __str__(self):
        return f"{self.aerodrome.icao_code} - {self.name}"