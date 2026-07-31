---
page_id: "11975327998"
space: "DCSDCS"
title: "Summary Care Record (SCR) V1.0.0"
version: 2
updated: "2022-05-10T13:36:19.999Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11975327998/Summary+Care+Record+SCR+V1.0.0"
labels: ["interop_standard_retired"]
---

# Summary Care Record (SCR) V1.0.0

|  |  |
| --- | --- |
| ID | S60 |
| Version | 1.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

/\*<![CDATA[\*/
div.rbtoc1785509728907 {padding: 0px;}
div.rbtoc1785509728907 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785509728907 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#SummaryCareRecord(SCR)V1.0.0-Introduction)
- [Compliance, Assurance and Testing](#SummaryCareRecord(SCR)V1.0.0-Compliance,AssuranceandTesting)
- [Documentation](#SummaryCareRecord(SCR)V1.0.0-Documentation)
  - [Summary Care Record Creation](#SummaryCareRecord(SCR)V1.0.0-SummaryCareRecordCreation)
  - [Summary Care Record Viewing](#SummaryCareRecord(SCR)V1.0.0-SummaryCareRecordViewing)
- [Dependencies](#SummaryCareRecord(SCR)V1.0.0-Dependencies)
- [Roadmap](#SummaryCareRecord(SCR)V1.0.0-Roadmap)

# Introduction

The Summary Care Record (SCR) is an electronic record of important Patient information, created from GP medical records. It can be seen and used by authorised staff in other areas of the health and care system involved in the Patient's direct care.

From an interoperability perspective there are two aspects to the summary care record:

1. The creation and updating of the summary care record
2. Providing the ability for authorised staff to access the summary care record, for which there are a range of options

Both of these aspects are covered in the documentation below.

Additional information is available at NHS Digital's summary care record site

# Compliance, Assurance and Testing

To gain access to SCR suppliers follow the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and activities are conducted.

As part of the CAP suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- External Interface Specification
- NHS Messaging Implementation Manual
- Personal Demographics Service Integration Requirements
- Summary Care Record Integration Requirements (see details below)

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

For advice, access to the documentation, and support from the NHS Business Partners programme, please contact [businesspartners@nhs.net](mailto:businesspartners@nhs.net) or visit https://digital.nhs.uk/services/nhs-business-partners

The NPFIT-SCR-SCRDOCS-0038.01 NHS CFH SCR Clinical Message Validation Process v1 document provides guidance on the clinical safety validation processes for SCR messaging.

# Documentation

## Summary Care Record Creation

GP Summaries are created and sent to the Summary Care Record repository (on Spine) via messaging from GP systems which implement the Patient Information Maintenance - GP capability.

To create summary care records and provide them to the service, suppliers must implement the requirements detailed in GP Summary Requirements v5.8.3.

Summary care messages contain XHTML information and generated messages must conform to the specification in [NPFIT-SHR-MODL-SUMREC-0025 08 GP Summary Presentation Text Specification v3.1 (Approved).xlsx](https://nhse-dsic.atlassian.net/wiki/download/attachments/11975327998/NPFIT-SHR-MODL-SUMREC-0025%2008%20GP%20Summary%20Presentation%20Text%20Specification%20v3.1%20(Approved).xlsx?version=1&modificationDate=1652188719169&cacheVersion=1&api=v2)

Implementations must comply with the NPFIT-EP-DB-0007.05 Allergy\_ADR\_Intolerance v 1.5 Draft for all representations of medication-related adverse clinical events.

Implementations must comply with the SCR GP Summary Sending Compliance v3 - Baseline Index v6.0

Message definitions are detailed in the Domain Message Specification (DMS) for Summary Care Record

Further information useful for implementers of this interface such as Use Cases, Trigger Events and Sequence Diagrams may be found in the Spine Message Implementation Manual (MIM).  NB version **4.2** is the version used for the GP Summary Update message.

Also, see MIM 4.2.00 Known Issues

## Summary Care Record Viewing

SCR viewing must be implemented in line with the Summary Care Record Permission To View Guidelines.pdf

General requirements for SCR viewing (regardless of implementation mechanism) are set out in [NPFIT-FNT-TO-DPM-0929.03 SCR Viewing Requirements v1.6 (Approved)](https://nhse-dsic.atlassian.net/wiki/download/attachments/11975327998/NPFIT-FNT-TO-DPM-0929.03%20SCR%20Viewing%20Requirements%20v1.6%20(Approved).docx?version=1&modificationDate=1652188716952&cacheVersion=1&api=v2)

Guidance for implementing Role-Based Access Control for SCR viewing is found in NPFIT-SI-SIGOV-0073 04 Guidance on Implementing RBAC for PSIS and PDS v2.0

Suppliers have a number of options for implementing summary care record viewing, as detailed below:

| Option | Description | Documentation |
| --- | --- | --- |
| 1 click | a simpler and less resource-intensive way to enable SCR viewing into local applications. This solution allows a user of an application to click and launch the SCRa in a separate window for a specific patient. | NPFIT-FNT-TO-DPM-1023 SCR 1-Click Supplier Requirements v2 7.docx |
| Spine mini services | Spine mini services (SMS) are a more lightweight way of developing read-only integration with some national Spine services. SMS Client systems allow SCR access with patient permission and for Emergency Reasons. SCR Viewing systems will be able “plug into” the SCR Spine Mini-Service functionality of the SMS Provider. The SMS Provider system provides various defined functions and services for SCR Viewing systems, e.g. the SMS Provider would retrieve GP Summaries and manage “Permission to View” on behalf of viewing systems (clients). | SCR - Spine Mini Service Provider Requirements-v1.3.docx  SCR - Spine Mini Service Client Requirement04.1.docx |
| Full SCR integration | Integration of SCR information into the GP clinical system.  A GP system retrieves GP Summaries from the Summary Care Record on Spine using the PSIS Query message and displays it via appropriate screens within the GP clinical system. | [SCR\_Viewing\_Requirements\_v3.0\_(Approved).docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/11975327998/SCR_Viewing_Requirements_v3.0_(Approved).docx?version=1&modificationDate=1652188718163&cacheVersion=1&api=v2)  Summary Care Record DMS 5.8  Message Implementation Manual (MIM 7.2) PSIS Query  NPFIT-FNT-TO-TIN-1228 14 Compliance Specification - Clinical Message Handling Addendum v4-0 (sections relevant to PSIS Query)  MIM 7.2.02 Known Issues 1.3 |

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)
- Spine Mini Services (optional)
- Authentication and Access

# Roadmap

| Title |
| --- |
| No content found. |

## Attachments

- [MIM 7 2 02 Known Issues 1.3.doc](../../../../.raw/DCSDCS/attachments/11975327998/att11975328023-MIM 7 2 02 Known Issues 1.3.doc)
- [NPFIT-FNT-TO-TIN-1228 14 Compliance Specification - Clinical Message Handling Addendum v4-0.doc](../../../../.raw/DCSDCS/attachments/11975327998/att11975328026-NPFIT-FNT-TO-TIN-1228 14 Compliance Specification - Clinical Message Handling Addendum v4-0.doc)
- [NPFIT-SI-SIGOV-0073 04 Guidance on Implementing RBAC for PSIS and PDS v2.0.doc](../../../../.raw/DCSDCS/attachments/11975327998/att11975328029-NPFIT-SI-SIGOV-0073 04 Guidance on Implementing RBAC for PSIS and PDS v2.0.doc)
- [NPFIT-FNT-TO-DPM-0929.03 SCR Viewing Requirements v1.6 (Approved).docx](../../../../.raw/DCSDCS/attachments/11975327998/att11975328032-NPFIT-FNT-TO-DPM-0929.03 SCR Viewing Requirements v1.6 (Approved).docx)
- [MIM 4.2.00 Known Issues.doc](../../../../.raw/DCSDCS/attachments/11975327998/att11975328035-MIM 4.2.00 Known Issues.doc)
- [NPFIT-EP-DB-0007.05 Allergy_ADR_Intolerance v 1.5 Draft.doc](../../../../.raw/DCSDCS/attachments/11975327998/att11975328038-NPFIT-EP-DB-0007.05 Allergy_ADR_Intolerance v 1.5 Draft.doc)
- [NPFIT-SCR-SCRDOCS-0038.01 NHS CFH SCR Clinical Message Validation Process v1.docx](../../../../.raw/DCSDCS/attachments/11975327998/att11975328041-NPFIT-SCR-SCRDOCS-0038.01 NHS CFH SCR Clinical Message Validation Process v1.docx)
- [GP Summary Requirements v5.8.3 FINAL.docx](../../../../.raw/DCSDCS/attachments/11975327998/att11975328044-GP Summary Requirements v5.8.3 FINAL.docx)
- [Summary Care Record Permission To View Guidelines.pdf](../../../../.raw/DCSDCS/attachments/11975327998/att11975328047-Summary Care Record Permission To View Guidelines.pdf)
- [SCR_Viewing_Requirements_v3.0_(Approved).docx](../../../../.raw/DCSDCS/attachments/11975327998/att11975328050-SCR_Viewing_Requirements_v3.0_(Approved).docx)
- [SCR - Spine Mini Service Client Requirement04.1.docx](../../../../.raw/DCSDCS/attachments/11975327998/att11975328053-SCR - Spine Mini Service Client Requirement04.1.docx)
- [SCR GP Summary Sending Compliance v3 - Baseline Index v6.0](../../../../.raw/DCSDCS/attachments/11975327998/att11975328056-SCR GP Summary Sending Compliance v3 - Baseline Index v6.0)
- [SCR - Spine Mini Service Provider Requirements-v1.3.docx](../../../../.raw/DCSDCS/attachments/11975327998/att11975328059-SCR - Spine Mini Service Provider Requirements-v1.3.docx)
- [NPFIT-FNT-TO-DPM-1023 SCR 1-Click Supplier Requirements v2 7.docx](../../../../.raw/DCSDCS/attachments/11975327998/att11975328062-NPFIT-FNT-TO-DPM-1023 SCR 1-Click Supplier Requirements v2 7.docx)
- [NPFIT-SHR-MODL-SUMREC-0025 08 GP Summary Presentation Text Specification v3.1 (Approved).xlsx](../../../../.raw/DCSDCS/attachments/11975327998/att11975328065-NPFIT-SHR-MODL-SUMREC-0025 08 GP Summary Presentation Text Specification v3.1 (Approved).xlsx)
