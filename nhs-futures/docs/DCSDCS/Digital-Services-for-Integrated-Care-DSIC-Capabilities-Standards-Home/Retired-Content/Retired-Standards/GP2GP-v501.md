---
page_id: "14425948161"
space: "DCSDCS"
title: "GP2GP v5.0.1"
version: 1
updated: "2025-10-22T09:57:12.709Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14425948161/GP2GP+v5.0.1"
labels: ["standard_retired"]
---

# GP2GP v5.0.1

|  |  |
| --- | --- |
| ID {#GP2GPv5.0.1-ID} | S43 |
| Version {#GP2GPv5.0.1-Version} | 5.0.1 |
| Type {#GP2GPv5.0.1-Type} | Standard |
| Status {#GP2GPv5.0.1-Status} | Retired |
| Effective Date {#GP2GPv5.0.1-EffectiveDate} | 18 Jul 2025 |
| Contracting Vehicle(s) {#GP2GPv5.0.1-ContractingVehicle(s)} | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) |

- [Introduction](#GP2GPv5.0.1-Introduction)
- [Requirements](#GP2GPv5.0.1-Requirements)
- [Compliance and Assurance](#GP2GPv5.0.1-ComplianceandAssurance)
  - [GP2GP FHIR Implementation](#GP2GPv5.0.1-GP2GPFHIRImplementation)
  - [GP2GP HL7](#GP2GPv5.0.1-GP2GPHL7)
- [Documentation](#GP2GPv5.0.1-Documentation)
  - [GP2GP FHIR Implementation](#GP2GPv5.0.1-GP2GPFHIRImplementation.1)
  - [GP2GP HL7](#GP2GPv5.0.1-GP2GPHL7.1)
- [Dependencies](#GP2GPv5.0.1-Dependencies)
  - [GP2GP FHIR Implementation](#GP2GPv5.0.1-GP2GPFHIRImplementation.2)
  - [GPGP HL7](#GP2GPv5.0.1-GPGPHL7)
- [Roadmap](#GP2GPv5.0.1-Roadmap)

# Introduction {#GP2GPv5.0.1-Introduction}

The GP2GP record transfer mechanism enables an Electronic Patient's Record (EPR) to be electronically transferred directly and securely when they move from one Practice to another.

# Requirements {#GP2GPv5.0.1-Requirements}

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Description** | **Level** |
| Suppliers of Solutions which ARE currently deployed into an operational environment, and have implemented GP2GP HL7. | GP2GP00 {#GP2GPv5.0.1-GP2GP00} | **GP2GP 1.1a**  Suppliers must meet the requirements for GP2GP 1.1a | MUST |
| GP2GP01 {#GP2GPv5.0.1-GP2GP01} | **GP2GP 2.2a**  Suppliers must meet the requirements for GP2GP 2.2a  [HSCIC-PC-BLD-0068 26 GP2…](../../../../attachments/DCSDCS/14425948161/att14425948216-HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf) | MUST |
| GP2GP02 {#GP2GPv5.0.1-GP2GP02} | **Available Documentation**  Suppliers must make available documentation to ensure that suppliers receiving GP2GP messages are fully able to interpret, consume and process the data to minimise data loss and degradation. This must include (but is not limited to):   - Structure of data - Any know issues or anomalies and how they should be handled - Code sets and associated meanings - Field specifications (types, lengths etc.) | MUST |
| GP2GP03 {#GP2GPv5.0.1-GP2GP03} | **Receivers of GP2GP Messages**  Suppliers must provide support to receivers of GP2GP messages to resolve any issues with interpreting, consuming and processing received messages | MUST |
| GP2GP04 {#GP2GPv5.0.1-GP2GP04} | **GP2GP 2.2b**  Suppliers must meet the requirements for GP2GP 2.2b and GP2GP Automatic Integration Specification v1.0  [HSCIC-PC-BLD-0068 26 GP2…](../../../../attachments/DCSDCS/14425948161/att14425948216-HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf)[GP2GP Automatic Integrat…](../../../../attachments/DCSDCS/14425948161/att14425948207-GP2GP Automatic Integration Specification v1.0.pdf) | MUST |
| GP2GP05 {#GP2GPv5.0.1-GP2GP05} | **Management Information**  Suppliers must implement and maintain the GP Registrations Management Information API inline with the latest specification version | MUST |
| - Suppliers of new Solutions (i.e. those which are NOT currently deployed into an operational environment with existing GP2GP compliance). - Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented the GP2GP FHIR Implementation. | GP2GP07 {#GP2GPv5.0.1-GP2GP07} | **GP2GP FHIR Implementation - GP2GP Sending Adaptor**  Implement and maintain the GP2GP Sending Adaptor inline with the latest Standard version | MUST |
| GP2GP08 {#GP2GPv5.0.1-GP2GP08} | **GP2GP FHIR Implementation - GP2GP Requesting Adaptor**  Implement and maintain the GP2GP Requesting Adaptor inline with the latest Standard version | MUST |
| GP2GP09 {#GP2GPv5.0.1-GP2GP09} | **Management Information**  Suppliers must implement and maintain the GP Registrations Management Information API inline with the latest specification version | MUST |

# Compliance and Assurance {#GP2GPv5.0.1-ComplianceandAssurance}

### GP2GP FHIR Implementation {#GP2GPv5.0.1-GP2GPFHIRImplementation}

For Suppliers of new Solutions and Solutions that have implemented the GP2GP FHIR Implementation:

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

### GP2GP HL7 {#GP2GPv5.0.1-GP2GPHL7}

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented GP2GP HL7:

Click here to expand...

The compliance baseline for GP2GP and document locations were correct at the time of original publication, but referenced documents can now be found embedded on this page, below. The exceptions to this are the references to the NHS Messaging Implementation Manual (MIM) and External Interface Specification (EIS) (follow these links for details).

[GP2GP 1.1a Compliance Mo…](../../../../attachments/DCSDCS/14425948161/att14425948288-GP2GP 1.1a Compliance Module.doc)

The GP2GP assurance is split into 2 streams:

1. Compliance testing - this tests the spine messaging patterns and functionality
2. Interoperability Testing - the testing of the clinically semantic testing of the message payload between different systems

For advice and support on assurance please contact businesspartners@nhs.net or visit NHS Business Partners - NHS England.

# Documentation {#GP2GPv5.0.1-Documentation}

### GP2GP FHIR Implementation {#GP2GPv5.0.1-GP2GPFHIRImplementation.1}

For Suppliers of new Solutions and Solutions that have implemented the GP2GP FHIR Implementation:

- API Catalogue - GP2GP Requesting Adaptor
- API Catalogue - GP2GP Sending Adaptor
- GP Registrations Management Information API
- Message Handling System (MHS) Adaptor

### GP2GP HL7 {#GP2GPv5.0.1-GP2GPHL7.1}

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented GP2GP HL7:

Click here to expand...

#### Message Fragments and Examples {#GP2GPv5.0.1-MessageFragmentsandExamples}

[NPFIT-FNT-TO-TIN-0562[1]…](../../../../attachments/DCSDCS/14425948161/att14425948222-NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc)

#### Supplementary specifications {#GP2GPv5.0.1-Supplementaryspecifications}

The following supplemental specifications contain additional requirements and guidance for GP2GP implementation:

[NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-FNT-TO-TIN-1087.02%20GP2GP%20Supplementary%20Specification%20on%20Handling%20Medication%20Discontinuation.pdf?api=v2)

[NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0069%2024%20GP2GP%20Spine%20Technical%20Design%20v7.1.pdf?api=v2)

[NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0083.08%20GP2GP%20Response%20Codes.pdf?api=v2)

[NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0099.04%20GP2GP%20Handling%20Missing%20Attachments.pdf?api=v2)

[NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0132.03%20GP2GP%20Supplementary%20Specification%20on%20Structured%20Degrade%20Handling.pdf?api=v2)

[NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0133.02%20GP2GP%20Supplementary%20Spec%20-%20Handling%20and%20Propagation%20of%20Non%20Consultation%20Data.pdf?api=v2)

[NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0134.05%20GP2GP%20Supplementary%20Specification%20Representing%20PMIP%20Data%20in%20GP2GP%20Messages.pdf?api=v2)

[NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0158%20GP2GP%20Supplementary%20Specification%20Attachment%20References.pdf?api=v2)

[NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0163.02%20Topic%20and%20Category%20Handling%20in%20GP2GP.pdf?api=v2)

[NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0170.03%20GP2GP%20SS%20Handling%20Large%20Messages.pdf?api=v2)

[NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0172.02%20GP2GP%20UC1%20Transfer%20Electronic%20Health%20Record.pdf?api=v2)

[NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0175.03%20GP2GP%20SS%20Handling%20A-B-A%20Transfers%20v1.3.pdf?api=v2)

[NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0177.01%20GP2GP%20SS%20User%20Experience.pdf?api=v2)

[NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0178%2002%20GP2GP%20Coding%20Scheme%20Translation%20v1.1.pdf?api=v2)

[NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0180.02%20GP2GP%20Transfer%20of%20Patient%20Facing%20Service%20Settings%2004.pdf?api=v2)

[NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-181.02%20GP2GP%20Handling%20the%20SCR%20indicator%20v03.pdf?api=v2)

[NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-FNT-TO-IG-DES-0115.01%20Statement%20on%20Data%20Retention%20v1.0.pdf?api=v2)

[NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-FNT-TO-TAR-0017.07%20Compliance%20Requirements%20for%20Patient%20Registration.pdf?api=v2)

[NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134336/NPFIT-FNT-TO-TIN-0289.08%20GP2GP%20Supplementary%20Specification%20on%20Handling%20Attachment%20Types.pdf?api=v2)

# Dependencies {#GP2GPv5.0.1-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface standards:

### GP2GP FHIR Implementation {#GP2GPv5.0.1-GP2GPFHIRImplementation.2}

For Suppliers of new Solutions and Solutions that have implemented the GP2GP FHIR Implementation:

- GP2GP Requesting Adaptor
- GP2GP Sending Adaptor
- Personal Demographics Service (PDS) - using FHIR API
- Spine Directory Service - FHIR API
- GP Connect - Access Record Structured API v1.6.0
- GP Registrations Management Information API

### GPGP HL7 {#GP2GPv5.0.1-GPGPHL7}

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented GP2GP HL7:

Click here to view historical dependencies

Creating a compliant implementation previously required implementing the following dependent interface standards:

- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)

# Roadmap {#GP2GPv5.0.1-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [GP2GP Automatic Integration Specification v1.0.pdf](../../../../attachments/DCSDCS/14425948161/att14425948207-GP2GP Automatic Integration Specification v1.0.pdf)
- [GP2GP%20Automatic%20Integration%20Specification%20v1.0.pdf?version=1&modificationDate=1703173855157&cacheVersion=1&api=v2&viewType=fileMacro](../../../../attachments/DCSDCS/14425948161/att14425948210-GP2GP_20Automatic_20Integration_20Specification_20v1.0.pdf_version_1_modificationDate_1703173855157_cacheVersion_1_api_v2_viewType_fileMacro)
- [HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf](../../../../attachments/DCSDCS/14425948161/att14425948216-HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf)
- [NPFIT-FNT-TO-TIN-0379.03 System Walkthrough and Induction Pack.ppt](../../../../attachments/DCSDCS/14425948161/att14425948219-NPFIT-FNT-TO-TIN-0379.03 System Walkthrough and Induction Pack.ppt)
- [NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc](../../../../attachments/DCSDCS/14425948161/att14425948222-NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc)
- [NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf](../../../../attachments/DCSDCS/14425948161/att14425948225-NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf)
- [NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf](../../../../attachments/DCSDCS/14425948161/att14425948228-NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf)
- [NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf](../../../../attachments/DCSDCS/14425948161/att14425948231-NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf)
- [NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf](../../../../attachments/DCSDCS/14425948161/att14425948234-NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf)
- [NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf](../../../../attachments/DCSDCS/14425948161/att14425948237-NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf)
- [NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf](../../../../attachments/DCSDCS/14425948161/att14425948240-NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf)
- [NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf](../../../../attachments/DCSDCS/14425948161/att14425948243-NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf)
- [NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf](../../../../attachments/DCSDCS/14425948161/att14425948246-NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf)
- [NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf](../../../../attachments/DCSDCS/14425948161/att14425948249-NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf)
- [NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf](../../../../attachments/DCSDCS/14425948161/att14425948252-NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf)
- [NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf](../../../../attachments/DCSDCS/14425948161/att14425948255-NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf)
- [NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf](../../../../attachments/DCSDCS/14425948161/att14425948258-NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf)
- [NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf](../../../../attachments/DCSDCS/14425948161/att14425948261-NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf)
- [NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf](../../../../attachments/DCSDCS/14425948161/att14425948264-NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf)
- [NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf](../../../../attachments/DCSDCS/14425948161/att14425948267-NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf)
- [NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf](../../../../attachments/DCSDCS/14425948161/att14425948270-NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf)
- [NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf](../../../../attachments/DCSDCS/14425948161/att14425948273-NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf)
- [NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf](../../../../attachments/DCSDCS/14425948161/att14425948276-NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf)
- [NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf](../../../../attachments/DCSDCS/14425948161/att14425948279-NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf)
- [NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf](../../../../attachments/DCSDCS/14425948161/att14425948282-NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf)
- [NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf](../../../../attachments/DCSDCS/14425948161/att14425948285-NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf)
- [GP2GP 1.1a Compliance Module.doc](../../../../attachments/DCSDCS/14425948161/att14425948288-GP2GP 1.1a Compliance Module.doc)


> **Warning**: attachment download failed for:
> - HSCIC-PC-BLD-0068%2026%20GP2GP%20R2%202%20Requirements%20Specification%20v7.2.pdf?version=1&modificationDate=1703173844510&cacheVersion=1&api=v2&viewType=fileMacro: no content (HTTP 202, 0 bytes)
