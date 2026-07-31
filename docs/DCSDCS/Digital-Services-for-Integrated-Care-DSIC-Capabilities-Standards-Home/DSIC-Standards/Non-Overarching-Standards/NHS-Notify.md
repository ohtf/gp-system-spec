---
page_id: "14968717313"
space: "DCSDCS"
title: "NHS Notify"
version: 4
updated: "2026-07-23T13:49:47.649Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14968717313/NHS+Notify"
labels: ["standard"]
---

# NHS Notify

|  |  |
| --- | --- |
| **ID** | S124 |
| **Version** | 1.0.0 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 16 Apr 2026 |
| **Contracting Vehicle(s)** | - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) |

/\*<![CDATA[\*/
div.rbtoc1785511574894 {padding: 0px;}
div.rbtoc1785511574894 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785511574894 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#NHSNotify-Introduction)
- [Requirements](#NHSNotify-Requirements)
  - [Using NHS Notify API](#NHSNotify-UsingNHSNotifyAPI)
  - [Using NHS Notify MESH](#NHSNotify-UsingNHSNotifyMESH)
- [Compliance, Assurance and Testing](#NHSNotify-Compliance,AssuranceandTesting)
- [Documentation](#NHSNotify-Documentation)
- [Dependencies](#NHSNotify-Dependencies)
- [Roadmap](#NHSNotify-Roadmap)

# Introduction

Integration with NHS Notify allows organisations and services to send NHS App messages, emails, texts and letters to Patients, the public and recipients of adult social care.

See [NHS Notify](https://notify.nhs.uk/) for further information.

# Requirements

To implement the NHS Notify requirements, you can either use NHS Notify API or NHS Notify MESH. To determine which method of integration is the most appropriate for your Solution, please refer to the ‘Who can use this API’ section in [NHS Notify API](https://digital.nhs.uk/developer/api-catalogue/nhs-notify) and the ‘Who can use this integration’ section in [NHS Notify MESH](https://digital.nhs.uk/developer/api-catalogue/nhs-notify-mesh).

## Using NHS Notify API

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| All Suppliers | NN01 | Implement and maintain the [NHS Notify API](https://digital.nhs.uk/developer/api-catalogue/nhs-notify) in line with the latest specification version. | MUST |

## Using NHS Notify MESH

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| All Suppliers | NN02 | Implement and maintain the [NHS Notify MESH](https://digital.nhs.uk/developer/api-catalogue/nhs-notify-mesh) integration in line with the latest specification version. | MUST |

# Compliance, Assurance and Testing

See the NHS Notify section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

- [Onboard with NHS Notify](https://notify.nhs.uk/get-started/onboard-with-nhs-notify)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md) - For Suppliers of Solutions who use Messaging Exchange for Social Care and Health (MESH) to integrate with NHS Notify

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |