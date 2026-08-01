---
page_id: "13166477313"
space: "DCSDCS"
title: "Multicast Notification Service (MNS)"
version: 9
updated: "2026-07-22T13:04:19.682Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/13166477313/Multicast+Notification+Service+MNS"
labels: ["standard"]
---

# Multicast Notification Service (MNS)

|  |  |
| --- | --- |
| **ID** | S112 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#MulticastNotificationService(MNS)-Introduction)
- [Requirements](#MulticastNotificationService(MNS)-Requirements)
  - [Message Implementation](#MulticastNotificationService(MNS)-MessageImplementation)
- [Compliance, Assurance and Testing](#MulticastNotificationService(MNS)-Compliance,AssuranceandTesting)
- [Documentation](#MulticastNotificationService(MNS)-Documentation)
- [Dependencies](#MulticastNotificationService(MNS)-Dependencies)
- [Roadmap](#MulticastNotificationService(MNS)-Roadmap)

# Introduction {#MulticastNotificationService(MNS)-Introduction}

The Multicast Notification Service (MNS) allows digital health and care services to publish and receive Patient-related state changes from a single centralised system.

# Requirements {#MulticastNotificationService(MNS)-Requirements}

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| GP Suppliers | **MNS01** | Subscribe to and implement the receipt of [Validated GP Registration Request](https://digital.nhs.uk/developer/api-catalogue/multicast-notification-service/validated-gp-registration-request-event) signals inline with the latest specification version. | MUST |

## Message Implementation {#MulticastNotificationService(MNS)-MessageImplementation}

Dependent on the care setting or system, the signals needing to be subscribed to may differ. The table below shows which MNS signals are required to be implement based on the Capability being delivered.

|  |  |  |
| --- | --- | --- |
| **Capability** | **Applicable Requirement** | **Signal** |
| [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | MNS01 | Validated GP Registration Request |

# Compliance, Assurance and Testing {#MulticastNotificationService(MNS)-Compliance,AssuranceandTesting}

See the Multicast Notification Service (MNS) section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation {#MulticastNotificationService(MNS)-Documentation}

- [API Catalogue - Multicast Notification Service API](https://digital.nhs.uk/developer/api-catalogue/multicast-notification-service)

# Dependencies {#MulticastNotificationService(MNS)-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface standards:

- [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md) - if signals received via MESH

# Roadmap {#MulticastNotificationService(MNS)-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [NHS Health Check online](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14924611585/NHS+Health+Check+online) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Multicast Notification Service (MNS)](Multicast-Notification-Service-MNS.md) | Draft | TBC | Ingestion of NHS Health Check online data into Patients' Electronic Patient Records (EPRs) | New | Managed Capacity - Other |
| [National Proxy Service](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15035203759/National+Proxy+Service) | [Patient Information Maintenance - GP](https://nhse-dsic.atlassian.net/wiki/x/5AXrUg), [Validated Relationship Service](Validated-Relationship-Service.md), [GP Connect (Patient Facing) User Permissions](GP-Connect-Patient-Facing-User-Permissions.md), [GP Connect (Patient Facing) Access Record](GP-Connect-Patient-Facing-Access-Record.md), [GP Connect (Patient Facing) Prescriptions](GP-Connect-Patient-Facing-Prescriptions.md), [Multicast Notification Service (MNS)](Multicast-Notification-Service-MNS.md) | Published | 20 Apr 2027 | Integrate with the National Proxy Service | New | Managed Capacity - Other |
| [Patient Flags Service - Reasonable Adjustments (RA) Flag](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/12194349077/Patient+Flags+Service+-+Reasonable+Adjustments+RA+Flag) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Multicast Notification Service (MNS)](Multicast-Notification-Service-MNS.md) | Published | 08 Jan 2027 | Enable national sharing and management of Patients Reasonable Adjustments Flag via the Patient Flags Service - FHIR API | New | Managed Capacity - Other |

## Attachments

- [NEMS Payload.pdf](../../../../.raw/DCSDCS/attachments/13166477313/att13166477326-NEMS Payload.pdf)
- [FHIR Payload of Health and Lifestyle information.pdf](../../../../.raw/DCSDCS/attachments/13166477313/att13166477329-FHIR Payload of Health and Lifestyle information.pdf)
- [FHIR Payload of Healthcare Data v2.0.pdf](../../../../.raw/DCSDCS/attachments/13166477313/att13166477332-FHIR Payload of Healthcare Data v2.0.pdf)
- [Screenshot 2024-05-01 at 17.23.13.png](../../../../.raw/DCSDCS/attachments/13166477313/att13166477335-Screenshot 2024-05-01 at 17.23.13.png)
- [FHIR Payload of Healthcare Data.pdf](../../../../.raw/DCSDCS/attachments/13166477313/att13166477338-FHIR Payload of Healthcare Data.pdf)
- [NEMS Payload (2).pdf](../../../../.raw/DCSDCS/attachments/13166477313/att13166477341-NEMS Payload (2).pdf)
