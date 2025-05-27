from krakenctl.charts import Waypoint
from krakenctl.gpx import to_gpx

TRACK = [Waypoint(51.5074, -0.1278, "London"), Waypoint(49.6337, -1.6221, "Cherbourg")]


def test_gpx_contains_every_mark():
    document = to_gpx(TRACK)
    assert document.count("<trkpt") == 2
    assert 'lat="51.507400"' in document
    assert "Cherbourg" in document


def test_gpx_carries_the_voyage_name():
    assert "Trafalgar run" in to_gpx(TRACK, name="Trafalgar run")
