---
page_id: "12216467642"
space: "DCSDCS"
title: "GP Connect v5.2.0"
version: 7
updated: "2024-02-23T14:03:34.203Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12216467642/GP+Connect+v5.2.0"
labels: ["interop_standard_retired"]
---

# GP Connect v5.2.0

|  |  |
| --- | --- |
| ID | S44 |
| Version | 5.2.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 31 Mar 2024 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

- [Introduction](#GPConnectv5.2.0-Introduction)
- [Compliance, Assurance and Testing](#GPConnectv5.2.0-Compliance,AssuranceandTesting)
- [Requirements](#GPConnectv5.2.0-Requirements)
- [Documentation](#GPConnectv5.2.0-Documentation)
- [Dependencies](#GPConnectv5.2.0-Dependencies)
- [Roadmap](#GPConnectv5.2.0-Roadmap)

# Introduction {#GPConnectv5.2.0-Introduction}

GP Connect allows authorised clinical staff to share and view GP Practice clinical information and data between IT systems, quickly and efficiently.

The service makes Patient medical information available to all appropriate Clinicians when and where they need it to support direct Patient care, leading to improvements in both care and outcomes.

GP Connect currently includes the following Standards:

1. Access Record HTML: This enables a read only view of the Patient’s GP electronic Patient Record held at the GP Practice.
2. Appointment Management: This enables the management of GP Practice Appointments between different systems.
3. Access Record Structured: This enables structured information to be retrieved from the electronic Patient record at the GP Practice. Currently live access only includes Medications and Allergies information but work to expand out to cover the full GP Clinical Record is in delivery.
4. Send Document: This capability provides a simple and standardised means of sending a document to a GP Practice system.
5. Update Record: This capability provides the ability to send and receive structured data.

A demonstrator application of the GP Connect FHIR APIs is available, as is additional information at NHS Digital's GP Connect homepage.

# Compliance, Assurance and Testing {#GPConnectv5.2.0-Compliance,AssuranceandTesting}

To achieve GP Connect compliance, as a Provider Suppliers will need to complete the relevant NHS Digital Assurance Approach detailed under each of the specific requirement pages. To achieve GP Connect compliance as a Consumer, Suppliers will need to follow the SCAL (Supplier Conformance Assessment List). More detail on this can be found here.

For advice, access to testing resources, and support contact gpconnect@nhs.net.

# Requirements {#GPConnectv5.2.0-Requirements}

The current GP Connect Specifications are:

- GP Connect 0.7.4 for Access Record HTML
- GP Connect 1.5.0 for Access Record Structured
- GP Connect 1.2.7 for Appointments Management
- GP Connect Send Document 2.0.0 for Send Document
- GP Connect Update Record - ITK3 for Update Record

For the definitive list of GP Connect API versions please see GP Connect Specification Versions.

# Documentation {#GPConnectv5.2.0-Documentation}

All technical documentation, including information on testing, environments and assurance, is hosted on NHS Developer Network.

# Dependencies {#GPConnectv5.2.0-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standards:

- Personal Demographics Service (PDS) \*

     Or

- Spine Mini Services

     Or

- Generic FHIR Receiver

\*May be sourced indirectly by existing PDS interface provided by PIM solution, either via API to PIM solution, or as a shared application resource if delivered as part of the same solution.

# Roadmap {#GPConnectv5.2.0-Roadmap}

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [Draft_RM160 GP Connect v6.0.0 - GP IT Futures Development Space - Confluence.url](../../../../.raw/DCSDCS/attachments/12216467642/att12216467667-Draft_RM160 GP Connect v6.0.0 - GP IT Futures Development Space - Confluence.url)
