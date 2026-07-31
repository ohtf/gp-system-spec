---
page_id: "15262941185"
space: "DCSDCS"
title: "Multicast Notification Service (MNS) v3.0.0"
version: 1
updated: "2026-07-20T08:46:04.714Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/15262941185/Multicast+Notification+Service+MNS+v3.0.0"
labels: ["standard"]
---

# Multicast Notification Service (MNS) v3.0.0

|  |  |
| --- | --- |
| ID | S112 |
| Version | 3.0.0 |
| Type | Standard |
| Status | Published |
| Effective Date | 20 Apr 2027 |
| Contracting Vehicle(s) | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

/\*<![CDATA[\*/
div.rbtoc1785511687668 {padding: 0px;}
div.rbtoc1785511687668 ul {list-style: default;margin-left: 0px;}
div.rbtoc1785511687668 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#MulticastNotificationService(MNS)v3.0.0-Introduction)
- [Requirements](#MulticastNotificationService(MNS)v3.0.0-Requirements)
  - [Event Implementation by Capability Mapping](#MulticastNotificationService(MNS)v3.0.0-EventImplementationbyCapabilityMapping)
- [Compliance, Assurance and Testing](#MulticastNotificationService(MNS)v3.0.0-Compliance,AssuranceandTesting)
- [Documentation](#MulticastNotificationService(MNS)v3.0.0-Documentation)
- [Dependencies](#MulticastNotificationService(MNS)v3.0.0-Dependencies)
- [Roadmap](#MulticastNotificationService(MNS)v3.0.0-Roadmap)

# Introduction

The Multicast Notification Service (MNS) allows digital health and care services to publish and receive Patient-related state changes from a single centralised system.

# Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| GP Suppliers | MNS01 | Subscribe to and implement the receipt of Multicast Notification Service events inline with the latest specification version as per the Event Implementation by Capability Mapping section. | MUST |

## Event Implementation by Capability Mapping

|  |  |
| --- | --- |
| **Capability** | **Event** |
| [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | [Validated GP Registration Request](https://digital.nhs.uk/developer/api-catalogue/multicast-notification-service/validated-gp-registration-request-event) |
| [Patient flags change event](https://digital.nhs.uk/developer/api-catalogue/multicast-notification-service/patient-flags-change-event) |
| [Proxy role change event](https://digital.nhs.uk/developer/api-catalogue/multicast-notification-service/proxy-role-changed-event) |
| [Proxy role deleted event](https://digital.nhs.uk/developer/api-catalogue/multicast-notification-service/proxy-role-deleted-event) |

# Compliance, Assurance and Testing

See the Multicast Notification Service (MNS) section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

- [API Catalogue - Multicast Notification Service API](https://digital.nhs.uk/developer/api-catalogue/multicast-notification-service)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) - if events received via MESH

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [NHS Health Check online](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14924611585/NHS+Health+Check+online) | [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Multicast Notification Service (MNS)](../DSIC-Standards/Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) | Draft | TBC | Ingestion of NHS Health Check online data into Patients' Electronic Patient Records (EPRs) | New | Managed Capacity - Other |
| [National Proxy Service](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15035203759/National+Proxy+Service) | [Patient Information Maintenance - GP](https://nhse-dsic.atlassian.net/wiki/x/5AXrUg), [Validated Relationship Service](../DSIC-Standards/Non-Overarching-Standards/Validated-Relationship-Service.md), [GP Connect (Patient Facing) User Permissions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-User-Permissions.md), [GP Connect (Patient Facing) Access Record](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Access-Record.md), [GP Connect (Patient Facing) Prescriptions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Prescriptions.md), [Multicast Notification Service (MNS)](../DSIC-Standards/Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) | Published | 20 Apr 2027 | Integrate with the National Proxy Service | New | Managed Capacity - Other |
| [Patient Flags Service - Reasonable Adjustments (RA) Flag](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/12194349077/Patient+Flags+Service+-+Reasonable+Adjustments+RA+Flag) | [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Multicast Notification Service (MNS)](../DSIC-Standards/Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) | Published | 08 Jan 2027 | Enable national sharing and management of Patients Reasonable Adjustments Flag via the Patient Flags Service - FHIR API | New | Managed Capacity - Other |

## Attachments

- [FHIR Payload of Healthcare Data v2.0.pdf](../../../.raw/DCSDCS/attachments/15262941185/att15262941202-FHIR Payload of Healthcare Data v2.0.pdf)
- [FHIR Payload of Health and Lifestyle information.pdf](../../../.raw/DCSDCS/attachments/15262941185/att15262941205-FHIR Payload of Health and Lifestyle information.pdf)
- [NEMS Payload.pdf](../../../.raw/DCSDCS/attachments/15262941185/att15262941208-NEMS Payload.pdf)
- [FHIR Payload of Healthcare Data.pdf](../../../.raw/DCSDCS/attachments/15262941185/att15262941211-FHIR Payload of Healthcare Data.pdf)
- [Screenshot 2024-05-01 at 17.23.13.png](../../../.raw/DCSDCS/attachments/15262941185/att15262941214-Screenshot 2024-05-01 at 17.23.13.png)
- [NEMS Payload (2).pdf](../../../.raw/DCSDCS/attachments/15262941185/att15262941217-NEMS Payload (2).pdf)
