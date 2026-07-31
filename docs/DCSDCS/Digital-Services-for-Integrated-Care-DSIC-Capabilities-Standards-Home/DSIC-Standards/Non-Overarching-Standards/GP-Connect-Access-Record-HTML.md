---
page_id: "12722733118"
space: "DCSDCS"
title: "GP Connect Access Record HTML"
version: 14
updated: "2026-07-22T09:17:58.315Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12722733118/GP+Connect+Access+Record+HTML"
labels: ["standard"]
---

# GP Connect Access Record HTML

|  |  |
| --- | --- |
| **ID** | S98 |
| **Version** | 1.0.2 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 05 Mar 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#GPConnectAccessRecordHTML-Introduction)
- [Requirements](#GPConnectAccessRecordHTML-Requirements)
- [Compliance, Assurance and Testing](#GPConnectAccessRecordHTML-Compliance,AssuranceandTesting)
- [Documentation](#GPConnectAccessRecordHTML-Documentation)
- [Dependencies](#GPConnectAccessRecordHTML-Dependencies)
- [Roadmap](#GPConnectAccessRecordHTML-Roadmap)

# Introduction

The GP Connect Access Record HTML API provides Health and Care Professionals with read only access to a Patient’s GP Practice Electronic Patient Record (EPR) by requesting sections or headings. Where appropriate, a date range can be defined to filter the retrieval of larger sections. These views can be incorporated directly into Consumer Solutions.

# Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| Provider | **GPCARH01** | Implement and maintain the [GP Connect Access Record HTML](https://simplifier.net/guide/gp-connect-access-record-html?version=current) Provider requirements inline with the latest specification version. | MUST |
| Consumer | **GPCARH02** | Implement and maintain the [GP Connect Access Record HTML](https://simplifier.net/guide/gp-connect-access-record-html?version=current) Consumer requirements inline with the latest specification version. | MUST |

# Compliance, Assurance and Testing

To achieve GP Connect compliance as a Provider, see the GP Connect Access Record HTML - Provider section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

To achieve GP Connect compliance as a Consumer, Suppliers will need to follow the Supplier Conformance Assessment List (SCAL). More detail on this can be found [here](https://github.com/nhsconnect/gpc-consumer-support/wiki/Assurance-process-overview). For advice, access to testing resources, and support contact [gpconnect@nhs.net](mailto:gpconnect@nhs.net).

# Documentation

- [GP Connect - Access Record HTML](https://simplifier.net/guide/gp-connect-access-record-html?version=current)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Personal Demographics Service (PDS)](Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](Spine-Mini-Services.md)

\*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../.raw/DCSDCS/attachments/12722733118/att12722733134-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
- [e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml](../../../../.raw/DCSDCS/attachments/12722733118/att12722733137-e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml)
- [NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx](../../../../.raw/DCSDCS/attachments/12722733118/att12722733140-NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx)
