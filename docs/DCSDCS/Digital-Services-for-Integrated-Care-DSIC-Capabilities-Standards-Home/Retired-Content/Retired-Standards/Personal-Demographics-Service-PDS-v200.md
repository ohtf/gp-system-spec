---
page_id: "13036683282"
space: "DCSDCS"
title: "Personal Demographics Service (PDS) v2.0.0"
version: 1
updated: "2024-06-06T11:30:55.354Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/13036683282/Personal+Demographics+Service+PDS+v2.0.0"
labels: ["interop_standard_retired"]
---

# Personal Demographics Service (PDS) v2.0.0

|  |  |
| --- | --- |
| ID {#PersonalDemographicsService(PDS)v2.0.0-ID} | S56 |
| Version {#PersonalDemographicsService(PDS)v2.0.0-Version} | 2.0.0 |
| Type {#PersonalDemographicsService(PDS)v2.0.0-Type} | Interoperability Standard |
| Status {#PersonalDemographicsService(PDS)v2.0.0-Status} | Retired |
| Effective Date {#PersonalDemographicsService(PDS)v2.0.0-EffectiveDate} | 27 Sep 2022 |
| Framework(s) {#PersonalDemographicsService(PDS)v2.0.0-Framework(s)} | - GP IT Futures - Tech Innovation |

- [Introduction](#PersonalDemographicsService(PDS)v2.0.0-Introduction)
- [Requirements](#PersonalDemographicsService(PDS)v2.0.0-Requirements)
- [Compliance, Assurance and Testing](#PersonalDemographicsService(PDS)v2.0.0-Compliance,AssuranceandTesting)
  - [PDS FHIR API](#PersonalDemographicsService(PDS)v2.0.0-PDSFHIRAPI)
  - [2018 PDS Integration Requirements – v1.0 or older](#PersonalDemographicsService(PDS)v2.0.0-2018PDSIntegrationRequirements–v1.0orolder)
- [Documentation](#PersonalDemographicsService(PDS)v2.0.0-Documentation)
  - [PDS FHIR API](#PersonalDemographicsService(PDS)v2.0.0-PDSFHIRAPI.1)
  - [2018 PDS Integration Requirements – v1.0](#PersonalDemographicsService(PDS)v2.0.0-2018PDSIntegrationRequirements–v1.0)
- [Dependencies](#PersonalDemographicsService(PDS)v2.0.0-Dependencies)
  - [PDS FHIR API](#PersonalDemographicsService(PDS)v2.0.0-PDSFHIRAPI.2)
  - [2018 PDS Integration Requirements – v1.0 or older](#PersonalDemographicsService(PDS)v2.0.0-2018PDSIntegrationRequirements–v1.0orolder.1)
- [Roadmap](#PersonalDemographicsService(PDS)v2.0.0-Roadmap)

# Introduction {#PersonalDemographicsService(PDS)v2.0.0-Introduction}

The Personal Demographics Service (PDS) is the national electronic database of NHS Patient details such as name, address, date of birth and NHS Number (known as demographic information).

# Requirements  {#PersonalDemographicsService(PDS)v2.0.0-Requirements}

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| Suppliers of services which ARE currently deployed into an operational environment, and have existing PDS compliance. | PDS01 {#PersonalDemographicsService(PDS)v2.0.0-PDS01} | PDS Integration Requirements 2006-B, or a later version (e.g. 2018 PDS Integration Requirements – v1.0 or PDS FHIR API). | MUST |
| Suppliers of new services or applications (i.e. those which are NOT currently deployed into an operational environment with existing PDS compliance). | PDS02 {#PersonalDemographicsService(PDS)v2.0.0-PDS02} | Implement and maintain the Personal Demographics Service (PDS) FHIR API inline with the latest specification version. | MUST |
| All Suppliers | PDS03 {#PersonalDemographicsService(PDS)v2.0.0-PDS03} | Implement and maintain PDS Record Change Event inline with the latest version specification. See National Event Management Service (NEMS) for further information. | MUST |

All Suppliers are encouraged to work towards compliance with the latest version as above.

# Compliance, Assurance and Testing {#PersonalDemographicsService(PDS)v2.0.0-Compliance,AssuranceandTesting}

### PDS FHIR API {#PersonalDemographicsService(PDS)v2.0.0-PDSFHIRAPI}

For Suppliers of new services or applications, see the Personal Demographics Service (PDS) section on Onboarding Overview of the Digital Services for Integrated Care (DSIC) Interoperability Standards and Requirements.

### 2018 PDS Integration Requirements – v1.0 or older {#PersonalDemographicsService(PDS)v2.0.0-2018PDSIntegrationRequirements–v1.0orolder}

For Suppliers of services which ARE currently deployed into an operational environment:

Click here to view historical assurance approach

To gain access to PDS suppliers previously will have followed the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and compliance activities are conducted.

As part of the CAP suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- NHS Messaging Implementation Manual (MIM)
- External Interface Specification (EIS)
- Personal Demographics Service Integration Requirements

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

The documents that define and support the compliance assurance and testing activity for the PDS compliance module are detailed within the above mentioned Foundation Module - Baseline Index V1.0.

For advice and support from the NHS Business Partners Programme, please contact businesspartners@nhs.net or visit https://digital.nhs.uk/services/nhs-business-partners

# Documentation {#PersonalDemographicsService(PDS)v2.0.0-Documentation}

Creating a compliant implementation requires implementing the following dependent interface Standards:

### PDS FHIR API {#PersonalDemographicsService(PDS)v2.0.0-PDSFHIRAPI.1}

For Suppliers of new services or applications:

- API Catalogue - Personal Demographics Service (PDS) FHIR API
- GP software developer guide
- Testing APIs

It is recommended to read GP software developer guide in conjunction with the API documentation.

### 2018 PDS Integration Requirements – v1.0 {#PersonalDemographicsService(PDS)v2.0.0-2018PDSIntegrationRequirements–v1.0}

For Suppliers of services which ARE currently deployed into an operational environment:

Click here to view previous PDS requirements documentation

The following documents form the PDS integration baseline for local systems wishing to integrate with PDS. This new set of requirements apply to all new system suppliers wishing to complete PDS integration. Existing suppliers are not expected to implement the full scope of new requirements until '2018 PDS Integration Requirements – v1.0' is mandated for all suppliers.

- 2018 PDS Integration Requirements Matrix - v1.0.xlsx
- 2018 PDS Integration Requirements - v1.0.docx
- 2018 PDS Integration Foundation Module - Baseline Index - v1.0.docx
- 2018 PDS Integration Guidance - v1.0.docx
- 2018 PDS Integration - Additional Requirements For Existing Compliant GP Systems- v0.1.docx

The two documents below are listed in the 2018 PDS Integration Foundation Module - Baseline Index - v1.0 document as Guidance documents. They are of a historic nature but contain important information that is still relevant today.

The following document tells supplier which RBAC is relevant to PDS-related activities and enables suppliers to focus their approach accordingly. Suppliers are advised to focus their attention on sections 1, 3 and 4.

- NPFIT-SI-SIGOV-0073.05 Guidance on Implementing RBAC for PSIS and PDS v2.1.docx

The following document provides useful background information on how a supplier might support business processes relating to BUS Sensitive patient records.

- NPFIT-FNT-TO-DSD-0120.06 BUC Sensitive Patients - LocalBusiness Processes v1.0.doc

# Dependencies {#PersonalDemographicsService(PDS)v2.0.0-Dependencies}

### PDS FHIR API {#PersonalDemographicsService(PDS)v2.0.0-PDSFHIRAPI.2}

For Suppliers of new services or applications

Creating a compliant implementation requires implementing the following dependent interface Standards:

- Authentication and Access - using NHS Care Identity Service 2 API
- SDS FHIR API

### 2018 PDS Integration Requirements – v1.0 or older {#PersonalDemographicsService(PDS)v2.0.0-2018PDSIntegrationRequirements–v1.0orolder.1}

For Suppliers of services which ARE currently deployed into an operational environment:

Click here to view historical dependencies

Creating a compliant implementation previously required implementing the following dependent interface standards:

- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)
- Authentication and Access

# Roadmap {#PersonalDemographicsService(PDS)v2.0.0-Roadmap}

| **Items on the Roadmap which impact or relate to this Standard** |
| --- |
| | Title | | --- | | No content found. | |

## Attachments

- [NPFIT-FNT-TO-DSD-0120.06 BUC Sensitive Patients - LocalBusiness Processes v1.0.doc](../../../../.raw/DCSDCS/attachments/13036683282/att13036683306-NPFIT-FNT-TO-DSD-0120.06 BUC Sensitive Patients - LocalBusiness Processes v1.0.doc)
- [NPFIT-SI-SIGOV-0073.05 Guidance on Implementing RBAC for PSIS and PDS v2.1.docx](../../../../.raw/DCSDCS/attachments/13036683282/att13036683309-NPFIT-SI-SIGOV-0073.05 Guidance on Implementing RBAC for PSIS and PDS v2.1.docx)
- [2018 PDS Integration - Additional Requirements For Existing Compliant GP Systems- v0.1.docx](../../../../.raw/DCSDCS/attachments/13036683282/att13036683312-2018 PDS Integration - Additional Requirements For Existing Compliant GP Systems- v0.1.docx)
- [2018 PDS Integration Foundation Module - Baseline Index - v1.0.docx](../../../../.raw/DCSDCS/attachments/13036683282/att13036683315-2018 PDS Integration Foundation Module - Baseline Index - v1.0.docx)
- [2018 PDS Integration Guidance - v1.0.docx](../../../../.raw/DCSDCS/attachments/13036683282/att13036683318-2018 PDS Integration Guidance - v1.0.docx)
- [2018 PDS Integration Requirements - v1.0.docx](../../../../.raw/DCSDCS/attachments/13036683282/att13036683321-2018 PDS Integration Requirements - v1.0.docx)
- [2018 PDS Integration Requirements Matrix - v1.0.xlsx](../../../../.raw/DCSDCS/attachments/13036683282/att13036683324-2018 PDS Integration Requirements Matrix - v1.0.xlsx)
