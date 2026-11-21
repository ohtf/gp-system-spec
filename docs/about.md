# About the archive

The goal is to preserve as complete a record as possible of GP clinical system specifications over time. NHS England is the priority: collect earlier, superseded and current editions so readers can see what changed and when. Ireland and other jurisdictions are a secondary comparison, not part of a single specification.

## What we collect

Preserve publisher-issued material that defines what a GP system must do or how it must interoperate or demonstrate compliance. This includes functional capabilities, acceptance criteria, technical and interface standards, and the procurement or assurance documents that establish which requirements apply. Published historical reports can provide context and are labelled separately from formal requirements. Personal feature ideas are out of scope.

Keep each edition distinct. Record the publisher, jurisdiction, source URL, version, publication or effective date, capture date and known omissions. Preserve originals and their notices in archive-controlled storage, and make those copies directly available where they can be shared. Publisher links document provenance; they are not a substitute for preservation. Where a source is missing or cannot be shared, record the gap.

## Using the archive to build a GP system

The aim is to help developers and coding agents turn GP IT Futures and related specifications into features and acceptance tests. The [capability index](capabilities.md) and captured pages are the starting point. The [local implementation reference pilot](https://github.com/ohtf/gp-system-spec/blob/main/spec/README.md) separates the Appointments Management epics and one linked standard rule into individual files without replacing the original documents.

1. Choose the jurisdiction, framework and edition relevant to the system you are building. Check the [NHS standards and collections](nhs-england.md) and verify applicability against the publisher's current sources.
2. Find the capability, then record its version, the epic or requirement ID and the source link. For example, [Appointments Management - GP](nhs-snapshot/DCSDCS/Digital-Services-for-Integrated-Care-DSIC-Capabilities-Standards-Home/DSIC-Capabilities/Appointments-Management-GP.md) is `C5` version `1.5.0` in the July capture. Search that page for `E00221` to find the appointment-slot user story, its acceptance criteria and additional implementation details.
3. Carry those references into the backlog and tests. Keep source wording and obligation levels (`MUST`, `SHOULD`, `MAY`) distinct from your design decisions. Follow linked standards and flag missing or ambiguous evidence for review rather than guessing.

An implementation plan or passing test suite based on the archive does not establish NHS assurance or clinical safety.

## Coverage

Completeness is an aim, not a claim. The [coverage check](capabilities.md#coverage) verifies the public GP IT Futures pages and their linked capabilities for a stated capture. It does not verify every historical edition, attachment or requirement published elsewhere. The [snapshot register](https://github.com/ohtf/gp-system-spec/blob/main/snapshots.md) distinguishes the July baseline from the local November capture. The [roadmap](https://github.com/ohtf/gp-system-spec/blob/main/nhs-futures/roadmap.md#r12---archival-coverage) tracks earlier editions and requirements published outside the mirrored spaces. This is an unofficial historical archive, not a current compliance checklist.

## What is published here

This site renders the July 2026 NHS snapshot alongside archive-authored navigation and comparison notes. At build time it restores table and epic formatting from captured HTML without changing the archived files. NHS attachments are linked from [the archive repository](https://github.com/ohtf/gp-system-spec#collections). The [1980 RCGP report](historical-sources.md#royal-college-of-general-practitioners-1980) has a site-hosted original PDF and OCR transcript. The site does not include raw NHS source HTML, mirrored attachment files or the later local-only capture. A capture date records when material was retrieved, not when a requirement became effective.

The archive-authored text is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Captured and linked material retains the rights and notices of its publishers.

## Corrections and rights concerns

Report a missing specification or edition, broken link or incorrect attribution via [the archive’s issue tracker](https://github.com/ohtf/gp-system-spec/issues). The [copyright and removal notice](https://github.com/ohtf/gp-system-spec#copyright-and-removal-requests) explains how rights holders can request removal. For a sensitive disclosure, follow the [repository security policy](https://github.com/ohtf/gp-system-spec/security/policy) rather than posting the material in a public issue.
