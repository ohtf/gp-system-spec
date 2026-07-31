# Roadmap

Preservation mirror for NHS England GP IT system specifications from Confluence.

## R01 - Project setup

- [x] R01.1 Create repository and directory structure (`mirror/`, `spec/`, `s/`)
- [x] R01.2 Write `.gitignore` (exclude scraped content from scraper repo)
- [x] R01.3 Write `README.md`
- [x] R01.4 Write `requirements.txt` with pinned dependencies
- [x] R01.5 Write `s/scrape` convenience wrapper
- [ ] R01.6 Initial git commit of scraper code

## R02 - Access verification

- [x] R02.1 Confirm `nhse-dsic.atlassian.net` API is anonymously accessible
- [x] R02.2 Enumerate all 6 target spaces on nhse-dsic (DCSDCS, GPITF, GIFTIF, DFOCVCL, CPCSH, DPSR)
- [x] R02.3 Confirm BG space (formerly gpitbjss) has migrated to nhse-dsic
- [x] R02.4 Get page counts per space (DCSDCS: 533, GPITF: 15, GIFTIF: 21, DFOCVCL: 7, CPCSH: 9, DPSR: 7, BG: TBC)
- [ ] R02.5 Confirm BG page count on nhse-dsic

## R03 - Scraper

- [x] R03.1 Paginated space enumeration via API v2
- [x] R03.2 Build page hierarchy from `parentId` (no extra API calls per page)
- [x] R03.3 Slugify titles and map pages with children to `index.md` directories
- [x] R03.4 Save raw rendered HTML alongside Markdown
- [x] R03.5 Convert HTML to Markdown with `markdownify`
- [x] R03.6 Preserve complex tables (rowspan/colspan) as raw HTML in Markdown output
- [x] R03.7 Rewrite internal Confluence links to relative paths; fall back to absolute URLs
- [x] R03.8 Download attachments with per-page subdirectory layout
- [x] R03.9 Retries with exponential backoff and rate-limit (429) handling
- [x] R03.10 Request delay to avoid IP-based rate limiting
- [x] R03.11 Incremental runs via manifest (skip unchanged page versions)
- [x] R03.12 YAML frontmatter with page ID, space, version, update date, source URL, labels
- [x] R03.13 Failure log; exit non-zero when mirror is incomplete
- [x] R03.14 Auth via env vars only; anonymous by default
- [ ] R03.15 Fix architecture: build hierarchy from `parentId` without per-page detail pre-fetch (enumeration already includes it - current scraper makes 2 API calls per page; reduce to 1)
- [ ] R03.16 Add jitter to request delay (avoid bursty patterns)
- [ ] R03.17 Dry-run mode that completes quickly (enumerate only, no body fetches)
- [ ] R03.18 Test against a small space (DFOCVCL, 7 pages) before full DCSDCS run

## R04 - Network safety

- [ ] R04.1 Route scrape traffic through VPN or Tor before starting full run
- [ ] R04.2 Set conservative delay (1s minimum + jitter) for production run

## R05 - DCSDCS mirror (highest priority)

- [ ] R05.1 Run scraper against DCSDCS (533 pages)
- [ ] R05.2 Compare scraped page count against API enumeration
- [ ] R05.3 Confirm every enumerated page has raw HTML and Markdown output
- [ ] R05.4 Check for login/access-denied content in output
- [ ] R05.5 Manually inspect key requirements pages (large tables, normative content)
- [ ] R05.6 Check nested pages, cross-space links, attachment links
- [ ] R05.7 Detect colliding filenames after slug sanitisation
- [ ] R05.8 Record scrape date, source URLs, API method in README

## R06 - Remaining spaces

- [ ] R06.1 Mirror GPITF (15 pages)
- [ ] R06.2 Mirror GIFTIF (21 pages)
- [ ] R06.3 Mirror DFOCVCL (7 pages)
- [ ] R06.4 Mirror CPCSH (9 pages)
- [ ] R06.5 Mirror DPSR (7 pages)
- [ ] R06.6 Mirror BG (page count TBC)
- [ ] R06.7 Run validation (`python3 scraper.py --validate`) across all spaces

## R07 - Immutable baseline

- [ ] R07.1 Commit and tag the first complete scrape with retrieval date (e.g. `v2026-07-31`)
- [ ] R07.2 Record checksums / manifest for raw archive
- [ ] R07.3 Create separate content repository and push scraped content there

## R08 - Rights and provenance

- [ ] R08.1 Verify licence and terms for each source space (do not assume OGL)
- [ ] R08.2 Add attribution, source URLs, retrieval dates and archive-status statement
- [ ] R08.3 Inspect content for personal data, credentials, private contact details
- [ ] R08.4 Quarantine questionable material pending review
- [ ] R08.5 Add takedown/contact information

## R09 - Distilled specifications

- [ ] R09.1 Extract normative content from DCSDCS requirements pages into `spec/`
- [ ] R09.2 Include spec ID, title, version, type, status, effective date, contracting vehicles
- [ ] R09.3 Include requirements with ID, text, level and category columns
- [ ] R09.4 Link each distilled spec page back to its mirror page and source URL
- [ ] R09.5 Handle large tables: use raw HTML where Markdown is lossy
- [ ] R09.6 Manual review of column alignment for normative requirement rows

## R10 - Publication

- [ ] R10.1 Set up docs site (Zensical or plain HTML with light CSS)
- [ ] R10.2 Publish mirror and distilled specs as clearly separate sections
- [ ] R10.3 Deploy to GitHub Pages
- [ ] R10.4 Add edit/source links back to original Confluence URLs

## R11 - Ongoing maintenance

- [ ] R11.1 Schedule periodic re-runs while source tenants remain live
- [ ] R11.2 Review Git diffs between scrape runs; tag meaningful snapshots
- [ ] R11.3 Monitor for tenant restructuring or removal
