import math

from krakenctl.charts import Waypoint, bearing, haversine

LONDON = Waypoint(51.5074, -0.1278, "London")
NEW_YORK = Waypoint(40.7128, -74.0060, "New York")


def test_distance_london_to_new_york():
    assert math.isclose(haversine(LONDON, NEW_YORK), 3009.0, rel_tol=0.01)


def test_bearing_is_westerly():
    assert 250 < bearing(LONDON, NEW_YORK) < 300


def test_waypoint_parse():
    mark = Waypoint.parse(" 12.5 , -3.25 ", "buoy")
    assert mark.latitude == 12.5
    assert mark.longitude == -3.25
    assert mark.name == "buoy"
