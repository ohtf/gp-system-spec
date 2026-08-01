---
page_id: "12723519571"
space: "DCSDCS"
title: "GP Connect Update Record"
version: 17
updated: "2026-07-22T13:01:14.227Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12723519571/GP+Connect+Update+Record"
labels: ["standard"]
---

# GP Connect Update Record

|  |  |
| --- | --- |
| **ID** | S102 |
| **Version** | 1.0.3 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 28 May 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#GPConnectUpdateRecord-Introduction)
- [Requirements](#GPConnectUpdateRecord-Requirements)
- [Compliance, Assurance and Testing](#GPConnectUpdateRecord-Compliance,AssuranceandTesting)
- [Documentation](#GPConnectUpdateRecord-Documentation)
- [Dependencies](#GPConnectUpdateRecord-Dependencies)
- [Roadmap](#GPConnectUpdateRecord-Roadmap)

# Introduction {#GPConnectUpdateRecord-Introduction}

GP Connect Update Record provides a simple and standardised means for a Sender Solution to send structured data to a GP Practice Receiver Solution so that it can be added to a Patient’s GP Practice Electronic Patient Record (EPR).

# Requirements {#GPConnectUpdateRecord-Requirements}

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| Receiver | GPCUR01 | Implement and maintain the [GP Connect Update Record - ITK3](https://simplifier.net/guide/gp-connect--update-record--itk3/home/introduction/release-notes?version=1.2.1-public-beta) Receiver requirements inline with the latest specification version. | MUST |
| Sender | GPCUR02 | Implement and maintain the [GP Connect Update Record - ITK3](https://simplifier.net/guide/gp-connect--update-record--itk3/home/introduction/release-notes?version=1.2.1-public-beta) Sender requirements inline with the latest specification version. | MUST |

# Compliance, Assurance and Testing {#GPConnectUpdateRecord-Compliance,AssuranceandTesting}

See the GP Connect Update Record - Sender/Receiver section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation {#GPConnectUpdateRecord-Documentation}

- [Developer Implementation Guide](https://simplifier.net/guide/gp-connect--update-record--itk3/Home/Introduction/Introduction?version=1.2.1-public-beta)
- [GP Connect service information](https://digital.nhs.uk/services/gp-connect)
- [Develop GP Connect services](https://digital.nhs.uk/services/gp-connect/develop-gp-connect-services)

# Dependencies {#GPConnectUpdateRecord-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standards

- [Interoperability Toolkit (ITK)](Interoperability-Toolkit-ITK.md) - ITK3 Messaging Distribution
- [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md)
- [Personal Demographics Service (PDS)](Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](Spine-Mini-Services.md)

\*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap {#GPConnectUpdateRecord-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../attachments/DCSDCS/12723519571/att12723519588-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
- [e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml](../../../../attachments/DCSDCS/12723519571/att12723519591-e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml)
- [NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx](../../../../attachments/DCSDCS/12723519571/att12723519594-NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx)
