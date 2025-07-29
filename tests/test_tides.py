import math

from krakenctl.tides import SEMIDIURNAL_PERIOD_H, TideStation, height_at, next_high_water

PORT_ROYAL = TideStation("Port Royal", mean_level_m=3.0, range_m=2.0)


def test_high_water_at_the_offset():
    assert math.isclose(height_at(PORT_ROYAL, 0.0), 4.0)


def test_low_water_half_a_cycle_later():
    assert math.isclose(height_at(PORT_ROYAL, SEMIDIURNAL_PERIOD_H / 2), 2.0, abs_tol=1e-9)


def test_next_high_water_rolls_forward():
    assert math.isclose(next_high_water(PORT_ROYAL, after_hours=1.0), SEMIDIURNAL_PERIOD_H)
