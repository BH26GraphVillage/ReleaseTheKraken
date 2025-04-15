"""Depth soundings: keep the keel off the seabed."""

from __future__ import annotations

from dataclasses import dataclass

SAFETY_MARGIN_M = 0.6


@dataclass(frozen=True)
class Sounding:
    """A single depth reading taken from the echo sounder."""

    depth_m: float
    tide_offset_m: float = 0.0

    @property
    def charted_depth_m(self) -> float:
        return self.depth_m - self.tide_offset_m


def under_keel_clearance(sounding: Sounding, draught_m: float) -> float:
    """Water left between the keel and the seabed, in metres."""
    return sounding.charted_depth_m - draught_m


def is_safe(sounding: Sounding, draught_m: float, margin_m: float = SAFETY_MARGIN_M) -> bool:
    """True when there is enough water to stay afloat with the agreed margin."""
    return under_keel_clearance(sounding, draught_m) >= margin_m
