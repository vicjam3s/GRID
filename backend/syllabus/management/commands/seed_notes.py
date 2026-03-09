from django.core.management.base import BaseCommand
from syllabus.models import Subject, Module, Subtopic, Note


class Command(BaseCommand):
    help = "Seed notes into the database"


    def handle(self, *args, **kwargs):

        # ---- SELECTS WHERE THE NOTES BELONG ----
        subject = Subject.objects.get(code="AL")  # Airlaw
        module = Module.objects.get(title="ICAO")
        subtopic = Subtopic.objects.get(title="ICAO Convention", module=module)


        # ---- NOTES FORMAT ----
        NOTES = [

        {
        "title": "ICAO Convention",
        "content": """
The Chicago Convention of 1944 established ICAO.

It created global rules for civil aviation and international airspace regulation.
"""
        },

        {
        "title": "Annexes",
        "content": """
ICAO publishes 19 annexes that regulate aviation operations,
safety standards, and air navigation procedures.
"""
        }

        ]


        # ---- INSERT NOTES ----
        for note in NOTES:
            Note.objects.create(
                subtopic=subtopic,
                title=note["title"],
                content=note["content"]
            )


        self.stdout.write(self.style.SUCCESS("Notes seeded successfully"))