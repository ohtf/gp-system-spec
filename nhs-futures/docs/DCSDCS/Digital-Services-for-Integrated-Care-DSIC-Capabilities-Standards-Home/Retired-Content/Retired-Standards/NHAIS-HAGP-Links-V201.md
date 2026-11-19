---
page_id: "11975327876"
space: "DCSDCS"
title: "NHAIS HA/GP Links V2.0.1"
version: 1
updated: "2022-05-10T13:05:55.195Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11975327876/NHAIS+HA+GP+Links+V2.0.1"
labels: ["interop_standard_retired"]
---

# NHAIS HA/GP Links V2.0.1

|  |  |
| --- | --- |
| ID | S53 |
| Version | 2.0.1 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 31 Aug 2021 |

- [Introduction](#NHAISHA/GPLinksV2.0.1-Introduction)
- [Compliance and Assurance](#NHAISHA/GPLinksV2.0.1-ComplianceandAssurance)
- [Requirements](#NHAISHA/GPLinksV2.0.1-Requirements)
- [Documentation](#NHAISHA/GPLinksV2.0.1-Documentation)
  - [NHAIS Registration GP System Specifications, version 2.0](#NHAISHA/GPLinksV2.0.1-NHAISRegistrationGPSystemSpecifications,version2.0)
  - [NHAIS Registration GP System Specifications Appendix A - K, version 2.0](#NHAISHA/GPLinksV2.0.1-NHAISRegistrationGPSystemSpecificationsAppendixA-K,version2.0)
  - [GP Comms & Messaging Specification, V3.0](#NHAISHA/GPLinksV2.0.1-GPComms&MessagingSpecification,V3.0)
  - [FHSREG Edifact Message Implementation Guidelines, V1.4](#NHAISHA/GPLinksV2.0.1-FHSREGEdifactMessageImplementationGuidelines,V1.4)
  - [Receipt Report Message, V1.3](#NHAISHA/GPLinksV2.0.1-ReceiptReportMessage,V1.3)
- [Roadmap](#NHAISHA/GPLinksV2.0.1-Roadmap)

# Introduction {#NHAISHA/GPLinksV2.0.1-Introduction}

National Health Application and Infrastructure Services (NHAIS) is a system which manages the primary care registration service and supports GP Payments and Cervical Cancer Screening. The system maintains patient registration and their demographic details for England, Wales, Isle of Man and Northern Ireland. NHAIS HA (Health Authority) / GP interfaces allow for the two-way exchange of data covering Registration changes.

# Compliance and Assurance {#NHAISHA/GPLinksV2.0.1-ComplianceandAssurance}

For advice and support on assurance please contact businesspartners@nhs.net or visit https://digital.nhs.uk/services/nhs-business-partners

# Requirements {#NHAISHA/GPLinksV2.0.1-Requirements}

| ID | Requirement | Level |
| --- | --- | --- |
| NH01 | Retransmission of a GP-NHAIS Registration EDIFACT message MUST be solely in response to a request from the receiving organisation: automatic re-transmission is not acceptable. | MUST |
| NH02 | Interchanges carrying NHS Standard EDIFACT GP-NHAIS messages MUST conform to the mandatory requirements specified within the following document:   - 'Interchange Implementation Guidelines for General Practice Systems' | MUST |
| NH03 | The system MUST conform to the general GP-NHAIS messaging specifications contained within the following document:   - ‘General Practitioner System Specification Communications and General System, v4.0’ | MUST |
| NH04 | The system MUST implement the FHSREG message in accordance with the following documents:   - NHAIS Registration GP System Specifications (see attachments below) - FHSREG' EDIFACT Message Implementation Guidelines Version 1.4   (see GP Systems v2 Baseline Index)   - PCRM GP Links requirements | MUST |
| NH05 | The system MUST support communication with at least 4 NHAIS systems per GP Practice at any one time. | MUST |

# Documentation {#NHAISHA/GPLinksV2.0.1-Documentation}

ISB 1558 - 36/97/P23 Revised General Medical Services Central Returns - message implementation guidelines.

### NHAIS Registration GP System Specifications, version 2.0 {#NHAISHA/GPLinksV2.0.1-NHAISRegistrationGPSystemSpecifications,version2.0}

[Cover.doc](../../../../attachments/DCSDCS/11975327876/att11975327947-Cover.doc)[Contents.doc](../../../../attachments/DCSDCS/11975327876/att11975327950-Contents.doc)[GP Spec Chapter1.doc](../../../../attachments/DCSDCS/11975327876/att11975327896-GP Spec Chapter1.doc)[GP Spec Chapter2.doc](../../../../attachments/DCSDCS/11975327876/att11975327893-GP Spec Chapter2.doc)[GP Spec Chapter3.doc](../../../../attachments/DCSDCS/11975327876/att11975327899-GP Spec Chapter3.doc)[GP Spec Chapter4.doc](../../../../attachments/DCSDCS/11975327876/att11975327902-GP Spec Chapter4.doc)

### NHAIS Registration GP System Specifications Appendix A - K, version 2.0 {#NHAISHA/GPLinksV2.0.1-NHAISRegistrationGPSystemSpecificationsAppendixA-K,version2.0}

[App-A.doc](../../../../attachments/DCSDCS/11975327876/att11975327944-App-A.doc)[App-B.doc](../../../../attachments/DCSDCS/11975327876/att11975327941-App-B.doc)[App-C.doc](../../../../attachments/DCSDCS/11975327876/att11975327938-App-C.doc)[App-D.doc](../../../../attachments/DCSDCS/11975327876/att11975327935-App-D.doc)[App-E.doc](../../../../attachments/DCSDCS/11975327876/att11975327932-App-E.doc)[App-F.doc](../../../../attachments/DCSDCS/11975327876/att11975327929-App-F.doc)

[App-G.doc](../../../../attachments/DCSDCS/11975327876/att11975327926-App-G.doc)[App-H.doc](../../../../attachments/DCSDCS/11975327876/att11975327923-App-H.doc)[App-I.doc](../../../../attachments/DCSDCS/11975327876/att11975327920-App-I.doc)[App-J.doc](../../../../attachments/DCSDCS/11975327876/att11975327917-App-J.doc)[App-K.doc](../../../../attachments/DCSDCS/11975327876/att11975327953-App-K.doc)

### GP Comms & Messaging Specification, V3.0 {#NHAISHA/GPLinksV2.0.1-GPComms&MessagingSpecification,V3.0}

[comspec3.doc](../../../../attachments/DCSDCS/11975327876/att11975327911-comspec3.doc)

### FHSREG Edifact Message Implementation Guidelines, V1.4 {#NHAISHA/GPLinksV2.0.1-FHSREGEdifactMessageImplementationGuidelines,V1.4}

[FHSREG v14.doc](../../../../attachments/DCSDCS/11975327876/att11975327908-FHSREG v14.doc)

### Receipt Report Message, V1.3 {#NHAISHA/GPLinksV2.0.1-ReceiptReportMessage,V1.3}

[Recep13.doc](../../../../attachments/DCSDCS/11975327876/att11975327905-Recep13.doc)

Read the Guide to NHAIS/GP Links Documentation to better understand how to digest some of the documents listed on this page.

# Roadmap {#NHAISHA/GPLinksV2.0.1-Roadmap}

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [GP Spec Chapter2.doc](../../../../attachments/DCSDCS/11975327876/att11975327893-GP Spec Chapter2.doc)
- [GP Spec Chapter1.doc](../../../../attachments/DCSDCS/11975327876/att11975327896-GP Spec Chapter1.doc)
- [GP Spec Chapter3.doc](../../../../attachments/DCSDCS/11975327876/att11975327899-GP Spec Chapter3.doc)
- [GP Spec Chapter4.doc](../../../../attachments/DCSDCS/11975327876/att11975327902-GP Spec Chapter4.doc)
- [Recep13.doc](../../../../attachments/DCSDCS/11975327876/att11975327905-Recep13.doc)
- [FHSREG v14.doc](../../../../attachments/DCSDCS/11975327876/att11975327908-FHSREG v14.doc)
- [comspec3.doc](../../../../attachments/DCSDCS/11975327876/att11975327911-comspec3.doc)
- [FHSREG' EDIFACT Message Implementation Guidelines Version 1.4](../../../../attachments/DCSDCS/11975327876/att11975327914-FHSREG' EDIFACT Message Implementation Guidelines Version 1.4)
- [App-J.doc](../../../../attachments/DCSDCS/11975327876/att11975327917-App-J.doc)
- [App-I.doc](../../../../attachments/DCSDCS/11975327876/att11975327920-App-I.doc)
- [App-H.doc](../../../../attachments/DCSDCS/11975327876/att11975327923-App-H.doc)
- [App-G.doc](../../../../attachments/DCSDCS/11975327876/att11975327926-App-G.doc)
- [App-F.doc](../../../../attachments/DCSDCS/11975327876/att11975327929-App-F.doc)
- [App-E.doc](../../../../attachments/DCSDCS/11975327876/att11975327932-App-E.doc)
- [App-D.doc](../../../../attachments/DCSDCS/11975327876/att11975327935-App-D.doc)
- [App-C.doc](../../../../attachments/DCSDCS/11975327876/att11975327938-App-C.doc)
- [App-B.doc](../../../../attachments/DCSDCS/11975327876/att11975327941-App-B.doc)
- [App-A.doc](../../../../attachments/DCSDCS/11975327876/att11975327944-App-A.doc)
- [Cover.doc](../../../../attachments/DCSDCS/11975327876/att11975327947-Cover.doc)
- [Contents.doc](../../../../attachments/DCSDCS/11975327876/att11975327950-Contents.doc)
- [App-K.doc](../../../../attachments/DCSDCS/11975327876/att11975327953-App-K.doc)
