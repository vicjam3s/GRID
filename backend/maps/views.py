from django.shortcuts import render
from rest_framework import generics
from aerodromes.models import Aerodrome
from .serializers import AerodromeGeoSerializer, AerodromeDetailSerializer

# Create your views here.

from rest_framework import generics
from django.contrib.gis.geos import Polygon
from aerodromes.models import Aerodrome
from .serializers import AerodromeGeoSerializer


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