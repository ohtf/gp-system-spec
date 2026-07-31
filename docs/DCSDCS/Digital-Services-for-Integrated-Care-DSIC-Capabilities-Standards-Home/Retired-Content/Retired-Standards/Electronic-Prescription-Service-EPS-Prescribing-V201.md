---
page_id: "11872731817"
space: "DCSDCS"
title: "Electronic Prescription Service (EPS) - Prescribing V2.0.1"
version: 2
updated: "2022-02-18T11:47:56.329Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11872731817/Electronic+Prescription+Service+EPS+-+Prescribing+V2.0.1"
labels: ["interop_standard_retired"]
---

# Electronic Prescription Service (EPS) - Prescribing V2.0.1

|  |  |
| --- | --- |
| ID | S36 |
| Version | 2.0.1 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 30 Sep 2020 |

- [Introduction](#ElectronicPrescriptionService(EPS)-PrescribingV2.0.1-Introduction)
- [Requirements](#ElectronicPrescriptionService(EPS)-PrescribingV2.0.1-Requirements)
- [Compliance and Assurance](#ElectronicPrescriptionService(EPS)-PrescribingV2.0.1-ComplianceandAssurance)
- [Testing](#ElectronicPrescriptionService(EPS)-PrescribingV2.0.1-Testing)
- [Environments](#ElectronicPrescriptionService(EPS)-PrescribingV2.0.1-Environments)
- [Documentation](#ElectronicPrescriptionService(EPS)-PrescribingV2.0.1-Documentation)
- [Dependencies](#ElectronicPrescriptionService(EPS)-PrescribingV2.0.1-Dependencies)
- [Roadmap](#ElectronicPrescriptionService(EPS)-PrescribingV2.0.1-Roadmap)

# Introduction

EPS allows prescribers (like GP Systems) to send prescriptions electronically to a dispenser (such as a pharmacy) of the patient's choice. This makes the prescribing and dispensing process more efficient and convenient for patients and staff. Please access the [EPS landing page](https://digital.nhs.uk/Electronic-Prescription-Service) on NHS Digital's website for further information.

# Requirements

| Applicable Suppliers | Requirement | Level |
| --- | --- | --- |
| Suppliers of new services or applications (i.e. those which are NOT currently deployed into an operational environment) | EPS Prescribing Systems Compliance Specification v6.11 (Document reference NPFIT-ETP-EDB-0025) | SHOULD |
| Suppliers of services which ARE currently deployed into an operational environment, and have an existing PDS compliance. | GPSoC CCN057 and EPS Prescribing Systems Compliance Specification v6.0, or a later version. | MUST |
| EPS Prescribing Systems Compliance Specification v6.11 (Document reference NPFIT-ETP-EDB-0025) Requirement 6.4.4 only | MUST |

All suppliers are encouraged to work towards compliance with the latest version as above.

# Compliance and Assurance

To gain access to EPS suppliers follow the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and activities are conducted.

As part of the CAP suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- External Interface Specification
- NHS Messaging Implementation Manual (**Note**: EPS compliance is currently using MIM 4.2.00)
- Personal Demographics Service Integration Requirements
- Electronic Prescription Service Integration Requirements

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

For advice, access to the documentation, and support from the NHS Business Partners programme, please contact businesspartners@nhs.netor visit https://digital.nhs.uk/services/nhs-business-partners

# Testing

Testing services can be accessed via the NHS Digital Solutions Assurance Team.

# Environments

EPS is a national service provided by NHS Digital as part of the Spine infrastructure. It therefore is supported on all of the Path to Live (PTL) environments.

# Documentation

Developer resources are available at the Developer resources for the Electronic Prescription Service.

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- Personal Demographics Service (PDS) \*
- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)

\*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap

| Title |
| --- |
| No content found. |