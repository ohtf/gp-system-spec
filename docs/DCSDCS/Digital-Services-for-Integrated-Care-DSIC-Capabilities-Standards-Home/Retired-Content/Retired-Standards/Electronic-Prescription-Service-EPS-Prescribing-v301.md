---
page_id: "14225506374"
space: "DCSDCS"
title: "Electronic Prescription Service (EPS) - Prescribing v3.0.1"
version: 1
updated: "2025-07-04T06:54:26.228Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14225506374/Electronic+Prescription+Service+EPS+-+Prescribing+v3.0.1"
labels: ["standard_retired"]
---

# Electronic Prescription Service (EPS) - Prescribing v3.0.1

|  |  |
| --- | --- |
| ID | S36 |
| Version | 3.0.1 |
| Type | Standard |
| Status | Retired |
| Effective Date | 28 Apr 2022 |
| Contracting Vehicle(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) |

- [Introduction](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-Introduction)
- [Requirements](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-Requirements)
- [Compliance, Assurance and Testing](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-Compliance,AssuranceandTesting)
  - [EPS FHIR API - Prescribing API](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-EPSFHIRAPI-PrescribingAPI)
  - [EPS Prescribing Systems Compliance Specification v6.11 or older](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-EPSPrescribingSystemsComplianceSpecificationv6.11orolder)
- [Documentation](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-Documentation)
  - [EPS FHIR API - Prescribing API](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-EPSFHIRAPI-PrescribingAPI.1)
  - [EPS Prescribing Systems Compliance Specification v6.11 or older](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-EPSPrescribingSystemsComplianceSpecificationv6.11orolder.1)
- [Dependencies](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-Dependencies)
  - [EPS FHIR API - Prescribing API](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-EPSFHIRAPI-PrescribingAPI.2)
  - [EPS Prescribing Systems Compliance Specification v6.11 or older](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-EPSPrescribingSystemsComplianceSpecificationv6.11orolder.2)
- [Roadmap](#ElectronicPrescriptionService(EPS)-Prescribingv3.0.1-Roadmap)

# Introduction

Electronic Prescription Service (EPS) allows prescribers (like those using GP Systems) to send Prescriptions electronically to a dispenser (such as a pharmacy) of the Patient's choice. This makes the prescribing and dispensing process more efficient and convenient for Patients and staff. Please access the [EPS landing page](https://digital.nhs.uk/Electronic-Prescription-Service) on The Authority's website for further information.

# Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| Suppliers of new services or applications (i.e. those which are NOT currently deployed into an operational environment with existing Electronic Prescription Service (EPS) compliance). | EPSP01 | Implement and maintain the Electronic Prescription Service (EPS) FHIR API - Prescribing API inline with the latest specification version. | MUST |
| Suppliers of services which ARE currently deployed into an operational environment, and have existing Electronic Prescription Service (EPS) compliance. | EPSP02 | GPSoC CCN057 and EPS Prescribing Systems Compliance Specification v6.0, or a later version. | MUST |
| EPSP03 | EPS Prescribing Systems Compliance Specification v6.11 (Document reference NPFIT-ETP-EDB-0025) Requirement 6.4.4 only | MUST |
| EPSP04 | *EPS Prescribing Systems Compliance Specification v6.11 (Document reference NPFIT-ETP-EDB-0025) Requirement 5.2.1, 5.2.5, 5.2.7, 6.7.7, 6.7.8, 6.9.10 only* | MUST |

All Suppliers are encouraged to work towards compliance with the latest version as above.

# Compliance, Assurance and Testing

### EPS FHIR API - Prescribing API

For Suppliers of new services or applications, see the Electronic Prescription Service (EPS) section on Onboarding Overview of the Digital Services for Integrated Care (DSIC) Interoperability Standards and Requirements.

### EPS Prescribing Systems Compliance Specification v6.11 or older

For Suppliers of services which ARE currently deployed into an operational environment:

Click here to view historical assurance approach

To gain access to EPS Suppliers previously followed the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and activities are conducted.

As part of the CAP Suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- External Interface Specification
- NHS Messaging Implementation Manual (**Note**: EPS compliance is currently using MIM 4.2.00)
- Personal Demographics Service Integration Requirements
- Electronic Prescription Service Integration Requirements

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

For advice, access to the documentation, and support from the NHS Business Partners programme, please contact businesspartners@nhs.net or visithttps://digital.nhs.uk/services/nhs-business-partners

Testing services can be accessed via the NHS Digital Solutions Assurance Team.

EPS is a national service provided by NHS Digital as part of the Spine infrastructure. It therefore is supported on all of the Path to Live (PTL) environments.

# Documentation

### EPS FHIR API - Prescribing API

For Suppliers of new services or applications:

- API Catalogue - Electronic Prescription Service (EPS) FHIR API
- GP software developer guide
- Testing APIs

It is recommended to read GP software developer guide in conjunction with the API documentation.

### EPS Prescribing Systems Compliance Specification v6.11 or older

For Suppliers of services which ARE currently deployed into an operational environment:

Click here to view previous EPS requirements documentation

Developer resources are available at the Developer resources for the Electronic Prescription Service.

# Dependencies

### EPS FHIR API - Prescribing API

For Suppliers of new services or applications:

Creating a compliant implementation requires implementing the following dependent interface standards:

- Personal Demographics Service (PDS) - using PDS FHIR API
- Authentication and Access - using NHS Care Identity Service 2 API
- Signing Service API

### EPS Prescribing Systems Compliance Specification v6.11 or older

For Suppliers of services which ARE currently deployed into an operational environment:

Click here to view historical dependencies

Creating a compliant implementation previously required implementing the following dependent interface standards:

- Personal Demographics Service (PDS) \*
- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)

\*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Directory of Healthcare Services (DoHS) (Service Search) API V3](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14592573441/Directory+of+Healthcare+Services+DoHS+Service+Search+API+V3) | [Electronic Prescription Service (EPS) - Prescribing](../../DSIC-Standards/Non-Overarching-Standards/Electronic-Prescription-Service-EPS-Prescribing.md) | Draft | TBC | GP Suppliers to implement the Directory of Healthcare Services (DoHS) (Service Search) API V3 | Uplift | Managed Capacity - Other |

## Attachments

- [EPS Prescribing Systems Compliance Specification v6-10.pdf](../../../../.raw/DCSDCS/attachments/14225506374/att14225506400-EPS Prescribing Systems Compliance Specification v6-10.pdf)
- [EPS Prescribing Systems Compliance Specification v6-10.docx](../../../../.raw/DCSDCS/attachments/14225506374/att14225506403-EPS Prescribing Systems Compliance Specification v6-10.docx)
- [EPS+v6.10.doc](../../../../.raw/DCSDCS/attachments/14225506374/att14225506406-EPS+v6.10.doc)
- [EPS Compliance Specification v6.9.pdf](../../../../.raw/DCSDCS/attachments/14225506374/att14225506409-EPS Compliance Specification v6.9.pdf)
- [EPS_Prescribing_Systems_Compliance_Specification_-_3_June_2016.pdf](../../../../.raw/DCSDCS/attachments/14225506374/att14225506412-EPS_Prescribing_Systems_Compliance_Specification_-_3_June_2016.pdf)
- [image2017-12-15_14-24-50.png](../../../../.raw/DCSDCS/attachments/14225506374/att14225506415-image2017-12-15_14-24-50.png)
- [image2017-12-15_13-11-32.png](../../../../.raw/DCSDCS/attachments/14225506374/att14225506418-image2017-12-15_13-11-32.png)
