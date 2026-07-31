---
page_id: "12723519530"
space: "DCSDCS"
title: "GP Connect Appointment Management"
version: 14
updated: "2026-07-22T12:21:40.482Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12723519530/GP+Connect+Appointment+Management"
labels: ["standard"]
---

# GP Connect Appointment Management

|  |  |
| --- | --- |
| **ID** | S100 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#GPConnectAppointmentManagement-Introduction)
- [Requirements](#GPConnectAppointmentManagement-Requirements)
- [Compliance, Assurance and Testing](#GPConnectAppointmentManagement-Compliance,AssuranceandTesting)
- [Documentation](#GPConnectAppointmentManagement-Documentation)
- [Dependencies](#GPConnectAppointmentManagement-Dependencies)
- [Roadmap](#GPConnectAppointmentManagement-Roadmap)

# Introduction

The GP Connect Appointment Management API enables Health or Care Professionals using a Consumer Solution to book and manage GP Practice Appointments held in any of the GP Practice Provider Solutions.

See [Appointment Management (developer.nhs.uk)](https://webarchive.nationalarchives.gov.uk/ukgwa/20250306181311/https://developer.nhs.uk/apis/gpconnect-1-2-7/appointments.html) for further information.

# Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| Provider | GPCAM01 | Implement and maintain the [GP Connect Appointment Management](https://webarchive.nationalarchives.gov.uk/ukgwa/20250306181311/https://developer.nhs.uk/apis/gpconnect-1-2-7/appointments.html) Provider requirements inline with the latest specification version. | MUST |
| Consumer | GPCAM02 | Implement and maintain the [GP Connect Appointment Management](https://webarchive.nationalarchives.gov.uk/ukgwa/20250306181311/https://developer.nhs.uk/apis/gpconnect-1-2-7/appointments.html) Consumer requirements inline with the latest specification version. | MUST |

# Compliance, Assurance and Testing

To achieve GP Connect compliance as a Provider, see the GP Connect Appointment Management - Provider section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

To achieve GP Connect compliance as a Consumer, Suppliers will need to follow the Supplier Conformance Assessment List (SCAL). More detail on this can be found [here](https://github.com/nhsconnect/gpc-consumer-support/wiki/Assurance-process-overview). For advice, access to testing resources, and support contact [gpconnect@nhs.net](mailto:gpconnect@nhs.net).

# Documentation

- [Developer Implementation Guide](https://developer.nhs.uk/apis/gpconnect-1-2-7/datalibraryappointment.html#)
- [GP Connect service information](https://digital.nhs.uk/services/gp-connect)
- [Develop GP Connect services](https://digital.nhs.uk/services/gp-connect/develop-gp-connect-services)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Personal Demographics Service (PDS)](Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](Spine-Mini-Services.md)

\*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [GP Connect Appointments Practitioner Role Update](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/12690849794/GP+Connect+Appointments+Practitioner+Role+Update) | [GP Connect Appointment Management](GP-Connect-Appointment-Management.md) | Draft | TBC | Expand the Job Roles (known as Care Connect SDS-Job Roles) the GP Practice Solution provides to each of the appointment slots it makes available via GP Connect Appointment Management API | Uplift | Managed Capacity - Other |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../.raw/DCSDCS/attachments/12723519530/att12723519546-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
- [e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml](../../../../.raw/DCSDCS/attachments/12723519530/att12723519549-e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml)
- [NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx](../../../../.raw/DCSDCS/attachments/12723519530/att12723519552-NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx)
