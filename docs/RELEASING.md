# Releasing

Since the refit, releases are **no longer cut from this repository**.

The Bosun runs the internal Deckhand CI rig on the dockside build fleet. It builds the
wheel, forges the build manifest and publishes the sailing to the
[Releases](../../releases) page.

## How a release happens now

1. Raise a release request with the Bosun (`@one-eyed-pete`).
2. Deckhand CI builds from `main` at the agreed commit.
3. The rig tags `vX.Y.Z` and publishes the release with its manifest attached.

## Why the shipyard automation was cut loose

The old in-repo rig needed a write-scoped token on the deck and tagged straight from
pushes, which the Captain judged too loose a knot. It has been hauled off the deck.

> Sailings published before the refit used the shipyard's own tag convention and are
> left on the Releases page for the record. Do not delete them — the manifests are the
> only proof of what shipped.
