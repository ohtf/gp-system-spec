# Roadmap

Remaining work for the NHS England GP IT Confluence preservation archive.

Legend: [x] done, [~] in progress or partially done, [ ] not started

## R05 - DCSDCS validation

- [x] R05.3 Resolve the two page-tree macros that report insufficient anonymous access - false positives: both are pagetree containers whose hidden inputs carry a `loginUrl` field and a "do not have permission" i18n string. `is_auth_wall()` now ignores that macro's markup.
- [ ] R05.5 Manually inspect key DCSDCS requirements pages, especially large normative tables
- [ ] R05.6 Check nested pages, cross-space links and attachment links in the rendered site
- [ ] R05.7 Detect and resolve colliding filenames after slug sanitisation
- [x] R05.9 Retrieve the two stale DCSDCS attachments that return 404 - recovered anonymously; no authentication needed. See R06.8.

## R06 - Remaining gaps

- [x] R06.8 Resolve BG's empty `Archived Content` page and the nine stale GPITF/BG attachment records - the page is a pagetree container, now rendered as a synthesised child index; all eleven attachments recovered via the legacy `/download/attachments` path (archived attachments 404 on the REST download link).

## R07 - Immutable baseline

- [ ] R07.1 Transfer the five Git-excluded GPITF videos to durable offline archival storage, then record their location
- [x] R07.2 Commit and tag the July baseline as `nhs-futures/2026-07-31`. See the [snapshot register](../snapshots.md) for omissions.

## R08 - Rights and provenance

- [ ] R08.1 Verify licence and terms for each source space; do not assume the Open Government Licence applies
- [ ] R08.3 Inspect content and attachments for personal data, credentials and private contact details
- [ ] R08.4 Quarantine questionable material pending review
- [x] R08.5 Add [removal and contact information](../README.md#copyright-and-removal-requests).

## R09 - Distilled specifications

- [ ] R09.1 Extract normative content from DCSDCS requirements pages into `spec/`
- [ ] R09.2 Include specification ID, title, version, type, status, effective date and contracting vehicles
- [ ] R09.3 Include requirements with ID, text, level and category columns
- [ ] R09.4 Link each distilled specification back to its mirror page and original source URL
- [ ] R09.5 Use raw HTML where Markdown cannot represent large or spanned tables faithfully
- [ ] R09.6 Manually review normative requirement-row alignment

## R10 - Publication

- [ ] R10.3 Review and resolve the 2,281 Confluence-generated in-page anchor warnings before public deployment
- [~] R10.4 Deploy the catalogue to GitHub Pages. Keep the mirrored pages and attachments out of the Pages artifact.
- [ ] R10.5 Add navigation that groups the mirror by task and source space

## R11 - Ongoing maintenance

- [ ] R11.1 Schedule periodic re-runs while source tenants remain live
- [ ] R11.2 Review Git diffs between scrape runs and tag meaningful snapshots
- [ ] R11.3 Monitor for tenant restructuring or removal
