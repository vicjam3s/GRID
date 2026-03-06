from collections import defaultdict

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from progress.models import QuestionAttempt


# Create your view here.

# Subject level analytics
class SubjectAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attempts = (
            QuestionAttempt.objects
            .filter(exam__user=request.user)
            .select_related(
                "question__subtopic__topic__subject"
            )
        )

        stats = defaultdict(lambda: {
            "subject_id": None,
            "subject_name": None,
            "total_questions": 0,
            "correct_answers": 0,
            "accuracy_percent": 0,
        })

        for attempt in attempts:
            subject = attempt.question.subtopic.topic.subject
            subject_id = subject.id

            stats[subject_id]["subject_id"] = subject.id
            stats[subject_id]["subject_name"] = subject.name
            stats[subject_id]["total_questions"] += 1

            if attempt.is_correct:
                stats[subject_id]["correct_answers"] += 1

        # calculate accuracy
        for subject_id, data in stats.items():
            if data["total_questions"] > 0:
                data["accuracy_percent"] = int(
                    (data["correct_answers"] / data["total_questions"]) * 100
                )

        # sort weakest → strongest
        results = sorted(
            stats.values(),
            key=lambda x: x["accuracy_percent"]
        )

        return Response(results)
    
# Topic level analytics view
class TopicAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attempts = (
            QuestionAttempt.objects
            .filter(exam__user=request.user)
            .select_related(
                "question__subtopic__topic__subject"
            )
        )

        stats = defaultdict(lambda: {
            "topic_id": None,
            "topic_name": None,
            "subject_name": None,
            "total_questions": 0,
            "correct_answers": 0,
            "accuracy_percent": 0,
        })

        for attempt in attempts:
            topic = attempt.question.subtopic.topic
            topic_id = topic.id

            stats[topic_id]["topic_id"] = topic.id
            stats[topic_id]["topic_name"] = topic.title
            stats[topic_id]["subject_name"] = topic.subject.name
            stats[topic_id]["total_questions"] += 1

            if attempt.is_correct:
                stats[topic_id]["correct_answers"] += 1

        for topic_id, data in stats.items():
            if data["total_questions"] > 0:
                data["accuracy_percent"] = int(
                    (data["correct_answers"] / data["total_questions"]) * 100
                )

        # weakest topics first
        results = sorted(
            stats.values(),
            key=lambda x: x["accuracy_percent"]
        )

        return Response(results)    

# Sub-topic level analytics
class SubtopicAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attempts = (
            QuestionAttempt.objects
            .filter(exam__user=request.user)
            .select_related(
                "question__subtopic__topic__subject"
            )
        )

        stats = defaultdict(lambda: {
            "subtopic_id": None,
            "subtopic_name": None,
            "topic_name": None,
            "subject_name": None,
            "total_questions": 0,
            "correct_answers": 0,
            "accuracy_percent": 0,
        })

        for attempt in attempts:
            subtopic = attempt.question.subtopic
            sid = subtopic.id

            stats[sid]["subtopic_id"] = subtopic.id
            stats[sid]["subtopic_name"] = subtopic.title
            stats[sid]["topic_name"] = subtopic.topic.title
            stats[sid]["subject_name"] = subtopic.topic.subject.name
            stats[sid]["total_questions"] += 1

            if attempt.is_correct:
                stats[sid]["correct_answers"] += 1

        for data in stats.values():
            if data["total_questions"] > 0:
                data["accuracy_percent"] = int(
                    (data["correct_answers"] / data["total_questions"]) * 100
                )

        # weakest subtopics first
        results = sorted(
            stats.values(),
            key=lambda x: x["accuracy_percent"]
        )

        return Response(results)    