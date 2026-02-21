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
    path("health/", health_check),
    path("api/", include("PROJECT.api_urls")),
]