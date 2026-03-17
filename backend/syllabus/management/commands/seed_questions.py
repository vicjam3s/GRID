from django.core.management.base import BaseCommand
from syllabus.models import Question, Subject, Course

import importlib


PPL_SUBJECTS = [
    "HP",
    "AL",
    "MET",
    "NAV",
    "OPS",
    "RNAV",
]


class Command(BaseCommand):

    help = "Seed all PPL questions"

    def handle(self, *args, **kwargs):

        course = Course.objects.get(code="PPL")

        created = 0
        updated = 0
        deleted = 0

        for subject_code in PPL_SUBJECTS:

            subject = Subject.objects.get(code=subject_code)

            module_path = f"knowledge_base.PPL.{subject_code}.questions"

            try:
                module = importlib.import_module(module_path)
            except ModuleNotFoundError:
                self.stdout.write(self.style.WARNING(f"No questions for {subject_code}"))
                continue

            questions = module.QUESTIONS

            existing_questions = Question.objects.filter(
                subject=subject,
                course=course
            )

            existing_map = {q.question: q for q in existing_questions}

            current_questions = []

            for q in questions:

                question_text = q["question"]

                current_questions.append(question_text)

                if question_text in existing_map:

                    obj = existing_map[question_text]

                    obj.choices = q["choices"]
                    obj.correct_answer = q["correct_answer"]
                    obj.explanation = q["explanation"]

                    obj.save()

                    updated += 1

                else:

                    Question.objects.create(
                        question=question_text,
                        subject=subject,
                        course=course,
                        choices=q["choices"],
                        correct_answer=q["correct_answer"],
                        explanation=q["explanation"],
                    )

                    created += 1

            # Delete removed questions
            for db_question in existing_questions:

                if db_question.question not in current_questions:

                    db_question.delete()
                    deleted += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"\nQuestions Sync Complete\n"
                f"Created: {created}\n"
                f"Updated: {updated}\n"
                f"Deleted: {deleted}"
            )
        )