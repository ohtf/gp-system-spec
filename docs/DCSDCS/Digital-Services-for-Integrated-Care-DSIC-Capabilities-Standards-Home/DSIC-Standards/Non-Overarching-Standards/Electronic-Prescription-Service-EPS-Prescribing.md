---
page_id: "1391133858"
space: "DCSDCS"
title: "Electronic Prescription Service (EPS) - Prescribing"
version: 23
updated: "2026-07-21T14:26:43.089Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133858/Electronic+Prescription+Service+EPS+-+Prescribing"
labels: ["standard"]
---

# Electronic Prescription Service (EPS) - Prescribing

|  |  |
| --- | --- |
| **ID** | S36 |
| **Version** | 4.0.2 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 18 Jul 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#ElectronicPrescriptionService(EPS)-Prescribing-Introduction)
- [Requirements](#ElectronicPrescriptionService(EPS)-Prescribing-Requirements)
- [Compliance, Assurance and Testing](#ElectronicPrescriptionService(EPS)-Prescribing-Compliance,AssuranceandTesting)
  - [EPS FHIR API - Prescribing API](#ElectronicPrescriptionService(EPS)-Prescribing-EPSFHIRAPI-PrescribingAPI)
  - [EPS Prescribing Systems Compliance Specification v6.11 or older](#ElectronicPrescriptionService(EPS)-Prescribing-EPSPrescribingSystemsComplianceSpecificationv6.11orolder)
- [Documentation](#ElectronicPrescriptionService(EPS)-Prescribing-Documentation)
  - [EPS FHIR API - Prescribing API](#ElectronicPrescriptionService(EPS)-Prescribing-EPSFHIRAPI-PrescribingAPI.1)
  - [EPS Prescribing Systems Compliance Specification v6.11 or older](#ElectronicPrescriptionService(EPS)-Prescribing-EPSPrescribingSystemsComplianceSpecificationv6.11orolder.1)
- [Dependencies](#ElectronicPrescriptionService(EPS)-Prescribing-Dependencies)
  - [EPS FHIR API - Prescribing API](#ElectronicPrescriptionService(EPS)-Prescribing-EPSFHIRAPI-PrescribingAPI.2)
  - [EPS Prescribing Systems Compliance Specification v6.11 or older](#ElectronicPrescriptionService(EPS)-Prescribing-EPSPrescribingSystemsComplianceSpecificationv6.11orolder.2)
- [Roadmap](#ElectronicPrescriptionService(EPS)-Prescribing-Roadmap)

# Introduction {#ElectronicPrescriptionService(EPS)-Prescribing-Introduction}

Electronic Prescription Service (EPS) allows prescribers (like those using GP Systems) to send Prescriptions electronically to a dispenser (such as a pharmacy) of the Patient's choice. This makes the prescribing and dispensing process more efficient and convenient for Patients and staff. Please access the [EPS landing page](https://digital.nhs.uk/Electronic-Prescription-Service) on The Authority's website for further information.

# Requirements {#ElectronicPrescriptionService(EPS)-Prescribing-Requirements}

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| - Suppliers of new Solutions (i.e. those which are NOT currently deployed into an operational environment with existing EPS compliance). - Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented the EPS FHIR API. | EPSP01 | Implement and maintain the [Electronic Prescription Service (EPS) FHIR API - Prescribing API](https://digital.nhs.uk/developer/api-catalogue/electronic-prescription-service-fhir) inline with the latest specification version. | MUST |
| Suppliers of Solutions which ARE currently deployed into an operational environment, and have implemented EPS HL7*.* | EPSP02 | GPSoC CCN057 and EPS Prescribing Systems Compliance Specification v6.0, or a later version. | MUST |
| EPSP03 | [EPS Prescribing Systems Compliance Specification v6.11 (Document reference NPFIT-ETP-EDB-0025](https://gpitbjss.atlassian.net/wiki/download/attachments/2335604773/eps-prescribing-systems-compliance-specification-v6_11.pdf?version=1&modificationDate=1629972019211&cacheVersion=1&api=v2)) Requirement 6.4.4 only | MUST |
| EPSP04 | [EPS Prescribing Systems Compliance Specification v6.11 (Document reference NPFIT-ETP-EDB-0025)](https://gpitbjss.atlassian.net/wiki/download/attachments/2335604773/eps-prescribing-systems-compliance-specification-v6_11.pdf?version=1&modificationDate=1629972019211&cacheVersion=1&api=v2) Requirement 5.2.1, 5.2.5, 5.2.7, 6.7.7, 6.7.8, 6.9.10 only | MUST |
| GP Suppliers | EPSP05 | All EPS Prescriptions to be signed using SHA-256.  The Authority has made SHA-256 [Signing API Packages](https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fssp.dirteam.nhs.uk%2Fdir%2Fdownloads%2Fsigningapi%2F&data=05%7C02%7Cmartin.eland1%40nhs.net%7C8533812b22dc4c09f1cd08dd4ce569af%7C37c354b285b047f5b22207b48d774ee3%7C0%7C0%7C638751270372525873%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=AAMs9XVWMKtxK3hYVGUlNwgyh3NHzbScCAEb28SbSlE%3D&reserved=0) available that Suppliers could optionally use as part of their implementation.  See [NIST - Hash Functions](https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcsrc.nist.gov%2Fprojects%2Fhash-functions&data=05%7C02%7Cmartin.eland1%40nhs.net%7C8533812b22dc4c09f1cd08dd4ce569af%7C37c354b285b047f5b22207b48d774ee3%7C0%7C0%7C638751270372548559%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=ulOsg3pm%2FneLANiDMBiSDGaPydsxgSo%2FxlEYRWdEnkU%3D&reserved=0) for further information. | MUST |

All Suppliers are encouraged to work towards compliance with the latest version as above.

# Compliance, Assurance and Testing {#ElectronicPrescriptionService(EPS)-Prescribing-Compliance,AssuranceandTesting}

### EPS FHIR API - Prescribing API {#ElectronicPrescriptionService(EPS)-Prescribing-EPSFHIRAPI-PrescribingAPI}

For Suppliers of new Solutions and Solutions that have implemented the EPS FHIR API, see the Electronic Prescription Service (EPS) section on [Onboarding Overview of the Digital Services for Integrated Care (DSIC) Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

### EPS Prescribing Systems Compliance Specification v6.11 or older {#ElectronicPrescriptionService(EPS)-Prescribing-EPSPrescribingSystemsComplianceSpecificationv6.11orolder}

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented EPS HL7:

Click here to view historical assurance approach

To gain access to EPS Suppliers previously followed the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and activities are conducted.

As part of the CAP Suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- [External Interface Specification](../../Retired-Content/Retired-Standards/Personal-Demographics-Service-PDS-V100.md)
- [NHS Messaging Implementation Manual](NHS-Messaging-Implementation-Manual-MIM.md) (**Note**: EPS compliance is currently using MIM 4.2.00)
- [Personal Demographics Service Integration Requirements](../../Retired-Content/Retired-Standards/Personal-Demographics-Service-PDS-V100.md)
- Electronic Prescription Service Integration Requirements

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

For advice, access to the documentation, and support from the NHS Business Partners programme, please contact[businesspartners@nhs.net](mailto:businesspartners@nhs.net)or visit<https://digital.nhs.uk/services/nhs-business-partners>

Testing services can be accessed via the NHS Digital Solutions Assurance Team.

EPS is a national service provided by NHS Digital as part of the Spine infrastructure. It therefore is supported on all of the Path to Live (PTL) environments.

# Documentation {#ElectronicPrescriptionService(EPS)-Prescribing-Documentation}

### EPS FHIR API - Prescribing API {#ElectronicPrescriptionService(EPS)-Prescribing-EPSFHIRAPI-PrescribingAPI.1}

For Suppliers of new Solutions and Solutions that have implemented the EPS FHIR API:

- [API Catalogue - Electronic Prescription Service (EPS) FHIR API](https://digital.nhs.uk/developer/api-catalogue/electronic-prescription-service-fhir)
- [GP software - integrating with national services](https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdigital.nhs.uk%2Fdeveloper%2Fguides-and-documentation%2Fbuilding-healthcare-software%2Fgeneral-practice%2Fintegrating-with-national-services&data=05%7C02%7Cmartin.eland1%40nhs.net%7Ca682bd53c0e14ed6839108ddc370a5d7%7C37c354b285b047f5b22207b48d774ee3%7C0%7C0%7C638881610823922146%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=ear5ln0uPKtupVzjn7n%2BiPLQ47hdnwJ6%2Fhcq83P5tc0%3D&reserved=0)
- [Testing APIs](https://digital.nhs.uk/developer/guides-and-documentation/testing)

It is recommended to read GP software developer guide in conjunction with the API documentation.

### EPS Prescribing Systems Compliance Specification v6.11 or older {#ElectronicPrescriptionService(EPS)-Prescribing-EPSPrescribingSystemsComplianceSpecificationv6.11orolder.1}

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented EPS HL7.

Click here to view previous EPS requirements documentation

Developer resources are available at the [Developer resources for the Electronic Prescription Service](https://digital.nhs.uk/services/electronic-prescription-service/developer-resources-for-eps).

# Dependencies {#ElectronicPrescriptionService(EPS)-Prescribing-Dependencies}

### EPS FHIR API - Prescribing API {#ElectronicPrescriptionService(EPS)-Prescribing-EPSFHIRAPI-PrescribingAPI.2}

For Suppliers of new Solutions and Solutions that have implemented the EPS FHIR API:

Creating a compliant implementation requires implementing the following dependent interface standards:

- [Personal Demographics Service (PDS)](Personal-Demographics-Service-PDS.md) - using PDS FHIR API
- [Authentication and Access](Authentication-and-Access.md) - using NHS Care Identity Service 2 API
- [Digital Signature Service API](https://digital.nhs.uk/developer/api-catalogue/signing-service)

### EPS Prescribing Systems Compliance Specification v6.11 or older {#ElectronicPrescriptionService(EPS)-Prescribing-EPSPrescribingSystemsComplianceSpecificationv6.11orolder.2}

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented EPS HL7.

Click here to view historical dependencies

Creating a compliant implementation previously required implementing the following dependent interface standards:

- [Personal Demographics Service (PDS)](../../Retired-Content/Retired-Standards/Personal-Demographics-Service-PDS-V100.md) \*
- [External Interface Specification (EIS)](../../Retired-Content/Retired-Standards/External-Interface-Specification-EIS-v100.md)
- [NHS Messaging Implementation Manual (MIM)](NHS-Messaging-Implementation-Manual-MIM.md)

\*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap {#ElectronicPrescriptionService(EPS)-Prescribing-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Directory of Healthcare Services (DoHS) (Service Search) API V3](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14592573441/Directory+of+Healthcare+Services+DoHS+Service+Search+API+V3) | [Electronic Prescription Service (EPS) - Prescribing](Electronic-Prescription-Service-EPS-Prescribing.md) | Draft | TBC | GP Suppliers to implement the Directory of Healthcare Services (DoHS) (Service Search) API V3 | Uplift | Managed Capacity - Other |

## Attachments

- [image2017-12-15_13-11-32.png](../../../../attachments/DCSDCS/1391133858/att1391140256-image2017-12-15_13-11-32.png)
- [image2017-12-15_14-24-50.png](../../../../attachments/DCSDCS/1391133858/att1391140257-image2017-12-15_14-24-50.png)
- [EPS_Prescribing_Systems_Compliance_Specification_-_3_June_2016.pdf](../../../../attachments/DCSDCS/1391133858/att1391140271-EPS_Prescribing_Systems_Compliance_Specification_-_3_June_2016.pdf)
- [EPS Compliance Specification v6.9.pdf](../../../../attachments/DCSDCS/1391133858/att1391140845-EPS Compliance Specification v6.9.pdf)
- [EPS+v6.10.doc](../../../../attachments/DCSDCS/1391133858/att1391155442-EPS+v6.10.doc)
- [EPS Prescribing Systems Compliance Specification v6-10.docx](../../../../attachments/DCSDCS/1391133858/att1391155560-EPS Prescribing Systems Compliance Specification v6-10.docx)
- [EPS Prescribing Systems Compliance Specification v6-10.pdf](../../../../attachments/DCSDCS/1391133858/att1391155564-EPS Prescribing Systems Compliance Specification v6-10.pdf)
