# Crew Handbook

Welcome aboard. A few rules of the deck before you touch the rigging.

## Signing on

1. Fork the vessel, branch from `main`.
2. Name your branch after the work: `deck/short-description`.
3. Keep commits small — a heavy commit sinks a review.

## Running the drills

```bash
pip install -e ".[dev]"
ruff check src tests
pytest -q
```

## Rules of the deck

- Every change to `src/krakenctl` needs a drill in `tests/`.
- No secrets in the bilge. Tokens, keys and charts of the treasure kind belong
  in repository secrets, never in a commit.
- The Quartermaster keeps [docs/CHANGELOG.md](docs/CHANGELOG.md); add your entry
  under _Unreleased_ and they will sort out the sailing.

## Cutting a release

Releases are the Bosun's business. Do not tag `main` yourself — flag the Bosun and
they will run the release rig and check that the build manifest lists the right hull.
