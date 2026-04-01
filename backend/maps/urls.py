from django.urls import path
from .views import AerodromeDetailView, AerodromeGeoView

urlpatterns = [
    path("airports/", AerodromeGeoView.as_view(), name="airports-geo"),
    path("airports/<str:icao_code>/", AerodromeDetailView.as_view(), name="airport-detail"),
]
