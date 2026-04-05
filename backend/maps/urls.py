from django.urls import path
from .views import *

urlpatterns = [
    path("airports/", AerodromeGeoView.as_view(), name="airports-geo"),
    path("airports/<str:icao_code>/", AerodromeDetailView.as_view(), name="airport-detail"),
    path("airspaces/", AirspaceGeoView.as_view(), name="airspaces-geo"),
    path("map-data/", MapDataView.as_view(), name="map-data"),
]
