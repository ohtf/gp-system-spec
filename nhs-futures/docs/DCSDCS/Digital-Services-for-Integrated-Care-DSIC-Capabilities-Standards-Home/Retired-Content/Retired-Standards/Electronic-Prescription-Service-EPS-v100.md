---
page_id: "2493120646"
space: "DCSDCS"
title: "Electronic Prescription Service (EPS) v1.0.0"
version: 1
updated: "2020-09-30T10:28:51.524Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/2493120646/Electronic+Prescription+Service+EPS+v1.0.0"
labels: ["interop_standard_retired"]
---

# Electronic Prescription Service (EPS) v1.0.0

|  |  |
| --- | --- |
| ID | S36 |
| Version | 1.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

- [Introduction](#ElectronicPrescriptionService(EPS)v1.0.0-Introduction)
- [Requirements](#ElectronicPrescriptionService(EPS)v1.0.0-Requirements)
- [Compliance and Assurance](#ElectronicPrescriptionService(EPS)v1.0.0-ComplianceandAssurance)
- [Testing](#ElectronicPrescriptionService(EPS)v1.0.0-Testing)
- [Environments](#ElectronicPrescriptionService(EPS)v1.0.0-Environments)
- [Documentation](#ElectronicPrescriptionService(EPS)v1.0.0-Documentation)
- [Dependencies](#ElectronicPrescriptionService(EPS)v1.0.0-Dependencies)
- [Roadmap](#ElectronicPrescriptionService(EPS)v1.0.0-Roadmap)

# Introduction {#ElectronicPrescriptionService(EPS)v1.0.0-Introduction}

EPS allows prescribers (like GP Systems) to send prescriptions electronically to a dispenser (such as a pharmacy) of the patient's choice. This makes the prescribing and dispensing process more efficient and convenient for patients and staff. Please access the [EPS landing page](https://digital.nhs.uk/Electronic-Prescription-Service) on NHS Digital's website for further information.

# Requirements {#ElectronicPrescriptionService(EPS)v1.0.0-Requirements}

| Applicable Suppliers | Requirement | Level |
| --- | --- | --- |
| Suppliers of new services or applications (i.e. those which are NOT currently deployed into an operational environment) | EPS Prescribing Systems Compliance Specification v6.11 (Document reference NPFIT-ETP-EDB-0025) | SHOULD |
| Suppliers of services which ARE currently deployed into an operational environment, and have an existing PDS compliance. | GPSoC CCN057 and EPS Prescribing Systems Compliance Specification v6.0, or a later version. | MUST |

All suppliers are encouraged to work towards compliance with the latest version as above.

# Compliance and Assurance {#ElectronicPrescriptionService(EPS)v1.0.0-ComplianceandAssurance}

To gain access to EPS suppliers follow the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and activities are conducted.

As part of the CAP suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- External Interface Specification
- NHS Messaging Implementation Manual (**Note**: EPS compliance is currently using MIM 4.2.00)
- Personal Demographics Service Integration Requirements
- Electronic Prescription Service Integration Requirements

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

For advice, access to the documentation, and support from the NHS Business Partners programme, please contact businesspartners@nhs.netor visit https://digital.nhs.uk/services/nhs-business-partners

# Testing {#ElectronicPrescriptionService(EPS)v1.0.0-Testing}

Testing services can be accessed via the NHS Digital Solutions Assurance Team.

# Environments {#ElectronicPrescriptionService(EPS)v1.0.0-Environments}

EPS is a national service provided by NHS Digital as part of the Spine infrastructure. It therefore is supported on all of the Path to Live (PTL) environments.

# Documentation {#ElectronicPrescriptionService(EPS)v1.0.0-Documentation}

Developer resources are available at the Developer resources for the Electronic Prescription Service.

# Dependencies {#ElectronicPrescriptionService(EPS)v1.0.0-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface standards:

- Personal Demographics Service (PDS) \*
- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)

\*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap {#ElectronicPrescriptionService(EPS)v1.0.0-Roadmap}

| Title |
| --- |
| No content found. |