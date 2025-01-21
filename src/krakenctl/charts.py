"""Great-circle maths for plotting a course between two waypoints."""

from __future__ import annotations

import math
from dataclasses import dataclass

EARTH_RADIUS_NM = 3440.065  # nautical miles


@dataclass(frozen=True)
class Waypoint:
    """A single mark on the chart."""

    latitude: float
    longitude: float
    name: str = "unnamed mark"

    @classmethod
    def parse(cls, raw: str, name: str = "unnamed mark") -> "Waypoint":
        lat_str, _, lon_str = raw.partition(",")
        return cls(float(lat_str.strip()), float(lon_str.strip()), name)


def haversine(start: Waypoint, end: Waypoint) -> float:
    """Distance between two waypoints in nautical miles."""
    lat1, lat2 = math.radians(start.latitude), math.radians(end.latitude)
    d_lat = lat2 - lat1
    d_lon = math.radians(end.longitude - start.longitude)

    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2) ** 2
    return 2 * EARTH_RADIUS_NM * math.asin(math.sqrt(a))


def bearing(start: Waypoint, end: Waypoint) -> float:
    """Initial true bearing from start to end, in degrees."""
    lat1, lat2 = math.radians(start.latitude), math.radians(end.latitude)
    d_lon = math.radians(end.longitude - start.longitude)

    x = math.sin(d_lon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(d_lon)
    return math.degrees(math.atan2(x, y)) % 360
