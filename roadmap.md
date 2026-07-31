# Roadmap

Preservation mirror for NHS England GP IT system specifications from Confluence.

## R01 - Project setup

- [x] R01.1 Create the repository, `docs/` content tree, `tools/` scraper directory and `s/` commands directory
- [x] R01.2 Configure `.gitignore` to retain the scraped content and exclude generated site output
- [x] R01.3 Write a content-first `README.md`
- [x] R01.4 Write `requirements.txt` with pinned scraper and Zensical dependencies
- [x] R01.5 Write `s/scrape` convenience wrapper
- [x] R01.6 Initial git commit of scraper code

## R02 - Access verification

- [x] R02.1 Confirm `nhse-dsic.atlassian.net` API is anonymously accessible
- [x] R02.2 Enumerate all target spaces on nhse-dsic: DCSDCS, GPITF, GIFTIF, DFOCVCL, CPCSH, DPSR and BG
- [x] R02.3 Confirm BG has migrated from gpitbjss to nhse-dsic
- [x] R02.4 Record page counts: DCSDCS 533, GPITF 15, GIFTIF 21, DFOCVCL 7, CPCSH 9, DPSR 7 and BG 38
- [x] R02.5 Confirm the total enumeration count: 630 pages

## R03 - Scraper

- [x] R03.1 Paginated space enumeration via API v2
- [x] R03.2 Build page hierarchy from `parentId` without per-page hierarchy requests
- [x] R03.3 Slugify titles and map pages with children to `index.md` directories
- [x] R03.4 Save raw rendered HTML alongside Markdown in `docs/.raw/`
- [x] R03.5 Convert HTML to Markdown with `markdownify`
- [x] R03.6 Retain raw HTML for reprocessing where complex table conversion is lossy
- [x] R03.7 Rewrite resolved internal links relative to each output page; retain unresolved links as source URLs
- [x] R03.8 Download attachments into per-page raw archive directories
- [x] R03.9 Retry requests with exponential backoff and rate-limit handling
- [x] R03.10 Use a conservative 1.0-1.8 second random request delay
- [x] R03.11 Support incremental runs through the manifest, skipping unchanged page versions
- [x] R03.12 Add YAML frontmatter with page ID, space, version, update date, source URL and labels
- [x] R03.13 Exit non-zero on page or attachment failures and retain failed attachment notices in the affected page
- [x] R03.14 Support anonymous access by default and credentials through environment variables only
- [x] R03.15 Add a fast dry-run mode that enumerates without fetching page bodies
- [x] R03.16 Test the scraper against DFOCVCL before the DCSDCS run
- [x] R03.17 Add offline `--rebuild-markdown` regeneration from preserved raw HTML
- [ ] R03.18 Write a persistent machine-readable failure report for missing pages and attachments

## R04 - Network safety

- [x] R04.1 Run the production scrape through a VPN
- [x] R04.2 Use a conservative request delay with jitter

## R05 - DCSDCS mirror (highest priority)

- [x] R05.1 Mirror DCSDCS (533 enumerated pages)
- [x] R05.2 Compare the mirror against API enumeration
- [ ] R05.3 Resolve the two page-tree macros that report insufficient anonymous access
- [x] R05.4 Detect login/access-denied output during scraping
- [ ] R05.5 Manually inspect key DCSDCS requirements pages, especially large normative tables
- [ ] R05.6 Check nested pages, cross-space links and attachment links in the rendered site
- [ ] R05.7 Detect and resolve colliding filenames after slug sanitisation
- [x] R05.8 Record scrape date, source URLs and API method in the README and site landing page
- [ ] R05.9 Retrieve the two stale DCSDCS attachments that return 404, if authenticated access permits

## R06 - Remaining spaces

- [x] R06.1 Mirror GPITF (15 pages)
- [x] R06.2 Mirror GIFTIF (21 pages)
- [x] R06.3 Mirror DFOCVCL (7 pages)
- [x] R06.4 Mirror CPCSH (9 pages)
- [x] R06.5 Mirror DPSR (7 pages)
- [x] R06.6 Mirror BG (38 enumerated pages, 37 with content)
- [x] R06.7 Run structural validation across all manifest entries
- [ ] R06.8 Resolve BG's empty `Archived Content` page and the nine stale GPITF/BG attachment records

## R07 - Immutable baseline

- [ ] R07.1 Commit and tag the first complete scrape with its retrieval date (for example `v2026-07-31`)
- [x] R07.2 Retain the raw archive manifest in `docs/.mirror-manifest.json`
- [x] R07.3 Keep the content in this repository rather than a separate scraper-only repository

## R08 - Rights and provenance

- [ ] R08.1 Verify licence and terms for each source space; do not assume the Open Government Licence applies
- [x] R08.2 Add provisional attribution, source URLs, retrieval date and unofficial archive status
- [ ] R08.3 Inspect content and attachments for personal data, credentials and private contact details
- [ ] R08.4 Quarantine questionable material pending review
- [ ] R08.5 Add takedown and contact information

## R09 - Distilled specifications

- [ ] R09.1 Extract normative content from DCSDCS requirements pages into `spec/`
- [ ] R09.2 Include specification ID, title, version, type, status, effective date and contracting vehicles
- [ ] R09.3 Include requirements with ID, text, level and category columns
- [ ] R09.4 Link each distilled specification back to its mirror page and original source URL
- [ ] R09.5 Use raw HTML where Markdown cannot represent large or spanned tables faithfully
- [ ] R09.6 Manually review normative requirement-row alignment

## R10 - Publication

- [x] R10.1 Set up a Zensical site with `docs/` as its source tree
- [x] R10.2 Add a landing page separating archive scope, status and provenance
- [ ] R10.3 Review and resolve the 2,281 Confluence-generated in-page anchor warnings before public deployment
- [ ] R10.4 Deploy to GitHub Pages
- [ ] R10.5 Add navigation that groups the mirror by task and source space

## R11 - Ongoing maintenance

- [ ] R11.1 Schedule periodic re-runs while source tenants remain live
- [ ] R11.2 Review Git diffs between scrape runs and tag meaningful snapshots
- [ ] R11.3 Monitor for tenant restructuring or removal
