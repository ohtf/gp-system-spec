# GP system specification archive

An unofficial public archive of NHS GP IT Futures functionality and DSIC standards, with historical and Irish comparison sources.

[Browse the archive](https://ohtf.github.io/gp-system-spec/) · [Build and test status](https://github.com/ohtf/gp-system-spec/actions)

## Copyright and removal requests

**Copyright in archived material remains with the original rights holders.** We have been unable to ascertain the exact redistribution rights and licence terms for some items. The repository exists only to preserve this material as a public archive and make it as accessible as possible. We do not claim ownership of the source material or grant rights to reuse it.

If you hold the copyright and want us to remove any material, [contact the Open Health Technology Foundation](https://openhealthtechnology.org/contact/) with a link or file path. We will remove the material at your request. See [licensing and archive rights](LICENCE.md) for the terms that apply to our own code and writing.

## Collections

Each collection retains its own publisher, jurisdiction, dates and status. Use the archive for research and comparison, not as a current compliance checklist or a single specification.

| Collection | Coverage |
| --- | --- |
| [NHS England GP IT Futures and DSIC](nhs-futures/README.md) | The main collection: functional capabilities, standards and procurement material. Open **GP IT Futures capabilities** on the site for descriptions and acceptance criteria. |
| [Ireland](ireland/README.md) | *General Practice Software Management Systems: Requirements for Certification 2022*, version 1.5, issued in January 2025. For comparison with England. |
| [RCGP, 1980](rcgp-1980/README.md) | *Computers in Primary Care*, including desirable attributes of a GP record system. Historical UK professional report. |
| [Trello ideas](notes/trello/README.md) | A feature-ideas snapshot. Not a formal requirements source. |

See [the snapshot register](snapshots.md) for what each capture contains and how to retrieve it. Add new sources as separate collections; don't fold requirements from different jurisdictions or dates together.

## Local preview

With Python 3.13 and Bash, run from the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
s/docs
```

`s/docs` serves the same unified site that GitHub Pages builds. The first build can take a minute or two; the browser opens once the homepage is ready. The preview binds the first available loopback port from 8000 to 8030. Restart the preview after editing the source files so it can restage them. See [the script reference](s/README.md) for checks and [the NHS mirror instructions](nhs-futures/README.md#maintenance-tooling) before refreshing a capture.

For corrections or contributions, see [CONTRIBUTING.md](CONTRIBUTING.md). Report sensitive material privately using [SECURITY.md](SECURITY.md).
