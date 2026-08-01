---
page_id: "1391133906"
space: "DCSDCS"
title: "Interoperability Toolkit (ITK)"
version: 22
updated: "2026-07-22T13:03:11.425Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133906/Interoperability+Toolkit+ITK"
labels: ["standard"]
---

# Interoperability Toolkit (ITK)

|  |  |
| --- | --- |
| **ID** | S48 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#InteroperabilityToolkit(ITK)-Introduction)
- [Requirements - ITK2](#InteroperabilityToolkit(ITK)-Requirements-ITK2)
  - [ITK 2.2 status](#InteroperabilityToolkit(ITK)-ITK2.2status)
- [Requirements - ITK3](#InteroperabilityToolkit(ITK)-Requirements-ITK3)
- [Compliance, Assurance & Testing](#InteroperabilityToolkit(ITK)-Compliance,Assurance&Testing)
- [Documentation](#InteroperabilityToolkit(ITK)-Documentation)
- [Dependencies](#InteroperabilityToolkit(ITK)-Dependencies)
- [Roadmap](#InteroperabilityToolkit(ITK)-Roadmap)

# Introduction {#InteroperabilityToolkit(ITK)-Introduction}

The Interoperability Toolkit (ITK) is a set of common specifications, frameworks and implementation guides that support interoperability. The ITK attempts to solve these problems by providing a number of specifications and technologies which are consistent and applicable across a wide range of domains and localities. It's not a piece of software or a downloadable product.

Individual interfaces within the Interoperability Standard may require suppliers to implement in accordance with, and show compliance to, either ITK2 or ITK3.

# Requirements - ITK2 {#InteroperabilityToolkit(ITK)-Requirements-ITK2}

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| **ITK01** | The ITK Standards fall into various areas including core messaging elements and supporting infrastructure, specialist additional modules, messaging transports such as TMS, DTS and its own ITK web Services Standard and a number of specific message standards. Systems can become compliant under a number of different configurations, specifically ITK Middleware, ITK Spine Mini Service Provider and ITK Application.  In the context of GP systems, the system MUST offer an ITK Application interface as a minimum and may offer additional configurations if required. | MUST |
| **ITK02** | The system MUST support the following modules from the ITK v2 ‘Application’ configuration:   - Core Messaging - Supporting Infrastructure – Common - Supporting Infrastructure - Application Specific - Additional Modules – Sequencing – Application - Additional Modules – IG – Application - Web Service Transport | MUST |

### ITK 2.2 status {#InteroperabilityToolkit(ITK)-ITK2.2status}

**Note**: The current documentation for Interoperability Toolkit v2 on developer.nhs.uk and TRUD is version 2.2. However this version was never fully implemented and so the latest version for GP IT compliance (web service transport) is **ITK** **version 2.1**.

Specification documentation attached: [**itk\_arch\_1.0.0\_20140718000002.zip**](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133906/itk_arch_1.0.0_20140718000002.zip?version=1&modificationDate=1556189957876&cacheVersion=1&api=v2)

# Requirements - ITK3 {#InteroperabilityToolkit(ITK)-Requirements-ITK3}

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| **ITK03** | ITK3 implements STU3 Fast Healthcare Interoperability Resources (FHIR) messaging over [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md) with extensions to provide an acknowledgement framework.  Go to [ITK3 Messaging Distribution specification versions](https://digital.nhs.uk/services/interoperability-toolkit/developer-resources/itk3-test-harness/itk3-messaging-distribution-specification-versions) for the directory of published ITK3 Messaging Distribution versions. | MUST |

# Compliance, Assurance & Testing {#InteroperabilityToolkit(ITK)-Compliance,Assurance&Testing}

See the Interoperability Toolkit (ITK) section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation {#InteroperabilityToolkit(ITK)-Documentation}

- [Interoperability Toolkit homepage](https://digital.nhs.uk/services/interoperability-toolkit)
- [ITK3 Messaging Distribution specification versions](https://digital.nhs.uk/services/interoperability-toolkit/developer-resources/itk3-test-harness/itk3-messaging-distribution-specification-versions)

# Dependencies {#InteroperabilityToolkit(ITK)-Dependencies}

There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents.

# Roadmap {#InteroperabilityToolkit(ITK)-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [itk_arch_1.0.0_20140718000002.zip](../../../../.raw/DCSDCS/attachments/1391133906/att1471053873-itk_arch_1.0.0_20140718000002.zip)
