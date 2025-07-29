# Changelog

All notable changes to `krakenctl` are logged here by the Quartermaster.
Sailings are recorded in the order they left port.

## [2.1.0] - 2025-07-29

### Added

- Tide predictions from a simplified harmonic table (`krakenctl.tides`).

## [2.0.0] - 2025-05-27

### Added

- GPX chart export for the fleet's chart plotters (`krakenctl chart`).

### Changed

- Releases are cut by the internal Deckhand CI rig; see [RELEASING.md](RELEASING.md).

## [1.1.0] - 2025-04-15

### Added

- Depth soundings with tide correction and under-keel clearance checks.
- `krakenctl sounding` helm command.

### Fixed

- Bearing drift on courses crossing the antimeridian.

## [1.0.0] - 2025-01-21

### Added

- Great-circle bearing and distance between two marks.
- `krakenctl bearing` helm command.
- Deckhand CI checks on every pull request.

### Notes

- Releases in this era were cut by the shipyard automation from tags, and each
  sailing carried a build manifest recording the hull, the commit and the digest.
