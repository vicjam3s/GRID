from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def health_check(request):
    return JsonResponse(
        {
            "app": "GRID",
            "status": "ok",
        }
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check),#practice run

    # API endpoints (app-level routing)
    path("api/auth/", include("users.urls")),
    path("api/syllabus/", include("syllabus.urls")),
    path("api/content/", include("content.urls")),
    path("api/exams/", include("assessments.urls")),
]