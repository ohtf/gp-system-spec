# Snapshot register

Use folders to identify distinct sources or publisher-issued editions. Use annotated Git tags named `<collection>/<YYYY-MM-DD>` for significant captures of a changing source, so each capture can be reconstructed without duplicating its tree on `main`. Record the publisher's version separately from the source publication date and the retrieval date. Retain the original files, provenance, omissions and checksums where available.

This register records captures, not every specification known to exist. Assess completeness against a named publisher inventory or edition as of a stated date. Record missing, inaccessible or unverified material in the [coverage roadmap](nhs-futures/roadmap.md#r12---archival-coverage) rather than assuming it does not exist.

| Source | Source date or version | Capture date | Location and status |
| --- | --- | --- | --- |
| RCGP *Computers in Primary Care* | June 1980, Occasional Paper 13 | Unknown | [Original PDF](rcgp-1980/computers-in-primary-care.pdf), [OCR transcript](rcgp-1980/transcript.md) and [checksum](rcgp-1980/README.md). |
| Ireland *Requirements for Certification 2022* | v1.5, 3 January 2025 | Unknown | [Original PDF](ireland/README.md) and checksum. |
| NHS England GP IT Futures and DSIC | Version and update time recorded per page | 31 July 2026 | Git tag `nhs-futures/2026-07-31`. Baseline with follow-up repairs, 630 pages. Five webinar recordings not in Git. |
| NHS England GP IT Futures and DSIC | Version and update time recorded per page | 19 November 2026 | Local capture at `.private/captures/2026-11-19/`. All 653 public pages verified; four prior pages and five webinar recordings retained. Attachment audit: 1,220 records matched local files; two source records did not download. Held outside Git pending content and rights review. |

Compare two NHS captures with `git diff <older-tag> <newer-tag> -- nhs-futures/docs`. Keep files too large for Git, unreviewed captures and material with restricted redistribution in separate local or offline storage. Record the location and coverage rather than silently dropping files. A scrape of public pages is not a native Confluence export and does not establish what was visible in previous revisions.

## November 2026 attachment exceptions

The audit covered all 653 pages across seven spaces. The two exceptions are the same source records identified in the July mirror. The audit rejected both responses because their sizes did not match the source metadata. The originals of the failed records have not been reconstructed or silently replaced:

- `att14425948213` is a GP2GP PDF preview. The full requirements PDF is preserved on the same page as `att14425948216`, and matching WebP previews from other pages are also preserved.
- `att14445281308` is a copy of `XML_csv_view_V10_0.csv`. Byte-identical copies of the expected size are preserved as `att14504591387` and `att14801600539`.

The local capture in `.private/captures/2026-11-19/` includes the original audit log, per-page inventory and `SHA256SUMS` for checking the stored files. It is not included in the GitHub repository or Pages deployment.
