from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Polygon
from maps.models import Airspace


class Command(BaseCommand):
    help = "Seed Kenyan airspaces"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding airspaces...")

        # Optional: clear existing
        Airspace.objects.all().delete()

        # =========================
        # Nairobi CTR (Sample)
        # =========================
        Airspace.objects.create(
            name="Nairobi CTR",
            airspace_type="CLASS_C",
            boundary=Polygon((
                (36.70, -1.40),
                (37.00, -1.40),
                (37.00, -1.10),
                (36.70, -1.10),
                (36.70, -1.40),  # close polygon
            )),
            lower_limit_ft=0,
            upper_limit_ft=8000,
            controlling_authority="Nairobi Control"
        )

        # =========================
        # Sample Restricted Area
        # =========================
        Airspace.objects.create(
            name="Restricted Area R1",
            airspace_type="RESTRICTED",
            boundary=Polygon((
                (36.80, -1.30),
                (36.90, -1.30),
                (36.90, -1.20),
                (36.80, -1.20),
                (36.80, -1.30),
            )),
            lower_limit_ft=0,
            upper_limit_ft=10000,
            controlling_authority="KCAA"
        )

        self.stdout.write(self.style.SUCCESS("Airspaces seeded successfully!"))