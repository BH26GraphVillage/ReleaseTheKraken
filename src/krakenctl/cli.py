"""Command line helm for krakenctl."""

from __future__ import annotations

import argparse

from .charts import Waypoint, bearing, haversine
from .soundings import Sounding, is_safe, under_keel_clearance


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="krakenctl", description="Deck utilities for the S.S. Kraken")
    sub = parser.add_subparsers(dest="command", required=True)

    course = sub.add_parser("bearing", help="Plot a course between two marks")
    course.add_argument("--from", dest="origin", required=True, help='e.g. "51.5074,-0.1278"')
    course.add_argument("--to", dest="destination", required=True, help='e.g. "40.7128,-74.0060"')

    sounding = sub.add_parser("sounding", help="Check under-keel clearance")
    sounding.add_argument("--depth", type=float, required=True, help="Echo sounder reading in metres")
    sounding.add_argument("--tide", type=float, default=0.0, help="Tide offset in metres")
    sounding.add_argument("--draught", type=float, required=True, help="Vessel draught in metres")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "bearing":
        start = Waypoint.parse(args.origin, "departure")
        end = Waypoint.parse(args.destination, "landfall")
        print(f"Bearing : {bearing(start, end):.2f} deg true")
        print(f"Distance: {haversine(start, end):.1f} nm")

    if args.command == "sounding":
        reading = Sounding(depth_m=args.depth, tide_offset_m=args.tide)
        clearance = under_keel_clearance(reading, args.draught)
        verdict = "safe passage" if is_safe(reading, args.draught) else "SHOAL WATER - come about"
        print(f"Clearance: {clearance:.2f} m ({verdict})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
