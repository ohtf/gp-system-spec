---
page_id: "12062785615"
space: "DCSDCS"
title: "e-Referrals Service (e-RS) v1.0.1"
version: 1
updated: "2022-07-29T09:26:21.842Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12062785615/e-Referrals+Service+e-RS+v1.0.1"
labels: ["interop_standard_retired"]
---

# e-Referrals Service (e-RS) v1.0.1

|  |  |
| --- | --- |
| ID | S35 |
| Version | 1.0.1 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 28 Apr 2022 |
| Framework(s) | - GP IT Futures - Tech Innovation |

- [Introduction](#e-ReferralsService(e-RS)v1.0.1-Introduction)
- [Requirements](#e-ReferralsService(e-RS)v1.0.1-Requirements)
- [Compliance, Assurance and Testing](#e-ReferralsService(e-RS)v1.0.1-Compliance,AssuranceandTesting)
  - [e-Referral Service FHIR API - Primary Care Referrer](#e-ReferralsService(e-RS)v1.0.1-e-ReferralServiceFHIRAPI-PrimaryCareReferrer)
  - [NHS e-Referrals Service - Referrer Compliance Document v1](#e-ReferralsService(e-RS)v1.0.1-NHSe-ReferralsService-ReferrerComplianceDocumentv1)
- [Documentation](#e-ReferralsService(e-RS)v1.0.1-Documentation)
  - [e-Referral Service FHIR API - Primary Care Referrer](#e-ReferralsService(e-RS)v1.0.1-e-ReferralServiceFHIRAPI-PrimaryCareReferrer.1)
  - [NHS e-Referrals Service - Referrer Compliance Document v1](#e-ReferralsService(e-RS)v1.0.1-NHSe-ReferralsService-ReferrerComplianceDocumentv1.1)
- [Dependencies](#e-ReferralsService(e-RS)v1.0.1-Dependencies)
  - [e-Referral Service FHIR API - Primary Care Referrer](#e-ReferralsService(e-RS)v1.0.1-e-ReferralServiceFHIRAPI-PrimaryCareReferrer.2)
  - [NHS e-Referrals Service - Referrer Compliance Document v1](#e-ReferralsService(e-RS)v1.0.1-NHSe-ReferralsService-ReferrerComplianceDocumentv1.2)
- [Roadmap](#e-ReferralsService(e-RS)v1.0.1-Roadmap)

# Introduction

The NHS e-Referral Service (NHS e-RS) combines electronic booking with a choice of place, date and time for first hospital or clinic Appointments. Patients can choose their initial hospital or clinic Appointment, book it in the GP surgery at the point of referral, or later at home on the phone or online.

# Requirements

| Applicable Suppliers | Requirement | Level |
| --- | --- | --- |
| Suppliers of new services or applications (i.e. those which are NOT currently deployed into an operational environment with existing e-Referral Service (e-RS) compliance). | Implement and maintain the e-Referral Service FHIR API - Primary Care Referrer inline with the latest specification version. | MUST |
| Suppliers of services which ARE currently deployed into an operational environment, and have existing e-Referral Service (e-RS) compliance. | NHS e-Referrals Service - Referrer Compliance Document v1.docx or a later version (e.g. e-Referral Service FHIR API)  Service integration is supported through the Health and Social Care Network (HSCN) -based HL7 message interactions from the NHS Message Implementation Manual (MiM). | MUST |

All suppliers are encouraged to work towards compliance with the latest version as above.

# Compliance, Assurance and Testing

### **e-Referral Service FHIR API - Primary Care Referrer**

For Suppliers of new services or applications, see the e-Referral Service (e-RS) section on Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements

### **NHS e-Referrals Service - Referrer Compliance Document v1**

For Suppliers of services which ARE currently deployed into an operational environment:

Click here to view historical assurance approach

To gain access to e-RS suppliers previously followed the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and activities are conducted.

As part of the CAP suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- External Interface Specification
- NHS Messaging Implementation Manual
- Personal Demographics Service Integration Requirements
- e-Referrals Service Integration Requirements

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

For advice, access to the documentation, and support from the NHS Business Partners programme, please contact businesspartners@nhs.netor visit https://digital.nhs.uk/services/nhs-business-partners

The design and testing of Supplier Solutions are based upon the NHS Connecting for Health MIM version 2.3 and 3.1.09.

System Suppliers can access the updated data dictionary for the NHS e-RS. Other technical messaging documents can be found on the archived Choose and Book site.

# Documentation

### **e-Referral Service FHIR API - Primary Care Referrer**

For Suppliers of new services or applications:

- API Catalogue - e-Referral Service FHIR API
- GP software developer guide
- Testing APIs

It is recommended to read GP software developer guide in conjunction with the API documentation.

### **NHS e-Referrals Service - Referrer Compliance Document v1**

For Suppliers of services which ARE currently deployed into an operational environment.

Click here to view previous e-RS requirements documentation

Developer resources are available on the official e-Referral Service landing page on NHS Digital's website; the Document Library is a component part of e-RS' requirements for suppliers seeking guidance and any implementation documentation. 

If you are interested in learning more about the NHS e-RS APIs, please visit the NHS Digital Developer Network website.

# Dependencies

### e-Referral Service FHIR API - Primary Care Referrer

For Suppliers of new services or applications:

- Personal Demographics Service (PDS) - using PDS FHIR API
- Authentication and Access - using NHS Care Identity Service 2 API

### NHS e-Referrals Service - Referrer Compliance Document v1

For Suppliers of services which ARE currently deployed into an operational environment:

Click here to view historical dependencies

Creating a compliant implementation previously required implementing the following dependent interface standards:

- Personal Demographics Service (PDS) \*
- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)

\*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../.raw/DCSDCS/attachments/12062785615/att12062785645-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
