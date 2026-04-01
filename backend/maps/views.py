from django.shortcuts import render
from rest_framework import generics
from aerodromes.models import Aerodrome

from .serializers import AerodromeGeoSerializer, AerodromeDetailSerializer, AirspaceGeoSerializer

from django.contrib.gis.geos import Polygon
from .models import Airspace

# Create your views here.

class AerodromeGeoView(generics.ListAPIView):
    serializer_class = AerodromeGeoSerializer

    def get_queryset(self):
        queryset = Aerodrome.objects.filter(status="OPEN")

        # BBOX filtering (MAP PERFORMANCE)
        bbox = self.request.query_params.get("bbox")

        if bbox:
            try:
                min_lon, min_lat, max_lon, max_lat = map(float, bbox.split(","))
                bbox_polygon = Polygon.from_bbox((min_lon, min_lat, max_lon, max_lat))
                queryset = queryset.filter(location__within=bbox_polygon)
            except:
                pass

        return queryset

class AerodromeDetailView(generics.RetrieveAPIView):
    queryset = Aerodrome.objects.all()
    serializer_class = AerodromeDetailSerializer
    lookup_field = "icao_code"    


from django.contrib.gis.geos import Polygon
from rest_framework import generics
from .models import Airspace
from .serializers import AirspaceGeoSerializer


class AirspaceGeoView(generics.ListAPIView):
    serializer_class = AirspaceGeoSerializer

    def get_queryset(self):
        queryset = Airspace.objects.all()

        bbox = self.request.query_params.get("bbox")

        if bbox:
            try:
                min_lon, min_lat, max_lon, max_lat = map(float, bbox.split(","))
                bbox_polygon = Polygon.from_bbox((min_lon, min_lat, max_lon, max_lat))
                queryset = queryset.filter(boundary__intersects=bbox_polygon)
            except:
                pass

        return queryset    