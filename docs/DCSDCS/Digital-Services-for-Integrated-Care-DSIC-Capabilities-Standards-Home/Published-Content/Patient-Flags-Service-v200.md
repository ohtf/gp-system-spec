---
page_id: "15244296216"
space: "DCSDCS"
title: "Patient Flags Service v2.0.0"
version: 1
updated: "2026-07-08T10:46:47.245Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/15244296216/Patient+Flags+Service+v2.0.0"
labels: ["standard"]
---

# Patient Flags Service v2.0.0

|  |  |
| --- | --- |
| **ID** | S115 |
| **Version** | 2.0.0 |
| **Type** | Standard |
| **Status** | Published |
| **Effective Date** | 08 Feb 2027 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

- [Introduction](#PatientFlagsServicev2.0.0-Introduction)
- [Requirements](#PatientFlagsServicev2.0.0-Requirements)
  - [Flag Implementation by Capability Mapping](#PatientFlagsServicev2.0.0-FlagImplementationbyCapabilityMapping)
- [Compliance, Assurance and Testing](#PatientFlagsServicev2.0.0-Compliance,AssuranceandTesting)
- [Documentation](#PatientFlagsServicev2.0.0-Documentation)
- [Dependencies](#PatientFlagsServicev2.0.0-Dependencies)
- [Roadmap](#PatientFlagsServicev2.0.0-Roadmap)

# Introduction {#PatientFlagsServicev2.0.0-Introduction}

The Patient Flags Service allows Health or Care Professionals to access and update Patient Flags and associated supporting resources.

# Requirements {#PatientFlagsServicev2.0.0-Requirements}

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| GP Suppliers | PFS-001 | Implement and maintain the [Patient Flags Service - FHIR API](https://digital.nhs.uk/developer/api-catalogue/patient-flags-service---fhir-api) inline with the latest API specification version for the Patient Flags and associated supporting resources as per the Flag Implementation by Capability Mapping section. | MUST |
| PFS-002 | The [Patient Flags Service - FHIR API](https://digital.nhs.uk/developer/api-catalogue/patient-flags-service---fhir-api) to be called to retrieve the latest Patient Flag information when a notification from the [Multicast Notification Service (MNS)](../DSIC-Standards/Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) is processed. | MUST |

## Flag Implementation by Capability Mapping {#PatientFlagsServicev2.0.0-FlagImplementationbyCapabilityMapping}

| **Capability** | **Flag** | **Create Flag** | **Create Supporting Resource** | **View Flag** | **View Supporting Resource** | **Amend Flag** | **Delete Flag** | **Delete Supporting Resource** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | Reasonable Adjustments Flag (RA) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) |
| Child Protection - Information Sharing (CP-IS) Flag | (error) | (error) | (tick) | (tick) | (error) | (error) | (error) |

# Compliance, Assurance and Testing {#PatientFlagsServicev2.0.0-Compliance,AssuranceandTesting}

See the Patient Flags Service section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation {#PatientFlagsServicev2.0.0-Documentation}

- [Patient Flags FHIR API (NHS England)](https://digital.nhs.uk/developer/api-catalogue/patient-flags-service---fhir-api#overview--overview)

# Dependencies {#PatientFlagsServicev2.0.0-Dependencies}

- Creating a compliant implementation requires implementing the following dependent interface Standards:

  - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md)
  - [Multicast Notification Service (MNS)](../DSIC-Standards/Non-Overarching-Standards/Multicast-Notification-Service-MNS.md)
  - [Authentication and Access](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API (unless Patient Flags Service is implemented using [Application-Restricted access](https://digital.nhs.uk/developer/api-catalogue/patient-flags-service---fhir-api#overview--security-and-authorisation))

# Roadmap {#PatientFlagsServicev2.0.0-Roadmap}

Items on the Roadmap which impact or relate to this Standard:

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Patient Flags Service - Female Genital Mutilation (FGM) Flag](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14101676093/Patient+Flags+Service+-+Female+Genital+Mutilation+FGM+Flag) | [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), Patient Flags Service | Published | 08 Mar 2027 | Enable national sharing and management of Female Genital Mutilation Flag data via the Patient Flags Service - FHIR API | Uplift | Managed Capacity - Other |
| [Patient Flags Service - Child Protection - Information Sharing (CP-IS) Flag](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14101446658/Patient+Flags+Service+-+Child+Protection+-+Information+Sharing+CP-IS+Flag) | [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), Patient Flags Service | Published | 08 Feb 2027 | Enable national sharing and management of Patients Child Protection - Information Sharing Flags via the Patient Flags Service - FHIR API | Uplift | Managed Capacity - Other |