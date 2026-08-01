---
page_id: "12557221889"
space: "DCSDCS"
title: "Summary Care Record (SCR) V1.0.1"
version: 4
updated: "2023-09-28T11:49:10.040Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12557221889/Summary+Care+Record+SCR+V1.0.1"
labels: ["interop_standard_retired"]
---

# Summary Care Record (SCR) V1.0.1

|  |  |
| --- | --- |
| ID | S60 |
| Version | 1.0.1 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 10 May 2022 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

- [Introduction](#SummaryCareRecord(SCR)V1.0.1-Introduction)
- [Requirements](#SummaryCareRecord(SCR)V1.0.1-Requirements)
- [Compliance, Assurance and Testing](#SummaryCareRecord(SCR)V1.0.1-Compliance,AssuranceandTesting)
  - [SCR FHIR API](#SummaryCareRecord(SCR)V1.0.1-SCRFHIRAPI)
  - [NHS Summary Care Record Service - GP Summary Requirements v5.8.3](#SummaryCareRecord(SCR)V1.0.1-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3)
- [Documentation](#SummaryCareRecord(SCR)V1.0.1-Documentation)
  - [SCR FHIR API](#SummaryCareRecord(SCR)V1.0.1-SCRFHIRAPI.1)
  - [NHS Summary Care Record Service - GP Summary Requirements v5.8.3](#SummaryCareRecord(SCR)V1.0.1-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3.1)
    - [Summary Care Record Creation](#SummaryCareRecord(SCR)V1.0.1-SummaryCareRecordCreation)
    - [Summary Care Record Viewing](#SummaryCareRecord(SCR)V1.0.1-SummaryCareRecordViewing)
- [Dependencies](#SummaryCareRecord(SCR)V1.0.1-Dependencies)
  - [Summary Care Record FHIR API](#SummaryCareRecord(SCR)V1.0.1-SummaryCareRecordFHIRAPI)
  - [NHS Summary Care Record Service - GP Summary Requirements v5.8.3](#SummaryCareRecord(SCR)V1.0.1-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3.2)
- [Roadmap](#SummaryCareRecord(SCR)V1.0.1-Roadmap)

# Introduction {#SummaryCareRecord(SCR)V1.0.1-Introduction}

The Summary Care Record (SCR) is an electronic record of important Patient information, created from GP medical records. It can be seen and used by authorised staff in other areas of the health and care system involved in the Patient's direct care.

From an interoperability perspective there are two aspects to the summary care record:

1. The creation and updating of the summary care record
2. Providing the ability for authorised staff to access the summary care record, for which there are a range of options

Both of these aspects are covered in the documentation below.

Additional information is available at NHS Digital's summary care record site

# Requirements  {#SummaryCareRecord(SCR)V1.0.1-Requirements}

| Applicable Suppliers | Requirement | Level |
| --- | --- | --- |
| Suppliers of new services or applications (i.e. those which are NOT currently deployed into an operational environment with existing SCR compliance). | Implement and maintain the API inline with the latest specification version of SCR FHIR API. | MUST |
| Suppliers of services which ARE currently deployed into an operational environment, and have existing SCR compliance. | Implement the requirements detailed in[GP Summary Requirements v5.8.3](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/GP%20Summary%20Requirements%20v5.8.3%20FINAL.docx?version=1&modificationDate=1695893951530&cacheVersion=1&api=v2) or later e.g. SCR FHIR API | MUST |

All suppliers are encouraged to work towards compliance with the latest version as above.

# Compliance, Assurance and Testing {#SummaryCareRecord(SCR)V1.0.1-Compliance,AssuranceandTesting}

### SCR FHIR API {#SummaryCareRecord(SCR)V1.0.1-SCRFHIRAPI}

For Suppliers of new services or applications, see the Summary Care Record(SCR) section on Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements.

### NHS Summary Care Record Service - [GP Summary Requirements v5.8.3](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/GP%20Summary%20Requirements%20v5.8.3%20FINAL.docx?version=1&modificationDate=1695893951530&cacheVersion=1&api=v2) {#SummaryCareRecord(SCR)V1.0.1-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3}

For Suppliers of services which ARE currently deployed into an operational environment:

 Click here to view historical assurance approach

To gain access to SCR suppliers follow the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and activities are conducted.

As part of the CAP suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- External Interface Specification
- NHS Messaging Implementation Manual
- Personal Demographics Service Integration Requirements
- Summary Care Record Integration Requirements (see details below)

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

For advice, access to the documentation, and support from the NHS Business Partners programme, please contact businesspartners@nhs.net or visit https://digital.nhs.uk/services/nhs-business-partners

The NPFIT-SCR-SCRDOCS-0038.01 NHS CFH SCR Clinical Message Validation Process v1.docx document provides guidance on the clinical safety validation processes for SCR messaging.

# Documentation {#SummaryCareRecord(SCR)V1.0.1-Documentation}

### SCR FHIR API {#SummaryCareRecord(SCR)V1.0.1-SCRFHIRAPI.1}

For Suppliers of new services or applications:

- API Catalogue - Summary Care Record (SCR) FHIR API
- GP software developer guide
- Testing APIs

It is recommended to read GP software developer guide in conjunction with the API documentation.

### NHS Summary Care Record Service - [GP Summary Requirements v5.8.3](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/GP%20Summary%20Requirements%20v5.8.3%20FINAL.docx?version=1&modificationDate=1695893951530&cacheVersion=1&api=v2) {#SummaryCareRecord(SCR)V1.0.1-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3.1}

For Suppliers of services which ARE currently deployed into an operational environment.

Click here to view previous SCR requirements documentation

#### Summary Care Record Creation {#SummaryCareRecord(SCR)V1.0.1-SummaryCareRecordCreation}

GP Summaries are created and sent to the Summary Care Record repository (on Spine) via messaging from GP systems which implement the Patient Information Maintenance - GP capability.

To create summary care records and provide them to the service, suppliers must implement the requirements detailed in[GP Summary Requirements v5.8.3](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/GP%20Summary%20Requirements%20v5.8.3%20FINAL.docx?version=1&modificationDate=1695893951530&cacheVersion=1&api=v2).

Summary care messages contain XHTML information and generated messages must conform to the specification in NPFIT-SHR-MODL-SUMREC-0025 08 GP Summary Presentation Text Specification v3.1 (Approved).xlsx

Implementations must comply with the NPFIT-EP-DB-0007.05 Allergy\_ADR\_Intolerance v 1.5 Draft.doc for all representations of medication-related adverse clinical events.

Implementations must comply with the [SCR GP Summary Sending Compliance v3 - Baseline Index v6.0](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/SCR%20GP%20Summary%20Sending%20Compliance%20v3%20-%20Baseline%20Index%20v6.0?version=1&modificationDate=1695893953328&cacheVersion=1&api=v2)

Message definitions are detailed in the Domain Message Specification (DMS) for Summary Care Record

Further information useful for implementers of this interface such as Use Cases, Trigger Events and Sequence Diagrams may be found in the Spine Message Implementation Manual (MIM).  NB version **4.2** is the version used for the GP Summary Update message.

Also, see MIM 4.2.00 Known Issues.doc

#### Summary Care Record Viewing {#SummaryCareRecord(SCR)V1.0.1-SummaryCareRecordViewing}

SCR viewing must be implemented in line with the [Summary Care Record Permission To View Guidelines.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/Summary%20Care%20Record%20Permission%20To%20View%20Guidelines.pdf?version=1&modificationDate=1695893951968&cacheVersion=1&api=v2)

General requirements for SCR viewing (regardless of implementation mechanism) are set out in [NPFIT-FNT-TO-DPM-0929.03 SCR Viewing Requirements v1.6 (Approved).docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/NPFIT-FNT-TO-DPM-0929.03%20SCR%20Viewing%20Requirements%20v1.6%20(Approved).docx?version=1&modificationDate=1695893949654&cacheVersion=1&api=v2)

Guidance for implementing Role-Based Access Control for SCR viewing is found in [NPFIT-SI-SIGOV-0073 04 Guidance on Implementing RBAC for PSIS and PDS v2.0.doc](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/NPFIT-SI-SIGOV-0073%2004%20Guidance%20on%20Implementing%20RBAC%20for%20PSIS%20and%20PDS%20v2.0.doc?version=1&modificationDate=1695893949256&cacheVersion=1&api=v2)

Suppliers have a number of options for implementing summary care record viewing, as detailed below:

| Option | Description | Documentation |
| --- | --- | --- |
| 1 click | a simpler and less resource-intensive way to enable SCR viewing into local applications. This solution allows a user of an application to click and launch the SCRa in a separate window for a specific patient. | [NPFIT-FNT-TO-DPM-1023 SCR 1-Click Supplier Requirements v2 7.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/NPFIT-FNT-TO-DPM-1023%20SCR%201-Click%20Supplier%20Requirements%20v2%207.docx?version=1&modificationDate=1695893954238&cacheVersion=1&api=v2) |
| Spine mini services | Spine mini services (SMS) are a more lightweight way of developing read-only integration with some national Spine services. SMS Client systems allow SCR access with patient permission and for Emergency Reasons. SCR Viewing systems will be able “plug into” the SCR Spine Mini-Service functionality of the SMS Provider. The SMS Provider system provides various defined functions and services for SCR Viewing systems, e.g. the SMS Provider would retrieve GP Summaries and manage “Permission to View” on behalf of viewing systems (clients). | [SCR - Spine Mini Service Provider Requirements-v1.3.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/SCR%20-%20Spine%20Mini%20Service%20Provider%20Requirements-v1.3.docx?version=1&modificationDate=1695893953796&cacheVersion=1&api=v2)  [SCR - Spine Mini Service Client Requirement04.1.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/SCR%20-%20Spine%20Mini%20Service%20Client%20Requirement04.1.docx?version=1&modificationDate=1695893952857&cacheVersion=1&api=v2) |
| Full SCR integration | Integration of SCR information into the GP clinical system.  A GP system retrieves GP Summaries from the Summary Care Record on Spine using the PSIS Query message and displays it via appropriate screens within the GP clinical system. | [SCR\_Viewing\_Requirements\_v3.0\_(Approved).docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/SCR_Viewing_Requirements_v3.0_(Approved).docx?version=1&modificationDate=1695893952402&cacheVersion=1&api=v2)  Summary Care Record DMS 5.8  Message Implementation Manual (MIM 7.2) PSIS Query  [NPFIT-FNT-TO-TIN-1228 14 Compliance Specification - Clinical Message Handling Addendum v4-0.doc](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/NPFIT-FNT-TO-TIN-1228%2014%20Compliance%20Specification%20-%20Clinical%20Message%20Handling%20Addendum%20v4-0.doc?version=1&modificationDate=1695893948801&cacheVersion=1&api=v2) (sections relevant to PSIS Query)  [MIM 7 2 02 Known Issues 1.3.doc](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/MIM%207%202%2002%20Known%20Issues%201.3.doc?version=1&modificationDate=1695893948323&cacheVersion=1&api=v2) |

# Dependencies {#SummaryCareRecord(SCR)V1.0.1-Dependencies}

### Summary Care Record FHIR API {#SummaryCareRecord(SCR)V1.0.1-SummaryCareRecordFHIRAPI}

For Suppliers of new services or applications:

- Authentication and Access - using NHS Care Identity Service 2 API

### NHS Summary Care Record Service - [GP Summary Requirements v5.8.3](https://nhse-dsic.atlassian.net/wiki/download/attachments/12557221889/GP%20Summary%20Requirements%20v5.8.3%20FINAL.docx?version=1&modificationDate=1695893951530&cacheVersion=1&api=v2) {#SummaryCareRecord(SCR)V1.0.1-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3.2}

For Suppliers of services which ARE currently deployed into an operational environment:

 Creating a compliant implementation requires implementing the following dependent interface standards, click here to see historical dependencies:

- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)
- Spine Mini Services (optional)
- Authentication and Access

# Roadmap {#SummaryCareRecord(SCR)V1.0.1-Roadmap}

| Title |
| --- |
| No content found. |

## Attachments

- [MIM 7 2 02 Known Issues 1.3.doc](../../../../attachments/DCSDCS/12557221889/att12557221916-MIM 7 2 02 Known Issues 1.3.doc)
- [NPFIT-FNT-TO-TIN-1228 14 Compliance Specification - Clinical Message Handling Addendum v4-0.doc](../../../../attachments/DCSDCS/12557221889/att12557221919-NPFIT-FNT-TO-TIN-1228 14 Compliance Specification - Clinical Message Handling Addendum v4-0.doc)
- [NPFIT-SI-SIGOV-0073 04 Guidance on Implementing RBAC for PSIS and PDS v2.0.doc](../../../../attachments/DCSDCS/12557221889/att12557221922-NPFIT-SI-SIGOV-0073 04 Guidance on Implementing RBAC for PSIS and PDS v2.0.doc)
- [NPFIT-FNT-TO-DPM-0929.03 SCR Viewing Requirements v1.6 (Approved).docx](../../../../attachments/DCSDCS/12557221889/att12557221925-NPFIT-FNT-TO-DPM-0929.03 SCR Viewing Requirements v1.6 (Approved).docx)
- [MIM 4.2.00 Known Issues.doc](../../../../attachments/DCSDCS/12557221889/att12557221928-MIM 4.2.00 Known Issues.doc)
- [NPFIT-EP-DB-0007.05 Allergy_ADR_Intolerance v 1.5 Draft.doc](../../../../attachments/DCSDCS/12557221889/att12557221931-NPFIT-EP-DB-0007.05 Allergy_ADR_Intolerance v 1.5 Draft.doc)
- [NPFIT-SCR-SCRDOCS-0038.01 NHS CFH SCR Clinical Message Validation Process v1.docx](../../../../attachments/DCSDCS/12557221889/att12557221934-NPFIT-SCR-SCRDOCS-0038.01 NHS CFH SCR Clinical Message Validation Process v1.docx)
- [GP Summary Requirements v5.8.3 FINAL.docx](../../../../attachments/DCSDCS/12557221889/att12557221937-GP Summary Requirements v5.8.3 FINAL.docx)
- [Summary Care Record Permission To View Guidelines.pdf](../../../../attachments/DCSDCS/12557221889/att12557221940-Summary Care Record Permission To View Guidelines.pdf)
- [SCR_Viewing_Requirements_v3.0_(Approved).docx](../../../../attachments/DCSDCS/12557221889/att12557221943-SCR_Viewing_Requirements_v3.0_(Approved).docx)
- [SCR - Spine Mini Service Client Requirement04.1.docx](../../../../attachments/DCSDCS/12557221889/att12557221946-SCR - Spine Mini Service Client Requirement04.1.docx)
- [SCR GP Summary Sending Compliance v3 - Baseline Index v6.0](../../../../attachments/DCSDCS/12557221889/att12557221949-SCR GP Summary Sending Compliance v3 - Baseline Index v6.0)
- [SCR - Spine Mini Service Provider Requirements-v1.3.docx](../../../../attachments/DCSDCS/12557221889/att12557221952-SCR - Spine Mini Service Provider Requirements-v1.3.docx)
- [NPFIT-FNT-TO-DPM-1023 SCR 1-Click Supplier Requirements v2 7.docx](../../../../attachments/DCSDCS/12557221889/att12557221955-NPFIT-FNT-TO-DPM-1023 SCR 1-Click Supplier Requirements v2 7.docx)
- [NPFIT-SHR-MODL-SUMREC-0025 08 GP Summary Presentation Text Specification v3.1 (Approved).xlsx](../../../../attachments/DCSDCS/12557221889/att12557221958-NPFIT-SHR-MODL-SUMREC-0025 08 GP Summary Presentation Text Specification v3.1 (Approved).xlsx)
