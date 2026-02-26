from django.core.management.base import BaseCommand
from syllabus.models import Course, Subject, Topic, Subtopic


PPL_SYLLABUS = {
    "Air Law": {
        "International Agreements & Organizations": [
            "Chicago Convention",
            "ICAO Structure",
            "National Aviation Law (Kenya)",
        ],
        "Personnel Licensing (ICAO Annex 1)": [
            "PPL Privileges & Limitations",
            "Medical Certification",
        ],
        "Rules of the Air (ICAO Annex 2)": [
            "General Rules",
            "Avoidance of Collisions",
            "VFR Weather Minima",
        ],
        "Air Traffic Services (ICAO Annex 11)": [
            "Airspace Classification",
            "ATS Services",
        ],
        "Aerodromes (ICAO Annex 14)": [
            "Markings & Lighting",
            "Aerodrome Signals",
        ],
    },

    "Navigation": {
        "Charts and Publications": [
            "Aeronautical Charts",
            "NOTAMs",
        ],
    },
}


CPL_SYLLABUS = {
    "Air Law": {
        "International Air Law": [
            "ICAO Annexes",
            "State Responsibilities",
        ],
    },
}


class Command(BaseCommand):
    help = "Seed PPL and CPL syllabus for GRID"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Seeding syllabus..."))

        self.seed_course(
            code="PPL",
            name="Private Pilot Licence",
            syllabus=PPL_SYLLABUS,
        )

        self.seed_course(
            code="CPL",
            name="Commercial Pilot Licence",
            syllabus=CPL_SYLLABUS,
        )

        self.stdout.write(self.style.SUCCESS("Syllabus seeding complete."))

    def seed_course(self, code, name, syllabus):
        course, _ = Course.objects.get_or_create(
            code=code,
            defaults={
                "name": name,
                "authority": "KCAA",
            },
        )

        for subject_order, (subject_name, topics) in enumerate(syllabus.items(), start=1):
            subject, _ = Subject.objects.get_or_create(
                course=course,
                name=subject_name,
                defaults={"order": subject_order},
            )

            for topic_order, (topic_title, subtopics) in enumerate(topics.items(), start=1):
                topic, _ = Topic.objects.get_or_create(
                    subject=subject,
                    title=topic_title,
                    defaults={"order": topic_order},
                )

                for subtopic_order, subtopic_title in enumerate(subtopics, start=1):
                    Subtopic.objects.get_or_create(
                        topic=topic,
                        title=subtopic_title,
                        defaults={"order": subtopic_order},
                    )