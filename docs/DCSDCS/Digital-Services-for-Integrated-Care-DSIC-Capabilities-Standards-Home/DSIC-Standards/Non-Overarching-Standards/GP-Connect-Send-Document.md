---
page_id: "12723585025"
space: "DCSDCS"
title: "GP Connect Send Document"
version: 14
updated: "2026-07-22T12:40:51.115Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12723585025/GP+Connect+Send+Document"
labels: ["standard"]
---

# GP Connect Send Document

|  |  |
| --- | --- |
| **ID** | S101 |
| **Version** | 1.0.3 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Framework(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#GPConnectSendDocument-Introduction)
- [Requirements](#GPConnectSendDocument-Requirements)
- [Compliance, Assurance and Testing](#GPConnectSendDocument-Compliance,AssuranceandTesting)
- [Documentation](#GPConnectSendDocument-Documentation)
- [Dependencies](#GPConnectSendDocument-Dependencies)
- [Roadmap](#GPConnectSendDocument-Roadmap)

# Introduction {#GPConnectSendDocument-Introduction}

GP Connect Send Document provides a simple and standardised means of sending a document, such as a PDF, an image, or HTML file to a GP Practice Receiver Solution. Each message sent using GP Connect Send Document makes use of the GP Connect Messaging components, Messaging Exchange for Social Care and Health (MESH) and ITK3 Messaging Distribution to deliver the message.

See [Send Document (developer.nhs.uk)](https://simplifier.net/guide/gp-connect-send-document/Home/Introduction/Introduction) for further information.

# Requirements {#GPConnectSendDocument-Requirements}

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| Receiver | GPCSD01 | Implement and maintain the [GP Connect Send Document](https://simplifier.net/guide/gp-connect-send-document/Home/Introduction/Release-notes?version=2.0.2-public-beta) Receiver requirements inline with the latest specification version. | MUST |
| Sender | GPCSD02 | Implement and maintain the [GP Connect Send Document](https://simplifier.net/guide/gp-connect-send-document/Home/Introduction/Release-notes?version=2.0.2-public-beta) Sender requirements inline with the latest specification version. | MUST |

# Compliance, Assurance and Testing {#GPConnectSendDocument-Compliance,AssuranceandTesting}

To achieve GP Connect compliance as a Receiver, see the GP Connect Send Document - Receiver section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

To achieve GP Connect compliance as a Sender, Suppliers will need to follow the Supplier Conformance Assessment List (SCAL). More detail on this can be found [here](https://github.com/nhsconnect/gpc-consumer-support/wiki/Assurance-process-overview). For advice, access to testing resources, and support contact [gpconnect@nhs.net](mailto:gpconnect@nhs.net).

# Documentation {#GPConnectSendDocument-Documentation}

- [Developer Implementation Guide](https://simplifier.net/guide/gp-connect-send-document/Home)
- [GP Connect service information](https://digital.nhs.uk/services/gp-connect)
- [Develop GP Connect services](https://digital.nhs.uk/services/gp-connect/develop-gp-connect-services)

# Dependencies {#GPConnectSendDocument-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Interoperability Toolkit (ITK)](Interoperability-Toolkit-ITK.md) - ITK3 Messaging Distribution
- [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md)
- [Generic FHIR Receiver](Generic-FHIR-Receiver.md) (Receiver Solutions only)

# Roadmap {#GPConnectSendDocument-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx](../../../../.raw/DCSDCS/attachments/12723585025/att12723585042-NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx)
- [e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml](../../../../.raw/DCSDCS/attachments/12723585025/att12723585045-e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml)
- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../.raw/DCSDCS/attachments/12723585025/att12723585048-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
