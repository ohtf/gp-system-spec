---
page_id: "1391133789"
space: "DCSDCS"
title: "Screening Messaging"
version: 14
updated: "2026-07-22T13:12:55.988Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133789/Screening+Messaging"
labels: ["standard"]
---

# Screening Messaging

|  |  |
| --- | --- |
| **ID** | S58 |
| **Version** | 1.0.2 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#ScreeningMessaging-Introduction)
- [Requirements](#ScreeningMessaging-Requirements)
  - [Using Lab Results adaptor](#ScreeningMessaging-UsingLabResultsadaptor)
  - [Without using Lab Results adaptor](#ScreeningMessaging-WithoutusingLabResultsadaptor)
- [Compliance, Assurance and Testing](#ScreeningMessaging-Compliance,AssuranceandTesting)
- [Documentation](#ScreeningMessaging-Documentation)
  - [Using Lab Results adaptor](#ScreeningMessaging-UsingLabResultsadaptor.1)
- [Dependencies](#ScreeningMessaging-Dependencies)
- [Roadmap](#ScreeningMessaging-Roadmap)

# Introduction

Some screening programmes use the [Digital Diagnostics & Pathology Messaging](Digital-Diagnostics-Pathology-Messaging.md) Standards to return results to GP systems. Variant NHS004 of the Medical Service Report (MEDRPT) message was created to enable it to carry screening results.

In addition to the minor changes to the message definition, the system is required to identify NHS004 messages as ‘screening messages’ rather than pathology messages and to present them as such to users for processing.

# Requirements

To comply with the Screening Messaging Standard there are currently two implementation options:

1. Using Lab Results adaptor
2. Without using Lab Results adaptor

### Using Lab Results adaptor

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| **SRN5** | If implementing Screening Messaging using the Lab Results adaptor (aka EDIFACT adaptor):   - Suppliers to Implement and maintain the adapter inline with the latest specification of the [Lab Results adaptor](https://digital.nhs.uk/developer/api-catalogue/lab-results-adaptor).   The adaptor provides a pre-assured implementation of the Screening Messaging Standard and covers requirements below. | MUST |

### Without using Lab Results adaptor

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| **SRN1** | The system MUST support MIG variant NHS004 of the EDIFACT Laboratory Service Report (MEDRPT) message. | MUST |
| **SRN2** | The system MUST perform the same validation checks (e.g. EDIFACT constructs, Patient, Receiving Organisation, sender/recipient identifiers, etc) on a NHS004 message as a NHS003 message with the exception of the clinical code validation check. | MUST |
| **SRN3** | The system MUST comply with the requirements contained in the following document: [Cancer Screening - eGP-Comms GP Software Supplier Requirements v4.1.doc](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133789/Cancer%20Screening%20-%20eGP-Comms%20GP%20Software%20Supplier%20Requirements%20v4.1.doc?version=1&modificationDate=1520365800044&cacheVersion=1&api=v2) | MUST |
| **SRN4** | From time to time the authority will provide updates to terminology code list and associated terminology mapping tables contained in the ‘Cancer Screening - eGP-Comms GP Software Supplier Requirements v4.1.doc’ requirement document (see SRN3 above)  Updates will be published as an addendum to the issued document and will additionally provide a schedule for implementation. Suppliers MUST be compliant with the updated code list aligned to the published schedule. The schedule will allow at least 3 months for implementation. | MUST |

# Compliance, Assurance and Testing

See the Screening Messaging section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

### Using Lab Results adaptor

For Suppliers of new services or applications:

- [API Catalogue - Lab Results adaptor](https://digital.nhs.uk/developer/api-catalogue/lab-results-adaptor)
- [GP software developer guide](https://digital.nhs.uk/developer/guides-and-documentation/developer-guides/gp-software-developer-guide)

It is recommended to read GP software developer guide in conjunction with the adaptor documentation.

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md)

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [Cancer Screening - eGP-Comms GP Software Supplier Requirements v4.1.doc](../../../../.raw/DCSDCS/attachments/1391133789/att1391142678-Cancer Screening - eGP-Comms GP Software Supplier Requirements v4.1.doc)
