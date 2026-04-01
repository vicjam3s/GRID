from django.shortcuts import render
from rest_framework import generics
from aerodromes.models import Aerodrome
from .serializers import AerodromeGeoSerializer

# Create your views here.

class AerodromeGeoView(generics.ListAPIView):
    queryset = Aerodrome.objects.all()
    serializer_class = AerodromeGeoSerializer

# maps/views.py

from rest_framework import generics
from aerodromes.models import Aerodrome
from .serializers import AerodromeDetailSerializer


class AerodromeDetailView(generics.RetrieveAPIView):
    queryset = Aerodrome.objects.all()
    serializer_class = AerodromeDetailSerializer
    lookup_field = "icao_code"    