from django.shortcuts import render
from rest_framework import generics
from aerodromes.models import Aerodrome
from .serializers import AerodromeGeoSerializer, AerodromeDetailSerializer, AirspaceGeoSerializer
from django.contrib.gis.geos import Polygon
from .models import Airspace
from rest_framework.views import APIView
from rest_framework.response import Response


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


class MapDataView(APIView):
    def get(self, request):

        bbox = request.GET.get("bbox")

        aerodromes = Aerodrome.objects.filter(status="OPEN")
        airspaces = Airspace.objects.all()

        if bbox:
            try:
                min_lon, min_lat, max_lon, max_lat = map(float, bbox.split(","))
                bbox_polygon = Polygon.from_bbox((min_lon, min_lat, max_lon, max_lat))

                aerodromes = aerodromes.filter(location__within=bbox_polygon)
                airspaces = airspaces.filter(boundary__intersects=bbox_polygon)
            except:
                pass

        aerodrome_data = AerodromeGeoSerializer(aerodromes, many=True).data
        airspace_data = AirspaceGeoSerializer(airspaces, many=True).data

        return Response({
            "aerodromes": aerodrome_data,
            "airspaces": airspace_data,
        })   