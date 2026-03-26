from django.core.management.base import BaseCommand
from syllabus.models import Course, Subject


COMMON_SUBJECTS = [
    ("AL", "Air Law"),
    ("MET", "Meteorology"),
    ("POF", "Principles of Flight"),
    ("INS", "Instruments"),
    ("OPS", "Operational Procedures"),
    ("GNAV", "General Navigation"),
    ("RNAV", "Radio Navigation"),
    ("AF", "Airframes"),
    ("ACP", "Aircraft Performance"),
    ("HP", "Human Performance"),
    ("FP", "Flight Planning"),
    ("MB", "Mass and Balance"),
]

PPL_ONLY = [
    ("COMMS", "Communications"),
    ("PIST", "Piston Engines"),
    ("DC", "DC Electrics"),
]

CPL_ONLY = [
    ("GT", "Gas Turbine"),
    ("AC", "AC Electrics"),
]


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        ppl, _ = Course.objects.get_or_create(code="PPL", name="Private Pilot Licence")
        cpl, _ = Course.objects.get_or_create(code="CPL", name="Commercial Pilot Licence")

        def add_subjects(course, subjects):
            for code, name in subjects:
                Subject.objects.get_or_create(
                    course=course,
                    code=code,
                    defaults={"name": name}
                )

        add_subjects(ppl, COMMON_SUBJECTS + PPL_ONLY)
        add_subjects(cpl, COMMON_SUBJECTS + CPL_ONLY)

        self.stdout.write(self.style.SUCCESS("Syllabus seeded successfully"))