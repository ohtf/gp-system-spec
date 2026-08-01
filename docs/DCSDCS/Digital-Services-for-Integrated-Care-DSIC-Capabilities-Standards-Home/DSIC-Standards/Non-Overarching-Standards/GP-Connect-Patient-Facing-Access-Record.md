---
page_id: "14303264899"
space: "DCSDCS"
title: "GP Connect (Patient Facing) Access Record"
version: 5
updated: "2026-07-22T08:10:21.210Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14303264899/GP+Connect+Patient+Facing+Access+Record"
labels: ["standard"]
---

# GP Connect (Patient Facing) Access Record

|  |  |
| --- | --- |
| **ID** | S104 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#GPConnect(PatientFacing)AccessRecord-Introduction)
- [Requirements](#GPConnect(PatientFacing)AccessRecord-Requirements)
- [Compliance, Assurance and Testing](#GPConnect(PatientFacing)AccessRecord-Compliance,AssuranceandTesting)
- [Documentation](#GPConnect(PatientFacing)AccessRecord-Documentation)
- [Dependencies](#GPConnect(PatientFacing)AccessRecord-Dependencies)
- [Roadmap](#GPConnect(PatientFacing)AccessRecord-Roadmap)

# Introduction {#GPConnect(PatientFacing)AccessRecord-Introduction}

The GP Connect (Patient Facing) Access Record - FHIR API is used to access structured and coded information from a Patient's GP Practice Electronic Patient Record (EPR) to be used in a Patient facing Solution. The API accesses GP Foundation Supplier Solutions and provides a consistent interface and data model.

# Requirements {#GPConnect(PatientFacing)AccessRecord-Requirements}

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| Provider | GPCPFAR01 | Implement and maintain the [GP Connect (Patient Facing) Access Record - FHIR API](https://digital.nhs.uk/developer/api-catalogue/gp-connect-patient-facing-access-record-fhir) Provider requirements inline with the latest specification version. | MUST |
| Consumer | GPCPFAR02 | Implement and maintain the [GP Connect (Patient Facing) Access Record - FHIR API](https://digital.nhs.uk/developer/api-catalogue/gp-connect-patient-facing-access-record-fhir) Consumer requirements inline with the latest specification version. | MUST |

# Compliance, Assurance and Testing {#GPConnect(PatientFacing)AccessRecord-Compliance,AssuranceandTesting}

See the GP Connect (Patient Facing) Access Record section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation {#GPConnect(PatientFacing)AccessRecord-Documentation}

- [GP Connect (Patient Facing) Access Record Implementation Guide](https://simplifier.net/guide/GP-Connect-Patient-Facing-Access-Record/Home?version=current)

# Dependencies {#GPConnect(PatientFacing)AccessRecord-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [NHS login service](NHS-login-service.md)

# Roadmap {#GPConnect(PatientFacing)AccessRecord-Roadmap}

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [National Proxy Service](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15035203759/National+Proxy+Service) | [Patient Information Maintenance - GP](https://nhse-dsic.atlassian.net/wiki/x/5AXrUg), [Validated Relationship Service](Validated-Relationship-Service.md), [GP Connect (Patient Facing) User Permissions](GP-Connect-Patient-Facing-User-Permissions.md), [GP Connect (Patient Facing) Access Record](GP-Connect-Patient-Facing-Access-Record.md), [GP Connect (Patient Facing) Prescriptions](GP-Connect-Patient-Facing-Prescriptions.md), [Multicast Notification Service (MNS)](Multicast-Notification-Service-MNS.md) | Published | 20 Apr 2027 | Integrate with the National Proxy Service | New | Managed Capacity - Other |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../.raw/DCSDCS/attachments/14303264899/att14303264911-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
- [e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml](../../../../.raw/DCSDCS/attachments/14303264899/att14303264914-e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml)
- [NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx](../../../../.raw/DCSDCS/attachments/14303264899/att14303264917-NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx)
