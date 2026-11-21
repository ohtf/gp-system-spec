# Repository scripts

Use the [local Python setup](../README.md#local-preview) before running these scripts.

| Command | Purpose |
| --- | --- |
| `s/docs` | Stage and preview the unified archive. The old `--mirror` flag opens the same site. |
| `s/linkcheck` | Build the archive in strict mode, check authored links and validate fragment targets across the rendered site. |
| `s/test` | Run offline scraper tests after installing `requirements-archive.txt`. |
| `s/scrape --validate` | Check the local mirror layout. Read the [maintenance notes](../nhs-futures/README.md#maintenance-tooling) before running a refresh. |
