"""Export a plotted course as a GPX track for the fleet's chart plotters."""

from __future__ import annotations

from xml.etree import ElementTree as ET

from .charts import Waypoint

GPX_NS = "http://www.topografix.com/GPX/1/1"


def to_gpx(track: list[Waypoint], name: str = "S.S. Kraken voyage") -> str:
    """Render a list of waypoints as a GPX 1.1 document."""
    gpx = ET.Element("gpx", {"version": "1.1", "creator": "krakenctl", "xmlns": GPX_NS})
    trk = ET.SubElement(gpx, "trk")
    ET.SubElement(trk, "name").text = name
    segment = ET.SubElement(trk, "trkseg")

    for mark in track:
        point = ET.SubElement(
            segment,
            "trkpt",
            {"lat": f"{mark.latitude:.6f}", "lon": f"{mark.longitude:.6f}"},
        )
        ET.SubElement(point, "name").text = mark.name

    return ET.tostring(gpx, encoding="unicode")
