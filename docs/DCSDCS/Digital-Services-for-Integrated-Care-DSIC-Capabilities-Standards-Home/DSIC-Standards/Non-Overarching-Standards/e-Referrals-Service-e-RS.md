---
page_id: "1391133966"
space: "DCSDCS"
title: "e-Referrals Service (e-RS)"
version: 18
updated: "2026-07-21T14:26:03.345Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133966/e-Referrals+Service+e-RS"
labels: ["standard"]
---

# e-Referrals Service (e-RS)

|  |  |
| --- | --- |
| **ID** | S35 |
| **Version** | 2.0.2 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 18 Jul 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#e-ReferralsService(e-RS)-Introduction)
- [Requirements](#e-ReferralsService(e-RS)-Requirements)
- [Compliance, Assurance and Testing](#e-ReferralsService(e-RS)-Compliance,AssuranceandTesting)
  - [e-Referral Service FHIR API - Primary Care Referrer](#e-ReferralsService(e-RS)-e-ReferralServiceFHIRAPI-PrimaryCareReferrer)
  - [NHS e-Referrals Service - Referrer Compliance Document v1](#e-ReferralsService(e-RS)-NHSe-ReferralsService-ReferrerComplianceDocumentv1)
- [Documentation](#e-ReferralsService(e-RS)-Documentation)
  - [e-Referral Service FHIR API - Primary Care Referrer](#e-ReferralsService(e-RS)-e-ReferralServiceFHIRAPI-PrimaryCareReferrer.1)
  - [NHS e-Referrals Service - Referrer Compliance Document v1](#e-ReferralsService(e-RS)-NHSe-ReferralsService-ReferrerComplianceDocumentv1.1)
- [Dependencies](#e-ReferralsService(e-RS)-Dependencies)
  - [e-Referral Service FHIR API - Primary Care Referrer](#e-ReferralsService(e-RS)-e-ReferralServiceFHIRAPI-PrimaryCareReferrer.2)
  - [NHS e-Referrals Service - Referrer Compliance Document v1](#e-ReferralsService(e-RS)-NHSe-ReferralsService-ReferrerComplianceDocumentv1.2)
- [Roadmap](#e-ReferralsService(e-RS)-Roadmap)

# Introduction

The NHS e-Referral Service (NHS e-RS) combines electronic booking with a choice of place, date and time for first hospital or clinic Appointments. Patients can choose their initial hospital or clinic Appointment, book it in the GP surgery at the point of referral, or later at home on the phone or online.

# Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| - Suppliers of new Solutions (i.e. those which are NOT currently deployed into an operational environment with existing e-RS compliance). - Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented the e-RS FHIR API. | ERS01 | Implement and maintain the [e-Referral Service FHIR API - Primary Care Referrer](https://digital.nhs.uk/developer/api-catalogue/e-referral-service-fhir#api-description__overview) inline with the latest specification version. | MUST |
| Suppliers of Solutions which ARE currently deployed into an operational environment, and have implemented e-RS HL7*.* | ERS02 | [NHS e-Referrals Service - Referrer Compliance Document v1.1.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133966/NHS%20e-Referrals%20Service%20-%20Referrer%20Compliance%20Document%20v1.1%20(1).docx?version=1&modificationDate=1659088340648&cacheVersion=1&api=v2) or a later version (e.g. e-Referral Service FHIR API)  Service integration is supported through the Health and Social Care Network (HSCN) -based HL7 message interactions from the[NHS Message Implementation Manual (MiM)](NHS-Messaging-Implementation-Manual-MIM.md). | MUST |

All Suppliers are encouraged to work towards compliance with the latest version as above.

# Compliance, Assurance and Testing

### e-Referral Service FHIR API - Primary Care Referrer

For Suppliers of new Solutions and Solutions that have implemented the e-RS FHIR API, see the e-Referral Service (e-RS) section on [Onboarding Overview of the Digital Services for Integrated Care (DSIC) Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md)

### NHS e-Referrals Service - Referrer Compliance Document v1

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented e-RS HL7:

Click here to view historical assurance approach

To gain access to e-RS Suppliers previously followed the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and activities are conducted.

As part of the CAP Suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- [External Interface Specification](../../Retired-Content/Retired-Standards/External-Interface-Specification-EIS-v100.md)
- [NHS Messaging Implementation Manual](NHS-Messaging-Implementation-Manual-MIM.md)
- [Personal Demographics Service Integration Requirements](../../Retired-Content/Retired-Standards/Personal-Demographics-Service-PDS-V100.md)
- e-Referrals Service Integration Requirements

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

For advice, access to the documentation, and support from the NHS Business Partners programme, please contact [businesspartners@nhs.net](mailto:businesspartners@nhs.net) or visit <https://digital.nhs.uk/services/nhs-business-partners>

The design and testing of Supplier Solutions are based upon the NHS Connecting for Health MIM version 2.3 and 3.1.09.

System Suppliers can access the updated data dictionary for the NHS e-RS. Other technical messaging documents can be found on the archived [Choose and Book site.](https://webarchive.nationalarchives.gov.uk/20160921151419/http://digital.nhs.uk/referrals)

# Documentation

### e-Referral Service FHIR API - Primary Care Referrer

For Suppliers of new Solutions and Solutions that have implemented the e-RS FHIR API:

- [API Catalogue - e-Referral Service FHIR API](https://digital.nhs.uk/developer/api-catalogue/e-referral-service-fhir)
- [GP software developer guide](https://digital.nhs.uk/developer/guides-and-documentation/building-healthcare-software/general-practice/integrating-with-national-services)
- [Testing APIs](https://digital.nhs.uk/developer/guides-and-documentation/testing)

It is recommended to read GP software developer guide in conjunction with the API documentation.

### NHS e-Referrals Service - Referrer Compliance Document v1

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented e-RS HL7.

Click here to view previous e-RS requirements documentation

Developer resources are available on the official [e-Referral Service landing page](https://digital.nhs.uk/services/nhs-e-referral-service) on NHS Digital's website; the [Document Library](https://digital.nhs.uk/services/nhs-e-referral-service/document-library)is a component part of e-RS' requirements for Suppliers seeking guidance and any implementation documentation.

If you are interested in learning more about the NHS e-RS APIs, please visit the [NHS Digital Developer Network website](https://developer.nhs.uk/apis/).

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

### e-Referral Service FHIR API - Primary Care Referrer

For Suppliers of new Solutions and Solutions that have implemented the e-RS FHIR API:

- [Personal Demographics Service (PDS)](Personal-Demographics-Service-PDS.md) - using PDS FHIR API
- [Authentication and Access](Authentication-and-Access.md) - using NHS Care Identity Service 2 API

### NHS e-Referrals Service - Referrer Compliance Document v1

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented e-RS HL7:

Click here to view historical dependencies

Creating a compliant implementation previously required implementing the following dependent interface standards:

- [Personal Demographics Service (PDS)](../../Retired-Content/Retired-Standards/Personal-Demographics-Service-PDS-V100.md) \*
- [External Interface Specification (EIS)](../../Retired-Content/Retired-Standards/External-Interface-Specification-EIS-v100.md)
- [NHS Messaging Implementation Manual (MIM)](NHS-Messaging-Implementation-Manual-MIM.md)

\*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../.raw/DCSDCS/attachments/1391133966/att1391155144-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
- [NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx](../../../../.raw/DCSDCS/attachments/1391133966/att12062228514-NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx)
- [e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml](../../../../.raw/DCSDCS/attachments/1391133966/att12062294058-e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml)
