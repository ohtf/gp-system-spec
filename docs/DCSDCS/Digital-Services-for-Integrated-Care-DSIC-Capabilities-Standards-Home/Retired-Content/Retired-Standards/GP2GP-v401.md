---
page_id: "12816154707"
space: "DCSDCS"
title: "GP2GP v4.0.1"
version: 1
updated: "2024-03-04T11:35:14.903Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12816154707/GP2GP+v4.0.1"
labels: ["interop_standard_retired"]
---

# GP2GP v4.0.1

|  |  |
| --- | --- |
| ID | S43 |
| Version | 4.0.1 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 21 Aug 2023 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

/\*<![CDATA[\*/
div.rbtoc1785510557795 {padding: 0px;}
div.rbtoc1785510557795 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785510557795 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#GP2GPv4.0.1-Introduction)
- [Requirements](#GP2GPv4.0.1-Requirements)
- [Documentation](#GP2GPv4.0.1-Documentation)
  - [GP2GP FHIR Implementation](#GP2GPv4.0.1-GP2GPFHIRImplementation)
  - [GP2GP HL7](#GP2GPv4.0.1-GP2GPHL7)
- [Compliance and Assurance](#GP2GPv4.0.1-ComplianceandAssurance)
  - [GP2GP FHIR Implementation](#GP2GPv4.0.1-GP2GPFHIRImplementation.1)
  - [GP2GP HL7](#GP2GPv4.0.1-GP2GPHL7.1)
- [Dependencies](#GP2GPv4.0.1-Dependencies)
  - [GP2GP FHIR Implementation](#GP2GPv4.0.1-GP2GPFHIRImplementation.2)
  - [GP2GP HL7](#GP2GPv4.0.1-GP2GPHL7.2)
- [Roadmap](#GP2GPv4.0.1-Roadmap)

# Introduction

The GP2GP record transfer mechanism enables an Electronic Patient's Record (EPR) to be electronically transferred directly and securely when they move from one Practice to another.

# Requirements

| Applicable Suppliers | ID | Description | Level |
| --- | --- | --- | --- |
| Suppliers of services which ARE currently deployed into an operational environment, and have existing GP2GP compliance. | GP2GP00 | **GP2GP 1.1a**  Suppliers must meet the requirements for GP2GP 1.1a | MUST |
| GP2GP01 | **GP2GP 2.2a**  Suppliers must meet the requirements for GP2GP 2.2a  [HSCIC-PC-BLD-0068 26 GP2…](GP2GP-v401.md) | MUST |
| GP2GP02 | **Available Documentation**  Suppliers must make available documentation to ensure that suppliers receiving GP2GP messages are fully able to interpret, consume and process the data to minimise data loss and degradation. This must include (but is not limited to):   - Structure of data - Any know issues or anomalies and how they should be handled - Code sets and associated meanings - Field specifications (types, lengths etc.) | MUST |
| GP2GP03 | **Receivers of GP2GP Messages**  Suppliers must provide support to receivers of GP2GP messages to resolve any issues with interpreting, consuming and processing received messages | MUST |
| GP2GP04 | **GP2GP 2.2b**  Suppliers must meet the requirements for GP2GP 2.2b  [HSCIC-PC-BLD-0068 26 GP2…](GP2GP-v401.md) | MUST |
| GP2GP05 | **Management Information**  Suppliers must implement and maintain the GP Registrations Management Information API inline with the latest specification version | MUST |
| Suppliers of new services or applications (i.e. those which are NOT currently deployed into an operational environment with existing GP2GPs compliance). | GP2GP07 | **GP2GP FHIR Implementation - GP2GP Sending Adaptor**  Implement and maintain the GP2GP Sending Adaptor inline with the latest Standard version | MUST |
| GP2GP08 | **GP2GP FHIR Implementation - GP2GP Requesting Adaptor**  Implement and maintain the GP2GP Requesting Adaptor inline with the latest Standard version | MUST |
| GP2GP09 | **Management Information**  Suppliers must implement and maintain the GP Registrations Management Information API inline with the latest specification version | MUST |

# Documentation

### GP2GP FHIR Implementation

For Suppliers of new services or applications:

- API Catalogue - GP2GP Requesting Adaptor
- API Catalogue - GP2GP Sending Adaptor
- GP Registrations Management Information API
- Message Handling System (MHS) Adaptor

### GP2GP HL7

For Suppliers of services which ARE currently deployed into an operational environment:

![](https://nhse-dsic.atlassian.net/wiki/images/icons/grey_arrow_down.png)Click here to expand...

#### Message Fragments and Examples

[NPFIT-FNT-TO-TIN-0562[1]…](GP2GP-v401.md)

#### Supplementary specifications

The following supplemental specifications contain additional requirements and guidance for GP2GP implementation:

[NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-FNT-TO-TIN-1087.02%20GP2GP%20Supplementary%20Specification%20on%20Handling%20Medication%20Discontinuation.pdf?version=1&modificationDate=1666084002918&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0069%2024%20GP2GP%20Spine%20Technical%20Design%20v7.1.pdf?version=1&modificationDate=1666084003135&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0083.08%20GP2GP%20Response%20Codes.pdf?version=1&modificationDate=1666084003329&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0099.04%20GP2GP%20Handling%20Missing%20Attachments.pdf?version=1&modificationDate=1666084003532&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0132.03%20GP2GP%20Supplementary%20Specification%20on%20Structured%20Degrade%20Handling.pdf?version=1&modificationDate=1666084003727&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0133.02%20GP2GP%20Supplementary%20Spec%20-%20Handling%20and%20Propagation%20of%20Non%20Consultation%20Data.pdf?version=1&modificationDate=1666084003930&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0134.05%20GP2GP%20Supplementary%20Specification%20Representing%20PMIP%20Data%20in%20GP2GP%20Messages.pdf?version=1&modificationDate=1666084004143&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0158%20GP2GP%20Supplementary%20Specification%20Attachment%20References.pdf?version=1&modificationDate=1666084004380&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0163.02%20Topic%20and%20Category%20Handling%20in%20GP2GP.pdf?version=1&modificationDate=1666084004581&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0170.03%20GP2GP%20SS%20Handling%20Large%20Messages.pdf?version=1&modificationDate=1666084004784&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0172.02%20GP2GP%20UC1%20Transfer%20Electronic%20Health%20Record.pdf?version=1&modificationDate=1666084005197&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0175.03%20GP2GP%20SS%20Handling%20A-B-A%20Transfers%20v1.3.pdf?version=1&modificationDate=1666084005612&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0177.01%20GP2GP%20SS%20User%20Experience.pdf?version=1&modificationDate=1666084005810&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0178%2002%20GP2GP%20Coding%20Scheme%20Translation%20v1.1.pdf?version=1&modificationDate=1666084006002&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-0180.02%20GP2GP%20Transfer%20of%20Patient%20Facing%20Service%20Settings%2004.pdf?version=1&modificationDate=1666084006253&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-PC-BLD-181.02%20GP2GP%20Handling%20the%20SCR%20indicator%20v03.pdf?version=1&modificationDate=1666084006465&cacheVersion=1&api=v2)

[NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-FNT-TO-IG-DES-0115.01%20Statement%20on%20Data%20Retention%20v1.0.pdf?version=1&modificationDate=1666084006689&cacheVersion=1&api=v2)

[NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-FNT-TO-TAR-0017.07%20Compliance%20Requirements%20for%20Patient%20Registration.pdf?version=1&modificationDate=1666084006883&cacheVersion=1&api=v2)

[NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/12167151617/NPFIT-FNT-TO-TIN-0289.08%20GP2GP%20Supplementary%20Specification%20on%20Handling%20Attachment%20Types.pdf?version=1&modificationDate=1666084007082&cacheVersion=1&api=v2)

# Compliance and Assurance

### GP2GP FHIR Implementation

For Suppliers of new services or applications:

A risk-based assurance to be followed by all New Foundation Solution Suppliers (NFSS).

- **Technical Assurance** - The Suppliers need to demonstrate that the GP2GP Sending Adapter and GP2GP Requesting Adaptor are successfully integrated and technically assured through a specific set of Technical risks.
- **E2E Solution Assurance** - The Suppliers need to demonstrate that the GP2GP FHIR Implementation Solution meets the E2E functional interoperability requirements through a set of Clinical and Technical risks covering the below high-level scenarios:
  - NFSS as a winning Practice
  - NFSS as losing Practice
  - Pathways assurance from NFSS to Incumbent Solutions
  - Pathways assurance from Incumbents to NFSS Solutions
  - Export of data from NFSS Solutions

Suppliers must contact Solution Assurance team through the Tech Innovation mailbox (gpit.techinnovation@nhs.net) to arrange a witness testing slot to provide evidence. Successful completion of the witness testing and evidencing will constitute compliance against this Roadmap Item.

An Assurance Statement will be provided when a supplier completes their testing and assurance related activities. The report will be used as the readiness for further onboarding stages and progression to Live assurance.

### GP2GP HL7

For Suppliers of services which ARE currently deployed into an operational environment:

![](https://nhse-dsic.atlassian.net/wiki/images/icons/grey_arrow_down.png)Click here to expand...

The compliance baseline for GP2GP and document locations were correct at the time of original publication, but referenced documents can now be found embedded on this page, below. The exceptions to this are the references to the NHS Messaging Implementation Manual (MIM) and External Interface Specification (EIS) (follow these links for details).

[GP2GP 1.1a Compliance Mo…](GP2GP-v401.md)

The GP2GP assurance is split into 2 streams:

1. Compliance testing - this tests the spine messaging patterns and functionality
2. Interoperability Testing - the testing of the clinically semantic testing of the message payload between different systems

For advice and support on assurance please contact businesspartners@nhs.net or visit https://digital.nhs.uk/services/nhs-business-partners

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

### GP2GP FHIR Implementation

For Suppliers of new services or applications:

- GP2GP Requesting Adaptor
- GP2GP Sending Adaptor
- Personal Demographics Service (PDS) - using FHIR API
- Spine Directory Service - FHIR API
- GP Connect - Access Record Structured API v1.6.0
- GP Registrations Management Information API

### GP2GP HL7

For Suppliers of services which ARE currently deployed into an operational environment:

![](https://nhse-dsic.atlassian.net/wiki/images/icons/grey_arrow_down.png)Click here to view historical dependencies

Creating a compliant implementation previously required implementing the following dependent interface standards:

- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)

# Roadmap

| Title |
| --- |
| No content found. |

## Attachments

- [HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154751-HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf)
- [NPFIT-FNT-TO-TIN-0379.03 System Walkthrough and Induction Pack.ppt](../../../../.raw/DCSDCS/attachments/12816154707/att12816154754-NPFIT-FNT-TO-TIN-0379.03 System Walkthrough and Induction Pack.ppt)
- [NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc](../../../../.raw/DCSDCS/attachments/12816154707/att12816154757-NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc)
- [NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154760-NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf)
- [NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154763-NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf)
- [NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154766-NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf)
- [NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154769-NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf)
- [NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154772-NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf)
- [NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154775-NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf)
- [NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154778-NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf)
- [NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154781-NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf)
- [NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154784-NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf)
- [NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154787-NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf)
- [NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154790-NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf)
- [NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154793-NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf)
- [NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154796-NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf)
- [NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154799-NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf)
- [NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154802-NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf)
- [NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154805-NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf)
- [NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154808-NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf)
- [NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154811-NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf)
- [NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154814-NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf)
- [NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154817-NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf)
- [NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf](../../../../.raw/DCSDCS/attachments/12816154707/att12816154820-NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf)
- [GP2GP 1.1a Compliance Module.doc](../../../../.raw/DCSDCS/attachments/12816154707/att12816154823-GP2GP 1.1a Compliance Module.doc)
