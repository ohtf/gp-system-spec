---
page_id: "11235885752"
space: "DCSDCS"
title: "Interoperability Standard v7.0.0"
version: 1
updated: "2021-05-13T11:27:18.818Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11235885752/Interoperability+Standard+v7.0.0"
labels: ["interop_standard_retired"]
---

# Interoperability Standard v7.0.0

|  |  |
| --- | --- |
| ID | S32 |
| Version | 7.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 28 Feb 2021 |

/\*<![CDATA[\*/
div.rbtoc1785509354807 {padding: 0px;}
div.rbtoc1785509354807 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785509354807 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#InteroperabilityStandardv7.0.0-Introduction)
- [Notes on quality and consistency of interface documentation](#InteroperabilityStandardv7.0.0-Notesonqualityandconsistencyofinterfacedocumentation)
- [Interoperability principles](#InteroperabilityStandardv7.0.0-Interoperabilityprinciples)
  - [Interoperability non-functional requirements](#InteroperabilityStandardv7.0.0-Interoperabilitynon-functionalrequirements)
  - [Minimum non-functional requirements for interfaces built to the Authority's specifications](#InteroperabilityStandardv7.0.0-Minimumnon-functionalrequirementsforinterfacesbuilttotheAuthority'sspecifications)
- [Capability-independent interoperability standards](#InteroperabilityStandardv7.0.0-Capability-independentinteroperabilitystandards)
  - [Spine](#InteroperabilityStandardv7.0.0-Spine)
  - [IM1 - Interface Mechanism](#InteroperabilityStandardv7.0.0-IM1-InterfaceMechanism)
  - [Authentication and authorisation](#InteroperabilityStandardv7.0.0-Authenticationandauthorisation)
  - [Communications](#InteroperabilityStandardv7.0.0-Communications)
  - [Generic FHIR Receiver](#InteroperabilityStandardv7.0.0-GenericFHIRReceiver)
- [Capability-specific interoperability standards](#InteroperabilityStandardv7.0.0-Capability-specificinteroperabilitystandards)
  - [Foundation Capabilities](#InteroperabilityStandardv7.0.0-FoundationCapabilities)
    - [Patient Information Maintenance - GP](#InteroperabilityStandardv7.0.0-PatientInformationMaintenance-GP)
    - [Using NHS 111 Report Adaptor](#InteroperabilityStandardv7.0.0-UsingNHS111ReportAdaptor)
    - [Without Using NHS 111 Report Adaptor](#InteroperabilityStandardv7.0.0-WithoutUsingNHS111ReportAdaptor)
    - [Consultation Management - GP](#InteroperabilityStandardv7.0.0-ConsultationManagement-GP)
    - [Appointments Management - GP](#InteroperabilityStandardv7.0.0-AppointmentsManagement-GP)
    - [Prescribing](#InteroperabilityStandardv7.0.0-Prescribing)
    - [Referral Management - GP](#InteroperabilityStandardv7.0.0-ReferralManagement-GP)
    - [Resource Management](#InteroperabilityStandardv7.0.0-ResourceManagement)
  - [Non-foundation capabilities](#InteroperabilityStandardv7.0.0-Non-foundationcapabilities)
    - [Communication Management](#InteroperabilityStandardv7.0.0-CommunicationManagement)
    - [Appointments Management - Citizen](#InteroperabilityStandardv7.0.0-AppointmentsManagement-Citizen)
    - [Prescription Ordering – Citizen](#InteroperabilityStandardv7.0.0-PrescriptionOrdering–Citizen)
    - [View Record - Citizen](#InteroperabilityStandardv7.0.0-ViewRecord-Citizen)
    - [Digital Diagnostics](#InteroperabilityStandardv7.0.0-DigitalDiagnostics)
    - [Communicate with Practice - Citizen](#InteroperabilityStandardv7.0.0-CommunicatewithPractice-Citizen)
  - [Capabilities to support new ways of working](#InteroperabilityStandardv7.0.0-Capabilitiestosupportnewwaysofworking)
    - [Cross-organisation Appointment Booking](#InteroperabilityStandardv7.0.0-Cross-organisationAppointmentBooking)
    - [Unified Care Record](#InteroperabilityStandardv7.0.0-UnifiedCareRecord)
    - [Medicines Verification v1.0.1](#InteroperabilityStandardv7.0.0-MedicinesVerificationv1.0.1)
    - [Medicines Optimisation](#InteroperabilityStandardv7.0.0-MedicinesOptimisation)
- [Deprecated Standards](#InteroperabilityStandardv7.0.0-DeprecatedStandards)
- [Roadmap](#InteroperabilityStandardv7.0.0-Roadmap)

# Introduction

This standard replaces General Practice Systems of Choice (GPSoC) requirements relating to integration and interoperability. It provides a single place for system suppliers to find out which interfaces they need to implement and to access the required documentation.

Future changes to interfaces will be communicated via the [Roadmap](../../../../GPITF/GP-IT-Futures-Capabilities-and-Standards-Home/Roadmap.md).

# Notes on quality and consistency of interface documentation

There are a large number of interfaces that GP systems need to implement. These interfaces, and their documentation, have been created over a very long period of time by a number of different organisations and programmes. The static nature of the GP systems market (no new entrants needing to implement) means that historically there has been limited justification and appetite for modernising or standardising existing documentation. This means that the format, quality and consistency of interface documentation is currently extremely variable.

Until these issues can be addressed suppliers and system implementers should expect to encounter issues with interface documentation. These could include:

- Inconsistencies in how optionality of requirements is expressed, e.g. MoSCoW ratings
- References to obsolete or outdated externalities, e.g. in-force legal frameworks, organisations or systems
- Descriptions of 'upcoming' or planned future phases which may or may not have actually occurred
- Broken links
- Referenced documents that have been included elsewhere in this standard rather than in the indicated location
- Referenced documents that interface owners have advised are no longer relevant
- Unavailable information relating to the impact of upcoming roadmap changes, e.g. where the replacement of existing [VUA/OSA/LOSA](../../Reference-Pages/Master-Glossary.md) based patient accounts by Nhs login could impact an interface implementation
- Verbose and/or difficult to follow documentation compared to modern best practices for interface documentation
- Unavailable sample files or test data

Suppliers should contact the NHS Digital team at [gpitfutures@nhs.net](mailto:gpitfutures@nhs.net) to resolve any documentation issues which block them from delivering compliant implementations.

# Interoperability principles

These interoperability principles are a SHOULD and suppliers are expected to adhere to them wherever possible.  Whilst adherence will not be assessed at onboarding, NHSD will expect any deviation from these principles to be supported by a valid rationale on delivery of interfaces.  NHSD may use adherence to these principles to guide decision making in circumstances of non-compliance or partial compliance against assured standards.

1. **True interoperability (defined as the ability of two or systems to work together unchanged, even if they weren't designed to work together) rather than integration (change is required to make the systems connect) should be achieved wherever possible - Integration takes work, interoperability just works.** Although the term interoperability is in widespread use within the NHS, what is meant is rarely well defined and the terms interoperability and integration are frequently used interchangeably. In our experience, the NHS uses a weak definition where two systems are said to be interoperable if they can exchange data in any way - even if that exchange is via a bespoke, point-to-point integration. True interoperability reduces the integration burden and allows systems to communicate more readily.
2. **Interoperability is more important than supporting customisation**. Use the base definition of standards wherever possible. Extend only by addition and by exception. Do not view integration as a source of competitive advantage.
3. **Use open design**. The effectiveness of security components included in a Solution design should not be compromised by any visibility of that design, i.e. should not rely on obscurity.
4. **Use open and government standards**. Design systems up front to support information sharing. This covers both alignment with Open Standards and the use of Open APIs. Use open standards (including from outside healthcare), and common government platforms (eg GOV.UK, identity assurance, shared services) where available.
5. **Make data open by default**. Whilst minimising and securing personal data, or data restricted for national security reasons. Public data should be made available by default in both human and open machine-readable formats. Users should have access to, and control over how their own personal data is shared.
6. **Use a common data model**. Healthcare systems are connected in a many-to-many fashion. In this scenario, the use of a common data model ensures that each system only has to be able to translate to and from the common model and does not need system-specific knowledge of myriad other connected systems.
7. **Messages should always be structured**. Adding preformatted ‘human readable’ text or formats such as HTML to messages increases coupling with the source system and reduces the reusability of the message while increasing the risk of a system receiving inappropriate data which cannot be detected. Receiving systems are responsible for transforming structured message into appropriate formats (e.g. HTML, PDF or images etc.). It's always preferable to store the structured data and render to a display format on demand.
8. **Interfaces must be system agnostic and semantically standardised**. Systems must not expose their internal complexity and data structures on interfaces, nor should they expect systems they interface with to understand their internal data encodings and semantics.
9. **Use decoupled integration patterns wherever possible**. Decoupling should be achieved using appropriate integration patterns such as publish-subscribe and event-based architectures.

## Interoperability non-functional requirements

The following overarching requirements apply to all interfaces in the scope of the Interoperability Standard which are offered by a Solution.    

| Req ID | Requirement Text | Level |
| --- | --- | --- |
| ISNFR01 | Suppliers will implement uplifts to the message & API specifications included within the interoperability standard as agreed & directed by the ‘Minor or patch changes’ section of the [Change Management Process](https://gpitbjss.atlassian.net/wiki/spaces/GPITF/pages/1391133471/Change+Management+Process+and+Roadmap+Introduction#ChangeManagementProcessandRoadmapIntroduction-HowwillversionupliftsbehandledthroughtheChangeprocess?) | MUST |
| ISNFR02 | The system will provide comprehensive audit facilities for ALL messages, including acknowledgements, over ALL transports and using ALL message types/syntax in order to satisfy general IG requirements and specific message flow requirements to ensure that support desks have access to the required information when investigating incidents/issues. | MUST |
| ISNFR03 | Suppliers will publicly publish full documentation for all currently live or in development and available-to-consumers interfaces, under a [Creative Commons Attribution-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nd/4.0/). Documentation must include, but is not limited to:   - Full details of all available endpoints - Message structures - Code sets - Intended interface behaviour, including any sequencing of calls, with pseudo code reference exemplars. - Requirements on consumers - Error handling - Authentication and authorisation requirements - Encryption, transport layer security and certificate requirements | MUST |
| ISNFR04 | For all currently live or in development and available-to-consumers interfaces, suppliers will make available public, mock versions of the interfaces to support consumer development and testing. Mocks must meet the following criteria:   1. They must cover the full scope of behaviour of the interface 2. They must offer sufficient fidelity to the live interface to fully support consumer development and testing    1. Test data/scenarios must be publicly documented, e.g. consumers will be clearly signposted which data they must submit in order to test a particular endpoint, error handling scenario or particular behaviour of the interface | MUST |
| ISNFR05 | Discrepancies discovered between ISNFR04 test mocks and behaviour of live interfaces will be rectified within two working days of first notification to the interface provider | SHOULD |
| ISNFR06 | Discrepancies discovered between ISNFR03 documentation and actual interfaces will be rectified within 5 working days of first notification to the interface provider | MUST |
| ISNFR07 | Within the scope of interfaces specified within the standard, Suppliers must not offer differential service, e.g all API functionality and behaviour will be equally available to all API consumers, including the API provider's own apps. | MUST |
| ISNFR08 | Suppliers should not offer multiple APIs for the same purpose, e.g. there should not be multiple, different Appointments Booking APIs. Suppliers are free to offer APIs to different consumers under different commercial terms if permitted by the contract and framework, but they should offer only one technical API for each purpose. | SHOULD |

## Minimum non-functional requirements for interfaces built to the Authority's specifications

Where an interface/extract is built to the Authority's functional specifications, e.g. [IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md), [(Archived) Draft\_GP Connect](#) the following requirements apply to the production implementation. For requirements relating to performance and availability suppliers should refer to the Service Level Agreement.

| Req ID | Requirement Text | Level |
| --- | --- | --- |
| ASNFR01 | Data currency. Updates to systems made through non-API mechanisms (e.g. user interface) should be available on APIs in real time, i.e. as soon as the update transaction is committed. | SHOULD |
| ASNFR02 | Data currency. Updates made through APIs must be available on APIs in real time, i.e. as soon as the update transaction is committed. | MUST |

# Capability-independent interoperability standards

This section lists the interoperability requirements which are not linked to single capabilities. These are typically (but not exclusively) supporting standards such as communications protocols or related technical standards.

## Spine

The NHS [Spine](../../Reference-Pages/Spine.md) provides national interoperability infrastructure as well as specific national services, for example the [Personal Demographics Service (PDS)](../../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) listed further below under Dependencies. 

Two specific [Spine](../../Reference-Pages/Spine.md) components are key supporting standards for a number of the interop standards, and are listed multiple times within the 'Dependencies' column below. They are:

- [External Interface Specification (EIS)](../../DSIC-Standards/Non-Overarching-Standards/External-Interface-Specification-EIS.md) describes how to connect to NHS Spine services
- [NHS Messaging Implementation Manual (MIM)](../../DSIC-Standards/Non-Overarching-Standards/NHS-Messaging-Implementation-Manual-MIM.md) describes the message formats used for Spine interactions

## IM1 - Interface Mechanism

[IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) is a mechanism for accessing data held in GP Systems (Systems providing one or more Capabilities as part of the GP IT Futures Framework). The interface mechanism facilitates three use-cases (Patient, Bulk and Practice) which are detailed within the IM1 page.

A system or application may wish to **consume** IM1 interfaces where they have a requirement to access data held in GP Systems.

A system or application is required to **provide**IM1 interfaces if ANY of the following are true:

- It offered IM1 interfaces under GPSoC
- It offers ALL Foundation capabilities under GP IT Futures

## Authentication and authorisation

Standards for confirming the identity of service users and controlling their access to services or specific resources.

- [Authentication and Access](../../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md)
- [NHS login service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md)

## Communications

- [Email](../../DSIC-Standards/Non-Overarching-Standards/Email.md) (system accounts for automated sending for purposes such as notifications)

## Generic FHIR Receiver

- [Generic FHIR Receiver](../../DSIC-Standards/Non-Overarching-Standards/Generic-FHIR-Receiver.md) (a component which will receive messages to the GP Practice)

# Capability-specific interoperability standards

This section details the interoperability requirements which are associated with each Capability. 

Some interdependencies between individual interface standards exist. Creating a compliant implementation requires implementing all the required dependent interface standards, as detailed in the 'Dependencies' column.

Suppliers need to comply with all of the requirements that are associated with the Capability/Capabilities which the supplier is offering. 

## Foundation Capabilities

### [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements (if offering all Foundation capabilities) |  |
| [NHAIS HA/GP Links](../../DSIC-Standards/Non-Overarching-Standards/NHAIS-HAGP-Links.md) | - [Messaging Exchange for Social Care and Health (MESH)](../../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |
| [Personal Demographics Service (PDS)](../../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) | For Suppliers of new Solutions, Solutions which ARE currently deployed into an operational environment and have implemented the PDS FHIR API, and Community Pharmacy Solutions (using Healthcare worker access).   - [Authentication and Access](../../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API |
| [GP2GP](../../DSIC-Standards/Non-Overarching-Standards/GP2GP.md) | For Suppliers of new Solutions and Solutions that have implemented the GP2GP FHIR Implementation
| [Summary Care Record (SCR)](../../DSIC-Standards/Non-Overarching-Standards/Summary-Care-Record-SCR.md) | For Suppliers of new Solutions and Solutions that have implemented the SCR FHIR API:   - [Authentication and Access](../../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API |
| [(Archived) Draft\_GP Connect](#) Access Record API | - [Personal Demographics Service (PDS)](../../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) |
| [111](../../DSIC-Standards/Non-Overarching-Standards/111.md) | Using NHS 111 Report Adaptor There are no Interoperability Standards within the Capabilities and Standards model that are dependents. Without Using NHS 111 Report Adaptor Creating a compliant implementation requires implementing the following dependent interface standards:   - [Interoperability Toolkit (ITK)](../../DSIC-Standards/Non-Overarching-Standards/Interoperability-Toolkit-ITK.md) - ITK3 Messaging Distribution - [Clinical Document Architecture (CDA)](../../DSIC-Standards/Non-Overarching-Standards/Clinical-Document-Architecture-CDA.md) |
| [GPES Data Extraction](../../DSIC-Standards/Non-Overarching-Standards/GPES-Data-Extraction.md) | - [Messaging Exchange for Social Care and Health (MESH)](../../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |
| [Secure Electronic File Transfer (SEFT)](../../DSIC-Standards/Non-Overarching-Standards/Secure-Electronic-File-Transfer-SEFT.md) (in order to meet Primary Care Clinical Terminology Usage Report) |  |
| [Digital Medicines and Pharmacy FHIR Payload](../../DSIC-Standards/Non-Overarching-Standards/Digital-Medicines-and-Pharmacy-FHIR-Payload.md) | [Generic FHIR Receiver](../../DSIC-Standards/Non-Overarching-Standards/Generic-FHIR-Receiver.md) |

### [Consultation Management - GP](../../DSIC-Capabilities/Consultation-Management-GP.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements (if offering all Foundation capabilities) |  |
| [Electronic Yellow Card Reporting](../../DSIC-Standards/Non-Overarching-Standards/Electronic-Yellow-Card-Reporting.md) |  |
| [Messaging Exchange for Social Care and Health (MESH)](../../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) (in order to meet eMED3 Fitnotes) |  |

### [Appointments Management - GP](../../DSIC-Capabilities/Appointments-Management-GP.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements (if offering all Foundation capabilities) |  |
| [(Archived) Draft\_GP Connect](#) Appointments API | - [Personal Demographics Service (PDS)](../../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \*   Or   - [Spine Mini Services](../../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution. |
| [Messaging Exchange for Social Care and Health (MESH)](../../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md)   Or   [Secure Electronic File Transfer (SEFT)](../../DSIC-Standards/Non-Overarching-Standards/Secure-Electronic-File-Transfer-SEFT.md)   (in order to meet General Practice Appointments Data Reporting) |  |

### [Prescribing](../../DSIC-Capabilities/Prescribing.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements (if offering all Foundation capabilities) |  |
| [Electronic Prescription Service (EPS) - Prescribing](../../DSIC-Standards/Non-Overarching-Standards/Electronic-Prescription-Service-EPS-Prescribing.md) | For Suppliers of new Solutions and Solutions that have implemented the EPS FHIR API:  Creating a compliant implementation requires implementing the following dependent interface standards:   - [Personal Demographics Service (PDS)](../../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) - using PDS FHIR API - [Authentication and Access](../../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API - [Digital Signature Service API](https://digital.nhs.uk/developer/api-catalogue/signing-service) |

### [Referral Management - GP](../../DSIC-Capabilities/Referral-Management-GP.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements  (if offering all Foundation capabilities) |  |
| [e-Referral Service (eRS)](../../DSIC-Standards/Non-Overarching-Standards/e-Referrals-Service-e-RS.md) | For Suppliers of new Solutions and Solutions that have implemented the e-RS FHIR API:   - [Personal Demographics Service (PDS)](../../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) - using PDS FHIR API - [Authentication and Access](../../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API |

### [Resource Management](../../DSIC-Capabilities/Resource-Management.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements  (if offering all Foundation capabilities) |  |

## Non-foundation capabilities

### [Communication Management](../../DSIC-Capabilities/Communication-Management.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [Email](../../DSIC-Standards/Non-Overarching-Standards/Email.md) |  |

### [Appointments Management - Citizen](../../DSIC-Capabilities/Appointments-Management-Citizen.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) (Patient interface Consumer) | - [NHS login service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

### [Prescription Ordering – Citizen](../../DSIC-Capabilities/Prescription-Ordering-Citizen.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) (Patient interface Consumer) | - [NHS login service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

### [View Record - Citizen](../../DSIC-Capabilities/View-Record-Citizen.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) (Patient interface Consumer) | - [NHS login service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

### [Digital Diagnostics](../../DSIC-Capabilities/Digital-Diagnostics.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [Digital Diagnostics & Pathology Messaging](../../DSIC-Standards/Non-Overarching-Standards/Digital-Diagnostics-Pathology-Messaging.md) | - [Messaging Exchange for Social Care and Health (MESH)](../../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |
| [Screening Messaging](../../DSIC-Standards/Non-Overarching-Standards/Screening-Messaging.md) | - [Messaging Exchange for Social Care and Health (MESH)](../../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |

### [Communicate with Practice - Citizen](../../Deprecated-Content/Deprecated-Capabilities/Communicate-With-Practice-Citizen.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [IM1 - Interface Mechanism](../../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) (Patient interface Consumer) | - [NHS login service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

## Capabilities to support new ways of working

### [Cross-organisation Appointment Booking](../../DSIC-Capabilities/Cross-organisation-Appointment-Booking.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [GP Connect (Appointments)](#) | - [Personal Demographics Service (PDS)](../../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \*   Or   - [Spine Mini Services](../../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution. |

### [Unified Care Record](../../DSIC-Capabilities/Unified-Care-Record.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [GP Connect (Access Record)](#) | - [Personal Demographics Service (PDS)](../../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \*   Or   - [Spine Mini Services](../../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution. |

### [Medicines Verification v1.0.1](../Retired-Capabilities/Medicines-Verification-v101.md)

| Interoperability Requirement | Dependencies |
| --- | --- |
| [National Medicines Verification System v1.0.0](National-Medicines-Verification-System-v100.md) |  |

### [Medicines Optimisation](../../DSIC-Capabilities/Medicines-Optimisation.md)

| Interoperability Requirement |  |
| --- | --- |
| [GP Connect (Access Record)](#) (Medication FHIR Resources) |  |

# Deprecated Standards

- [MIQUEST V1.0.0](MIQUEST-V100.md)

# Roadmap

| Title |
| --- |
| No content found. |