from django.contrib.gis.geos import Point


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