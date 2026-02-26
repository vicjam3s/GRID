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

    "Operational Procedures": {
        "01 General Requirements": [
            "ICAO Annex 6 (Operation of Aircraft)",
            "Operator Responsibilities (Safe conduct of flight)",
            "Documents to be Carried (The \"Checklist\" of certificates)",
        ],

        "02 Special Environments and Hazards": [
            "Wake Turbulence (Vortices, separation times)",
            "Windshear and Microburst (Recognition and recovery)",
            "Contaminated Runways (Hydroplaning, braking action)",
            "Bird Strike Hazards",
        ],

        "03 Emergency Procedures": [
            "Engine Failure (Standard restart and forced landing)",
            "Fires (Engine, Cabin, Electrical, Wing)",
            "Ditching (Water landing techniques)",
            "Depressurization (Oxygen requirements)",
        ],

        "04 Search and Rescue (SAR)": [
            "The Three Phases (INCERFA, ALERFA, DETRESFA)",
            "Visual Signals (Ground-to-Air codes)",
            "Emergency Locators (ELT frequencies and usage)",
        ],
    },

    "Human Performance": {
        "01 Basic Physiology": [
            "The Atmosphere and Gases (Composition: 78% Nitrogen, 21% Oxygen)",
            "Gas Laws (Dalton’s: Partial pressure; Boyle’s: Gas expansion)",
            "Pressure Changes (Trapped gas in ears, sinuses, and gut)",
            "Respiratory System (Lungs, Alveoli, Hemoglobin transport)",
            "Hypoxia Types (Hypoxic, Stagnant, Hypemic, Histotoxic)",
            "Hyperventilation (Loss of CO₂, alkalosis)",
            "Carbon Monoxide (Symptoms and disposal time – up to 48 hours)",
            "Circulatory System (Blood pressure, G-forces, G-LOC)",
            "Health Factors (Smoking, Obesity, Exercise)",
        ],

        "02 Sensory Systems": [
            "Vision – Functional Anatomy (Cones for day/color, Rods for night)",
            "Night Vision (Dark adaptation: 30 minutes; Empty field myopia)",
            "Scanning Techniques (Short eye movements, 10° sectors)",
            "The Ear (Outer, Middle, Inner, Cochlea)",
            "Balance (Vestibular system: Semicircular canals and Otoliths)",
            "Vestibular Illusions (The Leans, Coriolis illusion, Graveyard spin)",
            "Visual Illusions (Autokinesis, False horizons, Black hole approach)",
        ],

        "03 Health and Hygiene": [
            "Medication (Side effects of common drugs e.g. Aspirin, Antihistamines)",
            "Alcohol (8-hour rule vs KCAA 12-hour preference; 0.02% limit)",
            "Blood Donation (Wait 24–48 hours before flying)",
            "Circadian Dysrhythmia (Jet lag)",
            "Sleep and Fatigue (Acute vs Chronic fatigue)",
            "IMSAFE Checklist (Illness, Medication, Stress, Alcohol, Fatigue, Emotion/Eating)",
        ],

        "04 Basic Psychology": [
            "Information Processing (Perception and Memory)",
            "Memory Types (Short-term / Working vs Long-term)",
            "Attention (Selective vs Divided attention)",
            "Human Error Models (SHEL Model)",
            "Swiss Cheese Model (James Reason)",
            "Decision Making (Risk assessment and judgment)",
            "Hazardous Attitudes (Anti-authority, Impulsivity, Invulnerability, Macho, Resignation)",
            "Stress Management (Arousal levels and performance)",
        ],
    },
}


CPL_SYLLABUS = {
   
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