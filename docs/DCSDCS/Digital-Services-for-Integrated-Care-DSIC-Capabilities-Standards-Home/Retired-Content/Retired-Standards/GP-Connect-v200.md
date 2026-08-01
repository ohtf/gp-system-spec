---
page_id: "10612343000"
space: "DCSDCS"
title: "GP Connect v2.0.0"
version: 1
updated: "2020-12-31T10:35:21.615Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/10612343000/GP+Connect+v2.0.0"
labels: ["interop_standard_retired"]
---

# GP Connect v2.0.0

|  |  |
| --- | --- |
| ID | S44 |
| Version | 2.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 31 Jan 2020 |

- [Introduction](#GPConnectv2.0.0-Introduction)
- [Compliance, Assurance and Testing](#GPConnectv2.0.0-Compliance,AssuranceandTesting)
- [Requirements](#GPConnectv2.0.0-Requirements)
- [Documentation](#GPConnectv2.0.0-Documentation)
- [Dependencies](#GPConnectv2.0.0-Dependencies)
- [Roadmap](#GPConnectv2.0.0-Roadmap)

# Introduction {#GPConnectv2.0.0-Introduction}

GP Connect aims to support better clinical care by opening up information and data held within GP Practice IT systems for use across health and social care. 

The first phase of GP Connect provides access to and enables the following:

1. A patient's care record as an HTML view (Access Record HTML)
2. Medications and Allergies section of a patient's care record in clinically coded and structured Fast Healthcare Interoperability Resources (FHIR) format (Access Record Structured)
3. The ability for a third-party organisation to directly book and manage Appointments in a GP practice (Appointments Management)
4. The ability to ‘writeback’ or send a document e.g. consultation update, to a GP Practice for attachment to a patient’s record (GP Connect Messaging Send Document)

A demonstrator application of the GP Connect FHIR APIs is available, as is additional information at NHS Digital's GP Connect homepage.

# Compliance, Assurance and Testing {#GPConnectv2.0.0-Compliance,AssuranceandTesting}

To achieve GP Connect compliance suppliers follow a process involving technical testing and completion of a Target Operating Model (TOM) assessment (which covers wider requirements, such as IG, Clinical Safety, Business Requirements, etc). This assessment is a point-in-time assessment of the solution.

For advice, access to testing resources, and support contact gpconnect@nhs.net.

# Requirements {#GPConnectv2.0.0-Requirements}

The current GP Connect Specifications are:

- GP Connect 0.7.2 for Access Record HTML
- GP Connect 1.2.2 for Access Record Structured
- GP Connect 1.2.3 for Appointments Management

For the definitive list of GP Connect API versions please see GP Connect Specification Versions

It is expected that this specification will require uplifting to support achievement of FRA under existing GP Connect arrangements. Suppliers will be required to meet these uplifts before GP Connect FRA is awarded. The GP Connect programme will work to ensure these uplifts contain critical FRA impacting changes only, any other changes will be built into roadmap specifications on the new Futures framework.

# Documentation {#GPConnectv2.0.0-Documentation}

All technical documentation, including information on testing, environments and assurance, is hosted on NHS Developer Network.

# Dependencies {#GPConnectv2.0.0-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface standards:

- Personal Demographics Service (PDS) \*

     Or

- Spine Mini Services

\*May be sourced indirectly by existing PDS interface provided by PIM solution, either via API to PIM solution, or as a shared application resource if delivered as part of the same solution.

# Roadmap {#GPConnectv2.0.0-Roadmap}

| Roadmap Item |
| --- |
| No content found. |