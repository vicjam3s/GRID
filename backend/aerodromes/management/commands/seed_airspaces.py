from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Polygon
from maps.models import Airspace
from maps.utils import create_circular_airspace, parse_aip_point, build_airspace_polygon



class Command(BaseCommand):
    help = "Seed Kenyan airspaces (AIP-aligned structure)"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding airspaces...")

        Airspace.objects.all().delete()

        # ======================================================
        # CONTROL ZONES (CTR)
        # ======================================================
        ctr_airspaces = [
            {
                "name": "Nairobi Control Zone",
                "lon": 36.8750,
                "lat": -1.3192,
                "radius_nm": 15,
                "upper_ft": 9000,
                "class": "C",
                "unit": "Eastleigh TWR",
                "call_sign": "Eastleigh Tower",
                "freq_primary": 124.30,
                "freq_secondary": 124.80,
                "hours": "0500-1400 UTC",
                "remarks": "Military aerodrome (Eastleigh)",
            },
            {
                "name": "Mombasa Control Zone",
                "lon": 39.6682,
                "lat": -4.0348,
                "radius_nm": 15,
                "upper_ft": 3500,
                "class": "D",
                "unit": "Mombasa TWR",
                "call_sign": "Mombasa Tower",
                "freq_primary": 118.60,
                "hours": "H24",
            },
            {
                "name": "Kisumu Control Zone",
                "lon": 34.7289,
                "lat": -0.0861,
                "radius_nm": 15,
                "upper_ft": 9000,
                "class": "D",
                "unit": "Kisumu TWR",
                "call_sign": "Kisumu Tower",
                "freq_primary": 118.80,
                "hours": "0330-1800 UTC",
            },
            {
                "name": "Eldoret Control Zone",
                "lon": 35.2367,
                "lat": 0.4040,
                "radius_nm": 15,
                "upper_ft": 10000,
                "class": "D",
                "unit": "Eldoret TWR",
                "call_sign": "Eldoret TWR",
                "freq_primary": 120.80,
                "hours": "0330-1800 UTC",
            },
            {
                "name": "Embu Control Zone",
                "lon": 37.4948,
                "lat": -0.5723,
                "radius_nm": 15,
                "upper_ft": 9000,
                "class": "D",
                "unit": "Embu TWR",
                "call_sign": "Embu TWR",
                "freq_primary": 118.20,
                "hours": "0330-1500 UTC",
            },
            {
                "name": "Malindi Control Zone",
                "lon": 40.1010,
                "lat": -3.2214,
                "radius_nm": 15,
                "upper_ft": 3500,
                "class": "D",
                "unit": "Malindi TWR",
                "call_sign": "Malindi TWR",
                "freq_primary": 120.40,
                "hours": "0330-1730 UTC",
            },
            {
                "name": "Wajir Control Zone",
                "lon": 40.0915,
                "lat": 1.7332,
                "radius_nm": 15,
                "upper_ft": 5000,
                "class": "D",
                "unit": "Wajir TWR",
                "call_sign": "Wajir TWR",
                "freq_primary": 118.30,
                "hours": "0330-1530 UTC",
                "remarks": "Civil/Military airport",
            },
        ]

        for ctr in ctr_airspaces:
            Airspace.objects.update_or_create(
                name=ctr["name"],
                defaults={
                    "airspace_type": f"CLASS_{ctr['class']}",
                    "boundary": create_circular_airspace(
                        ctr["lon"], ctr["lat"], ctr["radius_nm"]
                    ),
                    "lower_limit_ft": 0,
                    "lower_limit_type": "GND",
                    "upper_limit_ft": ctr["upper_ft"],
                    "upper_limit_type": "AMSL",
                    "airspace_class": ctr["class"],
                    "unit_providing_service": ctr.get("unit"),
                    "call_sign": ctr.get("call_sign"),
                    "frequency_primary_mhz": ctr.get("freq_primary"),
                    "frequency_secondary_mhz": ctr.get("freq_secondary"),
                    "hours_of_service": ctr.get("hours"),
                    "remarks": ctr.get("remarks"),
                    "controlling_authority": ctr.get("unit"),
                },
            )

        # ======================================================
        # NAIROBI TMA (CORRECTED TO CLASS E)
        # ======================================================
        Airspace.objects.update_or_create(
            name="Nairobi TMA",
            defaults={
                "airspace_type": "CLASS_E",
                "boundary": create_circular_airspace(
                    lon=36.9542,
                    lat=-1.2999,
                    radius_nm=50,
                ),
                "lower_limit_ft": 1500,
                "lower_limit_type": "AGL",
                "upper_limit_ft": 14500,
                "upper_limit_type": "FL",
                "airspace_class": "E",
                "unit_providing_service": "Nairobi APP Radar",
                "call_sign": "Nairobi APP Radar",
                "frequency_primary_mhz": 122.30,
                "frequency_secondary_mhz": 124.10,
                "hours_of_service": "H24",
                "remarks": "VFR prohibited above FL145",
                "controlling_authority": "Nairobi APP",
            },
        )

        # ======================================================
        # ELDORET TMA (AIP-ACCURATE WITH ARC)
        # ======================================================

        # Key AIP points
        p1 = parse_aip_point("011441.48N", "0351346.82E")
        center = parse_aip_point("002423.96N", "0351351.82E")  # DVOR ELD
        p2 = parse_aip_point("002558.03S", "0351358.01E")      # NEVON
        p3 = parse_aip_point("002609.56S", "0335802.74E")
        p4 = parse_aip_point("011332.02N", "0344732.34E")      # GONGU

        eldoret_tma_polygon = build_airspace_polygon([
            {"type": "point", "coord": p1},

            {
                "type": "arc",
                "center": center,
                "radius_nm": 50,
                "start": p1,
                "end": p2,
                "clockwise": True,
            },

            {"type": "point", "coord": p3},

            # Border segment approximated as straight line
            {"type": "point", "coord": p4},

            {"type": "point", "coord": p1},  # close polygon
        ])


        Airspace.objects.update_or_create(
            name="Eldoret TMA",
            defaults={
                "airspace_type": "CLASS_E",

                "boundary": eldoret_tma_polygon,

                "lower_limit_ft": 1500,
                "lower_limit_type": "AMSL",

                "upper_limit_ft": 14500,
                "upper_limit_type": "FL",

                "airspace_class": "E",

                "unit_providing_service": "Eldoret APP",
                "call_sign": "Eldoret APP",

                "frequency_primary_mhz": 119.40,

                "hours_of_service": "0330-1800 UTC",
                "remarks": "VFR prohibited above FL145",

                "controlling_authority": "Eldoret APP",
            },
        )

        # ======================================================
        # MOMBASA TMA (AIP-ACCURATE WITH ARC)
        # ======================================================

        # AIP points
        p1 = parse_aip_point("025159.83S", "0393002.00E")

        center = parse_aip_point("031400.73S", "0400609.39E")  # DVOR MLD

        p2 = parse_aip_point("031421.25S", "0404850.69E")

        p3 = parse_aip_point("044004.10S", "0402823.24E")  # WPT MOKAD

        p4 = parse_aip_point("044208.40S", "0391403.20E")

        p5 = parse_aip_point("040230.28S", "0381736.00E")  # WPT EPTEL


        mombasa_tma_polygon = build_airspace_polygon([
            {"type": "point", "coord": p1},

            {
                "type": "arc",
                "center": center,
                "radius_nm": 42,
                "start": p1,
                "end": p2,
                "clockwise": True,
            },

            {"type": "point", "coord": p3},
            {"type": "point", "coord": p4},

            # Tanzania/Kenya border (simplified straight)
            {"type": "point", "coord": p5},

            {"type": "point", "coord": p1},
        ])


        Airspace.objects.update_or_create(
            name="Mombasa TMA",
            defaults={
                "airspace_type": "CLASS_E",

                "boundary": mombasa_tma_polygon,

                "lower_limit_ft": 1500,
                "lower_limit_type": "AGL",

                "upper_limit_ft": 14500,
                "upper_limit_type": "FL",

                "airspace_class": "E",

                "unit_providing_service": "Mombasa APP",
                "call_sign": "Mombasa APP",

                "frequency_primary_mhz": 120.30,
                "frequency_secondary_mhz": 121.70,

                "hours_of_service": "H24",
                "remarks": "VFR prohibited above FL145",

                "controlling_authority": "Mombasa APP",
            },
        )


        # ======================================================
        # MOMBASA TMA RADAR (SEPARATE SERVICE)
        # ======================================================

        Airspace.objects.update_or_create(
            name="Mombasa TMA Radar",
            defaults={
                "airspace_type": "CLASS_E",

                "boundary": mombasa_tma_polygon,

                "lower_limit_ft": 1500,
                "lower_limit_type": "AGL",

                "upper_limit_ft": 14500,
                "upper_limit_type": "FL",

                "airspace_class": "E",

                "unit_providing_service": "Mombasa APP Radar",
                "call_sign": "Mombasa APP Radar",

                "frequency_primary_mhz": 121.70,
                "frequency_secondary_mhz": 122.70,

                "hours_of_service": "H24",

                "controlling_authority": "Mombasa APP",
            },
        )

        # ======================================================
        # WAJIR TMA (AIP-ACCURATE WITH ARC)
        # ======================================================

        # AIP points
        p1 = parse_aip_point("013248.91N", "0391643.17E")

        center = parse_aip_point("014448.53N", "0400456.73E")  # DVOR WAV

        p2 = parse_aip_point("022352.79N", "0403614.43E")  # WPT OKNAV

        p3 = parse_aip_point("015943.94N", "0405909.35E")

        p4 = parse_aip_point("005949.89N", "0410003.47E")  # WPT ENABO

        p5 = parse_aip_point("005729.67N", "0392352.54E")

        p6 = parse_aip_point("012328.38N", "0390853.11E")


        wajir_tma_polygon = build_airspace_polygon([
            {"type": "point", "coord": p1},

            {
                "type": "arc",
                "center": center,
                "radius_nm": 50,
                "start": p1,
                "end": p2,
                "clockwise": True,
            },

            {"type": "point", "coord": p3},

            # Somalia border (simplified straight segments)
            {"type": "point", "coord": p4},
            {"type": "point", "coord": p5},

            {"type": "point", "coord": p6},

            {"type": "point", "coord": p1},  # close polygon
        ])


        Airspace.objects.update_or_create(
            name="Wajir TMA",
            defaults={
                "airspace_type": "CLASS_E",

                "boundary": wajir_tma_polygon,

                "lower_limit_ft": 1500,
                "lower_limit_type": "AGL",

                "upper_limit_ft": 14500,
                "upper_limit_type": "FL",

                "airspace_class": "E",

                "unit_providing_service": "Wajir APP",
                "call_sign": "Wajir APP",

                "frequency_primary_mhz": 118.30,

                "hours_of_service": "0330-1530 UTC",
                "remarks": "VFR prohibited above FL145",

                "controlling_authority": "Wajir APP",
            },
        )
        

        # ======================================================
        # NAIROBI FIR (AIP-ACCURATE POLYGON)
        # ======================================================

        fir_points = [
            ("040000.00N", "0340502.90E"),
            ("035849.16N", "0415418.60E"),
            ("014029.53S", "0413329.37E"),
            ("010203.00S", "0410656.00E"),
            ("012242.00S", "0404839.00E"),
            ("014116.00S", "0403930.00E"),
            ("015459.00S", "0401532.00E"),
            ("020925.00S", "0400337.00E"),
            ("021923.00S", "0395800.00E"),
            ("022659.00S", "0394545.00E"),
            ("025100.00S", "0393058.00E"),
            ("030000.00S", "0393000.00E"),
            ("033600.00S", "0393000.00E"),
            ("034600.00S", "0391400.00E"),
            ("035600.00S", "0380000.00E"),
            ("040000.00S", "0372000.00E"),
            ("012000.00N", "0370000.00E"),
            ("040000.00N", "0340502.90E"),
        ]

        fir_polygon = Polygon([
            parse_aip_point(lat, lon)
            for lat, lon in fir_points
        ])


        Airspace.objects.update_or_create(
            name="Nairobi FIR",
            defaults={
                "airspace_type": "CLASS_G",

                "boundary": fir_polygon,

                "lower_limit_ft": 0,
                "lower_limit_type": "GND",

                "upper_limit_ft": None,
                "upper_limit_type": "UNL",

                "airspace_class": "G",

                "unit_providing_service": "Nairobi ACC",
                "call_sign": "Nairobi Control",

                "frequency_primary_mhz": 121.30,
                "frequency_secondary_mhz": 128.70,

                "hours_of_service": "H24",

                "remarks": "Full FIR boundary from AIP",

                "controlling_authority": "Nairobi ACC",
            },
        )