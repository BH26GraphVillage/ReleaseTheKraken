from krakenctl.soundings import Sounding, is_safe, under_keel_clearance


def test_clearance_accounts_for_tide():
    sounding = Sounding(depth_m=8.0, tide_offset_m=1.5)
    assert under_keel_clearance(sounding, draught_m=4.0) == 2.5


def test_shallow_water_is_not_safe():
    assert not is_safe(Sounding(depth_m=4.2), draught_m=4.0)


def test_deep_water_is_safe():
    assert is_safe(Sounding(depth_m=12.0), draught_m=4.0)
