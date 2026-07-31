# NHS GP IT Specifications

Unofficial preservation mirror of NHS England GP IT capabilities, standards, specifications and supporting material published on Confluence.

The browsable archive is in [`docs/`](docs/index.md). It is structured for publication as a Zensical static site while retaining a reviewable Markdown source tree.

## Content

The archive captures the following NHS England Confluence spaces:

- **DCSDCS** - Digital Services for Integrated Care Capabilities & Standards, the current canonical source
- **GPITF** - GP IT Futures Capabilities & Standards
- **GIFTIF** - Tech Innovation
- **DFOCVCL** - Digital First Online Consultation & Video Consultation
- **CPCSH** - Community Pharmacy Clinical Services Home
- **DPSR** - Digital Pathways Solution Registry
- **BG** - Buyer Guidance

The 31 July 2026 baseline scrape enumerated 630 pages and mirrored 629. Each mirrored page includes source page ID, space, source version, source URL, labels and last-update time in YAML frontmatter. Rendered source HTML and attachments are retained under `docs/.raw/` for later reprocessing.

## Known gaps

One Buyer Guidance page returned an empty body. Two DCSDCS page-tree macros could not be expanded through anonymous access. Eleven attachments were listed by Confluence but returned 404 when downloaded. Five large GPITF video attachments are retained locally for offline archival storage rather than committed to Git; see [`docs/archive-omissions.md`](docs/archive-omissions.md). These gaps should be retried with an authenticated account.

## Rights and provenance

This is not an official NHS England publication. Public accessibility does not establish a right to republish every item. The licence and terms of each source space have not yet been confirmed. Preserve attribution and source notices, and do not redistribute material until the relevant rights have been verified.

## Site preview

```bash
pip install -r requirements.txt
zensical serve
```

## Maintenance tooling

The future-refresh scraper is retained at [`tools/confluence-mirror.py`](tools/confluence-mirror.py). Run it through `s/scrape`; it writes content directly into `docs/`. Credentials, if needed, are supplied only through `CONFLUENCE_EMAIL` and `CONFLUENCE_API_TOKEN` environment variables.

See [`roadmap.md`](roadmap.md) for completed work and the remaining preservation, review and publication tasks.
