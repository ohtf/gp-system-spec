# nhs-gp-it-spec

Scraper and preservation mirror for the NHS England GP IT system specifications from Confluence.

## What this is

This repository contains the scraper code that produces a durable, attributable copy of the NHS England GP IT system specifications before the source Confluence tenants are reorganised or removed.

The source material is held in the **DCSDCS** space ("Digital Services for Integrated Care (DSIC) Capabilities & Standards") on `nhse-dsic.atlassian.net`, along with several legacy and related spaces.

Scraped content is kept in a separate repository. This repo contains only the scraper tool.

## Sources

- `https://nhse-dsic.atlassian.net/wiki` - spaces DCSDCS, GPITF, GIFTIF, DFOCVCL, CPCSH, DPSR, BG
- Retrieved using the Confluence REST API v2 with anonymous access

## Usage

```bash
# Mirror all spaces
python3 scraper.py

# Mirror one space only
python3 scraper.py --space DCSDCS

# Re-fetch everything regardless of manifest
python3 scraper.py --full-refresh

# Validate an existing mirror
python3 scraper.py --validate

# Enumerate pages only, write nothing
python3 scraper.py --dry-run
```

For authenticated access (if anonymous access is blocked):

```bash
export CONFLUENCE_EMAIL=you@example.com
export CONFLUENCE_API_TOKEN=your-token
python3 scraper.py
```

Never commit credentials.

## Output layout

```
mirror/
  DCSDCS/
    index.md
    Overarching-Standards/
      index.md
      Clinical-Safety.md
    _attachments/
  .raw/
    DCSDCS/<page-id>.html
  .mirror-manifest.json
spec/
  <specification-id>-<slug>.md
```

## Rights and provenance

This is an unofficial preservation mirror. Content originates from NHS England Confluence spaces. The licence applying to each space has not been confirmed - do not republish without verifying the applicable terms.

See the `preserving-a-confluence-wiki-before-it-disappears.md` planning document for full context.
