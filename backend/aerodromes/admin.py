from django.contrib.gis import admin
from .models import Aerodrome, Runway, Communication, FBO


# ==============================
# INLINE MODELS (KEY FEATURE)
# ==============================

class RunwayInline(admin.TabularInline):
    model = Runway
    extra = 1


class CommunicationInline(admin.TabularInline):
    model = Communication
    extra = 1


class FBOInline(admin.TabularInline):
    model = FBO
    extra = 1


# ==============================
# AERODROME ADMIN
# ==============================

@admin.register(Aerodrome)
class AerodromeAdmin(admin.GISModelAdmin):
    list_display = (
        "icao_code",
        "name",
        "city",
        "elevation_ft",
        "timezone",
    )

    search_fields = (
        "icao_code",
        "name",
        "city",
    )

    list_filter = (
        "city",
        "timezone",
    )

    inlines = [RunwayInline, CommunicationInline, FBOInline]


# ==============================
# RUNWAY ADMIN
# ==============================

@admin.register(Runway)
class RunwayAdmin(admin.ModelAdmin):
    list_display = (
        "aerodrome",
        "identifier",
        "length_ft",
        "surface_type",
    )

    list_filter = ("surface_type",)
    search_fields = ("identifier",)


# ==============================
# COMMUNICATION ADMIN
# ==============================

@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    list_display = (
        "aerodrome",
        "service_type",
        "frequency_mhz",
    )

    list_filter = ("service_type",)


# ==============================
# FBO ADMIN
# ==============================

@admin.register(FBO)
class FBOAdmin(admin.ModelAdmin):
    list_display = (
        "aerodrome",
        "name",
    )
