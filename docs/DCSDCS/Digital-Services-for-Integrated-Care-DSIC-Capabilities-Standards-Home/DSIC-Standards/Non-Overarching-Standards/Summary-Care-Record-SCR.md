---
page_id: "1391133699"
space: "DCSDCS"
title: "Summary Care Record (SCR)"
version: 19
updated: "2026-07-22T13:14:55.506Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133699/Summary+Care+Record+SCR"
labels: ["standard"]
---

# Summary Care Record (SCR)

|  |  |
| --- | --- |
| **ID** | S60 |
| **Version** | 2.0.2 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 25 Jul 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#SummaryCareRecord(SCR)-Introduction)
- [Requirements](#SummaryCareRecord(SCR)-Requirements)
- [Compliance, Assurance and Testing](#SummaryCareRecord(SCR)-Compliance,AssuranceandTesting)
  - [SCR FHIR API](#SummaryCareRecord(SCR)-SCRFHIRAPI)
  - [NHS Summary Care Record Service - GP Summary Requirements v5.8.3](#SummaryCareRecord(SCR)-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3)
- [Documentation](#SummaryCareRecord(SCR)-Documentation)
  - [SCR FHIR API](#SummaryCareRecord(SCR)-SCRFHIRAPI.1)
  - [NHS Summary Care Record Service - GP Summary Requirements v5.8.3](#SummaryCareRecord(SCR)-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3.1)
- [Dependencies](#SummaryCareRecord(SCR)-Dependencies)
  - [SCR FHIR API](#SummaryCareRecord(SCR)-SCRFHIRAPI.2)
  - [NHS Summary Care Record Service - GP Summary Requirements v5.8.3](#SummaryCareRecord(SCR)-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3.2)
- [Roadmap](#SummaryCareRecord(SCR)-Roadmap)

# Introduction {#SummaryCareRecord(SCR)-Introduction}

The Summary Care Record (SCR) is an Electronic Record of important Patient Information, created from GP medical records. It can be seen and used by authorised Health or Care Professionals in other areas of the Health and Care System involved in the Patient's direct care.

From an interoperability perspective there are two aspects to the Summary Care Record:

1. The creation and updating of the Summary Care Record
2. Providing the ability for authorised Health or Care Professionals to access the Summary Care Record

Both of these aspects are covered in the documentation below. Additional information is available on the Authority's [Summary Care Records (SCR)](https://digital.nhs.uk/summary-care-records) site.

# Requirements  {#SummaryCareRecord(SCR)-Requirements}

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| - Suppliers of new Solutions (i.e. those which are NOT currently deployed into an operational environment with existing SCR compliance). - Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented the SCR FHIR API. | **SCR01** | Implement and maintain the API inline with the latest specification version of [SCR FHIR API](https://digital.nhs.uk/developer/api-catalogue/summary-care-record-fhir). | MUST |
| **SCR02** | Implement and maintain the SCR FHIR API inline with the GP Summary Requirements Refactored latest specification version.  [GP Summary Requirements …](../../../../attachments/DCSDCS/1391133699/att14258864134-GP Summary Requirements Refactored for SCR FHIR API v6.1.1.docx)  For further requirements clarification and Implementation guidance, please see the Guidance and special considerations document below.  [SCR Additional Informati…](../../../../attachments/DCSDCS/1391133699/att14258864142-SCR Additional Information Guidance and Special Considerations.docx) | MUST |
| **SCR03** | Implement and maintain the SCR FHIR API inline with the GP Summary Presentation Text Specification Refactored latest specification version.  [GP Summary Presentation …](../../../../attachments/DCSDCS/1391133699/att14258864148-GP Summary Presentation Text Specification Refactored for SCR FHIR API v4.1.1.xlsx) | MUST |
| **SCR04** | Implement and maintain the SCR FHIR API inline with the SCR Viewing Requirements Refactored latest specification version.  [SCR Viewing Requirements…](../../../../attachments/DCSDCS/1391133699/att14258864154-SCR Viewing Requirements Refactored for SCR FHIR API v5.1.1.docx) | MUST |
| **SCR05** | Implement and maintain the SCR FHIR API inline with the Technical Specification for GP Summary XHTML latest specification version.  [SCR FHIR API Technical S…](../../../../attachments/DCSDCS/1391133699/att12557156380-SCR FHIR API Technical Specification for the GP Summary XHTML.docx) | MUST |
| **SCR06** | Implement and maintain the requirements detailed in the COVID-19 SCR Additional Information Requirements latest specification version.  [COVID-19 SCR Additional …](../../../../attachments/DCSDCS/1391133699/att14258995331-COVID-19 SCR Additional Information requirements v1.21.docx) | MUST |
| Suppliers of Solutions which ARE currently deployed into an operational environment, and have implemented SCR HL7. | **SCR07** | Implement the requirements detailed in the GP Summary Requirements v5.8.3 or later e.g. [SCR FHIR API](https://digital.nhs.uk/developer/api-catalogue/summary-care-record-fhir)  [GP Summary Requirements …](../../../../attachments/DCSDCS/1391133699/att12556533824-GP Summary Requirements v5.8.3.docx) | MUST |

# Compliance, Assurance and Testing {#SummaryCareRecord(SCR)-Compliance,AssuranceandTesting}

All Suppliers are encouraged to work towards compliance with the latest version as above.

### SCR FHIR API {#SummaryCareRecord(SCR)-SCRFHIRAPI}

For Suppliers of new Solutions and Solutions that have implemented the SCR FHIR API, see the Summary Care Record (SCR) section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

### NHS Summary Care Record Service - GP Summary Requirements v5.8.3 {#SummaryCareRecord(SCR)-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3}

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented SCR HL7:

 Click here to view historical assurance approach

To gain access to SCR Suppliers follow the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and activities are conducted.

As part of the CAP Suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- [External Interface Specification](External-Interface-Specification-EIS.md)
- [NHS Messaging Implementation Manual](NHS-Messaging-Implementation-Manual-MIM.md)
- [Personal Demographics Service Integration Requirements](Personal-Demographics-Service-PDS.md)
- Summary Care Record Integration Requirements (see details below)

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

For advice, access to the documentation, and support from the NHS Business Partners programme, please contact [businesspartners@nhs.net](mailto:businesspartners@nhs.net) or visit <https://digital.nhs.uk/services/nhs-business-partners>

The [NPFIT-SCR-SCRDOCS-0038.01 NHS CFH SCR Clinical Message Validation Process v1.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/NPFIT-SCR-SCRDOCS-0038.01%20NHS%20CFH%20SCR%20Clinical%20Message%20Validation%20Process%20v1.docx?version=1&modificationDate=1610558048108&cacheVersion=1&api=v2) document provides guidance on the clinical safety validation processes for SCR messaging.

# Documentation {#SummaryCareRecord(SCR)-Documentation}

### SCR FHIR API {#SummaryCareRecord(SCR)-SCRFHIRAPI.1}

For Suppliers of new Solutions and Solutions that have implemented the SCR FHIR API:

- [API Catalogue - Summary Care Record (SCR) FHIR API](https://digital.nhs.uk/developer/api-catalogue/summary-care-record-fhir)
- [GP software developer guide](https://digital.nhs.uk/developer/guides-and-documentation/building-healthcare-software/general-practice)
- [Testing APIs](https://digital.nhs.uk/developer/guides-and-documentation/testing)
- [SCR permission to view guidelines](https://digital.nhs.uk/services/summary-care-records-scr/viewing-summary-care-records-scr#scr-permission-to-view-guidelines)
- [Registration Authority](https://digital.nhs.uk/services/care-identity-service/registration-authority-users)

It is recommended to read GP software developer guide in conjunction with the API documentation.

### NHS Summary Care Record Service - GP Summary Requirements v5.8.3 {#SummaryCareRecord(SCR)-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3.1}

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented SCR HL7:

Click here to view previous SCR requirements documentation

#### Summary Care Record Creation {#SummaryCareRecord(SCR)-SummaryCareRecordCreation}

GP Summaries are created and sent to the Summary Care Record repository (on Spine) via messaging from GP Systems which implement the [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) capability.

To create Summary Care Records and provide them to the Service, Suppliers must implement the requirements detailed in [GP Summary Requirements v5.8.3](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/GP%20Summary%20Requirements%20v5.8.3%20FINAL.docx?version=1&modificationDate=1539679969277&cacheVersion=1&api=v2).

Summary care messages contain XHTML information and generated messages must conform to the specification in [NPFIT-SHR-MODL-SUMREC-0025 08 GP Summary Presentation Text Specification v3.1 (Approved).xlsx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/NPFIT-SHR-MODL-SUMREC-0025%2008%20GP%20Summary%20Presentation%20Text%20Specification%20v3.1%20(Approved).xlsx?version=3&modificationDate=1513781341488&cacheVersion=1&api=v2)

Implementations must comply with the [NPFIT-EP-DB-0007.05 Allergy\_ADR\_Intolerance v 1.5 Draft.doc](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/NPFIT-EP-DB-0007.05%20Allergy_ADR_Intolerance%20v%201.5%20Draft.doc?version=1&modificationDate=1610621033836&cacheVersion=1&api=v2) for all representations of medication-related adverse clinical events.

Implementations must comply with the [SCR GP Summary Sending Compliance v3 - Baseline Index v6.0](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/SCR%20GP%20Summary%20Sending%20Compliance%20v3%20-%20Baseline%20Index%20v6.0_Refactor%20for%20NMEs.docx?api=v2)

Message definitions are detailed in the [Domain Message Specification (DMS)](https://data.developer.nhs.uk/dms/mim/6.3.01/Index.htm) for Summary Care Record

Further information useful for implementers of this interface such as Use Cases, Trigger Events and Sequence Diagrams may be found in the Spine [Message Implementation Manual (MIM)](NHS-Messaging-Implementation-Manual-MIM.md). NB version **4.2** is the version used for the GP Summary Update message.

Also, see [MIM 4.2.00 Known Issues.doc](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/MIM%204.2.00%20Known%20Issues.doc?version=1&modificationDate=1610621137597&cacheVersion=1&api=v2)

#### Summary Care Record Viewing {#SummaryCareRecord(SCR)-SummaryCareRecordViewing}

SCR viewing must be implemented in line with the [Summary Care Record Permission To View Guidelines.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/Summary%20Care%20Record%20Permission%20To%20View%20Guidelines.pdf?version=1&modificationDate=1518091153560&cacheVersion=1&api=v2)

General requirements for SCR viewing (regardless of implementation mechanism) are set out in [NPFIT-FNT-TO-DPM-0929.03 SCR Viewing Requirements v1.6 (Approved).docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/NPFIT-FNT-TO-DPM-0929.03%20SCR%20Viewing%20Requirements%20v1.6%20(Approved).docx?version=1&modificationDate=1610621368327&cacheVersion=1&api=v2)

Guidance for implementing Role-Based Access Control for SCR viewing is found in [NPFIT-SI-SIGOV-0073 04 Guidance on Implementing RBAC for PSIS and PDS v2.0.doc](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/NPFIT-SI-SIGOV-0073%2004%20Guidance%20on%20Implementing%20RBAC%20for%20PSIS%20and%20PDS%20v2.0.doc?version=1&modificationDate=1610621802577&cacheVersion=1&api=v2)

Suppliers have a number of options for implementing Summary Care Record viewing, as detailed below:

|  |  |  |
| --- | --- | --- |
| **Option** | **Description** | **Documentation** |
| 1 click | a simpler and less resource-intensive way to enable SCR viewing into local applications. This solution allows a user of an application to click and launch the SCRa in a separate window for a specific Patient. | [NPFIT-FNT-TO-DPM-1023 SCR 1-Click Supplier Requirements v2 7.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/NPFIT-FNT-TO-DPM-1023%20SCR%201-Click%20Supplier%20Requirements%20v2%207.docx?version=1&modificationDate=1513781555759&cacheVersion=1&api=v2) |
| Spine mini Services | [Spine mini Services (SMS)](https://digital.nhs.uk/services/spine/spine-mini-service-simplified-ways-to-connect-to-spine) are a more lightweight way of developing read-only integration with some national Spine Services. SMS Client Systems allow SCR access with Patient permission and for Emergency Reasons. SCR Viewing Systems will be able “plug into” the SCR Spine Mini-Service functionality of the SMS Provider. The SMS Provider System provides various defined functions and Services for SCR Viewing Systems, e.g. the SMS Provider would retrieve GP Summaries and manage “Permission to View” on behalf of viewing Systems (clients). | [SCR - Spine Mini Service Provider Requirements-v1.3.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/SCR%20-%20Spine%20Mini%20Service%20Provider%20Requirements-v1.3.docx?version=1&modificationDate=1513781786340&cacheVersion=1&api=v2)  [SCR - Spine Mini Service Client Requirement04.1.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/SCR%20-%20Spine%20Mini%20Service%20Client%20Requirement04.1.docx?version=1&modificationDate=1513782079551&cacheVersion=1&api=v2) |
| Full SCR integration | Integration of SCR information into the GP clinical System.  A GP System retrieves GP Summaries from the Summary Care Record on Spine using the PSIS Query message and displays it via appropriate screens within the GP clinical System. | [SCR\_Viewing\_Requirements\_v3.0\_(Approved).docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/SCR_Viewing_Requirements_v3.0_(Approved).docx?version=1&modificationDate=1513782355833&cacheVersion=1&api=v2)  [Message Implementation Manual (MIM 7.2)](NHS-Messaging-Implementation-Manual-MIM.md) PSIS Query  [NPFIT-FNT-TO-TIN-1228 14 Compliance Specification - Clinical Message Handling Addendum v4-0.doc](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/NPFIT-FNT-TO-TIN-1228%2014%20Compliance%20Specification%20-%20Clinical%20Message%20Handling%20Addendum%20v4-0.doc?version=1&modificationDate=1610621905246&cacheVersion=1&api=v2) (sections relevant to PSIS Query)  [MIM 7 2 02 Known Issues 1.3.doc](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133699/MIM%207%202%2002%20Known%20Issues%201.3.doc?version=1&modificationDate=1610621971395&cacheVersion=1&api=v2) |

# Dependencies {#SummaryCareRecord(SCR)-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standards:

### SCR FHIR API {#SummaryCareRecord(SCR)-SCRFHIRAPI.2}

For Suppliers of new Solutions and Solutions that have implemented the SCR FHIR API:

- [Authentication and Access](Authentication-and-Access.md) - using NHS Care Identity Service 2 API

### NHS Summary Care Record Service - GP Summary Requirements v5.8.3 {#SummaryCareRecord(SCR)-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3.2}

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented SCR HL7:

Click here to view historical dependencies

- [External Interface Specification (EIS)](External-Interface-Specification-EIS.md)
- [NHS Messaging Implementation Manual (MIM)](NHS-Messaging-Implementation-Manual-MIM.md)
- [Spine Mini Services](Spine-Mini-Services.md) (optional)
- [Authentication and Access](Authentication-and-Access.md)

# Roadmap {#SummaryCareRecord(SCR)-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NPFIT-FNT-TO-DPM-1023 SCR 1-Click Supplier Requirements v2 7.docx](../../../../attachments/DCSDCS/1391133699/att1391136064-NPFIT-FNT-TO-DPM-1023 SCR 1-Click Supplier Requirements v2 7.docx)
- [SCR GP Summary Sending Compliance v3 - Baseline Index v6.0](../../../../attachments/DCSDCS/1391133699/att1391136107-SCR GP Summary Sending Compliance v3 - Baseline Index v6.0)
- [NPFIT-SHR-MODL-SUMREC-0025 08 GP Summary Presentation Text Specification v3.1 (Approved).xlsx](../../../../attachments/DCSDCS/1391133699/att1391136149-NPFIT-SHR-MODL-SUMREC-0025 08 GP Summary Presentation Text Specification v3.1 (Approved).xlsx)
- [SCR - Spine Mini Service Client Requirement04.1.docx](../../../../attachments/DCSDCS/1391133699/att1391136235-SCR - Spine Mini Service Client Requirement04.1.docx)
- [SCR_Viewing_Requirements_v3.0_(Approved).docx](../../../../attachments/DCSDCS/1391133699/att1391136393-SCR_Viewing_Requirements_v3.0_(Approved).docx)
- [SCR - Spine Mini Service Provider Requirements-v1.3.docx](../../../../attachments/DCSDCS/1391133699/att1391136394-SCR - Spine Mini Service Provider Requirements-v1.3.docx)
- [Summary Care Record Permission To View Guidelines.pdf](../../../../attachments/DCSDCS/1391133699/att1391139487-Summary Care Record Permission To View Guidelines.pdf)
- [GP Summary Requirements v5.8.3 FINAL.docx](../../../../attachments/DCSDCS/1391133699/att1391158259-GP Summary Requirements v5.8.3 FINAL.docx)
- [NPFIT-SCR-SCRDOCS-0038.01 NHS CFH SCR Clinical Message Validation Process v1.docx](../../../../attachments/DCSDCS/1391133699/att10698063936-NPFIT-SCR-SCRDOCS-0038.01 NHS CFH SCR Clinical Message Validation Process v1.docx)
- [MIM 7 2 02 Known Issues 1.3.doc](../../../../attachments/DCSDCS/1391133699/att10699505733-MIM 7 2 02 Known Issues 1.3.doc)
- [NPFIT-EP-DB-0007.05 Allergy_ADR_Intolerance v 1.5 Draft.doc](../../../../attachments/DCSDCS/1391133699/att10701340718-NPFIT-EP-DB-0007.05 Allergy_ADR_Intolerance v 1.5 Draft.doc)
- [NPFIT-SI-SIGOV-0073 04 Guidance on Implementing RBAC for PSIS and PDS v2.0.doc](../../../../attachments/DCSDCS/1391133699/att10701340723-NPFIT-SI-SIGOV-0073 04 Guidance on Implementing RBAC for PSIS and PDS v2.0.doc)
- [MIM 4.2.00 Known Issues.doc](../../../../attachments/DCSDCS/1391133699/att10701471825-MIM 4.2.00 Known Issues.doc)
- [NPFIT-FNT-TO-DPM-0929.03 SCR Viewing Requirements v1.6 (Approved).docx](../../../../attachments/DCSDCS/1391133699/att10701602884-NPFIT-FNT-TO-DPM-0929.03 SCR Viewing Requirements v1.6 (Approved).docx)
- [NPFIT-FNT-TO-TIN-1228 14 Compliance Specification - Clinical Message Handling Addendum v4-0.doc](../../../../attachments/DCSDCS/1391133699/att10701602895-NPFIT-FNT-TO-TIN-1228 14 Compliance Specification - Clinical Message Handling Addendum v4-0.doc)
- [GP Summary Presentation Text Specification Refactored for SCR FHIR API.xlsx](../../../../attachments/DCSDCS/1391133699/att12556370017-GP Summary Presentation Text Specification Refactored for SCR FHIR API.xlsx)
- [GP Summary Requirements v5.8.3.docx](../../../../attachments/DCSDCS/1391133699/att12556533824-GP Summary Requirements v5.8.3.docx)
- [SCR Viewing Requirements Refactored for SCR FHIR API.docx](../../../../attachments/DCSDCS/1391133699/att12556894280-SCR Viewing Requirements Refactored for SCR FHIR API.docx)
- [GP Summary Requirements Refactored for SCR FHIR API.docx](../../../../attachments/DCSDCS/1391133699/att12557025332-GP Summary Requirements Refactored for SCR FHIR API.docx)
- [SCR FHIR API Technical Specification for the GP Summary XHTML.docx](../../../../attachments/DCSDCS/1391133699/att12557156380-SCR FHIR API Technical Specification for the GP Summary XHTML.docx)
- [GP Summary Requirements Refactored for SCR FHIR API v6.1.1.docx](../../../../attachments/DCSDCS/1391133699/att14258864134-GP Summary Requirements Refactored for SCR FHIR API v6.1.1.docx)
- [SCR Additional Information Guidance and Special Considerations.docx](../../../../attachments/DCSDCS/1391133699/att14258864142-SCR Additional Information Guidance and Special Considerations.docx)
- [GP Summary Presentation Text Specification Refactored for SCR FHIR API v4.1.1.xlsx](../../../../attachments/DCSDCS/1391133699/att14258864148-GP Summary Presentation Text Specification Refactored for SCR FHIR API v4.1.1.xlsx)
- [SCR Viewing Requirements Refactored for SCR FHIR API v5.1.1.docx](../../../../attachments/DCSDCS/1391133699/att14258864154-SCR Viewing Requirements Refactored for SCR FHIR API v5.1.1.docx)
- [COVID-19 SCR Additional Information requirements v1.21.docx](../../../../attachments/DCSDCS/1391133699/att14258995331-COVID-19 SCR Additional Information requirements v1.21.docx)
- [SCR GP Summary Sending Compliance v3 - Baseline Index v6.0_Refactor for NMEs.docx](../../../../attachments/DCSDCS/1391133699/att14259027981-SCR GP Summary Sending Compliance v3 - Baseline Index v6.0_Refactor for NMEs.docx)
