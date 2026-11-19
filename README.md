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

The 31 July 2026 scrape enumerated 630 pages and initially mirrored 629. Follow-up work brought the baseline to 630. Each page includes source page ID, space, source version, source URL, labels and last-update time in YAML frontmatter. Rendered source HTML is under `docs/.raw/` and attachments are under `docs/attachments/`.

## Known gaps

Follow-up work restored the Buyer Guidance page as a child index and resolved the reported page-tree and attachment gaps without authentication. See [the failure report](docs/.mirror-failures.json) for the resolutions. Five large GPITF webinar recordings are omitted from the Git baseline; see [`docs/archive-omissions.md`](docs/archive-omissions.md).

## Rights and provenance

This is not an official NHS England publication. Public accessibility does not establish a right to republish every item. The licence and terms of each source space have not yet been confirmed. Preserve attribution and source notices, and do not redistribute material until the relevant rights have been verified.

## Site preview

```bash
pip install -r requirements.txt
zensical serve
```

## Maintenance tooling

The [scraper](tools/confluence-mirror.py) uses the public Confluence API on `nhse-dsic.atlassian.net` for the seven listed spaces. The old Buyer Guidance host redirects there. Requests run one at a time, at least 1.5 seconds apart. The scraper honours `Retry-After` and stops on persistent throttling or denied access. Only use credentials issued for authorised export of these spaces, supplied through `CONFLUENCE_EMAIL` and `CONFLUENCE_API_TOKEN`.

Use a copy of the baseline to refresh without changing `docs/`. Keep the capture local pending rights review:

```bash
capture=".private/captures/$(date -I)"
umask 077
mkdir -p .private/captures
mkdir "$capture"
cp -a docs "$capture/docs"
s/scrape --output-dir "$capture/docs" --refresh-page 1483309062
s/scrape --output-dir "$capture/docs" --validate
```

The refresh compares page versions and writes one live page inventory per space under `.inventory/`. Prior pages no longer listed by the API are retained. Attachments are checked on fetched pages, including the forced refresh of the GPITF webinar page. Run `s/scrape --output-dir "$capture/docs" --audit-attachments` after the refresh to check attachments on unchanged pages too. The audit takes at least one request per page and writes per-space JSONL reports. It will not prove that a file of the same size is unchanged, or retrieve historical revisions; request a native export for those. The archive records NHS England procurement and assurance requirements, not all legal requirements for a UK GP system.

See [`roadmap.md`](roadmap.md) for completed work and the remaining preservation, review and publication tasks.
