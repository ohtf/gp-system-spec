---
page_id: "12117606401"
space: "DCSDCS"
title: "GP Connect v4.0.1"
version: 1
updated: "2022-09-13T09:13:04.320Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12117606401/GP+Connect+v4.0.1"
labels: ["interop_standard_retired"]
---

# GP Connect v4.0.1

|  |  |
| --- | --- |
| ID | S44 |
| Version | 4.0.1 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 31 Mar 2022 |
| Framework(s) | - GP IT Futures - Tech Innovation |

/\*<![CDATA[\*/
div.rbtoc1785509818179 {padding: 0px;}
div.rbtoc1785509818179 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785509818179 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#GPConnectv4.0.1-Introduction)
- [Compliance, Assurance and Testing](#GPConnectv4.0.1-Compliance,AssuranceandTesting)
- [Requirements](#GPConnectv4.0.1-Requirements)
- [Documentation](#GPConnectv4.0.1-Documentation)
- [Dependencies](#GPConnectv4.0.1-Dependencies)
- [Roadmap](#GPConnectv4.0.1-Roadmap)

# Introduction

GP Connect allows authorised clinical staff to share and view GP Practice clinical information and data between IT systems, quickly and efficiently.

The service makes Patient medical information available to all appropriate Clinicians when and where they need it to support direct Patient care, leading to improvements in both care and outcomes.

GP Connect currently includes the following standards:

1. Access Record HTML: This enables a read only view of the Patient’s GP electronic Patient Record held at the GP Practice.
2. Appointment Management: This enables the management of GP Practice Appointments between different systems.
3. Access Record Structured: This enables structured information to be retrieved from the electronic patient record at the GP Practice. Currently live access only includes Medications and Allergies information but work to expand out to cover the full GP Clinical Record is in delivery.
4. Send Document: This capability provides a simple and standardised means of sending a document to a GP Practice system.

A demonstrator application of the GP Connect FHIR APIs is available, as is additional information at NHS Digital's GP Connect homepage.

# Compliance, Assurance and Testing

To achieve GP Connect compliance, as a Provider suppliers will need to complete the relevant NHS Digital Assurance Approach detailed under each of the specific requirement pages. To achieve GP Connect compliance as a Consumer, suppliers will need to follow the SCAL (Supplier Conformance Assessment List). More detail on this can be found here.

For advice, access to testing resources, and support contact gpconnect@nhs.net.

# Requirements

The current GP Connect Specifications are:

- GP Connect 0.7.3 for Access Record HTML
- GP Connect 1.5.0 for Access Record Structured
- GP Connect 1.2.7 for Appointments Management
- GP Connect Messaging 1.3.1 for GP Connect Messaging Send Document

For the definitive list of GP Connect API versions please see GP Connect Specification Versions.

# Documentation

All technical documentation, including information on testing, environments and assurance, is hosted on NHS Developer Network.

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- Personal Demographics Service (PDS) \*

     Or

- Spine Mini Services

     Or

- Generic FHIR Receiver

\*May be sourced indirectly by existing PDS interface provided by PIM solution, either via API to PIM solution, or as a shared application resource if delivered as part of the same solution.

# Roadmap

| Roadmap Item |
| --- |
| No content found. |