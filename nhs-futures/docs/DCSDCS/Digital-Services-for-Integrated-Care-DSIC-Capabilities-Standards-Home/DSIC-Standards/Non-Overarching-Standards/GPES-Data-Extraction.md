---
page_id: "1391134238"
space: "DCSDCS"
title: "GPES Data Extraction"
version: 20
updated: "2026-07-22T13:01:49.130Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391134238/GPES+Data+Extraction"
labels: ["standard"]
---

# GPES Data Extraction

|  |  |
| --- | --- |
| **ID** | S46 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#GPESDataExtraction-Introduction)
- [Requirements](#GPESDataExtraction-Requirements)
  - [GPES Interoperability Requirements](#GPESDataExtraction-GPESInteroperabilityRequirements)
  - [GPES Uplift Supplier Requirements](#GPESDataExtraction-GPESUpliftSupplierRequirements)
  - [GPES Uplift Reporting Pack](#GPESDataExtraction-GPESUpliftReportingPack)
  - [GPES Sizing Extracts by Complexity and Capacity](#GPESDataExtraction-GPESSizingExtractsbyComplexityandCapacity)
  - [GPES Extract Request](#GPESDataExtraction-GPESExtractRequest)
  - [Current Live Extract Specifications](#GPESDataExtraction-CurrentLiveExtractSpecifications)
- [Compliance and Assurance and Testing](#GPESDataExtraction-ComplianceandAssuranceandTesting)
- [Dependencies](#GPESDataExtraction-Dependencies)
- [Roadmap](#GPESDataExtraction-Roadmap)

# Introduction {#GPESDataExtraction-Introduction}

The General Practice Extraction Service (GPES) is a service that securely collects information, with consent from GP systems, and delivers it to approved organisations with the aim of directly improving Patient care. Further information is available at The Authority's [GPES homepage](https://digital.nhs.uk/services/general-practice-extraction-service).

# Requirements {#GPESDataExtraction-Requirements}

## GPES Interoperability Requirements  {#GPESDataExtraction-GPESInteroperabilityRequirements}

The GPES-I requirements (V6.0.1), shown below, describes the functionality and interfaces that GP systems Suppliers supporting GPES data extraction need to implement. 

[PD009 GPES Interoperabil…](../../../../attachments/DCSDCS/1391134238/att1391148528-PD009 GPES Interoperability Standard Version V 6 0 1.docx)

In addition, the following requirements have been incorporated into CCN100 with the GP system Suppliers under GPSoC for Step 2 of GPES Uplift:

## GPES Uplift Supplier Requirements  {#GPESDataExtraction-GPESUpliftSupplierRequirements}

The GPES Uplift Supplier Requirements contains the baselined set of requirements.

[GPES Uplift - Supplier R…](../../../../attachments/DCSDCS/1391134238/att1494515869-GPES Uplift - Supplier Requirements V2.3 - Post Step 2.docx)

The purpose of this document is to present the business requirements to the Supplier(s) to provide continued support for providing data collections. These collections are currently commissioned by The Authority using the General Practice Extraction Service (GPES). The requirements within this document will enable The Authority to transition from the current GPET-E process and use an alternative service to request and process the Extract Data.

GP system Suppliers and Suppliers should liaise with The Authority prior to developing any GPES requirements.

## GPES Uplift Reporting Pack {#GPESDataExtraction-GPESUpliftReportingPack}

A Supplier must refer to the Version 3.10 reporting pack when providing estimates.

[GPES Uplift Reporting Pa…](../../../../attachments/DCSDCS/1391134238/att1391149450-GPES Uplift Reporting Pack v3.10.xlsx)

## GPES Sizing Extracts by Complexity and Capacity {#GPESDataExtraction-GPESSizingExtractsbyComplexityandCapacity}

There are two kinds of data extracts that are requested through GPES (Aggregate and Patient-Level). The complexity and capacity need to be broadly understood during the elaboration to determine timescales for their development and impact on available extract capacity on the GPSS infrastructure. The information in this document provides detail on how complexity and capacity are assessed.

[Sizing extracts by compl…](../../../../attachments/DCSDCS/1391134238/att1391149473-Sizing extracts by complexity and capacity v0.4.docx)

## GPES Extract Request {#GPESDataExtraction-GPESExtractRequest}

[Extract Request - Templa…](../../../../attachments/DCSDCS/1391134238/att1494646910-Extract Request - Template v6.4.docx)

The extract request template forms the agreement between The Authority and Supplier when a new data collection is commissioned.

## Current Live Extract Specifications {#GPESDataExtraction-CurrentLiveExtractSpecifications}

The GPES Service is required to both develop and support NHS England, Public Health England (PHE) and Department of Health and Social Care (DHSC) data extractions. These data extractions are required for General Medical Services (GMS) contract practices payment and statistical and direct Patient care Information purposes. 

Details of the currently live extract specifications are available on the [GPES landing page](https://digital.nhs.uk/services/general-practice-extraction-service) on The Authority's website, while the latest version of the collection timetable can be accessed via the [GPES landing page](https://digital.nhs.uk/services/general-practice-extraction-service) hosted on The Authority's website.  Similar details are also published by the [Data Collection Board](https://digital.nhs.uk/data-and-information/information-standards/information-standards-and-data-collections-including-extractions/publications-and-notifications/standards-and-collections/gp-data-collections).

Suppliers choosing to implement the [GP Extracts Verification](../../DSIC-Capabilities/GP-Extracts-Verification.md) Capability must meet the GPES live extract specifications.

Suppliers who have any questions or concerns relating to extract parameter values, which GPES must provide to Suppliers, should contact [primarycare.domain@nhs.net](mailto:primarycare.domain@nhs.net)

A [SharePoint site for](https://hscic365.sharepoint.com/sites/GPESESEI/default.aspx) Suppliers is available which hosts information on current and planned GPES extracts. Please contact GPES team ([gpses@nhs.net](mailto:gpses@nhs.net)) for access to the site.

# Compliance and Assurance and Testing {#GPESDataExtraction-ComplianceandAssuranceandTesting}

See the General Practice Extraction Service (GPES) section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Dependencies {#GPESDataExtraction-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standard:

- [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md)

# Roadmap {#GPESDataExtraction-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Improved GP contract indicators for Index of Deprivation](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/12361236539/Improved+GP+contract+indicators+for+Index+of+Deprivation) | [GPES Data Extraction](GPES-Data-Extraction.md), [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | Draft | TBC | Uplifts to the GPES Data Extraction and indicators for GP Index of Deprivation | Uplift | Managed Capacity - Minor/Patch uplifts |

## Attachments

- [PD009 GPES Interoperability Standard Version V 6 0 1.docx](../../../../attachments/DCSDCS/1391134238/att1391148528-PD009 GPES Interoperability Standard Version V 6 0 1.docx)
- [GPES Uplift Reporting Pack v3.10.xlsx](../../../../attachments/DCSDCS/1391134238/att1391149450-GPES Uplift Reporting Pack v3.10.xlsx)
- [Sizing extracts by complexity and capacity v0.4.docx](../../../../attachments/DCSDCS/1391134238/att1391149473-Sizing extracts by complexity and capacity v0.4.docx)
- [GPES Uplift - Supplier Requirements V2.3 - Post Step 2.docx](../../../../attachments/DCSDCS/1391134238/att1494515869-GPES Uplift - Supplier Requirements V2.3 - Post Step 2.docx)
- [Extract Request - Template v6.4.docx](../../../../attachments/DCSDCS/1391134238/att1494646910-Extract Request - Template v6.4.docx)
