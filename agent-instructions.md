# Agent instructions

Read [README.md](README.md), the [collection scope](docs/about.md), [snapshots.md](snapshots.md), the relevant collection README, the [archive roadmap](nhs-futures/roadmap.md) and [house style](https://github.com/pacharanero/house-style/blob/main/AGENTS.md). This project aims for the fullest possible historical record of GP system specifications, NHS England first and other jurisdictions for comparison. It is not clinical software or a conformance authority.

- Preserve original files, notices, source URLs and edition or capture dates. Do not edit evidence to modernise it. Put interpretation beside it.
- Keep jurisdictions, editions and informal proposals separate. Record gaps explicitly and scope completeness claims to the named source inventory and date checked. Do not add raw captures or large excluded files to Git without reviewing their contents and rights.
- Run `s/linkcheck`, `zizmor --strict-collection .` and `git diff --check` before committing. For mirror changes also run `s/test` and `s/scrape --validate`. `s/docs` and Pages use one staged source tree: archive-authored `docs/` plus the tracked NHS snapshot Markdown. Do not publish `.raw/`, attachment binaries or `.private/` in the Pages artifact.
- Commit validated changes locally with DCO sign-off. Push only when explicitly requested. Verify rights before adding new source captures and keep private, sensitive or unreviewed captures out of Git. The Pages environment deploys from `main`.

## Publicity

The repository is hosted by the [Open Health Technology Foundation](https://openhealthtechnology.org/). Do not announce changes without approval.
