from django.contrib.gis.geos import Point
import re
import math
from django.contrib.gis.geos import Polygon

def create_circular_airspace(lon, lat, radius_nm):
    """
    Create a circular polygon (approx) from center + radius in nautical miles.
    """
    # 1 NM = 1852 meters
    radius_m = radius_nm * 1852

    point = Point(lon, lat, srid=4326)

    # buffer expects meters → transform to projected system
    point.transform(3857)  # Web Mercator
    circle = point.buffer(radius_m)
    circle.transform(4326)

    return circle

def aip_to_decimal(coord_str):
    """
    Converts AIP coordinate format:
    011441.48N → decimal latitude
    0351346.82E → decimal longitude
    """

   

    match = re.match(r"(\d+)(\d{2})(\d{2}\.\d+)([NSEW])", coord_str)

    if not match:
        raise ValueError(f"Invalid AIP coordinate: {coord_str}")

    deg, minutes, seconds, direction = match.groups()

    decimal = int(deg) + int(minutes) / 60 + float(seconds) / 3600

    if direction in ["S", "W"]:
        decimal = -decimal

    return decimal

def parse_aip_point(lat_str, lon_str):
    return (
        aip_to_decimal(lon_str),
        aip_to_decimal(lat_str),
    )



def generate_arc(center_lon, center_lat, radius_nm, start_point, end_point, clockwise=True, steps=32):
    """
    Generates points along an arc between two points.
    """

    def bearing(cx, cy, px, py):
        return math.atan2(py - cy, px - cx)

    cx, cy = center_lon, center_lat

    start_angle = bearing(cx, cy, start_point[0], start_point[1])
    end_angle = bearing(cx, cy, end_point[0], end_point[1])

    if clockwise:
        if end_angle > start_angle:
            end_angle -= 2 * math.pi
        step = -abs((start_angle - end_angle) / steps)
    else:
        if end_angle < start_angle:
            end_angle += 2 * math.pi
        step = abs((end_angle - start_angle) / steps)

    radius_deg = radius_nm / 60  # approx conversion

    points = []

    angle = start_angle
    while (clockwise and angle >= end_angle) or (not clockwise and angle <= end_angle):
        x = cx + radius_deg * math.cos(angle)
        y = cy + radius_deg * math.sin(angle)
        points.append((x, y))
        angle += step

    return points




def build_airspace_polygon(segments):
    """
    segments = list of:
    - ("point", (lon, lat))
    - ("arc", {...})
    """

    coords = []

    for segment in segments:
        if segment["type"] == "point":
            coords.append(segment["coord"])

        elif segment["type"] == "arc":
            arc_points = generate_arc(
                center_lon=segment["center"][0],
                center_lat=segment["center"][1],
                radius_nm=segment["radius_nm"],
                start_point=segment["start"],
                end_point=segment["end"],
                clockwise=segment.get("clockwise", True),
            )
            coords.extend(arc_points)

    # Close polygon
    if coords[0] != coords[-1]:
        coords.append(coords[0])

    return Polygon(coords)


