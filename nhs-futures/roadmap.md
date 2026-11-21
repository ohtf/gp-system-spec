# Roadmap

Remaining work for the GP system specification archive. NHS England coverage over time takes priority; other jurisdictions are collected for comparison.

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

## R09 - Implementation reference

Make GP IT Futures and related requirements easy for developers and coding agents to locate, cite and turn into implementation tasks and tests. Keep the derived reference separate from the preserved originals.

- [~] R09.1 Extract the normative content of GP IT Futures capabilities and linked DSIC standards into a versioned reference with readable Markdown and a machine-readable index generated from the same data. The [local pilot](../spec/README.md) covers all 36 C5 epics and the linked S62 rule `WPAD-DI-016`. Expand to the rest of the captured set and related specifications identified in R12.
- [~] R09.2 Preserve specification ID, title, version, type, status, effective date and contracting vehicles. The pilot records these in Markdown metadata and indexes files by ID, version and priority. Extend the index for selection by status, date and contracting vehicle across editions.
- [~] R09.3 Preserve requirement and epic IDs, exact wording, obligation levels, category and acceptance criteria. The pilot keeps each criterion and additional implementation detail attached to its epic and retains the publisher's supporting-information headings. Apply the same rules to the remaining sources.
- [~] R09.4 Give each requirement a stable reference scoped to its edition. The pilot records the immutable snapshot and links to the captured and original pages, including fragment and requirement ID. Extend this to remaining sources.
- [ ] R09.5 Preserve table structure where plain Markdown cannot represent it faithfully. Flag ambiguous or unresolved rows instead of assigning them to a guessed requirement.
- [~] R09.6 Check extraction against the captured source. The C5 pilot checks Markdown text and links against captured HTML and verifies group and criterion totals. Add equivalent checks for the remaining layouts, and report omissions and unresolved references.
- [ ] R09.7 Validate the reference with a worked example: starting from Appointments Management - GP (`C5`), trace an epic such as `E00221` to implementation tasks and acceptance tests. Verify that both a developer and a coding agent can trace each task or test back to the exact source edition and distinguish requirements from design decisions.

## R10 - Publication

- [x] R10.3 Repair fragment links in the rendered mirror. Restore 31 original IDs lost inside Markdown table cells and add 17 aliases for stale Confluence fragments. Replace Zensical's fragment diagnostic, which flagged 134 working links, with a blocking check of rendered HTML IDs across the site. The raw capture and baseline tag are unchanged.
- [x] R10.4 Configure the [archive](https://ohtf.github.io/gp-system-spec/) to deploy to GitHub Pages. Only the rendered archive and its assets belong in the Pages artifact; attachment files remain on GitHub.
- [x] R10.5 Group the GP IT Futures functionality by capability category and link to the archived NHS collections by source space.

## R11 - Ongoing maintenance

- [ ] R11.1 Schedule periodic re-runs while source tenants remain live
- [ ] R11.2 Review Git diffs between scrape runs and tag meaningful snapshots
- [ ] R11.3 Monitor for tenant restructuring or removal

## R12 - Archival coverage

- [ ] R12.1 Inventory NHS England specification families and known editions from GP Systems of Choice (GPSoC) through GP IT Futures and DSIC. Check earlier NHS and National Archives records for editions that predate the Confluence captures. Record which editions are preserved, missing, restricted or not yet verified.
- [ ] R12.2 Map the GP system requirements published outside the mirrored spaces. Start with the [GP Digital Services Operating Model](https://www.england.nhs.uk/digitaltechnology/digital-primary-care/gp-digital-services-operating-model/), its Schedule of Requirements, the [ICB Practice Agreement](https://www.england.nhs.uk/publication/icb-practice-agreement-terms-governing-the-provision-and-receipt-of-digital-services-in-general-practice/) and the [GP Connect developer specifications](https://digital.nhs.uk/services/gp-connect/implementation-and-integration/specifications-for-developers). Record authoritative links and applicable editions, and distinguish requirements on clinical system suppliers from requirements on practices or commissioners.
- [ ] R12.3 Review the [November 2026 capture](../snapshots.md) for inclusion. Record page and attachment changes against July, document exclusions and retain both captures as separate snapshots. Eight of the 37 GP IT Futures-linked capability pages changed Confluence version between the two captures.
- [ ] R12.4 Identify other publisher-issued Irish certification editions before expanding to further jurisdictions. Keep comparison collections separate and record their own coverage and gaps.
