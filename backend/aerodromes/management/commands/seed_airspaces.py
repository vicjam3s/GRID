from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Polygon
from maps.models import Airspace
from maps.utils import create_circular_airspace


class Command(BaseCommand):
    help = "Seed Kenyan airspaces (AIP-aligned structure)"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding airspaces...")

        Airspace.objects.all().delete()

        # ======================================================
        # CONTROL ZONES (CTR) - CIRCULAR (AIP PLACEHOLDERS)
        # ======================================================
        ctr_airspaces = [
            {
                "name": "Nairobi Control Zone",
                "lon": 36.8750,
                "lat": -1.3192,
                "radius_nm": 15,
                "upper_ft": 9000,
                "class": "C",
                "unit": "Eastleigh TWR",
                "call_sign": "Eastleigh Tower",
                "freq_primary": 124.30,
                "freq_secondary": 124.80,
                "hours": "0500-1400 UTC",
                "remarks": "Military aerodrome (Eastleigh)",
            },
            {
                "name": "Mombasa Control Zone",
                "lon": 39.6682,
                "lat": -4.0348,
                "radius_nm": 15,
                "upper_ft": 3500,
                "class": "D",
                "unit": "Mombasa TWR",
                "call_sign": "Mombasa Tower",
                "freq_primary": 118.60,
                "hours": "H24",
            },
            {
                "name": "Kisumu Control Zone",
                "lon": 34.7289,
                "lat": -0.0861,
                "radius_nm": 15,
                "upper_ft": 9000,
                "class": "D",
                "unit": "Kisumu TWR",
                "call_sign": "Kisumu Tower",
                "freq_primary": 118.80,
                "hours": "0330-1800 UTC",
            },
        
            {
                "name": "Eldoret Control Zone",
                "lon": 35.2367,
                "lat": 0.4040,
                "radius_nm": 15,
                "upper_ft": 10000,
                "class": "D",
                "unit": "Eldoret TWR",
                "call_sign": "Eldoret TWR",
                "freq_primary": 120.80,
                "hours": "0330-1800 UTC",
            },
            {
                "name": "Embu Control Zone",
                "lon": 37.4948,
                "lat": -0.5723,
                "radius_nm": 15,
                "upper_ft": 9000,
                "class": "D",
                "unit": "Embu TWR",
                "call_sign": "Embu TWR",
                "freq_primary": 118.20,
                "hours": "0330-1500 UTC",
            },
            {
                "name": "Malindi Control Zone",
                "lon": 40.1010,
                "lat": -3.2214,
                "radius_nm": 15,
                "upper_ft": 3500,
                "class": "D",
                "unit": "Malindi TWR",
                "call_sign": "Malindi TWR",
                "freq_primary": 120.40,
                "hours": "0330-1730 UTC",
            },
            {
                "name": "Wajir Control Zone",
                "lon": 40.0915,
                "lat": 1.7332,
                "radius_nm": 15,
                "upper_ft": 5000,
                "class": "D",
                "unit": "Wajir TWR",
                "call_sign": "Wajir TWR",
                "freq_primary": 118.30,
                "hours": "0330-1530 UTC",
                "remarks": "Civil/Military airport",
            },
            
        ]

        for ctr in ctr_airspaces:
            Airspace.objects.update_or_create(
                name=ctr["name"],
                defaults={
                    "airspace_type": f"CLASS_{ctr['class']}",

                    "boundary": create_circular_airspace(
                        ctr["lon"],
                        ctr["lat"],
                        ctr["radius_nm"],
                    ),

                    "lower_limit_ft": 0,
                    "lower_limit_type": "GND",

                    "upper_limit_ft": ctr["upper_ft"],
                    "upper_limit_type": "AMSL",

                    "airspace_class": ctr["class"],

                    "unit_providing_service": ctr.get("unit"),
                    "call_sign": ctr.get("call_sign"),

                    "frequency_primary_mhz": ctr.get("freq_primary"),
                    "frequency_secondary_mhz": ctr.get("freq_secondary"),

                    "hours_of_service": ctr.get("hours"),
                    "remarks": ctr.get("remarks"),

                    "controlling_authority": ctr.get("unit"),
                },
            )

        # ======================================================
        # TERMINAL AREA (TMA) - NAIROBI (CIRCULAR)
        # ======================================================
        Airspace.objects.update_or_create(
            name="Nairobi TMA",
            defaults={
                "airspace_type": "CLASS_A",

                "boundary": create_circular_airspace(
                    lon=36.9542,   # DVOR NV approx
                    lat=-1.2999,
                    radius_nm=50,
                ),

                "lower_limit_ft": 14500,
                "lower_limit_type": "FL",

                "upper_limit_ft": 19500,
                "upper_limit_type": "FL",

                "airspace_class": "A",

                "unit_providing_service": "Nairobi APP Radar",
                "call_sign": "Nairobi APP Radar",

                "frequency_primary_mhz": 122.30,
                "frequency_secondary_mhz": 124.10,

                "hours_of_service": "H24",
                "remarks": "VFR prohibited above FL145",

                "controlling_authority": "Nairobi APP",
            },
        )
        # ======================================================
        # ADDITIONAL TMAs (AIP-ALIGNED)
        # ======================================================

        tmas = [
            {
                "name": "Eldoret TMA",
                "lon": 35.2367,
                "lat": 0.4040,
                "radius_nm": 50,
                "unit": "Eldoret APP",
                "call_sign": "Eldoret APP",
                "freq_primary": 119.40,
                "hours": "0330-1800 UTC",
                "remarks": "VFR prohibited above FL145",
            },
            {
                "name": "Mombasa TMA",
                "lon": 40.1097,
                "lat": -3.2333,
                "radius_nm": 42,
                "unit": "Mombasa APP",
                "call_sign": "Mombasa APP",
                "freq_primary": 120.30,
                "freq_secondary": 121.70,
                "hours": "H24",
                "remarks": "VFR prohibited above FL145",
            },
            {
                "name": "Mombasa TMA Radar",
                "lon": 40.1097,
                "lat": -3.2333,
                "radius_nm": 42,
                "unit": "Mombasa APP Radar",
                "call_sign": "Mombasa APP Radar",
                "freq_primary": 121.70,
                "freq_secondary": 122.70,
                "hours": "H24",
            },
            {
                "name": "Wajir TMA",
                "lon": 40.0824,
                "lat": 1.7330,
                "radius_nm": 50,
                "unit": "Wajir APP",
                "call_sign": "Wajir APP",
                "freq_primary": 118.30,
                "hours": "0330-1530 UTC",
                "remarks": "VFR prohibited above FL145",
            },
        ]

        for tma in tmas:
            Airspace.objects.update_or_create(
                name=tma["name"],
                defaults={
                    "airspace_type": "CLASS_E",

                    "boundary": create_circular_airspace(
                        tma["lon"],
                        tma["lat"],
                        tma["radius_nm"],
                    ),

                    "lower_limit_ft": 1500,
                    "lower_limit_type": "AGL",

                    "upper_limit_ft": 14500,
                    "upper_limit_type": "FL",

                    "airspace_class": "E",

                    "unit_providing_service": tma["unit"],
                    "call_sign": tma["call_sign"],

                    "frequency_primary_mhz": tma.get("freq_primary"),
                    "frequency_secondary_mhz": tma.get("freq_secondary"),

                    "hours_of_service": tma.get("hours"),
                    "remarks": tma.get("remarks"),

                    "controlling_authority": tma["unit"],
                },
            )

        # ======================================================
        # FIR (SIMPLIFIED PLACEHOLDER POLYGON)
        # ======================================================
        Airspace.objects.update_or_create(
            name="Nairobi FIR (Simplified)",
            defaults={
                "airspace_type": "CLASS_G",

                "boundary": Polygon((
                    (34.0, 4.0),
                    (41.5, 3.5),
                    (41.3, -1.4),
                    (34.0, -1.0),
                    (34.0, 4.0),
                )),

                "lower_limit_ft": 0,
                "lower_limit_type": "GND",

                "upper_limit_ft": None,
                "upper_limit_type": "UNL",

                "airspace_class": "G",

                "unit_providing_service": "Nairobi ACC",
                "call_sign": "Nairobi Control",

                "frequency_primary_mhz": 121.30,
                "frequency_secondary_mhz": 128.70,

                "hours_of_service": "H24",
            },
        )

        # ======================================================
        # RESTRICTED AREA (PLACEHOLDER)
        # ======================================================
        Airspace.objects.update_or_create(
            name="Restricted Area R1",
            defaults={
                "airspace_type": "RESTRICTED",

                "boundary": Polygon((
                    (36.80, -1.30),
                    (36.90, -1.30),
                    (36.90, -1.20),
                    (36.80, -1.20),
                    (36.80, -1.30),
                )),

                "lower_limit_ft": 0,
                "lower_limit_type": "GND",

                "upper_limit_ft": 10000,
                "upper_limit_type": "AMSL",

                "airspace_class": "D",

                "unit_providing_service": "KCAA",
                "call_sign": "KCAA",

                "hours_of_service": "H24",
                "remarks": "Placeholder - replace with AIP coordinates",
            },
        )

        self.stdout.write(self.style.SUCCESS("Airspaces seeded successfully!"))