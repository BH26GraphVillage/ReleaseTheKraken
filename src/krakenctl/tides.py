"""Tide predictions from a harmonic table, simplified for deck use."""

from __future__ import annotations

import math
from dataclasses import dataclass

SEMIDIURNAL_PERIOD_H = 12.42  # M2 constituent


@dataclass(frozen=True)
class TideStation:
    """A harbour with a known tidal range."""

    name: str
    mean_level_m: float
    range_m: float
    high_water_offset_h: float = 0.0


def height_at(station: TideStation, hours_after_midnight: float) -> float:
    """Predicted tide height in metres at the given hour."""
    phase = 2 * math.pi * (hours_after_midnight - station.high_water_offset_h) / SEMIDIURNAL_PERIOD_H
    return station.mean_level_m + (station.range_m / 2) * math.cos(phase)


def next_high_water(station: TideStation, after_hours: float = 0.0) -> float:
    """Hour of the next high water after the given hour."""
    elapsed = after_hours - station.high_water_offset_h
    cycles = math.floor(elapsed / SEMIDIURNAL_PERIOD_H) + 1
    return station.high_water_offset_h + cycles * SEMIDIURNAL_PERIOD_H
