---
page_id: "14439350273"
space: "DCSDCS"
title: "Validated Relationship Service"
version: 4
updated: "2026-07-22T13:16:33.652Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14439350273/Validated+Relationship+Service"
labels: ["standard"]
---

# Validated Relationship Service

|  |  |
| --- | --- |
| **ID** | S114 |
| **Version** | 1.0.0 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 01 Apr 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#ValidatedRelationshipService-Introduction)
- [Requirements](#ValidatedRelationshipService-Requirements)
  - [Validated Relationship Service Operations](#ValidatedRelationshipService-ValidatedRelationshipServiceOperations)
- [Compliance, Assurance and Testing](#ValidatedRelationshipService-Compliance,AssuranceandTesting)
- [Documentation](#ValidatedRelationshipService-Documentation)
- [Dependencies](#ValidatedRelationshipService-Dependencies)
- [Roadmap](#ValidatedRelationshipService-Roadmap)

# Introduction

The Validated Relationship Service - FHIR API enables a Solution to access the Validated Relationship Service. This is the national electronic database of relationships that have been verified for the purpose of enabling individuals to access healthcare services on behalf of those they care for. The relationships held by this service are strictly for the purpose of enabling access to healthcare services.

# Requirements

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| All Suppliers | VRS01 | Implement and maintain the [Validated Relationship Service - FHIR API](https://digital.nhs.uk/developer/api-catalogue/validated-relationship-service) inline with the latest specification version as per the Validated Relationship Service Operations section. | MUST |

## Validated Relationship Service Operations

| **Capability** | **Get Verified Candidate Relationships** | **Get Proxy Roles** | **Create Proxy Roles** |
| --- | --- | --- | --- |
| [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | (tick) | (error) | (error) |

# Compliance, Assurance and Testing

See the Validated Relationship Service section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

- [Validated Relationship Service - FHIR API](https://digital.nhs.uk/developer/api-catalogue/validated-relationship-service)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- [Authentication and Access](Authentication-and-Access.md) - using NHS Care Identity Service 2 API

# Roadmap

Items on the Roadmap which impact or relate to this Standard.

| Title | **Change Route** | **Change Type** | **Contracting Vehicle(s)** | **Date Added** | **Description** | **Effective Date** | **ID** | **Incentive / Funding Dates** | **Incentives / Funding** | **Publication Date** | **Standards and Capabilities** | **Status** | **Title** | **Type** | **Version** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [National Proxy Service](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15035203759/National+Proxy+Service) | Managed Capacity - Other | New | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) | 07 May 2026 | Integrate with the National Proxy Service | 20 Apr 2027 | RM279 | **Applicability:** This incentive amount is applicable to Catalogue Solutions which are live in GP Practices in England at the time of publication of this Roadmap Item.  **Incentive amount:** An incentive payment of £265,000 is conditional upon the successful delivery of the Roadmap Item.  **Payment Rules:**   1. All assurance evidence is provided on or before Incentive End Date 2. The deployment of the Roadmap Item into the agreed pilot sites as defined below 3. The work the Supplier will undertake for this incentive will not impact the delivery of any other mandated Roadmap Items applicable to them | **Incentive Start Date**: The date on which this Roadmap Item attains “Published” status.  **Incentive End Date**: 29 Jan 2027 | 20 Jul 2026 | [Patient Information Maintenance - GP](https://nhse-dsic.atlassian.net/wiki/x/5AXrUg), [Validated Relationship Service](Validated-Relationship-Service.md), [GP Connect (Patient Facing) User Permissions](GP-Connect-Patient-Facing-User-Permissions.md), [GP Connect (Patient Facing) Access Record](GP-Connect-Patient-Facing-Access-Record.md), [GP Connect (Patient Facing) Prescriptions](GP-Connect-Patient-Facing-Prescriptions.md), [Multicast Notification Service (MNS)](Multicast-Notification-Service-MNS.md) | Published | National Proxy Service | Roadmap Item | 1.2.1 |