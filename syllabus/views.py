from rest_framework import viewsets, permissions
from .models import Course
from .serializers import CourseSerializer

# Create your views here.

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related(
        "subjects__topics__subtopics"
    )
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]