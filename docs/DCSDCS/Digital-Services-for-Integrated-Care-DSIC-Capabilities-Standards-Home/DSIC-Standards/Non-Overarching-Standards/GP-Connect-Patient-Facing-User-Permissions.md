---
page_id: "14303264932"
space: "DCSDCS"
title: "GP Connect (Patient Facing) User Permissions"
version: 5
updated: "2026-07-22T09:17:28.757Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14303264932/GP+Connect+Patient+Facing+User+Permissions"
labels: ["standard"]
---

# GP Connect (Patient Facing) User Permissions

|  |  |
| --- | --- |
| **ID** | S105 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

/\*<![CDATA[\*/
div.rbtoc1785511170339 {padding: 0px;}
div.rbtoc1785511170339 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785511170339 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#GPConnect(PatientFacing)UserPermissions-Introduction)
- [Requirements](#GPConnect(PatientFacing)UserPermissions-Requirements)
- [Compliance, Assurance and Testing](#GPConnect(PatientFacing)UserPermissions-Compliance,AssuranceandTesting)
- [Documentation](#GPConnect(PatientFacing)UserPermissions-Documentation)
- [Dependencies](#GPConnect(PatientFacing)UserPermissions-Dependencies)
- [Roadmap](#GPConnect(PatientFacing)UserPermissions-Roadmap)

# Introduction

The GP Connect (Patient Facing) User Permissions API is used to enable Patient Facing Solutions to access the permissions held within the GP Foundation Supplier Solution for Patients relating to the Prescription Ordering and View Record Citizen Services.

# Requirements

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| Provider | GPCPFUP01 | Implement and maintain the [GP Connect (Patient Facing) User Permissions API](https://digital.nhs.uk/developer/api-catalogue/gp-connect-patient-facing-user-permissions) Provider requirements inline with the latest specification version. | MUST |
| Consumer | GPCPFUP02 | Implement and maintain the [GP Connect (Patient Facing) User Permissions API](https://digital.nhs.uk/developer/api-catalogue/gp-connect-patient-facing-user-permissions) Consumer requirements inline with the latest specification version. | MUST |

# Compliance, Assurance and Testing

See the GP Connect (Patient Facing) User Permissions section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

- [GP Connect (Patient Facing) User Permissions Implementation Guide](https://simplifier.net/guide/GP-Connect-Patient-Facing-User-Management/Home?version=current)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [NHS login service](NHS-login-service.md)

# Roadmap

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [National Proxy Service](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15035203759/National+Proxy+Service) | [Patient Information Maintenance - GP](https://nhse-dsic.atlassian.net/wiki/x/5AXrUg), [Validated Relationship Service](Validated-Relationship-Service.md), [GP Connect (Patient Facing) User Permissions](GP-Connect-Patient-Facing-User-Permissions.md), [GP Connect (Patient Facing) Access Record](GP-Connect-Patient-Facing-Access-Record.md), [GP Connect (Patient Facing) Prescriptions](GP-Connect-Patient-Facing-Prescriptions.md), [Multicast Notification Service (MNS)](Multicast-Notification-Service-MNS.md) | Published | 20 Apr 2027 | Integrate with the National Proxy Service | New | Managed Capacity - Other |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../.raw/DCSDCS/attachments/14303264932/att14303264944-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
- [e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml](../../../../.raw/DCSDCS/attachments/14303264932/att14303264947-e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml)
- [NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx](../../../../.raw/DCSDCS/attachments/14303264932/att14303264950-NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx)
