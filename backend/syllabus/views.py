from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, Subject, Topic


class CourseListView(APIView):

    def get(self, request):
        courses = Course.objects.all()

        data = [
            {
                "code": c.code,
                "name": c.name
            }
            for c in courses
        ]

        return Response(data)


class SubjectListView(APIView):

    def get(self, request):
        course_code = request.GET.get("course")

        subjects = Subject.objects.filter(course__code=course_code)

        data = [
            {
                "code": s.code,
                "name": s.name
            }
            for s in subjects
        ]

        return Response(data)


class TopicListView(APIView):

    def get(self, request):
        subject_code = request.GET.get("subject")
        course_code = request.GET.get("course")

        topics = Topic.objects.filter(
            subject__code=subject_code,
            subject__course__code=course_code
        )

        data = [
            {
                "id": t.id,
                "title": t.title
            }
            for t in topics
        ]

        return Response(data)