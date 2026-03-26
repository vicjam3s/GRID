from django.core.management.base import BaseCommand
from syllabus.models import Course, Subject
from assessments.models import Question

import importlib


PPL_SUBJECTS = [
    "HP", "AL", "MET", "POF", "INS", "OPS",
    "GNAV", "RNAV", "AF", "ACP", "FP", "MB",
    "COMMS", "PIST", "DC"
]


class Command(BaseCommand):

    help = "Seed all PPL questions"

    def handle(self, *args, **kwargs):

        course = Course.objects.get(code="PPL")

        created = 0
        updated = 0
        deleted = 0

        for subject_code in PPL_SUBJECTS:

            try:
                subject = Subject.objects.get(
                    course=course,
                    code=subject_code
                )
            except Subject.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Missing subject: {subject_code}"))
                continue

            module_path = f"knowledge_base.PPL.{subject_code}.questions"

            try:
                module = importlib.import_module(module_path)
            except ModuleNotFoundError:
                self.stdout.write(self.style.WARNING(f"No file: {subject_code}"))
                continue

            questions = module.QUESTIONS

            existing = Question.objects.filter(
                course=course,
                subject=subject
            )

            existing_map = {q.question_text: q for q in existing}
            current_questions = []

            for q in questions:

                text = q["question"]
                current_questions.append(text)

                if text in existing_map:
                    obj = existing_map[text]

                    obj.option_a = q["choices"][0]
                    obj.option_b = q["choices"][1]
                    obj.option_c = q["choices"][2]
                    obj.option_d = q["choices"][3]
                    obj.correct_option = q["correct_answer"]
                    obj.explanation = q["explanation"]

                    obj.save()
                    updated += 1

                else:
                    Question.objects.create(
                        course=course,
                        subject=subject,
                        question_text=text,
                        option_a=q["choices"][0],
                        option_b=q["choices"][1],
                        option_c=q["choices"][2],
                        option_d=q["choices"][3],
                        correct_option=q["correct_answer"],
                        explanation=q["explanation"],
                    )
                    created += 1

            # Delete removed questions
            for db_q in existing:
                if db_q.question_text not in current_questions:
                    db_q.delete()
                    deleted += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"\nDone → Created: {created}, Updated: {updated}, Deleted: {deleted}"
            )
        )