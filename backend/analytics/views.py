from collections import defaultdict

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from progress.models import ExamAttempt


# Subject level analytics
class SubjectAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attempts = (
            ExamAttempt.objects
            .filter(user=request.user)
            .select_related("subject", "course")
        )

        stats = defaultdict(lambda: {
            "subject_id": None,
            "subject_name": None,
            "total_attempts": 0,
            "average_score": 0,
            "average_percentage": 0,
        })

        for attempt in attempts:
            subject = attempt.subject
            sid = subject.id

            stats[sid]["subject_id"] = subject.id
            stats[sid]["subject_name"] = subject.name
            stats[sid]["total_attempts"] += 1
            stats[sid]["average_score"] += attempt.score
            stats[sid]["average_percentage"] += attempt.percentage

        for data in stats.values():
            if data["total_attempts"] > 0:
                data["average_score"] = round(
                    data["average_score"] / data["total_attempts"], 2
                )
                data["average_percentage"] = round(
                    data["average_percentage"] / data["total_attempts"], 2
                )

        results = sorted(
            stats.values(),
            key=lambda x: x["average_percentage"]
        )

        return Response(results)


# Topic level analytics
class TopicAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attempts = (
            ExamAttempt.objects
            .filter(user=request.user)
            .select_related("subject")
        )

        stats = defaultdict(lambda: {
            "subject_id": None,
            "subject_name": None,
            "total_attempts": 0,
            "average_percentage": 0,
        })

        for attempt in attempts:
            subject = attempt.subject
            sid = subject.id

            stats[sid]["subject_id"] = subject.id
            stats[sid]["subject_name"] = subject.name
            stats[sid]["total_attempts"] += 1
            stats[sid]["average_percentage"] += attempt.percentage

        for data in stats.values():
            if data["total_attempts"] > 0:
                data["average_percentage"] = round(
                    data["average_percentage"] / data["total_attempts"], 2
                )

        results = sorted(
            stats.values(),
            key=lambda x: x["average_percentage"]
        )

        return Response(results)


# Weak areas (failed questions)
class WeakAreasView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        failed = (
            request.user.examattempt_set
            .prefetch_related("failed_questions__question__subject")
        )

        stats = defaultdict(lambda: {
            "subject_id": None,
            "subject_name": None,
            "failed_count": 0,
        })

        for attempt in failed:
            for fq in attempt.failed_questions.all():
                subject = fq.question.subject
                sid = subject.id

                stats[sid]["subject_id"] = subject.id
                stats[sid]["subject_name"] = subject.name
                stats[sid]["failed_count"] += 1

        results = sorted(
            stats.values(),
            key=lambda x: x["failed_count"],
            reverse=True
        )

        return Response(results)