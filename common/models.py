from django.db import models

# Create your models here.

class UnitSystem(models.TextChoices):
    SPEED = "KT", "Knots"
    DISTANCE = "NM", "Nautical Miles"
    ALTITUDE = "FT", "Feet"
    TEMPERATURE = "C", "Celsius"