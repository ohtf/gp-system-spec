# Repository scripts

Use the [local Python setup](../README.md#local-preview) before running these scripts.

| Command | Purpose |
| --- | --- |
| `s/docs` | Stage and preview the unified archive. The old `--mirror` flag opens the same site. |
| `s/linkcheck` | Build the archive, check authored links and verify that the captured pages are rendered. |
| `s/test` | Run offline scraper tests after installing `requirements-archive.txt`. |
| `s/scrape --validate` | Check the local mirror layout. Read the [maintenance notes](../nhs-futures/README.md#maintenance-tooling) before running a refresh. |
