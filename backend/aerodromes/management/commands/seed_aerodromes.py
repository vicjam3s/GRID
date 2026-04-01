from django.core.management.base import BaseCommand
from aerodromes.models import Aerodrome, Runway, Communication
from django.contrib.gis.geos import Point


class Command(BaseCommand):
    help = "Seed Kenyan aerodromes with runways and communications"

    def handle(self, *args, **kwargs):

        self.stdout.write("Seeding aerodromes...")

        # =========================
        # HKJK - Jomo Kenyatta
        # =========================
        HKJK, _ = Aerodrome.objects.update_or_create(
            icao_code="HKJK",
            defaults={
                "iata_code": "NBO",
                "name": "Jomo Kenyatta International Airport",
                "city": "Nairobi",
                "elevation_ft": 5330,
                "location": Point(36.9278, -1.3192),
                "magnetic_variation": 1.5,
                "timezone": "UTC+3",
            }
        )

        Runway.objects.update_or_create(
            aerodrome=HKJK,
            identifier="06/24",
            defaults={
                "length_ft": 13507,
                "width_ft": 197,
                "surface_type": "ASPHALT",
                "glide_path_type": "PAPI",
                "glide_path_angle": 3.0,
                "edge_lighting": True,
            }
        )

        Communication.objects.update_or_create(
            aerodrome=HKJK,
            service_type="ATIS",
            defaults={"frequency_mhz": 127.0, "name": "Nairobi ATIS"}
        )

        Communication.objects.update_or_create(
            aerodrome=HKJK,
            service_type="GROUND",
            defaults={"frequency_mhz": 121.9, "name": "Nairobi Ground"}
        )

        Communication.objects.update_or_create(
            aerodrome=HKJK,
            service_type="TOWER",
            defaults={"frequency_mhz": 118.7, "name": "Nairobi Tower"}
        )

        # =========================
        # HKMO - Moi International
        # =========================
        HKMO, _ = Aerodrome.objects.update_or_create(
            icao_code="HKMO",
            defaults={
                "iata_code": "MBA",
                "name": "Moi International Airport",
                "city": "Mombasa",
                "elevation_ft": 200,
                "location": Point(39.5942, -4.0348),
                "magnetic_variation": 1.2,
                "timezone": "UTC+3",
            }
        )

        Runway.objects.update_or_create(
            aerodrome=HKMO,
            identifier="03/21",
            defaults={
                "length_ft": 10998,
                "width_ft": 148,
                "surface_type": "ASPHALT",
                "glide_path_type": "PAPI",
                "glide_path_angle": 3.0,
            }
        )

        Communication.objects.update_or_create(
            aerodrome=HKMO,
            service_type="TOWER",
            defaults={"frequency_mhz": 118.2, "name": "Mombasa Tower"}
        )

        # =========================
        # HKNW - Wilson Airport
        # =========================
        HKNW, _ = Aerodrome.objects.update_or_create(
            icao_code="HKNW",  # FIXED ICAO
            defaults={
                "name": "Wilson Airport",
                "city": "Nairobi",
                "elevation_ft": 5546,
                "location": Point(36.8148, -1.3217),
                "magnetic_variation": 1.5,
                "timezone": "UTC+3",
            }
        )

        # RWY 07/25
        Runway.objects.update_or_create(
            aerodrome=HKNW,
            identifier="07/25",
            defaults={
                "length_ft": 5300,
                "width_ft": 100,
                "surface_type": "ASPHALT",
                "edge_lighting": True,
                "glide_path_type": "PAPI",
                "glide_path_angle": 3.0,
            }
        )

        # RWY 14/32 (AIP-aligned structure)
        Runway.objects.update_or_create(
            aerodrome=HKNW,
            identifier="14/32",
            defaults={
                "length_ft": 5050,              # ~1540 m (VERIFY with AIP)
                "width_ft": 75,                 # ~23 m
                "surface_type": "ASPHALT",
                "gradient_percent": 1.0,        # Approx (VERIFY)
                "displaced_threshold_ft": 246,  # RWY 14 (~75 m)
                "edge_lighting": False,         # Non-lighted
                "glide_path_type": None,
                "glide_path_angle": None,
            }
        )

        Communication.objects.update_or_create(
            aerodrome=HKNW,
            service_type="TOWER",
            defaults={"frequency_mhz": 118.1, "name": "Wilson Tower"}
        )

        self.stdout.write(self.style.SUCCESS("Seeding complete!"))