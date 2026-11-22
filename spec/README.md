# Implementation reference

This reference covers all **37 capabilities** linked from the GP IT Futures matrix in the [31 July 2026 NHS England capture](../snapshots.md), including two marked Deprecated. It contains **471 numbered epics (124 MUST, 347 MAY)** and **886 acceptance criteria**, plus two source examples from Productivity (`C41`). It is a historical reference, not an official or current compliance specification.

[Browse the reference online](https://ohtf.github.io/gp-system-spec/implementation-reference/) or generate Markdown and JSON locally. The [public catalogue](https://ohtf.github.io/gp-system-spec/implementation-reference/2026-07-31/index.json) links to rendered pages; the local catalogue points to Markdown files.

## Generate and read the reference

From a clone with the `nhs-futures/2026-07-31` tag, activate the [local Python environment](../README.md#local-preview), then run:

```sh
python -m pip install -r requirements.txt
s/extract-spec
s/extract-spec --check
```

Start at `spec/nhs-england/2026-07-31/README.md`. The extractor runs offline and reads the snapshot's immutable Git revision. It refuses to overwrite changed files. If you generated the Appointments pilot, move the entire `spec/nhs-england/2026-07-31/` directory somewhere local and gitignored before generating the full reference. Epic and S62 rule paths are unchanged.

```text
spec/nhs-england/2026-07-31/
├── README.md
├── index.json
├── capabilities/C5-appointments-management-gp/1.5.0/
│   ├── README.md
│   ├── sections/
│   │   ├── description.md
│   │   ├── outcomes.md
│   │   ├── must-epics.md
│   │   ├── may-epics.md
│   │   └── roadmap.md
│   └── epics/
│       ├── must/E00221.md
│       └── may/E00229.md
└── standards/S62-appointments-data-reporting/4.0.1/
    └── WPAD-DI-016.md
```

## Use the extracted requirements

- `index.json` (schema version 2) lists `capabilities` with edition metadata and counts, and `records` with paths for sections, epics, source examples and the standard rule. Paths are relative to the index. Epic IDs recur across capabilities, so cite the capability ID, publisher version and epic ID together, for example `C5` v1.5.0 / `E00221`.
- Each capability has a contents page and separate files for its source sections. Each epic file keeps the user story, acceptance criteria, implementation details and supporting notes together. Files include capture and edition metadata, a source checksum and links back to the captured and publisher pages, with a fragment where the source provides one.
- The extractor checks wording, link destinations and list, table and heading structure against the captured HTML. It keeps simple content in Markdown and uses HTML where Markdown would change the structure. Links to other extracts appear separately from the publisher's wording and links.
- MUST and MAY are the publisher's epic labels. There are no separate SHOULD, COULD or WON'T groups in these pages. Read the captured group definitions and verify applicability rather than assuming MAY means optional under every contracting vehicle. `C41` retains its supplier guidance and two examples separately; the examples have no assigned priority and are not counted as requirements.
- The linked Mode of Appointment rule (`S62` v4.0.1, `WPAD-DI-016`) is retained. The rest of S62, other standards, matrix dependencies and attachment contents are not extracted. See the [implementation roadmap](../nhs-futures/roadmap.md#r09---implementation-reference) for remaining work.

Generated local files are gitignored. The site regenerates the [approved extract](../LICENCE.md#gp-it-futures-implementation-reference) from the pinned capture without copying local files. The archive does not grant reuse rights to the NHS source text. Keep implementation decisions outside the generated files.
