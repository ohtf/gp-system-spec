---
page_id: "1391133999"
space: "DCSDCS"
title: "Personal Demographics Service (PDS)"
version: 31
updated: "2026-07-22T13:11:13.698Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133999/Personal+Demographics+Service+PDS"
labels: ["standard"]
---

# Personal Demographics Service (PDS)

|  |  |
| --- | --- |
| **ID** | S56 |
| **Version** | 3.0.3 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 03 Jul 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#PersonalDemographicsService(PDS)-Introduction)
- [Requirements](#PersonalDemographicsService(PDS)-Requirements)

  - [GP Suppliers](#PersonalDemographicsService(PDS)-GPSuppliers)
  - [Community Pharmacy Suppliers](#PersonalDemographicsService(PDS)-CommunityPharmacySuppliers)- [Functionality Mapping](#PersonalDemographicsService(PDS)-FunctionalityMapping)
- [Compliance, Assurance and Testing](#PersonalDemographicsService(PDS)-Compliance,AssuranceandTesting)
  - [PDS FHIR API](#PersonalDemographicsService(PDS)-PDSFHIRAPI)
  - [2018 PDS Integration Requirements – v1.0 or older](#PersonalDemographicsService(PDS)-2018PDSIntegrationRequirements–v1.0orolder)
- [Documentation](#PersonalDemographicsService(PDS)-Documentation)
  - [PDS FHIR API](#PersonalDemographicsService(PDS)-PDSFHIRAPI.1)
  - [2018 PDS Integration Requirements – v1.0](#PersonalDemographicsService(PDS)-2018PDSIntegrationRequirements–v1.0)
- [Dependencies](#PersonalDemographicsService(PDS)-Dependencies)
  - [PDS FHIR API](#PersonalDemographicsService(PDS)-PDSFHIRAPI.2)
  - [2018 PDS Integration Requirements – v1.0 or older](#PersonalDemographicsService(PDS)-2018PDSIntegrationRequirements–v1.0orolder.1)
- [Roadmap](#PersonalDemographicsService(PDS)-Roadmap)

# Introduction {#PersonalDemographicsService(PDS)-Introduction}

The Personal Demographics Service (PDS) is the national electronic database of NHS Patient details such as name, address, date of birth and NHS Number (known as demographic information).

# Requirements  {#PersonalDemographicsService(PDS)-Requirements}

### GP Suppliers {#PersonalDemographicsService(PDS)-GPSuppliers}

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| Suppliers of Solutions which ARE currently deployed into an operational environment, and have implemented PDS HL7 | PDS01 | PDS Integration Requirements 2006-B, or a later version (e.g. 2018 PDS Integration Requirements – v1.0 or PDS FHIR API). | MUST |
| - Suppliers of new Solutions (i.e. those which are NOT currently deployed into an operational environment with existing PDS compliance). - Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented the PDS FHIR API. | PDS02 | Implement and maintain the [Personal Demographics Service (PDS) FHIR API](https://digital.nhs.uk/developer/api-catalogue/personal-demographics-service-fhir) inline with the latest specification version as per Functionality Mapping section. | MUST |

### Community Pharmacy Suppliers {#PersonalDemographicsService(PDS)-CommunityPharmacySuppliers}

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| Community Pharmacy Suppliers | PDS04 | Implement and maintain the [Personal Demographics Service (PDS) FHIR API](https://digital.nhs.uk/developer/api-catalogue/personal-demographics-service-fhir) inline with the latest specification version as per Functionality Mapping section. | MUST |

All Suppliers are encouraged to work towards compliance with the latest version as above.

## Functionality Mapping {#PersonalDemographicsService(PDS)-FunctionalityMapping}

| **Applicable Capability** | **Search for a Patient** | **Get Patient details** | **Update Patient details** |
| --- | --- | --- | --- |
| [Consultation Management - Community Pharmacy](../../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) | (tick) | (tick) | (error) |
| [Online Patient Consultation](../../DSIC-Capabilities/Online-Patient-Consultation.md) | (tick) | (tick) | (error) |
| [Online Patient Request](../../DSIC-Capabilities/Online-Patient-Request.md) | (tick) | (tick) | (error) |
| [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | (tick) | (tick) | (tick) |

# Compliance, Assurance and Testing {#PersonalDemographicsService(PDS)-Compliance,AssuranceandTesting}

### PDS FHIR API {#PersonalDemographicsService(PDS)-PDSFHIRAPI}

For Suppliers of new Solutions, Solutions which ARE currently deployed into an operational environment and have implemented the PDS FHIR API, and Community Pharmacy Solutions, see the Personal Demographics Service (PDS) section in [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

### 2018 PDS Integration Requirements – v1.0 or older {#PersonalDemographicsService(PDS)-2018PDSIntegrationRequirements–v1.0orolder}

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented PDS HL7:

Click here to view historical assurance approach

To gain access to PDS Suppliers previously will have followed the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and compliance activities are conducted.

As part of the CAP Suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- [NHS Messaging Implementation Manual (MIM)](NHS-Messaging-Implementation-Manual-MIM.md)
- [External Interface Specification (EIS)](External-Interface-Specification-EIS.md)
- Personal Demographics Service Integration Requirements

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

The documents that define and support the compliance assurance and testing activity for the PDS compliance module are detailed within the above mentioned Foundation Module - Baseline Index V1.0.

For advice and support from the NHS Business Partners Programme, please contact [businesspartners@nhs.net](mailto:businesspartners@nhs.net) or visit <https://digital.nhs.uk/services/nhs-business-partners>

# Documentation {#PersonalDemographicsService(PDS)-Documentation}

### PDS FHIR API {#PersonalDemographicsService(PDS)-PDSFHIRAPI.1}

For Suppliers of new Solutions, Solutions which ARE currently deployed into an operational environment and have implemented the PDS FHIR API, and Community Pharmacy Solutions:

- [API Catalogue - Personal Demographics Service (PDS) FHIR API](https://digital.nhs.uk/developer/api-catalogue/personal-demographics-service-fhir)
- [GP software developer guide](https://digital.nhs.uk/developer/guides-and-documentation/building-healthcare-software)
- [Testing APIs](https://digital.nhs.uk/developer/guides-and-documentation/testing)

It is recommended to read GP software developer guide in conjunction with the API documentation.

### 2018 PDS Integration Requirements – v1.0 {#PersonalDemographicsService(PDS)-2018PDSIntegrationRequirements–v1.0}

For Suppliers of Solutions which ARE currently deployed into an operational environment, and have implemented PDS HL7:

Click here to view previous PDS requirements documentation

The following documents form the PDS integration baseline for local systems wishing to integrate with PDS. This new set of requirements apply to all new system suppliers wishing to complete PDS integration. Existing suppliers are not expected to implement the full scope of new requirements until '2018 PDS Integration Requirements – v1.0' is mandated for all Suppliers.

- [2018 PDS Integration Requirements Matrix - v1.0.xlsx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133999/2018%20PDS%20Integration%20Requirements%20Matrix%20-%20v1.0.xlsx?version=1&modificationDate=1524480281191&cacheVersion=1&api=v2)
- [2018 PDS Integration Requirements - v1.0.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133999/2018%20PDS%20Integration%20Requirements%20-%20v1.0.docx?version=1&modificationDate=1524480287339&cacheVersion=1&api=v2)
- [2018 PDS Integration Foundation Module - Baseline Index - v1.0.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133999/2018%20PDS%20Integration%20Foundation%20Module%20-%20Baseline%20Index%20-%20v1.0.docx?version=1&modificationDate=1524480297477&cacheVersion=1&api=v2)
- [2018 PDS Integration Guidance - v1.0.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133999/2018%20PDS%20Integration%20Guidance%20-%20v1.0.docx?version=1&modificationDate=1524480294012&cacheVersion=1&api=v2)
- [2018 PDS Integration - Additional Requirements For Existing Compliant GP Systems- v0.1.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133999/2018%20PDS%20Integration%20-%20Additional%20Requirements%20For%20Existing%20Compliant%20GP%20Systems-%20v0.1.docx?version=1&modificationDate=1524732474267&cacheVersion=1&api=v2)

The two documents below are listed in the 2018 PDS Integration Foundation Module - Baseline Index - v1.0 document as Guidance documents. They are of a historic nature but contain important information that is still relevant today.

The following document tells Supplier which RBAC is relevant to PDS-related activities and enables Suppliers to focus their approach accordingly. Suppliers are advised to focus their attention on sections 1, 3 and 4.

- [NPFIT-SI-SIGOV-0073.05 Guidance on Implementing RBAC for PSIS and PDS v2.1.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133999/NPFIT-SI-SIGOV-0073.05%20Guidance%20on%20Implementing%20RBAC%20for%20PSIS%20and%20PDS%20v2.1.docx?version=1&modificationDate=1545131256518&cacheVersion=1&api=v2)

The following document provides useful background information on how a Supplier might support business processes relating to BUS Sensitive patient records.

- [NPFIT-FNT-TO-DSD-0120.06 BUC Sensitive Patients - LocalBusiness Processes v1.0.doc](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133999/NPFIT-FNT-TO-DSD-0120.06%20BUC%20Sensitive%20Patients%20-%20LocalBusiness%20Processes%20v1.0.doc?version=2&modificationDate=1653996236157&cacheVersion=1&api=v2)

# Dependencies {#PersonalDemographicsService(PDS)-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface standards:

### PDS FHIR API {#PersonalDemographicsService(PDS)-PDSFHIRAPI.2}

For Suppliers of new Solutions, Solutions which ARE currently deployed into an operational environment and have implemented the PDS FHIR API, and Community Pharmacy Solutions (using Healthcare worker access).

- [Authentication and Access](Authentication-and-Access.md) - using NHS Care Identity Service 2 API

### 2018 PDS Integration Requirements – v1.0 or older {#PersonalDemographicsService(PDS)-2018PDSIntegrationRequirements–v1.0orolder.1}

For Suppliers of Solutions which ARE currently deployed into an operational environment, and have implemented PDS HL7:

Click here to view historical dependencies

Creating a compliant implementation previously required implementing the following dependent interface Standards:

- [External Interface Specification (EIS)](../../Retired-Content/Retired-Standards/External-Interface-Specification-EIS-v100.md)
- [NHS Messaging Implementation Manual (MIM)](NHS-Messaging-Implementation-Manual-MIM.md)
- [Authentication and Access](Authentication-and-Access.md)

# Roadmap {#PersonalDemographicsService(PDS)-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NPFIT-FNT-TO-DSD-0120.06 BUC Sensitive Patients - LocalBusiness Processes v1.0.doc](../../../../.raw/DCSDCS/attachments/1391133999/att1391148376-NPFIT-FNT-TO-DSD-0120.06 BUC Sensitive Patients - LocalBusiness Processes v1.0.doc)
- [NPFIT-SI-SIGOV-0073.05 Guidance on Implementing RBAC for PSIS and PDS v2.1.docx](../../../../.raw/DCSDCS/attachments/1391133999/att1391148377-NPFIT-SI-SIGOV-0073.05 Guidance on Implementing RBAC for PSIS and PDS v2.1.docx)
- [2018 PDS Integration Foundation Module - Baseline Index - v1.0.docx](../../../../.raw/DCSDCS/attachments/1391133999/att1391155511-2018 PDS Integration Foundation Module - Baseline Index - v1.0.docx)
- [2018 PDS Integration Guidance - v1.0.docx](../../../../.raw/DCSDCS/attachments/1391133999/att1391155512-2018 PDS Integration Guidance - v1.0.docx)
- [2018 PDS Integration Requirements - v1.0.docx](../../../../.raw/DCSDCS/attachments/1391133999/att1391155516-2018 PDS Integration Requirements - v1.0.docx)
- [2018 PDS Integration - Additional Requirements For Existing Compliant GP Systems- v0.1.docx](../../../../.raw/DCSDCS/attachments/1391133999/att1391155561-2018 PDS Integration - Additional Requirements For Existing Compliant GP Systems- v0.1.docx)
- [2018 PDS Integration Requirements Matrix - v1.0.xlsx](../../../../.raw/DCSDCS/attachments/1391133999/att1391155563-2018 PDS Integration Requirements Matrix - v1.0.xlsx)
