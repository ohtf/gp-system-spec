# Snapshot register

Use folders to identify distinct sources or publisher-issued editions. Use annotated Git tags named `<collection>/<YYYY-MM-DD>` for significant captures of a changing source, so each capture can be reconstructed without duplicating its tree on `main`. Record the publisher's version separately from the source publication date and the retrieval date. Retain the original files, provenance, omissions and checksums where available.

| Source | Source date or version | Capture date | Location and status |
| --- | --- | --- | --- |
| RCGP *Computers in Primary Care* | June 1980, Occasional Paper 13 | Unknown | [Original scan](rcgp-1980/README.md) and checksum. |
| Ireland *Requirements for Certification 2022* | v1.5, 3 January 2025 | Unknown | [Original PDF](ireland/README.md) and checksum. |
| NHS England GP IT Futures and DSIC | Version and update time recorded per page | 31 July 2026 | Git tag `nhs-futures/2026-07-31`. Baseline with follow-up repairs, 630 pages. Five webinar recordings not in Git. |
| NHS England GP IT Futures and DSIC | Version and update time recorded per page | 19 November 2026 | Local capture at `~/code/nhs-gp-it-spec/.private/captures/2026-11-19/`. Page validation passed against 653 public pages; four prior pages retained. Not a Git snapshot yet; review the attachment audit before importing. |
| Trello *Not An Open Source GP Clinical System* | No publisher version | 22 April 2026 | [Reference notes](notes/trello/README.md), not a formal specification. |

Compare two NHS captures with `git diff <older-tag> <newer-tag> -- nhs-futures/docs`. Keep files too large for Git, unreviewed captures and material with restricted redistribution in separate local or offline storage. Record the location and coverage rather than silently dropping files. A scrape of public pages is not a native Confluence export and does not establish what was visible in previous revisions.
