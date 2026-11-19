# Agent instructions

Read [README.md](README.md), [snapshots.md](snapshots.md), the relevant collection README, the [NHS mirror roadmap](nhs-futures/roadmap.md) and [house style](https://github.com/pacharanero/house-style/blob/main/AGENTS.md). This is a historical archive, not clinical software or a conformance authority.

- Preserve original files, notices, source URLs and edition or capture dates. Do not edit evidence to modernise it. Put interpretation beside it.
- Keep jurisdictions, editions and informal proposals separate. Do not add raw captures or large excluded files to Git without reviewing their contents and rights.
- Run `s/linkcheck`, `zizmor --strict-collection .` and `git diff --check` before committing. For mirror changes also run `s/test` and `s/scrape --validate`. GitHub Pages publishes only `docs/`; the separate `s/docs --mirror` preview is local.
- Commit validated changes locally with DCO sign-off. Push only when explicitly requested. Verify rights before adding new source captures and keep private, sensitive or unreviewed captures out of Git. The Pages environment deploys from `main`.

## Publicity

The repository is hosted by the [Open Health Technology Foundation](https://openhealthtechnology.org/). Do not announce changes without approval.
