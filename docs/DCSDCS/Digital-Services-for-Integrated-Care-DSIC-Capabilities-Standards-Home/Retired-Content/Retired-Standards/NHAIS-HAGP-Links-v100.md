---
page_id: "11747197328"
space: "DCSDCS"
title: "NHAIS HA/GP Links v1.0.0"
version: 1
updated: "2021-11-08T12:47:05.728Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11747197328/NHAIS+HA+GP+Links+v1.0.0"
labels: ["interop_standard_retired"]
---

# NHAIS HA/GP Links v1.0.0

|  |  |
| --- | --- |
| ID | S53 |
| Version | 1.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

/\*<![CDATA[\*/
div.rbtoc1785509410309 {padding: 0px;}
div.rbtoc1785509410309 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785509410309 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#NHAISHA/GPLinksv1.0.0-Introduction)
- [Compliance and Assurance](#NHAISHA/GPLinksv1.0.0-ComplianceandAssurance)
- [Requirements](#NHAISHA/GPLinksv1.0.0-Requirements)
- [Documentation](#NHAISHA/GPLinksv1.0.0-Documentation)
  - [NHAIS Registration GP System Specifications, version 2.0](#NHAISHA/GPLinksv1.0.0-NHAISRegistrationGPSystemSpecifications,version2.0)
  - [NHAIS Registration GP System Specifications Appendix A - K, version 2.0](#NHAISHA/GPLinksv1.0.0-NHAISRegistrationGPSystemSpecificationsAppendixA-K,version2.0)
  - [GP Comms & Messaging Specification, V3.0](#NHAISHA/GPLinksv1.0.0-GPComms&MessagingSpecification,V3.0)
  - [FHSREG Edifact Message Implementation Guidelines, V1.4](#NHAISHA/GPLinksv1.0.0-FHSREGEdifactMessageImplementationGuidelines,V1.4)
  - [Receipt Report Message, V1.3](#NHAISHA/GPLinksv1.0.0-ReceiptReportMessage,V1.3)
- [Roadmap](#NHAISHA/GPLinksv1.0.0-Roadmap)

# Introduction

National Health Application and Infrastructure Services (NHAIS) is a system which manages the primary care registration service and supports GP Payments and Cervical Cancer Screening. The system maintains patient registration and their demographic details for England, Wales, Isle of Man and Northern Ireland. NHAIS HA (Health Authority) / GP interfaces allow for the two-way exchange of data covering Registration changes.

# Compliance and Assurance

For advice and support on assurance please contact businesspartners@nhs.net or visit https://digital.nhs.uk/services/nhs-business-partners

# Requirements

Note that in addition to the requirements below, additional requirements relating to the recording of data and triggering of transactions are contained in Patient Information Maintenance - Standard

| ID | Requirement | Level |
| --- | --- | --- |
| NH01 | Retransmission of a GP-NHAIS Registration EDIFACT message MUST be solely in response to a request from the receiving organisation: automatic re-transmission is not acceptable. | MUST |
| NH02 | Interchanges carrying NHS Standard EDIFACT GP-NHAIS messages MUST conform to the mandatory requirements specified within the following document:   - 'Interchange Implementation Guidelines for General Practice Systems' | MUST |
| NH03 | The system MUST conform to the general GP-NHAIS messaging specifications contained within the following document:   - ‘General Practitioner System Specification Communications and General System, v4.0’ | MUST |
| NH04 | The system MUST implement the FHSREG message in accordance with the following documents:   - NHAIS Registration GP System Specifications (see attachments below) - FHSREG' EDIFACT Message Implementation Guidelines Version 1.4  (see GP Systems v2 Baseline Index) | MUST |
| NH05 | The system MUST support communication with at least 4 NHAIS systems per GP Practice at any one time. | MUST |

# Documentation

ISB 1558 - 36/97/P23 Revised General Medical Services Central Returns - message implementation guidelines.

### NHAIS Registration GP System Specifications, version 2.0

[Cover.doc](NHAIS-HAGP-Links-v100.md)[Contents.doc](NHAIS-HAGP-Links-v100.md)[GP Spec Chapter1.doc](NHAIS-HAGP-Links-v100.md)[GP Spec Chapter2.doc](NHAIS-HAGP-Links-v100.md)[GP Spec Chapter3.doc](NHAIS-HAGP-Links-v100.md)[GP Spec Chapter4.doc](NHAIS-HAGP-Links-v100.md)

### NHAIS Registration GP System Specifications Appendix A - K, version 2.0

[App-A.doc](NHAIS-HAGP-Links-v100.md)[App-B.doc](NHAIS-HAGP-Links-v100.md)[App-C.doc](NHAIS-HAGP-Links-v100.md)[App-D.doc](NHAIS-HAGP-Links-v100.md)[App-E.doc](NHAIS-HAGP-Links-v100.md)[App-F.doc](NHAIS-HAGP-Links-v100.md)

[App-G.doc](NHAIS-HAGP-Links-v100.md)[App-H.doc](NHAIS-HAGP-Links-v100.md)[App-I.doc](NHAIS-HAGP-Links-v100.md)[App-J.doc](NHAIS-HAGP-Links-v100.md)[App-K.doc](NHAIS-HAGP-Links-v100.md)

### GP Comms & Messaging Specification, V3.0

[comspec3.doc](NHAIS-HAGP-Links-v100.md)

### FHSREG Edifact Message Implementation Guidelines, V1.4

[FHSREG v14.doc](NHAIS-HAGP-Links-v100.md)

### Receipt Report Message, V1.3

[Recep13.doc](NHAIS-HAGP-Links-v100.md)

Read the Guide to NHAIS/GP Links Documentation to better understand how to digest some of the documents listed on this page.

# Roadmap

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [GP Spec Chapter2.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197346-GP Spec Chapter2.doc)
- [GP Spec Chapter1.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197349-GP Spec Chapter1.doc)
- [GP Spec Chapter3.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197352-GP Spec Chapter3.doc)
- [GP Spec Chapter4.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197355-GP Spec Chapter4.doc)
- [Recep13.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197358-Recep13.doc)
- [FHSREG v14.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197361-FHSREG v14.doc)
- [comspec3.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197364-comspec3.doc)
- [FHSREG' EDIFACT Message Implementation Guidelines Version 1.4](../../../../.raw/DCSDCS/attachments/11747197328/att11747197367-FHSREG' EDIFACT Message Implementation Guidelines Version 1.4)
- [App-J.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197370-App-J.doc)
- [App-I.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197373-App-I.doc)
- [App-H.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197376-App-H.doc)
- [App-G.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197379-App-G.doc)
- [App-F.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197382-App-F.doc)
- [App-E.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197385-App-E.doc)
- [App-D.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197388-App-D.doc)
- [App-C.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197391-App-C.doc)
- [App-B.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197394-App-B.doc)
- [App-A.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197397-App-A.doc)
- [Cover.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197400-Cover.doc)
- [Contents.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197403-Contents.doc)
- [App-K.doc](../../../../.raw/DCSDCS/attachments/11747197328/att11747197406-App-K.doc)
