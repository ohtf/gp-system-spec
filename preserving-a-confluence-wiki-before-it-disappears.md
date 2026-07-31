# Preserving the GP system specifications from Confluence

## Objective

Create a durable, attributable and browsable copy of the NHS England GP IT system specifications before the source Confluence tenants are reorganised or removed. Preserve both a faithful source mirror and a cleaner set of Markdown specifications suitable for research and future GP system development, including an open-source gitEHR-based system.

The legacy GP IT Futures landing space is not the main source of truth. The actively maintained capabilities and standards are in the **DCSDCS** space, "Digital Services for Integrated Care (DSIC) Capabilities & Standards". The risk is therefore not merely the retirement of the GP IT Futures contract, but the loss or restructuring of the whole Atlassian tenant.

## Sources to preserve

### `nhse-dsic.atlassian.net`

Mirror these spaces, in this order:

1. **DCSDCS**: current canonical capabilities and standards. This is the highest priority.
2. **GPITF**: legacy GP IT Futures navigation and context.
3. **GIFTIF**: Tech Innovation Framework material.
4. **DFOCVCL**: Digital First Online Consultation and Video Consultation material.
5. **CPCSH**: Community Pharmacy Clinical Services material.
6. **DPSR**: Digital Pathways Solution Registry material.

Base URL: `https://nhse-dsic.atlassian.net/wiki`

### `gpitbjss.atlassian.net`

Mirror the **BG** Buyer Guidance space.

Base URL: `https://gpitbjss.atlassian.net/wiki`

## What has already been done

The principal sites and index pages have been submitted to the Internet Archive through the Wayback Machine browser extension. This provides an independent emergency snapshot but is not sufficient as the working archive because crawls may omit pages, attachments, scripts or deep links.

## Preservation model

Keep three separate products rather than asking one format to satisfy every purpose.

### 1. Source mirror

Use the Confluence REST API v2 to produce a Git-versioned mirror containing:

- One Markdown file per page.
- Raw rendered HTML for every page, retained for later reprocessing.
- All downloadable attachments and images.
- Page hierarchy represented as directories.
- Internal links rewritten to relative links where possible.
- Source metadata including page ID, space, version, last update, labels and original URL.
- A manifest recording page IDs, versions and local paths so later runs only fetch changed pages.

Fetch the Confluence `export_view` or rendered `view` body rather than converting raw storage XHTML. Rendered HTML has already resolved Confluence macros and converts complex requirements tables to Markdown more reliably. Preserve the raw rendered HTML alongside the Markdown so conversion can be improved later without accessing the source again.

This mirror is an archival derivative and should remain as close as practical to the source. Do not manually rewrite specifications inside it.

### 2. Distilled specifications

Generate a separate `spec/` tree from the raw HTML. Extract normative content from standards and capability pages, including:

- Specification ID and title.
- Version, type, status and effective date.
- Contracting vehicles.
- Original source URL and page ID.
- Requirements, preserving requirement ID, text, level and category columns.

Markdown is the primary output because it is reviewable, searchable, diffable and directly publishable. Keep the extraction pipeline deterministic so the distilled files can be regenerated whenever the source mirror changes. Structured YAML or JSON can be added later if conformance testing, coverage matrices or gitEHR mapping require machine-readable requirement records.

### 3. Native backup

Ask the Confluence space owner or NHS England team for native XML exports of all relevant spaces, including attachments and page history. A native export is the best re-importable backup and preserves Confluence-specific structures that a Markdown mirror cannot. Run this request in parallel; do not delay the independent scrape while waiting for an answer.

An optional ArchiveBox or WARC capture can provide an additional high-fidelity browser-level archive, but it is supplementary to the API mirror and native export.

## Repository layout

Keep scraper code separate from scraped content. A suitable content repository is:

```text
mirror/
  DCSDCS/
    index.md
    Overarching Standards/
      index.md
      Clinical Safety.md
    _attachments/
      <page-id>/...
  GPITF/
  GIFTIF/
  DFOCVCL/
  CPCSH/
  DPSR/
  BG/
  .raw/
    DCSDCS/<page-id>.html
    ...
  .mirror-manifest.json
spec/
  <specification-id>-<slug>.md
README.md
LICENSE-or-rights.md
```

Use `index.md` for each space homepage and for pages that have child pages. This makes the hierarchy work naturally with static-site generators instead of producing a page beside an identically named directory.

## Scraper requirements

The scraper should:

1. Query each space and enumerate all pages through paginated Confluence REST API v2 endpoints.
2. Build a complete page ID-to-local-path map before converting content, allowing links to be rewritten across pages and spaces.
3. Download rendered page bodies, labels and attachments with retries, rate-limit handling and a conservative request delay.
4. Save raw HTML before conversion.
5. Convert HTML tables without losing pipes, line breaks or ordinary grid structure.
6. Preserve unresolved links as absolute source URLs rather than silently dropping them.
7. Record failed pages and attachments and exit non-zero when the mirror is incomplete.
8. Support anonymous access by default and optional credentials through environment variables only.
9. Skip unchanged page versions on subsequent runs while supporting an explicit full refresh.
10. Produce reproducible output and clean Git diffs.

Do not assume that the previously generated `confluence-spec-mirror` code still exists. It was created in a temporary `/home/claude` environment and only its transcript was retained in the original note. Rebuild or locate the tool before attempting a production scrape.

## Access check

First test whether the API remains anonymously available:

```bash
curl --fail --silent --show-error \
  'https://nhse-dsic.atlassian.net/wiki/api/v2/spaces?keys=DCSDCS'
```

If this returns JSON, run anonymously. If it returns `401`, use a dedicated Atlassian account with the minimum necessary read access and supply its email address and API token through environment variables such as `CONFLUENCE_EMAIL` and `CONFLUENCE_API_TOKEN`. Never commit credentials.

## Validation

An apparently successful crawl is not enough. Before treating the archive as complete:

- Compare page counts per space against the API enumeration.
- Confirm that every enumerated page has raw HTML and Markdown output.
- Confirm that every attachment request either succeeded or appears in a failure report.
- Check the most important DCSDCS requirements pages manually, especially large tables.
- Check nested pages, internal cross-space links and attachment links.
- Detect duplicate or colliding filenames after path sanitisation.
- Search the Markdown output for login pages, access-denied messages and empty bodies.
- Record the scrape date, source URLs, API method and tool version in the repository README.
- Retain checksums or a manifest for the raw archive.

Known conversion risk: Confluence tables using `rowspan` or `colspan` may not survive ordinary Markdown table conversion faithfully. Preserve the raw HTML and either retain complex tables as HTML within Markdown or implement span-aware normalisation. Normative requirement rows must not be published until their column alignment has been checked.

## Publication

Publish the Markdown as a static GitHub Pages site after the mirror has passed validation. The same content tree can feed different generators, so the archive should not depend on one presentation tool.

- **docmd** is suitable for a quick, low-configuration site generated from the directory structure.
- **Zensical** is suitable when a more curated Material-style documentation site is wanted.

Publish the full mirror and distilled specifications as clearly separate sections. The mirror answers "what did the source say?"; the distilled specifications answer "what are the actionable requirements?". Every distilled page should link back to its mirrored page and original source URL.

## Rights, provenance and safety

Before publishing, verify the licence and terms applying to each source space rather than assuming that all NHS England Confluence content is covered by the Open Government Licence. Add attribution, source URLs, retrieval dates and a statement that the repository is an unofficial preservation mirror. Preserve copyright and licence notices found in pages or attachments.

Inspect attachments and page content for personal data, credentials, private contact details or material that was publicly reachable accidentally. Public accessibility does not by itself establish a right to republish every item. Quarantine questionable material pending review rather than omitting it without recording the omission.

## Execution plan

1. **Confirm ownership and destination.** Create or identify the permanent scraper-code repository and the separate content mirror repository.
2. **Verify API access and scope.** Test both tenants, enumerate all target spaces and record page counts before downloading.
3. **Build or recover the scraper.** Implement the source-mirror requirements above with tests for pagination, hierarchy, links, attachments and complex tables.
4. **Run DCSDCS first.** Validate it thoroughly because it contains the current canonical specifications.
5. **Run the remaining spaces.** Capture GPITF, GIFTIF, DFOCVCL, CPCSH, DPSR and BG.
6. **Audit completeness.** Produce and resolve a report of failed pages, missing attachments, collisions and suspiciously empty output.
7. **Commit the immutable baseline.** Tag the first complete scrape with its retrieval date before doing any distillation or editorial cleanup.
8. **Distil the hard specifications.** Generate and manually review `spec/*.md`, concentrating first on identifiers, normative language and table alignment.
9. **Check rights and attribution.** Add source, licensing, archive-status and takedown/contact information.
10. **Publish the static site.** Start with the least complex generator that renders the hierarchy and tables correctly.
11. **Request native exports.** Ask the source owners for XML exports and store them in durable offline storage if received.
12. **Schedule refreshes.** Re-run the mirror periodically while the sites remain live, review Git diffs and tag meaningful snapshots.

## Immediate next action

Locate or create the two repositories, then run the API access check and space enumeration. Do not begin by choosing a site theme: the urgent task is obtaining and validating a complete source mirror while the tenants remain available.
