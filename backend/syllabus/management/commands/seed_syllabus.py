from django.core.management.base import BaseCommand
from syllabus.models import Course, Subject, Topic, Subtopic

from syllabus.data import PPL_SYLLABUS, CPL_SYLLABUS


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

        # Ensure course stays updated
        course.name = name
        course.authority = "KCAA"
        course.save()

        for subject_order, (subject_name, topics) in enumerate(syllabus.items(), start=1):

            subject, _ = Subject.objects.get_or_create(
                course=course,
                name=subject_name,
                defaults={"order": subject_order},
            )

            subject.order = subject_order
            subject.save()

            for topic_order, (topic_title, subtopics) in enumerate(topics.items(), start=1):

                topic, _ = Topic.objects.get_or_create(
                    subject=subject,
                    title=topic_title,
                    defaults={"order": topic_order},
                )

                topic.order = topic_order
                topic.save()

                # Create or update subtopics
                for subtopic_order, subtopic_title in enumerate(subtopics, start=1):

                    subtopic, _ = Subtopic.objects.get_or_create(
                        topic=topic,
                        title=subtopic_title,
                        defaults={"order": subtopic_order},
                    )

                    subtopic.order = subtopic_order
                    subtopic.save()

                # Remove obsolete subtopics
                existing = set(
                    Subtopic.objects.filter(topic=topic)
                    .values_list("title", flat=True)
                )

                new = set(subtopics)

                for obsolete in existing - new:
                    Subtopic.objects.filter(
                        topic=topic,
                        title=obsolete
                    ).delete()