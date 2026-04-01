from rest_framework_gis.serializers import GeoFeatureModelSerializer
from aerodromes.models import Aerodrome, Runway, Communication, FBO
from rest_framework import serializers
from .models import Airspace

class AerodromeGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Aerodrome
        geo_field = "location"

        fields = (
            "id",
            "icao_code",
            "name",
            "city",
            "elevation_ft",
            "status",

        )

class RunwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Runway
        fields = "__all__"


class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = "__all__"


class FBOSerializer(serializers.ModelSerializer):
    class Meta:
        model = FBO
        fields = "__all__"


class AerodromeDetailSerializer(serializers.ModelSerializer):
    runways = RunwaySerializer(many=True)
    communications = CommunicationSerializer(many=True)
    fbos = FBOSerializer(many=True)

    class Meta:
        model = Aerodrome
        fields = "__all__"





class AirspaceGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Airspace
        geo_field = "boundary"
        fields = (
            "id",
            "name",
            "airspace_type",
            "lower_limit_ft",
            "upper_limit_ft",
        )