---
page_id: "13165985851"
space: "DCSDCS"
title: "Register with a GP Surgery Service"
version: 8
updated: "2026-07-22T13:12:30.696Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/13165985851/Register+with+a+GP+Surgery+Service"
labels: ["standard"]
---

# Register with a GP Surgery Service

|  |  |
| --- | --- |
| **ID** | S113 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

/\*<![CDATA[\*/
div.rbtoc1785510758677 {padding: 0px;}
div.rbtoc1785510758677 ul {list-style: default;margin-left: 0px;}
div.rbtoc1785510758677 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#RegisterwithaGPSurgeryService-Introduction)
- [Requirements](#RegisterwithaGPSurgeryService-Requirements)
- [Compliance, Assurance and Testing](#RegisterwithaGPSurgeryService-Compliance,AssuranceandTesting)
- [Documentation](#RegisterwithaGPSurgeryService-Documentation)
- [Dependencies](#RegisterwithaGPSurgeryService-Dependencies)
- [Roadmap](#RegisterwithaGPSurgeryService-Roadmap)

# Introduction

The Register with a GP Surgery Service allows Patients to submit registration application information and for digital health and care services to retrieve this information submitted by Patients.

# Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| GP Suppliers | **RGPSS01** | Implement and maintain the [Register with a GP Surgery](https://digital.nhs.uk/developer/api-catalogue/register-with-a-gp-surgery/content) API to obtain Patient Health and Lifestyle Information inline with the latest specification version. | MUST |

# Compliance, Assurance and Testing

See the Register with a GP Surgery Service section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

- [Register with a GP Surgery Service information](https://digital.nhs.uk/services/register-with-a-gp-surgery-service)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- [Personal Demographics Service (PDS)](Personal-Demographics-Service-PDS.md)

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Automated Patient Registration - uplift to include all encounter types](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15185477635/Automated+Patient+Registration+-+uplift+to+include+all+encounter+types) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Register with a GP Surgery Service](Register-with-a-GP-Surgery-Service.md) | Draft | TBC | Update to automated Patient Registration - Register with a GP Surgery Service requirements to automatically process GP Registrations for encounter types 1, 2, 4 and 5 in addition to encounter type 3, that is already being processed | Uplift | Managed Capacity - Other |

## Attachments

- [NEMS Payload (2).pdf](../../../../.raw/DCSDCS/attachments/13165985851/att13165985862-NEMS Payload (2).pdf)
- [FHIR Payload of Healthcare Data.pdf](../../../../.raw/DCSDCS/attachments/13165985851/att13165985865-FHIR Payload of Healthcare Data.pdf)
- [Screenshot 2024-05-01 at 17.23.13.png](../../../../.raw/DCSDCS/attachments/13165985851/att13165985868-Screenshot 2024-05-01 at 17.23.13.png)
- [FHIR Payload of Healthcare Data v2.0.pdf](../../../../.raw/DCSDCS/attachments/13165985851/att13165985871-FHIR Payload of Healthcare Data v2.0.pdf)
- [FHIR Payload of Health and Lifestyle information.pdf](../../../../.raw/DCSDCS/attachments/13165985851/att13165985874-FHIR Payload of Health and Lifestyle information.pdf)
- [NEMS Payload.pdf](../../../../.raw/DCSDCS/attachments/13165985851/att13165985877-NEMS Payload.pdf)
