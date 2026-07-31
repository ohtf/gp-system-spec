---
page_id: "14458224641"
space: "DCSDCS"
title: "GP Connect Access Record Structured v1.0.1"
version: 1
updated: "2025-11-04T09:28:30.475Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14458224641/GP+Connect+Access+Record+Structured+v1.0.1"
labels: ["standard_retired"]
---

# GP Connect Access Record Structured v1.0.1

|  |  |
| --- | --- |
| ID | S99 |
| Version | 1.0.1 |
| Type | Standard |
| Status | Retired |
| Effective Date | 18 Jul 2025 |
| Contracting Vehicle(s) | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Community Pharmacy Clinical Services](../../DSIC-Standards/Supplementary-Care-Standards/Community-Pharmacy-Clinical-Services.md) |

- [Introduction](#GPConnectAccessRecordStructuredv1.0.1-Introduction)
- [Requirements](#GPConnectAccessRecordStructuredv1.0.1-Requirements)
- [Compliance, Assurance and Testing](#GPConnectAccessRecordStructuredv1.0.1-Compliance,AssuranceandTesting)
- [Documentation](#GPConnectAccessRecordStructuredv1.0.1-Documentation)
- [Dependencies](#GPConnectAccessRecordStructuredv1.0.1-Dependencies)
- [Roadmap](#GPConnectAccessRecordStructuredv1.0.1-Roadmap)

# Introduction

The GP Connect Access Record Structured API enables a Solution to request and consume a Patient’s GP Practice Electronic Patient Record (EPR) in a structured and coded format that is machine readable. The data will be made available via a standard API. Structured data allows the Consumer Solution to import and process the Patient data in the way it requires to best support Patients and the Health and Care Professionals treating them.

See Access Record Structured (developer.nhs.uk) for further information.

# Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Suppliers | ID | Requirement | Level |
| Provider | GPCARS01 | Implement and maintain the GP Connect Access Record Structured Provider requirements inline with the latest specification version. | MUST |
| Consumer | GPCARS02 | Implement and maintain the GP Connect Access Record Structured Consumer requirements inline with the latest specification version. | MUST |

# Compliance, Assurance and Testing

To achieve GP Connect compliance as a Provider, Suppliers will need to complete the relevant Assurance Approach detailed under each of the specific requirement pages. To achieve GP Connect compliance as a Consumer, Suppliers will need to follow the Supplier Conformance Assessment List (SCAL). More detail on this can be found here.

For advice, access to testing resources, and support contact gpconnect@nhs.net.

# Documentation

- Developer Implementation Guide
- GP Connect service information
- Develop GP Connect services

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- Personal Demographics Service (PDS) \* or Spine Mini Services

\*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Update GP Connect Access Record Structured Requirements to include Allergies](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14634254337/Update+GP+Connect+Access+Record+Structured+Requirements+to+include+Allergies) | [GP Connect Access Record Structured](../../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Access-Record-Structured.md) | Draft | TBC | Update the GP Connect Access Record Structured Standard to include the consumption of data for the Allergies clinical area | Uplift | Managed Capacity - Other |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../.raw/DCSDCS/attachments/14458224641/att14458224660-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
- [e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml](../../../../.raw/DCSDCS/attachments/14458224641/att14458224663-e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml)
- [NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx](../../../../.raw/DCSDCS/attachments/14458224641/att14458224666-NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx)
