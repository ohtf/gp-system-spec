---
page_id: "13879771185"
space: "DCSDCS"
title: "NHAIS HA/GP Links V2.0.2"
version: 3
updated: "2025-02-28T10:30:38.290Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/13879771185/NHAIS+HA+GP+Links+V2.0.2"
labels: ["standard_retired"]
---

# NHAIS HA/GP Links V2.0.2

|  |  |
| --- | --- |
| ID | S53 |
| Version | 2.0.2 |
| Type | Standard |
| Status | Retired |
| Effective Date | 10 May 2022 |
| Contracting Vehicle(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) |

- [Introduction](#NHAISHA/GPLinksV2.0.2-Introduction)
- [Requirements](#NHAISHA/GPLinksV2.0.2-Requirements)
  - [Using NHAIS GP Links Adaptor](#NHAISHA/GPLinksV2.0.2-UsingNHAISGPLinksAdaptor)
  - [Without Using NHAIS GP Links Adaptor](#NHAISHA/GPLinksV2.0.2-WithoutUsingNHAISGPLinksAdaptor)
- [Compliance, Assurance and Testing](#NHAISHA/GPLinksV2.0.2-Compliance,AssuranceandTesting)
  - [Using NHAIS GP Links Adaptor](#NHAISHA/GPLinksV2.0.2-UsingNHAISGPLinksAdaptor.1)
  - [Without Using NHAIS GP Links Adaptor](#NHAISHA/GPLinksV2.0.2-WithoutUsingNHAISGPLinksAdaptor.1)
- [Documentation](#NHAISHA/GPLinksV2.0.2-Documentation)
  - [Using NHAIS GP Links Adaptor](#NHAISHA/GPLinksV2.0.2-UsingNHAISGPLinksAdaptor.2)
  - [Without Using NHAIS GP Links Adaptor](#NHAISHA/GPLinksV2.0.2-WithoutUsingNHAISGPLinksAdaptor.2)
- [Dependencies](#NHAISHA/GPLinksV2.0.2-Dependencies)
  - [Using NHAIS GP Links Adaptor](#NHAISHA/GPLinksV2.0.2-UsingNHAISGPLinksAdaptor.3)
- [Roadmap](#NHAISHA/GPLinksV2.0.2-Roadmap)

# Introduction

National Health Application and Infrastructure Services (NHAIS) is a system which manages the primary care registration service and supports GP payments and cervical cancer screening. The system maintains Patient registration and their demographic details for England, Wales, Isle of Man and Northern Ireland. NHAIS HA (Health Authority) / GP interfaces allow for the two-way exchange of data covering registration changes.

# Requirements

To comply with the NHAIS HA/GP Links Standard there are currently two implementation options:

1. Using NHAIS GP Links adaptor
2. Without using NHAIS GP Links adaptor

### Using NHAIS GP Links Adaptor

|  |  |  |
| --- | --- | --- |
| ID | Requirement | Level |
| NH06 | If implementing NHAIS HA/GP Links using the NHAIS GP Links adaptor:   - Suppliers to implement and maintain the adapter inline with the latest specification of the NHAIS GP Links adaptor   The adaptor provides a pre-assured implementation of the NHAIS/GP Links Standard and covers the requirements below. | MUST |

### Without Using NHAIS GP Links Adaptor

|  |  |  |
| --- | --- | --- |
| ID | Requirement | Level |
| NH01 | Retransmission of a GP-NHAIS Registration EDIFACT message MUST be solely in response to a request from the receiving organisation: automatic re-transmission is not acceptable. | MUST |
| NH02 | Interchanges carrying NHS Standard EDIFACT GP-NHAIS messages MUST conform to the mandatory requirements specified within the following document:   - 'Interchange Implementation Guidelines for General Practice Systems' | MUST |
| NH03 | The system MUST conform to the general GP-NHAIS messaging specifications contained within the following document:   - ‘General Practitioner System Specification Communications and General System, v4.0’ | MUST |
| NH04 | The system MUST implement the FHSREG message in accordance with the following documents:   - NHAIS Registration GP System Specifications (see attachments below) - [FHSREG EDIFACT Message Implementation Guidelines Version 1.4](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133619/FHSREG%27%20EDIFACT%20Message%20Implementation%20Guidelines%20Version%201.4?version=1&modificationDate=1528885394317&cacheVersion=1&api=v2)   (see GP Systems v2 Baseline Index)   - [PCRM GP Links Requirements](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133619/PCRM%20Requirements_171219%20(10).xlsx?version=1&modificationDate=1654085853323&cacheVersion=1&api=v2) | MUST |
| NH05 | The system MUST support communication with at least 4 NHAIS systems per GP Practice at any one time. | MUST |

# Compliance, Assurance and Testing

### Using NHAIS GP Links Adaptor

- For Suppliers of new Services or applications, see the NHAIS section on Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements.

### Without Using NHAIS GP Links Adaptor

- For advice and support on assurance please contact businesspartners@nhs.net or visit https://digital.nhs.uk/services/nhs-business-partners

# Documentation

### Using NHAIS GP Links Adaptor

For Suppliers of new Services or applications:

- API Catalogue - NHAIS GP Links adaptor
- [Solution Assurance - Assurance Approach for New Market Entrants Integration with NHAIS](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133619/SA%20Assurance%20Approach%20for%20New%20Market%20Entrants%20Integration%20with%20NHAIS%20v0.41.docx?api=v2)
- GP software developer guide

It is recommended to read GP software developer guide in conjunction with the adaptor documentation

### Without Using NHAIS GP Links Adaptor

ISB 1558 - 36/97/P23 Revised General Medical Services Central Returns - message implementation guidelines.

#### NHAIS Registration GP System Specifications, version 2.0

[Cover.doc](NHAIS-HAGP-Links-V202.md)

[Contents.doc](NHAIS-HAGP-Links-V202.md)

[GP Spec Chapter1.doc](NHAIS-HAGP-Links-V202.md)

[GP Spec Chapter2.doc](NHAIS-HAGP-Links-V202.md)

[GP Spec Chapter3.doc](NHAIS-HAGP-Links-V202.md)

[GP Spec Chapter4.doc](NHAIS-HAGP-Links-V202.md)

#### NHAIS Registration GP System Specifications Appendix A - K, version 2.0

[App-A.doc](NHAIS-HAGP-Links-V202.md)

[App-B.doc](NHAIS-HAGP-Links-V202.md)

[App-C.doc](NHAIS-HAGP-Links-V202.md)

[App-D.doc](NHAIS-HAGP-Links-V202.md)

[App-E.doc](NHAIS-HAGP-Links-V202.md)

[App-F.doc](NHAIS-HAGP-Links-V202.md)

[App-G.doc](NHAIS-HAGP-Links-V202.md)

[App-H.doc](NHAIS-HAGP-Links-V202.md)

[App-I.doc](NHAIS-HAGP-Links-V202.md)

[App-J.doc](NHAIS-HAGP-Links-V202.md)

[App-K.doc](NHAIS-HAGP-Links-V202.md)

#### GP Comms & Messaging Specification, V3.0

[comspec3.doc](NHAIS-HAGP-Links-V202.md)

#### FHSREG Edifact Message Implementation Guidelines, V1.4

[FHSREG v14.doc](NHAIS-HAGP-Links-V202.md)

#### Receipt Report Message, V1.3

[Recep13.doc](NHAIS-HAGP-Links-V202.md)

Read the Guide to NHAIS/GP Links Documentation to better understand how to digest some of the documents listed on this page.

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

### Using NHAIS GP Links Adaptor

Creating a compliant implementation requires:

MESH mailbox but MESH is implemented with adaptor

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [SA Assurance Approach for New Market Entrants Integration with NHAIS v0.41.docx](../../../../.raw/DCSDCS/attachments/13879771185/att13879771208-SA Assurance Approach for New Market Entrants Integration with NHAIS v0.41.docx)
- [PCRM Requirements_171219 (10).xlsx](../../../../.raw/DCSDCS/attachments/13879771185/att13879771211-PCRM Requirements_171219 (10).xlsx)
- [GP Spec Chapter2.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771214-GP Spec Chapter2.doc)
- [GP Spec Chapter1.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771217-GP Spec Chapter1.doc)
- [GP Spec Chapter3.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771220-GP Spec Chapter3.doc)
- [GP Spec Chapter4.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771223-GP Spec Chapter4.doc)
- [Recep13.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771226-Recep13.doc)
- [FHSREG v14.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771229-FHSREG v14.doc)
- [comspec3.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771232-comspec3.doc)
- [FHSREG' EDIFACT Message Implementation Guidelines Version 1.4](../../../../.raw/DCSDCS/attachments/13879771185/att13879771235-FHSREG' EDIFACT Message Implementation Guidelines Version 1.4)
- [App-J.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771238-App-J.doc)
- [App-I.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771241-App-I.doc)
- [App-H.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771244-App-H.doc)
- [App-G.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771247-App-G.doc)
- [App-F.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771250-App-F.doc)
- [App-E.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771253-App-E.doc)
- [App-D.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771256-App-D.doc)
- [App-C.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771259-App-C.doc)
- [App-B.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771262-App-B.doc)
- [App-A.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771265-App-A.doc)
- [Cover.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771268-Cover.doc)
- [Contents.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771271-Contents.doc)
- [App-K.doc](../../../../.raw/DCSDCS/attachments/13879771185/att13879771274-App-K.doc)
