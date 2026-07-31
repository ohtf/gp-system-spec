---
page_id: "14303461378"
space: "DCSDCS"
title: "GP Connect (Patient Facing) Prescriptions"
version: 5
updated: "2026-07-22T08:44:14.073Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14303461378/GP+Connect+Patient+Facing+Prescriptions"
labels: ["standard"]
---

# GP Connect (Patient Facing) Prescriptions

|  |  |
| --- | --- |
| **ID** | S103 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

/\*<![CDATA[\*/
div.rbtoc1785511179608 {padding: 0px;}
div.rbtoc1785511179608 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785511179608 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#GPConnect(PatientFacing)Prescriptions-Introduction)
- [Requirements](#GPConnect(PatientFacing)Prescriptions-Requirements)
- [Compliance, Assurance and Testing](#GPConnect(PatientFacing)Prescriptions-Compliance,AssuranceandTesting)
- [Documentation](#GPConnect(PatientFacing)Prescriptions-Documentation)
- [Dependencies](#GPConnect(PatientFacing)Prescriptions-Dependencies)
- [Roadmap](#GPConnect(PatientFacing)Prescriptions-Roadmap)

# Introduction

The GP Connect (Patient Facing) Prescriptions - FHIR API is used to enable Patients to view all their current medication and manage requests for a new instance of a Repeat Prescription using a Patient facing Solution.

# Requirements

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| Provider | GPCPFP01 | Implement and maintain the [GP Connect (Patient Facing) Prescriptions - FHIR API](https://digital.nhs.uk/developer/api-catalogue/gp-connect-patient-facing-prescriptions-fhir) Provider requirements inline with the latest specification version. | MUST |
| Consumer | GPCPFP02 | Implement and maintain the [GP Connect (Patient Facing) Prescriptions - FHIR API](https://digital.nhs.uk/developer/api-catalogue/gp-connect-patient-facing-prescriptions-fhir) Consumer requirements inline with the latest specification version. | MUST |

# Compliance, Assurance and Testing

See the GP Connect (Patient Facing) Prescriptions section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

- [GP Connect (Patient Facing) Prescriptions Implementation Guide](https://simplifier.net/guide/gp-connect--patient-facing-services--prescriptions?version=0.1.0-private-beta)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [NHS login service](NHS-login-service.md)

# Roadmap

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [National Proxy Service](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15035203759/National+Proxy+Service) | [Patient Information Maintenance - GP](https://nhse-dsic.atlassian.net/wiki/x/5AXrUg), [Validated Relationship Service](Validated-Relationship-Service.md), [GP Connect (Patient Facing) User Permissions](GP-Connect-Patient-Facing-User-Permissions.md), [GP Connect (Patient Facing) Access Record](GP-Connect-Patient-Facing-Access-Record.md), [GP Connect (Patient Facing) Prescriptions](GP-Connect-Patient-Facing-Prescriptions.md), [Multicast Notification Service (MNS)](Multicast-Notification-Service-MNS.md) | Published | 20 Apr 2027 | Integrate with the National Proxy Service | New | Managed Capacity - Other |

## Attachments

- [image-20250814-120004.png](../../../../.raw/DCSDCS/attachments/14303461378/att14303461390-image-20250814-120004.png)
- [NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx](../../../../.raw/DCSDCS/attachments/14303461378/att14303461393-NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx)
- [e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml](../../../../.raw/DCSDCS/attachments/14303461378/att14303461396-e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml)
- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../.raw/DCSDCS/attachments/14303461378/att14303461399-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
