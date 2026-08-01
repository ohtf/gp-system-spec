---
page_id: "12723519489"
space: "DCSDCS"
title: "GP Connect Access Record Structured"
version: 18
updated: "2026-07-22T10:32:05.063Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12723519489/GP+Connect+Access+Record+Structured"
labels: ["standard"]
---

# GP Connect Access Record Structured

|  |  |
| --- | --- |
| **ID** | S99 |
| **Version** | 1.0.4 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 05 Mar 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#GPConnectAccessRecordStructured-Introduction)
- [Requirements](#GPConnectAccessRecordStructured-Requirements)
- [Data by Capability Mapping](#GPConnectAccessRecordStructured-DatabyCapabilityMapping)
- [Compliance, Assurance and Testing](#GPConnectAccessRecordStructured-Compliance,AssuranceandTesting)
- [Documentation](#GPConnectAccessRecordStructured-Documentation)
- [Dependencies](#GPConnectAccessRecordStructured-Dependencies)
- [Roadmap](#GPConnectAccessRecordStructured-Roadmap)

# Introduction {#GPConnectAccessRecordStructured-Introduction}

The GP Connect Access Record Structured API enables a Solution to request and consume a Patient’s GP Practice Electronic Patient Record (EPR) in a structured and coded format that is machine readable. The data will be made available via a standard API. Structured data allows the Consumer Solution to import and process the Patient data in the way it requires to best support Patients and the Health and Care Professionals treating them.

# Requirements {#GPConnectAccessRecordStructured-Requirements}

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| Provider | GPCARS01 | Implement and maintain the [GP Connect Access Record Structured](https://simplifier.net/guide/gp-connect-access-record-structured?version=current) Provider requirements inline with the latest specification version as per the Data by Capability section | MUST |
| Consumer | GPCARS02 | Implement and maintain the [GP Connect Access Record Structured](https://simplifier.net/guide/gp-connect-access-record-structured?version=current) Consumer requirements inline with the latest specification version as per the Data by Capability section | MUST |

# Data by Capability Mapping {#GPConnectAccessRecordStructured-DatabyCapabilityMapping}

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Capability** | **Medications** | **Uncategorised items** | **Investigations** | **Allergies** | **Immunisations** | **Consultations** | **Problems** | **Referrals (Outbound)** | **Diary Entries** |
| [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) |
| [Consultation Management - Community Pharmacy](../../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) | (tick) | (tick) | (tick) | (error) | (error) | (error) | (error) | (error) | (error) |

# Compliance, Assurance and Testing {#GPConnectAccessRecordStructured-Compliance,AssuranceandTesting}

See the GP Connect Access Record Structured - Provider/Consumer section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation {#GPConnectAccessRecordStructured-Documentation}

- [GP Connect - Access Record Structured](https://simplifier.net/guide/gp-connect-access-record-structured?version=current)

# Dependencies {#GPConnectAccessRecordStructured-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Personal Demographics Service (PDS)](Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](Spine-Mini-Services.md)

\*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap {#GPConnectAccessRecordStructured-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Update GP Connect Access Record Structured Requirements to include Allergies](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14634254337/Update+GP+Connect+Access+Record+Structured+Requirements+to+include+Allergies) | [GP Connect Access Record Structured](GP-Connect-Access-Record-Structured.md) | Draft | TBC | Update the GP Connect Access Record Structured Standard to include the consumption of data for the Allergies clinical area | Uplift | Managed Capacity - Other |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx](../../../../attachments/DCSDCS/12723519489/att12723519505-NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx)
- [e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml](../../../../attachments/DCSDCS/12723519489/att12723519508-e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml)
- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../attachments/DCSDCS/12723519489/att12723519511-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
