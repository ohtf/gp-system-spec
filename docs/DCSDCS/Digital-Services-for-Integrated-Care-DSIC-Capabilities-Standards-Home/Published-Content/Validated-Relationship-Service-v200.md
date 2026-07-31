---
page_id: "15262941236"
space: "DCSDCS"
title: "Validated Relationship Service v2.0.0"
version: 1
updated: "2026-07-20T08:45:23.647Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/15262941236/Validated+Relationship+Service+v2.0.0"
labels: ["standard"]
---

# Validated Relationship Service v2.0.0

|  |  |
| --- | --- |
| **ID** | S114 |
| **Version** | 2.0.0 |
| **Type** | Standard |
| **Status** | Published |
| **Effective Date** | 20 Apr 2027 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

- [Introduction](#ValidatedRelationshipServicev2.0.0-Introduction)
- [Requirements](#ValidatedRelationshipServicev2.0.0-Requirements)
  - [Validated Relationship Service Operations by Capability Mapping](#ValidatedRelationshipServicev2.0.0-ValidatedRelationshipServiceOperationsbyCapabilityMapping)
- [Compliance, Assurance and Testing](#ValidatedRelationshipServicev2.0.0-Compliance,AssuranceandTesting)
- [Documentation](#ValidatedRelationshipServicev2.0.0-Documentation)
- [Dependencies](#ValidatedRelationshipServicev2.0.0-Dependencies)
- [Roadmap](#ValidatedRelationshipServicev2.0.0-Roadmap)

# Introduction

The Validated Relationship Service - FHIR API enables a Solution to access the Validated Relationship Service. This is the national electronic database of relationships that have been verified for the purpose of enabling individuals to access healthcare services on behalf of those they care for. The relationships held by this service are strictly for the purpose of enabling access to healthcare services.

# Requirements

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| GP Suppliers | VRS01 | Implement and maintain the [Validated Relationship Service - FHIR API](https://digital.nhs.uk/developer/api-catalogue/validated-relationship-service) inline with the latest specification version as per the Validated Relationship Service Operations by Capability Mapping section. | MUST |
| VRS02 | **Reliability - Retries**  The GP Practice Solution must attempt a minimum of 3 retries (with a configurable option to extend to 5) before classifying a request to the Validated Relationship Service as failed. | MUST |
| VRS03 | **Performance - Data Processing**  Proxy role data must be processed and made available in the GP IT System within 5 minutes of receipt of the MNS event notification from MNS, measured end-to-end. | MUST |
| VRS04 | **Reliability - Dead Letter Queue (DLQ)**  Unprocessable events or requests stemming from background processing must be published to a Dead Letter Queue (DLQ) for investigation and out-of-band processing. | MUST |
| VRS05 | **Reliability - DLQ Retry**  Events or requests in the DLQ must be retried after the cause of failure has been resolved, within 1 working day. | MUST |
| VRS06 | **Reliability - Exponential Backoff Strategy**  Retry logic for failed request processing must follow an exponential backoff strategy to prevent system overload and ensure safe reprocessing. | MUST |

## Validated Relationship Service Operations by Capability Mapping

Dependent on the care setting or system, the operations required may differ. The table below shows which Validated Relationship Service Operations are required to be implement based on the Capability being delivered.

| **Capability** | **New Access request** | **Get a proxy access request** | **Get verified candidate relationships** | **Get proxy roles** | **Create a proxy role** | **Get proxy role** | **Update a proxy role** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | (error) | (error) | (tick) | (tick) | (tick) | (tick) | (tick) |

# Compliance, Assurance and Testing

See the Validated Relationship Service section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

- [National Proxy Service Integration Documents](https://nhsdigital.github.io/national-proxy-service-integration-docs/)
- [Validated Relationship Service - FHIR API](https://digital.nhs.uk/developer/api-catalogue/validated-relationship-service)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- [Authentication and Access](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API
- [Multicast Notification Service (MNS)](../DSIC-Standards/Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) Standard

# Roadmap

Items on the Roadmap which impact or relate to this Standard.

| Title | **Change Route** | **Change Type** | **Contracting Vehicle(s)** | **Date Added** | **Description** | **Effective Date** | **ID** | **Incentive / Funding Dates** | **Incentives / Funding** | **Publication Date** | **Standards and Capabilities** | **Status** | **Title** | **Type** | **Version** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [National Proxy Service](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15035203759/National+Proxy+Service) | Managed Capacity - Other | New | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) | 07 May 2026 | Integrate with the National Proxy Service | 20 Apr 2027 | RM279 | **Applicability:** This incentive amount is applicable to Catalogue Solutions which are live in GP Practices in England at the time of publication of this Roadmap Item.  **Incentive amount:** An incentive payment of £265,000 is conditional upon the successful delivery of the Roadmap Item.  **Payment Rules:**   1. All assurance evidence is provided on or before Incentive End Date 2. The deployment of the Roadmap Item into the agreed pilot sites as defined below 3. The work the Supplier will undertake for this incentive will not impact the delivery of any other mandated Roadmap Items applicable to them | **Incentive Start Date**: The date on which this Roadmap Item attains “Published” status.  **Incentive End Date**: 29 Jan 2027 | 20 Jul 2026 | [Patient Information Maintenance - GP](https://nhse-dsic.atlassian.net/wiki/x/5AXrUg), [Validated Relationship Service](../DSIC-Standards/Non-Overarching-Standards/Validated-Relationship-Service.md), [GP Connect (Patient Facing) User Permissions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-User-Permissions.md), [GP Connect (Patient Facing) Access Record](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Access-Record.md), [GP Connect (Patient Facing) Prescriptions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Prescriptions.md), [Multicast Notification Service (MNS)](../DSIC-Standards/Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) | Published | National Proxy Service | Roadmap Item | 1.2.1 |