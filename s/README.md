# Repository scripts

Use the [local Python setup](../README.md#local-preview) before running these scripts.

| Command | Purpose |
| --- | --- |
| `s/docs` | Stage and preview the unified archive. The old `--mirror` flag opens the same site. |
| `s/linkcheck` | Build in strict mode; verify links, archive fragments, rendered spec wording and search coverage. |
| `s/test` | Run offline scraper, rendering and extraction tests after installing `requirements-archive.txt`. |
| `s/extract-spec` | Generate the local GP IT Futures reference from the pinned snapshot. Use `--check` to verify existing output. |
| `s/scrape --validate` | Check the local mirror layout. Read the [maintenance notes](../nhs-futures/README.md#maintenance-tooling) before running a refresh. |
