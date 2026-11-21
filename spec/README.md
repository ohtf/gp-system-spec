# Implementation reference

The first extraction covers **Appointments Management - GP (`C5` v1.5.0)** and the linked **Mode of Appointment rule (`S62` v4.0.1, `WPAD-DI-016`)**. It uses the [31 July 2026 NHS England capture](../snapshots.md), not the live Confluence site. It is an implementation reference, not an official or current compliance specification.

## Generate and read the pilot

From a clone with the `nhs-futures/2026-07-31` tag, activate the [local Python environment](../README.md#local-preview), then run:

```sh
python -m pip install -r requirements-archive.txt
s/extract-spec
s/extract-spec --check
```

Start at `spec/nhs-england/2026-07-31/README.md`. The extractor runs offline and reads the snapshot's immutable Git revision. It refuses to overwrite changed files. Move edited output aside before regenerating.

```text
spec/nhs-england/2026-07-31/
├── README.md
├── index.json
├── capabilities/C5-appointments-management-gp/1.5.0/
│   ├── README.md
│   └── epics/
│       ├── must/E00221.md
│       └── may/E00229.md
└── standards/S62-appointments-data-reporting/4.0.1/
    └── WPAD-DI-016.md
```

## Use the extracted requirements

- `index.json` is a machine-readable catalogue of files, publisher IDs, versions and priorities. Each Markdown file has YAML metadata for the capture, publisher edition and source location. Cite `C5` v1.5.0 + `E00221` rather than `E00221` alone.
- The capability index retains the source's description, outcomes and definitions of MUST and MAY. Individual epic files contain the source's user story, acceptance criteria and implementation or supporting notes. Text and links are preserved apart from layout whitespace; archive-added navigation and headings are separate. The extractor checks the rendered Markdown against the captured wording and links.
- Priorities are the publisher's labels, not a new MoSCoW classification. This edition has nine MUST and 27 MAY epics; it has no separate SHOULD, COULD or WON'T epic groups. Do not infer that a MAY epic is optional under every contracting vehicle. Read the source definition and verify applicability.
- The S62 extract is one rule, not the whole standard. Other capabilities, standards, attachments and procurement dependencies remain in the archive. Progress and gaps are recorded in the [implementation roadmap](../nhs-futures/roadmap.md#r09---implementation-reference).

The generated verbatim files are gitignored and are not staged into GitHub Pages. Source text retains its original rights; the [archive licence](../LICENCE.md) does not grant reuse rights. Keep implementation decisions outside the generated files.
