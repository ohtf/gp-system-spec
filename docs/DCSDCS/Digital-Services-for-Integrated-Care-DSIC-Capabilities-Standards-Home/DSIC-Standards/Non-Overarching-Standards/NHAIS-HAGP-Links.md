---
page_id: "1391133619"
space: "DCSDCS"
title: "NHAIS HA/GP Links"
version: 19
updated: "2026-07-22T13:05:54.381Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133619/NHAIS+HA+GP+Links"
labels: ["standard"]
---

# NHAIS HA/GP Links

|  |  |
| --- | --- |
| **ID** | S53 |
| **Version** | 2.0.4 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

/\*<![CDATA[\*/
div.rbtoc1785497495180 {padding: 0px;}
div.rbtoc1785497495180 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785497495180 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#NHAISHA/GPLinks-Introduction)
- [Requirements](#NHAISHA/GPLinks-Requirements)
  - [Using NHAIS GP Links Adaptor](#NHAISHA/GPLinks-UsingNHAISGPLinksAdaptor)
  - [Without Using NHAIS GP Links Adaptor](#NHAISHA/GPLinks-WithoutUsingNHAISGPLinksAdaptor)
- [Compliance, Assurance and Testing](#NHAISHA/GPLinks-Compliance,AssuranceandTesting)
- [Documentation](#NHAISHA/GPLinks-Documentation)
  - [Using NHAIS GP Links Adaptor](#NHAISHA/GPLinks-UsingNHAISGPLinksAdaptor.1)
  - [Without Using NHAIS GP Links Adaptor](#NHAISHA/GPLinks-WithoutUsingNHAISGPLinksAdaptor.1)
- [Dependencies](#NHAISHA/GPLinks-Dependencies)
  - [Using NHAIS GP Links Adaptor](#NHAISHA/GPLinks-UsingNHAISGPLinksAdaptor.2)
- [Roadmap](#NHAISHA/GPLinks-Roadmap)

# Introduction

National Health Application and Infrastructure Services (NHAIS) is a system which manages the primary care registration service and supports GP payments and cervical cancer screening. The system maintains Patient registration and their demographic details for England, Wales, Isle of Man and Northern Ireland. NHAIS HA (Health Authority) / GP interfaces allow for the two-way exchange of data covering registration changes.

# Requirements

To comply with the NHAIS HA/GP Links Standard there are currently two implementation options:

1. Using NHAIS GP Links adaptor
2. Without using NHAIS GP Links adaptor

### Using NHAIS GP Links Adaptor

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| **NH06** | If implementing NHAIS HA/GP Links using the NHAIS GP Links adaptor:   - Suppliers to implement and maintain the adapter inline with the latest specification of the [NHAIS GP Links adaptor](https://digital.nhs.uk/developer/api-catalogue/nhais-gp-links/nhais-gp-links-adaptor) and the [PCRM GP Links Requirements](https://nhse-dsic.atlassian.net/wiki/download/attachments/13659570177/PCRM%20Requirements%20for%20NMEs%20including%20additional%20clarification%20and%20guidance.xlsx?api=v2)   The adaptor provides a pre-assured implementation of the NHAIS/GP Links Standard and covers the requirements below. | MUST |

### Without Using NHAIS GP Links Adaptor

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| **NH01** | Retransmission of a GP-NHAIS Registration EDIFACT message MUST be solely in response to a request from the receiving organisation: automatic re-transmission is not acceptable. | MUST |
| **NH02** | Interchanges carrying NHS Standard EDIFACT GP-NHAIS messages MUST conform to the mandatory requirements specified within the following document:   - 'Interchange Implementation Guidelines for General Practice Systems' | MUST |
| **NH03** | The system MUST conform to the general GP-NHAIS messaging specifications contained within the following document:   - ‘General Practitioner System Specification Communications and General System, v4.0’ | MUST |
| **NH04** | The system MUST implement the FHSREG message in accordance with the following documents:   - NHAIS Registration GP System Specifications (see attachments below) - [FHSREG EDIFACT Message Implementation Guidelines Version 1.4](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133619/FHSREG%27%20EDIFACT%20Message%20Implementation%20Guidelines%20Version%201.4?version=1&modificationDate=1528885394317&cacheVersion=1&api=v2)   (see GP Systems v2 Baseline Index)   - [PCRM GP Links Requirements](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133619/PCRM%20Requirements_171219%20(10).xlsx?version=1&modificationDate=1654085853323&cacheVersion=1&api=v2) | MUST |
| **NH05** | The system MUST support communication with at least 4 NHAIS systems per GP Practice at any one time. | MUST |

# Compliance, Assurance and Testing

See the NHAIS HA / GP Links (Primary Care Registration Management (PCRM)) section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

### Using NHAIS GP Links Adaptor

For Suppliers of new Services or applications:

- [API Catalogue - NHAIS GP Links adaptor](https://digital.nhs.uk/developer/api-catalogue/nhais-gp-links/nhais-gp-links-adaptor)
- [Solution Assurance - Assurance Approach for New Market Entrants Integration with NHAIS](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133619/SA%20Assurance%20Approach%20for%20New%20Market%20Entrants%20Integration%20with%20NHAIS%20v0.41.docx?api=v2)
- [GP software developer guide](https://digital.nhs.uk/developer/guides-and-documentation/building-healthcare-software/general-practice/integrating-with-national-services)

It is recommended to read GP software developer guide in conjunction with the adaptor documentation

### Without Using NHAIS GP Links Adaptor

[ISB 1558 - 36/97/P23 Revised General Medical Services Central Returns](https://webarchive.nationalarchives.gov.uk/20150107150141/http://www.isb.nhs.uk/documents/isb-1558/36-97-p23) - message implementation guidelines.

#### NHAIS Registration GP System Specifications, version 2.0

[Cover.doc](NHAIS-HAGP-Links.md)

[Contents.doc](NHAIS-HAGP-Links.md)

[GP Spec Chapter1.doc](NHAIS-HAGP-Links.md)

[GP Spec Chapter2.doc](NHAIS-HAGP-Links.md)

[GP Spec Chapter3.doc](NHAIS-HAGP-Links.md)

[GP Spec Chapter4.doc](NHAIS-HAGP-Links.md)

#### NHAIS Registration GP System Specifications Appendix A - K, version 2.0

[App-A.doc](NHAIS-HAGP-Links.md)

[App-B.doc](NHAIS-HAGP-Links.md)

[App-C.doc](NHAIS-HAGP-Links.md)

[App-D.doc](NHAIS-HAGP-Links.md)

[App-E.doc](NHAIS-HAGP-Links.md)

[App-F.doc](NHAIS-HAGP-Links.md)

[App-G.doc](NHAIS-HAGP-Links.md)

[App-H.doc](NHAIS-HAGP-Links.md)

[App-I.doc](NHAIS-HAGP-Links.md)

[App-J.doc](NHAIS-HAGP-Links.md)

[App-K.doc](NHAIS-HAGP-Links.md)

#### GP Comms & Messaging Specification, V3.0

[comspec3.doc](NHAIS-HAGP-Links.md)

#### FHSREG Edifact Message Implementation Guidelines, V1.4

[FHSREG v14.doc](NHAIS-HAGP-Links.md)

#### Receipt Report Message, V1.3

[Recep13.doc](NHAIS-HAGP-Links.md)

Read the [Guide to NHAIS/GP Links Documentation](https://developer.nhs.uk/library/systems/nhais/guide-to-nhais-gp-links-documentation/) to better understand how to digest some of the documents listed on this page.

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

### Using NHAIS GP Links Adaptor

Creating a compliant implementation requires:

MESH mailbox but [MESH](Messaging-Exchange-for-Social-Care-and-Health-MESH.md) is implemented with adaptor

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [App-F.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391139248-App-F.doc)
- [Cover.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391139256-Cover.doc)
- [App-J.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391139290-App-J.doc)
- [App-D.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391142747-App-D.doc)
- [App-A.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391142753-App-A.doc)
- [App-E.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391142758-App-E.doc)
- [App-G.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391142760-App-G.doc)
- [Contents.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391142761-Contents.doc)
- [App-H.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391142764-App-H.doc)
- [App-K.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391142834-App-K.doc)
- [App-B.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391142835-App-B.doc)
- [App-C.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391142841-App-C.doc)
- [App-I.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391142843-App-I.doc)
- [GP Spec Chapter3.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391149571-GP Spec Chapter3.doc)
- [GP Spec Chapter4.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391149578-GP Spec Chapter4.doc)
- [GP Spec Chapter1.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391149583-GP Spec Chapter1.doc)
- [GP Spec Chapter2.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391149647-GP Spec Chapter2.doc)
- [FHSREG' EDIFACT Message Implementation Guidelines Version 1.4](../../../../.raw/DCSDCS/attachments/1391133619/att1391154816-FHSREG' EDIFACT Message Implementation Guidelines Version 1.4)
- [comspec3.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391159583-comspec3.doc)
- [Recep13.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391160708-Recep13.doc)
- [FHSREG v14.doc](../../../../.raw/DCSDCS/attachments/1391133619/att1391160713-FHSREG v14.doc)
- [PCRM Requirements_171219 (10).xlsx](../../../../.raw/DCSDCS/attachments/1391133619/att11999510603-PCRM Requirements_171219 (10).xlsx)
- [SA Assurance Approach for New Market Entrants Integration with NHAIS v0.41.docx](../../../../.raw/DCSDCS/attachments/1391133619/att13189218317-SA Assurance Approach for New Market Entrants Integration with NHAIS v0.41.docx)
