---
page_id: "13000933377"
space: "DCSDCS"
title: "National Events Management Service (NEMS)"
version: 13
updated: "2026-07-22T13:05:25.067Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/13000933377/National+Events+Management+Service+NEMS"
labels: ["standard"]
---

# National Events Management Service (NEMS)

|  |  |
| --- | --- |
| **ID** | S111 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#NationalEventsManagementService(NEMS)-Introduction)
- [Requirements](#NationalEventsManagementService(NEMS)-Requirements)
  - [Message Implementation](#NationalEventsManagementService(NEMS)-MessageImplementation)
- [Compliance, Assurance and Testing](#NationalEventsManagementService(NEMS)-Compliance,AssuranceandTesting)
- [Documentation](#NationalEventsManagementService(NEMS)-Documentation)
- [Dependencies](#NationalEventsManagementService(NEMS)-Dependencies)
- [Roadmap](#NationalEventsManagementService(NEMS)-Roadmap)

# Introduction {#NationalEventsManagementService(NEMS)-Introduction}

The National Events Management Service (NEMS) allows digital Health and Care services to notify other digital services that an ‘event’ has occurred, using ‘publish-subscribe’ messages.

For further information, see [National Events Management Service (NEMS)](https://digital.nhs.uk/services/national-events-management-service).

# Requirements {#NationalEventsManagementService(NEMS)-Requirements}

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| GP Suppliers | **NEMS01** | Subscribe to and implement the receipt of [PDS Record Change](https://digital.nhs.uk/developer/api-catalogue/personal-demographics-service-notifications-fhir) event messages inline with the latest specification version. | MUST |

## Message Implementation {#NationalEventsManagementService(NEMS)-MessageImplementation}

Dependent on the care setting or system, the messages needing to be subscribed to may differ. The table below shows which NEMS messages are required to be implemented based on the Capability being delivered.

|  |  |  |
| --- | --- | --- |
| **Capability** | **Applicable Requirement** | **Message** |
| [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | NEMS01 | PDS Record Change |

# Compliance, Assurance and Testing {#NationalEventsManagementService(NEMS)-Compliance,AssuranceandTesting}

See the National Event Monitoring Service (NEMS) section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation {#NationalEventsManagementService(NEMS)-Documentation}

- [Personal Demographics Service Notifications - FHIR Overview (developer.nhs.uk)](https://digital.nhs.uk/developer/api-catalogue/personal-demographics-service-notifications-fhir)

# Dependencies {#NationalEventsManagementService(NEMS)-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md)

# Roadmap {#NationalEventsManagementService(NEMS)-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NEMS Payload.pdf](../../../../attachments/DCSDCS/13000933377/att13000933393-NEMS Payload.pdf)
- [FHIR Payload of Health and Lifestyle information.pdf](../../../../attachments/DCSDCS/13000933377/att13000933396-FHIR Payload of Health and Lifestyle information.pdf)
- [FHIR Payload of Healthcare Data v2.0.pdf](../../../../attachments/DCSDCS/13000933377/att13000933399-FHIR Payload of Healthcare Data v2.0.pdf)
- [Screenshot 2024-05-01 at 17.23.13.png](../../../../attachments/DCSDCS/13000933377/att13000933402-Screenshot 2024-05-01 at 17.23.13.png)
- [FHIR Payload of Healthcare Data.pdf](../../../../attachments/DCSDCS/13000933377/att13000933405-FHIR Payload of Healthcare Data.pdf)
- [NEMS Payload (2).pdf](../../../../attachments/DCSDCS/13000933377/att13000933408-NEMS Payload (2).pdf)
