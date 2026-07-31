---
page_id: "1391134336"
space: "DCSDCS"
title: "GP2GP"
version: 23
updated: "2026-07-22T08:01:31.968Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391134336/GP2GP"
labels: ["standard"]
---

# GP2GP

|  |  |
| --- | --- |
| **ID** | S43 |
| **Version** | 6.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

/\*<![CDATA[\*/
div.rbtoc1785498433822 {padding: 0px;}
div.rbtoc1785498433822 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785498433822 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#GP2GP-Introduction)
- [Requirements](#GP2GP-Requirements)
- [Compliance and Assurance](#GP2GP-ComplianceandAssurance)
  - [GP2GP FHIR Implementation](#GP2GP-GP2GPFHIRImplementation)
  - [GP2GP HL7](#GP2GP-GP2GPHL7)
- [Documentation](#GP2GP-Documentation)
  - [GP2GP FHIR Implementation](#GP2GP-GP2GPFHIRImplementation.1)
  - [GP2GP HL7](#GP2GP-GP2GPHL7.1)
- [Dependencies](#GP2GP-Dependencies)
  - [GP2GP FHIR Implementation](#GP2GP-GP2GPFHIRImplementation.2)
  - [GPGP HL7](#GP2GP-GPGPHL7)
- [Roadmap](#GP2GP-Roadmap)

# Introduction

The GP2GP record transfer mechanism enables an Electronic Patient's Record (EPR) to be electronically transferred directly and securely when they move from one Practice to another.

# Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Description** | **Level** |
| Suppliers of Solutions which ARE currently deployed into an operational environment, and have implemented GP2GP HL7. | **GP2GP00** | **GP2GP 1.1a**  Suppliers must meet the requirements for GP2GP 1.1a | MUST |
| **GP2GP01** | **GP2GP 2.2a**  Suppliers must meet the requirements for GP2GP 2.2a  [HSCIC-PC-BLD-0068 26 GP2…](GP2GP.md) | MUST |
| **GP2GP02** | **Available Documentation**  Suppliers must make available documentation to ensure that suppliers receiving GP2GP messages are fully able to interpret, consume and process the data to minimise data loss and degradation. This must include (but is not limited to):   - Structure of data - Any know issues or anomalies and how they should be handled - Code sets and associated meanings - Field specifications (types, lengths etc.) | MUST |
| **GP2GP03** | **Receivers of GP2GP Messages**  Suppliers must provide support to receivers of GP2GP messages to resolve any issues with interpreting, consuming and processing received messages | MUST |
| **GP2GP04** | **GP2GP 2.2b**  Suppliers must meet the requirements for GP2GP 2.2b and GP2GP Automatic Integration Specification v1.0  [HSCIC-PC-BLD-0068 26 GP2…](GP2GP.md)[GP2GP Automatic Integrat…](GP2GP.md) | MUST |
| **GP2GP05** | **Management Information**  Suppliers must implement and maintain the [GP Registrations Management Information API](https://digital.nhs.uk/developer/api-catalogue/gp-registrations-management-information) inline with the latest specification version | MUST |
| **GP2GP06** | Suppliers must meet the requirements for GP2GP Redactions v1.01  [GP2GPRedactions\_MIMDesig…](GP2GP.md)  The new Schema definition file to be consistent with the following Schema version:   - [RCMR\_IN030000UK07.xsd](GP2GP.md) - [RCMR\_MT030101UK05.xsd](GP2GP.md) - [RCMR\_EX030101UK05.xml](GP2GP.md) | MUST |
| - Suppliers of new Solutions (i.e. those which are NOT currently deployed into an operational environment with existing GP2GP compliance). - Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented the GP2GP FHIR Implementation. | **GP2GP07** | **GP2GP FHIR Implementation - GP2GP Sending Adaptor**  Implement and maintain the [GP2GP Sending Adaptor](GP2GP-Sending-Adaptor.md) inline with the latest Standard version | MUST |
| **GP2GP08** | **GP2GP FHIR Implementation - GP2GP Requesting Adaptor**  Implement and maintain the [GP2GP Requesting Adaptor](GP2GP-Requesting-Adaptor.md) inline with the latest Standard version | MUST |
| **GP2GP09** | **Management Information**  Suppliers must implement and maintain the [GP Registrations Management Information API](https://digital.nhs.uk/developer/api-catalogue/gp-registrations-management-information) inline with the latest specification version | MUST |

# Compliance and Assurance

### GP2GP FHIR Implementation

See the GP2GP (including GP2GP Sending Adaptor/GP2GP Requesting Adaptor) section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

### GP2GP HL7

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented GP2GP HL7:

![](https://nhse-dsic.atlassian.net/wiki/images/icons/grey_arrow_down.png)Click here to expand...

The compliance baseline for GP2GP and document locations were correct at the time of original publication, but referenced documents can now be found embedded on this page, below. The exceptions to this are the references to the [NHS Messaging Implementation Manual (MIM)](NHS-Messaging-Implementation-Manual-MIM.md) and [External Interface Specification (EIS)](External-Interface-Specification-EIS.md) (follow these links for details).

[GP2GP 1.1a Compliance Mo…](GP2GP.md)

The GP2GP assurance is split into 2 streams:

1. Compliance testing - this tests the spine messaging patterns and functionality
2. Interoperability Testing - the testing of the clinically semantic testing of the message payload between different systems

For advice and support on assurance please contact [businesspartners@nhs.net](mailto:businesspartners@nhs.net) or visit <https://digital.nhs.uk/services/nhs-business-partners>

# Documentation

### GP2GP FHIR Implementation

For Suppliers of new Solutions and Solutions that have implemented the GP2GP FHIR Implementation:

- [API Catalogue - GP2GP Requesting Adaptor](https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdigital.nhs.uk%2Fdeveloper%2Fapi-catalogue%2Fgp2gp%2Fgp2gp-receiving-adaptor&data=05%7C02%7Cbhoopalan.parthiban1%40nhs.net%7C912d83d397f64695633f08dc37a79f20%7C37c354b285b047f5b22207b48d774ee3%7C0%7C0%7C638446440263988497%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=%2FQdkp3Ee0NWjLvTJoeruiX6fIwURypz8bWGclf3hXTw%3D&reserved=0)
- [API Catalogue - GP2GP Sending Adaptor](https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdigital.nhs.uk%2Fdeveloper%2Fapi-catalogue%2Fgp2gp%2Fgp2gp-sending-adaptor&data=05%7C02%7Cbhoopalan.parthiban1%40nhs.net%7C912d83d397f64695633f08dc37a79f20%7C37c354b285b047f5b22207b48d774ee3%7C0%7C0%7C638446440263973667%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=fov%2FIN%2B7GvjbwCgXgoZXDEqszs9WYPOHf9rLeI6d%2BAc%3D&reserved=0)
- [GP Registrations Management Information API](https://digital.nhs.uk/developer/api-catalogue/gp-registrations-management-information)
- [Message Handling System (MHS) Adaptor](https://digital.nhs.uk/developer/api-catalogue/mhs)

### GP2GP HL7

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented GP2GP HL7:

![](https://nhse-dsic.atlassian.net/wiki/images/icons/grey_arrow_down.png)Click here to expand...

#### Message Fragments and Examples

[NPFIT-FNT-TO-TIN-0562[1]…](GP2GP.md)

#### Supplementary specifications

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

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

### GP2GP FHIR Implementation

For Suppliers of new Solutions and Solutions that have implemented the GP2GP FHIR Implementation:

- [GP2GP Requesting Adaptor](GP2GP-Requesting-Adaptor.md)
- [GP2GP Sending Adaptor](GP2GP-Sending-Adaptor.md)
- [Personal Demographics Service (PDS)](Personal-Demographics-Service-PDS.md) - using FHIR API
- [Spine Directory Service - FHIR API](https://digital.nhs.uk/developer/api-catalogue/spine-directory-service-fhir)
- [GP Connect Access Record Structured](GP-Connect-Access-Record-Structured.md) - Refer to ‘Migrate a Patient’s structured record' and ‘Migrate a document’ for more information
- [GP Registrations Management Information API](https://digital.nhs.uk/developer/api-catalogue/gp-registrations-management-information)

### GPGP HL7

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented GP2GP HL7:

![](https://nhse-dsic.atlassian.net/wiki/images/icons/grey_arrow_down.png)Click here to view historical dependencies

Creating a compliant implementation previously required implementing the following dependent interface standards:

- [External Interface Specification (EIS)](External-Interface-Specification-EIS.md)
- [NHS Messaging Implementation Manual (MIM)](NHS-Messaging-Implementation-Manual-MIM.md)

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391138889-NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf)
- [NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391138890-NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf)
- [NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391138898-NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf)
- [NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391138914-NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf)
- [NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391142695-NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf)
- [NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391142701-NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf)
- [NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391142874-NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf)
- [NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391142878-NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf)
- [NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391142886-NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf)
- [NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391142887-NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf)
- [NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391142890-NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf)
- [NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391142892-NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf)
- [NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391142984-NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf)
- [NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391142987-NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf)
- [NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391143000-NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf)
- [NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391143009-NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf)
- [GP2GP 1.1a Compliance Module.doc](../../../../.raw/DCSDCS/attachments/1391134336/att1391143020-GP2GP 1.1a Compliance Module.doc)
- [NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391143022-NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf)
- [NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391143030-NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf)
- [NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391143035-NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf)
- [NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391143044-NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf)
- [NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391143047-NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf)
- [HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att1391143049-HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf)
- [NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc](../../../../.raw/DCSDCS/attachments/1391134336/att1391155303-NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc)
- [NPFIT-FNT-TO-TIN-0379.03 System Walkthrough and Induction Pack.ppt](../../../../.raw/DCSDCS/attachments/1391134336/att1391155306-NPFIT-FNT-TO-TIN-0379.03 System Walkthrough and Induction Pack.ppt)
- [HSCIC-PC-BLD-0068%2026%20GP2GP%20R2%202%20Requirements%20Specification%20v7.2.pdf?version=1&modificationDate=1703173844510&cacheVersion=1&api=v2&viewType=fileMacro](../../../../.raw/DCSDCS/attachments/1391134336/att13096288391-HSCIC-PC-BLD-0068%2026%20GP2GP%20R2%202%20Requirements%20Specification%20v7.2.pdf?version=1&modificationDate=1703173844510&cacheVersion=1&api=v2&viewType=fileMacro)
- [GP2GP%20Automatic%20Integration%20Specification%20v1.0.pdf?version=1&modificationDate=1703173855157&cacheVersion=1&api=v2&viewType=fileMacro](../../../../.raw/DCSDCS/attachments/1391134336/att13096288398-GP2GP%20Automatic%20Integration%20Specification%20v1.0.pdf?version=1&modificationDate=1703173855157&cacheVersion=1&api=v2&viewType=fileMacro)
- [GP2GP Automatic Integration Specification v1.0.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att13097435179-GP2GP Automatic Integration Specification v1.0.pdf)
- [GP2GPRedactions_MIMDesign_IOPS_v1.01.pdf](../../../../.raw/DCSDCS/attachments/1391134336/att14448361475-GP2GPRedactions_MIMDesign_IOPS_v1.01.pdf)
- [RCMR_IN030000UK07.xsd](../../../../.raw/DCSDCS/attachments/1391134336/att14448361482-RCMR_IN030000UK07.xsd)
- [RCMR_MT030101UK05.xsd](../../../../.raw/DCSDCS/attachments/1391134336/att14448361488-RCMR_MT030101UK05.xsd)
- [RCMR_EX030101UK05.xml](../../../../.raw/DCSDCS/attachments/1391134336/att14448361494-RCMR_EX030101UK05.xml)
