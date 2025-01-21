"""Command line helm for krakenctl."""

from __future__ import annotations

import argparse

from .charts import Waypoint, bearing, haversine


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="krakenctl", description="Deck utilities for the S.S. Kraken")
    sub = parser.add_subparsers(dest="command", required=True)

    course = sub.add_parser("bearing", help="Plot a course between two marks")
    course.add_argument("--from", dest="origin", required=True, help='e.g. "51.5074,-0.1278"')
    course.add_argument("--to", dest="destination", required=True, help='e.g. "40.7128,-74.0060"')

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "bearing":
        start = Waypoint.parse(args.origin, "departure")
        end = Waypoint.parse(args.destination, "landfall")
        print(f"Bearing : {bearing(start, end):.2f} deg true")
        print(f"Distance: {haversine(start, end):.1f} nm")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
