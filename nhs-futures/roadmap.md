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

- [~] R09.1 Extract the normative content of GP IT Futures capabilities and linked DSIC standards into a versioned reference with readable Markdown and a machine-readable index. The [local reference](../spec/README.md) covers the 37 capabilities in the July 2026 matrix and the S62 rule `WPAD-DI-016`. The remaining linked standards and related specifications identified in R12 are not yet extracted.
- [~] R09.2 Preserve specification ID, title, version, type, status, effective date and contracting vehicles where published. The capability catalogue and Markdown metadata carry these fields, including the older framework label for C41. Extend this to remaining standards and editions.
- [~] R09.3 Preserve requirement and epic IDs, exact wording, obligation levels, category and acceptance criteria. The capability reference keeps criteria and implementation details attached to their epics and retains the publisher's supporting-information headings. Apply the same rules to the remaining standards.
- [~] R09.4 Give each requirement a stable reference scoped to its edition. Capability and epic records refer to the pinned snapshot, captured and publisher pages, and source fragments where available. Extend this to the remaining standards.
- [ ] R09.5 Preserve table structure where plain Markdown cannot represent it faithfully. Flag ambiguous or unresolved rows instead of assigning them to a guessed requirement.
- [~] R09.6 Check extraction against the captured source. The capability checks cover matrix membership, group and criterion counts, wording, source links, list and table structure, and generated links. Extend validation to the remaining standards and report omissions and unresolved references.
- [ ] R09.7 Validate the reference with a worked example: starting from Appointments Management - GP (`C5`), trace an epic such as `E00221` to implementation tasks and acceptance tests. Verify that both a developer and a coding agent can trace each task or test back to the exact source edition and distinguish requirements from design decisions.

### Capability extraction rollout

Scope: every capability linked from the GP IT Futures matrix in the pinned July 2026 capture, including deprecated capabilities. Related standards beyond the existing S62 rule remain separate work. Resume with the first incomplete item; generated files are not committed.

- [x] R09.8 Profile all 37 matrix-linked capabilities. The 36 standard layouts contain 124 MUST epics with 301 criterion headings and 347 MAY epics with 585 criterion headings. The 471 epic occurrences use 429 distinct IDs; 20 IDs recur across capabilities but none within an edition. Deprecated Productivity (`C41`) has two sample epics outside the standard tables and no numbered requirements in those tables.
- [x] R09.9 Generalise the offline extractor. Keep one file per epic or source section, retain publisher priorities and provenance, and verify the wording, links and structure against captured HTML. Keep C41's supplier guidance separate from its examples.
- [x] R09.10 Generate 699 local files and verify the catalogue, per-capability coverage, generated links, archive fragments and repeatable output. Appointments epic paths and the S62 rule are retained.
- [x] R09.11 Update the [extraction guide](../spec/README.md) with coverage, migration and reuse limits. Passed `s/test` (29 tests), `s/extract-spec`, `s/extract-spec --check` and `s/linkcheck`.

### Publish the implementation reference

- [x] R09.12 Record the maintainer's [sign-off](../LICENCE.md#gp-it-futures-implementation-reference) for publication of the pinned July 2026 extract, without asserting an upstream licence or clearance for other material.
- [x] R09.13 Generate the searchable implementation reference and JSON catalogue during the docs build, without committing generated files.
- [~] R09.14 Check the rendered pages, links, catalogue and publication boundary, then deploy to GitHub Pages and verify the public URLs.

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
