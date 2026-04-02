from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Polygon
from maps.models import Airspace
from maps.utils import create_circular_airspace


class Command(BaseCommand):
    help = "Seed Kenyan airspaces (AIP-ready structure)"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding airspaces...")

        # Optional: clear existing
        Airspace.objects.all().delete()

        # ======================================================
        # CTR AIRSPACES (CIRCULAR PLACEHOLDERS - UPDATES PENDING FROM AIP)
        # ======================================================
        ctr_airspaces = [
            {
                "name": "Nairobi CTR",
                "lon": 36.8219,
                "lat": -1.2921,
                "radius_nm": 25,  # To be updated with actual AIP data
                "upper_limit_ft": 8000,  # To be verified with actual AIP data
                "authority": "Nairobi Control",
            },
            {
                "name": "Mombasa CTR",
                "lon": 39.5942,
                "lat": -4.0348,
                "radius_nm": 20,  # To be updated with actual AIP data
                "upper_limit_ft": 8000,
                "authority": "Mombasa Control",
            },
            {
                "name": "Kisumu CTR",
                "lon": 34.7289,
                "lat": -0.0861,
                "radius_nm": 15,  # To be updated with actual AIP data
                "upper_limit_ft": 8000,
                "authority": "Kisumu Control",
            },
        ]

        for ctr in ctr_airspaces:
            Airspace.objects.update_or_create(
                name=ctr["name"],
                defaults={
                    "airspace_type": "CLASS_C",
                    "boundary": create_circular_airspace(
                        ctr["lon"],
                        ctr["lat"],
                        ctr["radius_nm"],
                    ),
                    "lower_limit_ft": 0,
                    "upper_limit_ft": ctr["upper_limit_ft"],
                    "controlling_authority": ctr["authority"],
                },
            )

        # ======================================================
        # RESTRICTED / PROHIBITED AREAS (PLACEHOLDER POLYGONS)
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
                "upper_limit_ft": 10000,
                "controlling_authority": "KCAA",
            },
        )

        self.stdout.write(self.style.SUCCESS("Airspaces seeded successfully!"))