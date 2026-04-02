from django.contrib import admin

from django.contrib.gis import admin
from .models import Airspace

# Register your models here.

@admin.register(Airspace)
class AirspaceAdmin(admin.GISModelAdmin):
    list_display = ("name", "airspace_type", "lower_limit_ft", "upper_limit_ft")

    # Optional map settings
    default_lon = 36.8219
    default_lat = -1.2921
    default_zoom = 7