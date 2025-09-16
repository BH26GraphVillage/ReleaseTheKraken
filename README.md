# 🐙 ReleaseTheKraken

> _"Ye can scrub the deck, but the bilge remembers."_ — Quartermaster's Log, entry 41

`krakenctl` is the deck utility used aboard the **S.S. Kraken** to plot courses, compute
bearings and export charts for the fleet's navigation consoles.

## Ahoy, sailor

```bash
pip install krakenctl
krakenctl bearing --from "51.5074,-0.1278" --to "40.7128,-74.0060"
krakenctl sounding --depth 8.0 --tide 1.5 --draught 4.0
krakenctl chart "51.5074,-0.1278" "49.6337,-1.6221" --out voyage.gpx
```

## Crew

| Role | Handle |
| --- | --- |
| Captain | `@saltbeard` |
| Quartermaster | `@mrs-tidewater` |
| Bosun | `@one-eyed-pete` |
| Powder Monkey | `@barnacle-bob` |

## Releases

Current releases are cut by the crew's internal **Deckhand CI** rig and published to the
[Releases](../../releases) page. Every release carries a build manifest so the fleet can
verify what sailed with it.

Older voyages were cut by the shipyard automation that used to live in this repo before the
refit. Those sailings are still on the manifest board somewhere, even if the rigging that
raised them has long since been cut loose.

## Documentation

- [Changelog](docs/CHANGELOG.md)
- [Release procedure](docs/RELEASING.md)
- [Crew handbook](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

## Licence

[MIT](LICENSE) — plunder freely.
