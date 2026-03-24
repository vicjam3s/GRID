from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Resource


class ResourceView(APIView):

    def get(self, request):

        course_code = request.GET.get("course")
        subject_code = request.GET.get("subject")
        resource_type = request.GET.get("type")

        resources = Resource.objects.filter(
            course__code=course_code,
            subject__code=subject_code,
            resource_type=resource_type,
            is_active=True
        )

        data = [
            {
                "id": r.id,
                "title": r.title,
                "file": request.build_absolute_uri(r.file.url)
            }
            for r in resources
        ]

        return Response(data)