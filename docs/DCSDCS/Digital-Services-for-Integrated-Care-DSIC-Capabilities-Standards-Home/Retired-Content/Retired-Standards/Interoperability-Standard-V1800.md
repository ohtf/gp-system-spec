---
page_id: "13389037578"
space: "DCSDCS"
title: "Interoperability Standard V18.0.0"
version: 1
updated: "2024-10-17T10:51:20.127Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/13389037578/Interoperability+Standard+V18.0.0"
labels: ["overarching_standard_retired"]
---

# Interoperability Standard V18.0.0

|  |  |
| --- | --- |
| ID {#InteroperabilityStandardV18.0.0-ID} | S32 |
| Version {#InteroperabilityStandardV18.0.0-Version} | 18.0.0 |
| Type {#InteroperabilityStandardV18.0.0-Type} | Overarching Standard |
| Status {#InteroperabilityStandardV18.0.0-Status} | Retired |
| Effective Date {#InteroperabilityStandardV18.0.0-EffectiveDate} | 30 Aug 2024 |
| Contracting Vehicle(s) {#InteroperabilityStandardV18.0.0-ContractingVehicle(s)} | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Vaccinations - Local/PCN Delivery](https://nhse-dsic.atlassian.net/wiki/spaces/CVPDR) |

- [Introduction](#InteroperabilityStandardV18.0.0-Introduction)
- [Notes on quality and consistency of interface documentation](#InteroperabilityStandardV18.0.0-Notesonqualityandconsistencyofinterfacedocumentation)
- [Interoperability principles](#InteroperabilityStandardV18.0.0-Interoperabilityprinciples)
- [Requirements](#InteroperabilityStandardV18.0.0-Requirements)
- [Capability-independent interoperability Standards](#InteroperabilityStandardV18.0.0-Capability-independentinteroperabilityStandards)
  - [Spine](#InteroperabilityStandardV18.0.0-Spine)
  - [IM1 - Interface Mechanism](#InteroperabilityStandardV18.0.0-IM1-InterfaceMechanism)
  - [Authentication and authorisation](#InteroperabilityStandardV18.0.0-Authenticationandauthorisation)
  - [Communications](#InteroperabilityStandardV18.0.0-Communications)
  - [Generic FHIR Receiver](#InteroperabilityStandardV18.0.0-GenericFHIRReceiver)
- [Capability-specific interoperability Standards](#InteroperabilityStandardV18.0.0-Capability-specificinteroperabilityStandards)
  - [Foundation Capabilities](#InteroperabilityStandardV18.0.0-FoundationCapabilities)
    - [Patient Information Maintenance - GP](#InteroperabilityStandardV18.0.0-PatientInformationMaintenance-GP)
    - [Consultation Management - GP](#InteroperabilityStandardV18.0.0-ConsultationManagement-GP)
    - [Appointments Management - GP](#InteroperabilityStandardV18.0.0-AppointmentsManagement-GP)
    - [Prescribing](#InteroperabilityStandardV18.0.0-Prescribing)
    - [Referral Management - GP](#InteroperabilityStandardV18.0.0-ReferralManagement-GP)
    - [Resource Management](#InteroperabilityStandardV18.0.0-ResourceManagement)
  - [Non-foundation capabilities](#InteroperabilityStandardV18.0.0-Non-foundationcapabilities)
    - [Communication Management](#InteroperabilityStandardV18.0.0-CommunicationManagement)
    - [Appointments Management - Citizen](#InteroperabilityStandardV18.0.0-AppointmentsManagement-Citizen)
    - [Prescription Ordering – Citizen](#InteroperabilityStandardV18.0.0-PrescriptionOrdering–Citizen)
    - [View Record - Citizen](#InteroperabilityStandardV18.0.0-ViewRecord-Citizen)
    - [Digital Diagnostics](#InteroperabilityStandardV18.0.0-DigitalDiagnostics)
    - [Communicate with Practice - Citizen](#InteroperabilityStandardV18.0.0-CommunicatewithPractice-Citizen)
  - [Community Pharmacy Capabilities](#InteroperabilityStandardV18.0.0-CommunityPharmacyCapabilities)
    - [Consultation Management - Community Pharmacy](#InteroperabilityStandardV18.0.0-ConsultationManagement-CommunityPharmacy)
    - [Referral Management - Community Pharmacy](#InteroperabilityStandardV18.0.0-ReferralManagement-CommunityPharmacy)
  - [Capabilities to support new ways of working](#InteroperabilityStandardV18.0.0-Capabilitiestosupportnewwaysofworking)
    - [Cross-organisation Appointment Booking](#InteroperabilityStandardV18.0.0-Cross-organisationAppointmentBooking)
    - [Unified Care Record](#InteroperabilityStandardV18.0.0-UnifiedCareRecord)
    - [Medicines Optimisation](#InteroperabilityStandardV18.0.0-MedicinesOptimisation)
- [Dependencies](#InteroperabilityStandardV18.0.0-Dependencies.17)
- [Deprecated Standards](#InteroperabilityStandardV18.0.0-DeprecatedStandards)
- [Roadmap](#InteroperabilityStandardV18.0.0-Roadmap)

# Introduction {#InteroperabilityStandardV18.0.0-Introduction}

This Standard replaces General Practice Systems of Choice (GPSoC) requirements relating to integration and interoperability. It provides a single place for system Suppliers to find out which interfaces they need to implement and to access the required documentation.

Future changes to interfaces will be communicated via the Roadmap.

# Notes on quality and consistency of interface documentation {#InteroperabilityStandardV18.0.0-Notesonqualityandconsistencyofinterfacedocumentation}

There are a large number of interfaces that GP systems need to implement. These interfaces, and their documentation, have been created over a very long period of time by a number of different organisations and programmes. The static nature of the GP systems market (no new entrants needing to implement) means that historically there has been limited justification and appetite for modernising or standardising existing documentation. This means that the format, quality and consistency of interface documentation is currently extremely variable.

Until these issues can be addressed Suppliers and system implementers should expect to encounter issues with interface documentation. These could include:

- Inconsistencies in how optionality of requirements is expressed, e.g. MoSCoW ratings
- References to obsolete or outdated externalities, e.g. in-force legal frameworks, organisations or systems
- Descriptions of 'upcoming' or planned future phases which may or may not have actually occurred
- Broken links
- Referenced documents that have been included elsewhere in this Standard rather than in the indicated location
- Referenced documents that interface owners have advised are no longer relevant
- Unavailable information relating to the impact of upcoming roadmap changes, e.g. where the replacement of existing VUA/OSA/LOSA based Patient accounts by NHS login could impact an interface implementation
- Verbose and/or difficult to follow documentation compared to modern best practices for interface documentation
- Unavailable sample files or test data

Suppliers should contact The Authority’s team at gpitfutures@nhs.net to resolve any documentation issues which block them from delivering compliant implementations.

# Interoperability principles {#InteroperabilityStandardV18.0.0-Interoperabilityprinciples}

These interoperability principles are a SHOULD and Suppliers are expected to adhere to them wherever possible. Whilst adherence will not be assessed at onboarding, NHSD will expect any deviation from these principles to be supported by a valid rationale on delivery of interfaces. NHSD may use adherence to these principles to guide decision making in circumstances of non-compliance or partial compliance against assured Standards.

1. **True interoperability (defined as the ability of two or systems to work together unchanged, even if they weren't designed to work together) rather than integration (change is required to make the systems connect) should be achieved wherever possible - Integration takes work, interoperability just works.** Although the term interoperability is in widespread use within the NHS, what is meant is rarely well defined and the terms interoperability and integration are frequently used interchangeably. In our experience, the NHS uses a weak definition where two systems are said to be interoperable if they can exchange data in any way - even if that exchange is via a bespoke, point-to-point integration. True interoperability reduces the integration burden and allows systems to communicate more readily.
2. **Interoperability is more important than supporting customisation**. Use the base definition of Standards wherever possible. Extend only by addition and by exception. Do not view integration as a source of competitive advantage.
3. **Use open design**. The effectiveness of security components included in a Solution design should not be compromised by any visibility of that design, i.e. should not rely on obscurity.
4. **Use open and government standards**. Design systems up front to support information sharing. This covers both alignment with Open Standards and the use of Open APIs. Use open Standards (including from outside healthcare), and common government platforms (eg GOV.UK, identity assurance, shared services) where available.
5. **Make data open by default**. Whilst minimising and securing personal data, or data restricted for national security reasons. Public data should be made available by default in both human and open machine-readable formats. Users should have access to, and control over how their own personal data is shared.
6. **Use a common data model**. Healthcare systems are connected in a many-to-many fashion. In this scenario, the use of a common data model ensures that each system only has to be able to translate to and from the common model and does not need system-specific knowledge of myriad other connected systems.
7. **Messages should always be structured**. Adding preformatted ‘human readable’ text or formats such as HTML to messages increases coupling with the source system and reduces the reusability of the message while increasing the risk of a system receiving inappropriate data which cannot be detected. Receiving systems are responsible for transforming structured message into appropriate formats (e.g. HTML, PDF or images etc.). It's always preferable to store the structured data and render to a display format on demand.
8. **Interfaces must be system agnostic and semantically standardised**. Systems must not expose their internal complexity and data structures on interfaces, nor should they expect systems they interface with to understand their internal data encodings and semantics.
9. **Use decoupled integration patterns wherever possible**. Decoupling should be achieved using appropriate integration patterns such as publish-subscribe and event-based architectures.

# Requirements {#InteroperabilityStandardV18.0.0-Requirements}

#### Interoperability non-functional requirements {#InteroperabilityStandardV18.0.0-Interoperabilitynon-functionalrequirements}

The following overarching requirements apply to all interfaces in the scope of the Interoperability Standard which are offered by a Solution. 

| Applicable Contracting Vehicle(s) {#InteroperabilityStandardV18.0.0-ApplicableContractingVehicle(s)} | Requirement ID {#InteroperabilityStandardV18.0.0-RequirementID} | Requirement {#InteroperabilityStandardV18.0.0-Requirement} | Level {#InteroperabilityStandardV18.0.0-Level} |
| --- | --- | --- | --- |
| All {#InteroperabilityStandardV18.0.0-All} | ISNFR01 {#InteroperabilityStandardV18.0.0-ISNFR01} | Suppliers will implement uplifts to the message & API specifications included within the interoperability Standard as agreed & directed by the ‘Minor or patch changes’ section of the Change Management Process | MUST |
| All {#InteroperabilityStandardV18.0.0-All.1} | ISNFR02 {#InteroperabilityStandardV18.0.0-ISNFR02} | The system will provide comprehensive audit facilities for ALL messages, including acknowledgements, over ALL transports and using ALL message types/syntax in order to satisfy general IG requirements and specific message flow requirements to ensure that support desks have access to the required information when investigating incidents/issues. | MUST |
| All {#InteroperabilityStandardV18.0.0-All.2} | ISNFR03 {#InteroperabilityStandardV18.0.0-ISNFR03} | Suppliers will publicly publish full documentation for all currently live or in development and available-to-consumers interfaces, under a Creative Commons Attribution-NoDerivatives 4.0 International License. Documentation must include, but is not limited to:   - Full details of all available endpoints - Message structures - Code sets - Intended interface behaviour, including any sequencing of calls, with pseudo code reference exemplars. - Requirements on consumers - Error handling - Authentication and authorisation requirements - Encryption, transport layer security and certificate requirements | MUST |
| All {#InteroperabilityStandardV18.0.0-All.3} | ISNFR04 {#InteroperabilityStandardV18.0.0-ISNFR04} | For all currently live or in development and available-to-consumers interfaces, Suppliers will make available public, mock versions of the interfaces to support consumer development and testing. Mocks must meet the following criteria:   1. They must cover the full scope of behaviour of the interface 2. They must offer sufficient fidelity to the live interface to fully support consumer development and testing     1. Test data/scenarios must be publicly documented, e.g. consumers will be clearly signposted which data they must submit in order to test a particular endpoint, error handling scenario or particular behaviour of the interface | MUST |
| All {#InteroperabilityStandardV18.0.0-All.4} | ISNFR05 {#InteroperabilityStandardV18.0.0-ISNFR05} | Discrepancies discovered between ISNFR04 test mocks and behaviour of live interfaces will be rectified within two working days of first notification to the interface provider | SHOULD |
| All {#InteroperabilityStandardV18.0.0-All.5} | ISNFR06 {#InteroperabilityStandardV18.0.0-ISNFR06} | Discrepancies discovered between ISNFR03 documentation and actual interfaces will be rectified within 5 working days of first notification to the interface provider | MUST |
| All {#InteroperabilityStandardV18.0.0-All.6} | ISNFR07 {#InteroperabilityStandardV18.0.0-ISNFR07} | Within the scope of interfaces specified within the Standard, Suppliers must not offer differential service, e.g all API functionality and behaviour will be equally available to all API consumers, including the API provider's own apps. | MUST |
| All {#InteroperabilityStandardV18.0.0-All.7} | ISNFR08 {#InteroperabilityStandardV18.0.0-ISNFR08} | Suppliers should not offer multiple APIs for the same purpose, e.g. there should not be multiple, different Appointments Booking APIs. Suppliers are free to offer APIs to different consumers under different commercial terms if permitted by the contract and framework, but they should offer only one technical API for each purpose. | SHOULD |

#### Minimum non-functional requirements for interfaces built to The Authority's specifications {#InteroperabilityStandardV18.0.0-Minimumnon-functionalrequirementsforinterfacesbuilttoTheAuthority'sspecifications}

Where an interface/extract is built to The Authority's functional specifications, e.g. IM1 - Interface Mechanism, GP Connect the following requirements apply to the production implementation. For requirements relating to performance and availability Suppliers should refer to the Service Level Agreement.

| Req ID {#InteroperabilityStandardV18.0.0-ReqID} | Requirement {#InteroperabilityStandardV18.0.0-Requirement.1} | Level {#InteroperabilityStandardV18.0.0-Level.1} |
| --- | --- | --- |
| ASNFR01 {#InteroperabilityStandardV18.0.0-ASNFR01} | Data currency. Updates to systems made through non-API mechanisms (e.g. user interface) should be available on APIs in real time, i.e. as soon as the update transaction is committed. | SHOULD |
| ASNFR02 {#InteroperabilityStandardV18.0.0-ASNFR02} | Data currency. Updates made through APIs must be available on APIs in real time, i.e. as soon as the update transaction is committed. | MUST |

# Capability-independent interoperability Standards {#InteroperabilityStandardV18.0.0-Capability-independentinteroperabilityStandards}

This section lists the interoperability requirements which are not linked to single capabilities. These are typically (but not exclusively) supporting Standards such as communications protocols or related technical Standards.

## Spine {#InteroperabilityStandardV18.0.0-Spine}

The NHS Spine provides national interoperability infrastructure as well as specific national services, for example the Personal Demographics Service (PDS) listed further below under Dependencies. 

Two specific Spine components are key supporting Standards for a number of the interop Standards, and are listed multiple times within the 'Dependencies' column below. They are:

- External Interface Specification (EIS) describes how to connect to NHS Spine services
- NHS Messaging Implementation Manual (MIM) describes the message formats used for Spine interactions

## IM1 - Interface Mechanism {#InteroperabilityStandardV18.0.0-IM1-InterfaceMechanism}

IM1 - Interface Mechanism is a mechanism for accessing data held in GP Systems (Systems providing one or more Capabilities as part of the GP IT Futures Framework). The interface mechanism facilitates three use-cases (Patient, Bulk and Practice) which are detailed within the IM1 page.

A system or application may wish to **consume** IM1 interfaces where they have a requirement to access data held in GP Systems.

A system or application is required to **provide**IM1 interfaces if ANY of the following are true:

- It offered IM1 interfaces under GPSoC
- It offers ALL Foundation Capabilities

## Authentication and authorisation {#InteroperabilityStandardV18.0.0-Authenticationandauthorisation}

Standards for confirming the identity of service users and controlling their access to services or specific resources.

- Authentication and Access
- NHS login service

## Communications {#InteroperabilityStandardV18.0.0-Communications}

- Email (system accounts for automated sending for purposes such as notifications)

## Generic FHIR Receiver  {#InteroperabilityStandardV18.0.0-GenericFHIRReceiver}

- Generic FHIR Receiver (a component which will receive messages to the GP Practice)

# Capability-specific interoperability Standards {#InteroperabilityStandardV18.0.0-Capability-specificinteroperabilityStandards}

This section details the interoperability requirements which are associated with each Capability.

Some interdependencies between individual interface Standards exist. Creating a compliant implementation requires implementing all the required dependent interface Standards, as detailed in the 'Dependencies' column.

Suppliers need to comply with all of the requirements that are associated with the Capability/Capabilities which the Supplier is offering.

## Foundation Capabilities {#InteroperabilityStandardV18.0.0-FoundationCapabilities}

### Patient Information Maintenance - GP {#InteroperabilityStandardV18.0.0-PatientInformationMaintenance-GP}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies} |
| --- | --- |
| IM1 - Interface Mechanism Provider requirements (if offering all Foundation capabilities) | - NHS login service (Foundation Solution Suppliers requirements) |
| NHAIS HA/GP Links | - Messaging Exchange for Social Care and Health (MESH) |
| Personal Demographics Service (PDS) | PDS FHIR API {#InteroperabilityStandardV18.0.0-PDSFHIRAPI} For Suppliers of new services or applications:   - Authentication and Access- using NHS Care Identity Service 2 API - SDS FHIR API  2018 PDS Integration Requirements – v1.0 or older {#InteroperabilityStandardV18.0.0-2018PDSIntegrationRequirements–v1.0orolder} For Suppliers of services which ARE currently deployed into an operational environment:   - External Interface Specification (EIS) - NHS Messaging Implementation Manual (MIM) - Authentication and Access |
| GP2GP | GP2GP FHIR Implementation {#InteroperabilityStandardV18.0.0-GP2GPFHIRImplementation} For Suppliers of new services or applications:   - GP2GP Requesting Adaptor - GP2GP Sending Adaptor - Personal Demographics Service (PDS) - using FHIR API - Spine Directory Service - FHIR API - GP Connect - Access Record Structured API v1.6.0 - GP Registrations Management Information API  GP2GP HL7 {#InteroperabilityStandardV18.0.0-GP2GPHL7} For Suppliers of services which ARE currently deployed into an operational environment:   - External Interface Specification (EIS) - NHS Messaging Implementation Manual (MIM) |
| Summary Care Record (SCR) | Summary Care Record FHIR API {#InteroperabilityStandardV18.0.0-SummaryCareRecordFHIRAPI} For Suppliers of new services or applications:   - Authentication and Access - using NHS Care Identity Service 2 API  NHS Summary Care Record Service - GP Summary Requirements v5.8.3 {#InteroperabilityStandardV18.0.0-NHSSummaryCareRecordService-GPSummaryRequirementsv5.8.3} For Suppliers of services which ARE currently deployed into an operational environment:   - External Interface Specification (EIS) - NHS Messaging Implementation Manual (MIM) - Spine Mini Services (optional) - Authentication and Access |
| GP Connect Access Record HTML (Provider requirements) | - Personal Demographics Service (PDS) |
| GP Connect Access Record Structured (Provider requirements) | - Personal Demographics Service (PDS) |
| GP Connect Send Document (Receiver requirements) | - Interoperability Toolkit (ITK) - ITK3 Messaging Distribution - Messaging Exchange for Social Care and Health (MESH) - Generic FHIR Receiver (Receiver Solutions only) |
| GP Connect Update Record (Receiver requirements) | - Interoperability Toolkit (ITK) - ITK3 Messaging Distribution - Messaging Exchange for Social Care and Health (MESH) - Personal Demographics Service (PDS) \* or Spine Mini Services   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP (PIM) Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| 111 | **Without Using NHS 111 Report Adaptor** {#InteroperabilityStandardV18.0.0-WithoutUsingNHS111ReportAdaptor}  - Interoperability Toolkit (ITK) - Clinical Document Architecture (CDA) |
| GPES Data Extraction | - Messaging Exchange for Social Care and Health (MESH) |
| Secure Electronic File Transfer (SEFT) (in order to meet Primary Care Clinical Terminology Usage Report) |  |
| Digital Medicines and Pharmacy FHIR Payload | - Generic FHIR Receiver |
| National Data Opt-Out | - Messaging Exchange for Social Care and Health (MESH) |
| GP Data for Planning and Research | - Messaging Exchange for Social Care and Health (MESH) \*   \*May alternatively use AWS Direct S3-S3 transfers as the secure transport mechanism |
| Transfer of Care FHIR Payload | - Workflow - Generic FHIR Receiver |
| National Events Management Service (NEMS) | - Messaging Exchange for Social Care and Health (MESH) |

### Consultation Management - GP {#InteroperabilityStandardV18.0.0-ConsultationManagement-GP}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.1} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.1} |
| --- | --- |
| IM1 - Interface Mechanism Provider requirements (if offering all Foundation capabilities) | - NHS login service (Foundation Solution Suppliers requirements) |
| Electronic Yellow Card Reporting |  |
| Messaging Exchange for Social Care and Health (MESH) (in order to meet eMED3 Fitnotes) |  |

### Appointments Management - GP {#InteroperabilityStandardV18.0.0-AppointmentsManagement-GP}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.2} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.2} |
| --- | --- |
| IM1 - Interface Mechanism Provider requirements (if offering all Foundation capabilities) | - NHS login service (Foundation Solution Suppliers requirements) |
| GP Connect Appointment Management (Provider requirements) | - Personal Demographics Service (PDS) \* or Spine Mini Services   \*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution. |
| Messaging Exchange for Social Care and Health (MESH)  Or  Secure Electronic File Transfer (SEFT)  (in order to meet General Practice Appointments Data Reporting) |  |
| GP Data for Planning and Research | - Messaging Exchange for Social Care and Health (MESH) \*   \*May alternatively use AWS Direct S3-S3 transfers as the secure transport mechanism |

### Prescribing {#InteroperabilityStandardV18.0.0-Prescribing}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.3} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.3} |
| --- | --- |
| IM1 - Interface Mechanism Provider requirements (if offering all Foundation capabilities) | - NHS login service (Foundation Solution Suppliers requirements) |
| Electronic Prescription Service (EPS) - Prescribing | EPS FHIR API - Prescribing API {#InteroperabilityStandardV18.0.0-EPSFHIRAPI-PrescribingAPI} For Suppliers of new services or applications:   - Personal Demographics Service (PDS) - using PDS FHIR API - Authentication and Access - using NHS Care Identity Service 2 API - Signing Service API  EPS Prescribing Systems Compliance Specification v6.11 or older {#InteroperabilityStandardV18.0.0-EPSPrescribingSystemsComplianceSpecificationv6.11orolder} For Suppliers of services which ARE currently deployed into an operational environment:   - Personal Demographics Service (PDS) \* - External Interface Specification (EIS) - NHS Messaging Implementation Manual (MIM)   \*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution. |

### Referral Management - GP {#InteroperabilityStandardV18.0.0-ReferralManagement-GP}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.4} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.4} |
| --- | --- |
| IM1 - Interface Mechanism Provider requirements (if offering all Foundation capabilities) | - NHS login service (Foundation Solution Suppliers requirements) |
| e-Referral Service (eRS) | e-Referral Service FHIR API - Primary Care Referrer {#InteroperabilityStandardV18.0.0-e-ReferralServiceFHIRAPI-PrimaryCareReferrer} For Suppliers of new services or applications:   - Personal Demographics Service (PDS) - using PDS FHIR API - Authentication and Access - using NHS Care Identity Service 2 API  NHS e-Referrals Service - Referrer Compliance Document v1 {#InteroperabilityStandardV18.0.0-NHSe-ReferralsService-ReferrerComplianceDocumentv1} For Suppliers of services which ARE currently deployed into an operational environment:   - Personal Demographics Service (PDS) \* - External Interface Specification (EIS) - NHS Messaging Implementation Manual (MIM)   \*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution. |
| Booking and Referral Standard (BaRS) | - BaRS provides a list of prerequisites in the BaRS Implementation Guide - The are no other dependent framework standards |

### Resource Management {#InteroperabilityStandardV18.0.0-ResourceManagement}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.5} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.5} |
| --- | --- |
| IM1 - Interface Mechanism Provider requirements (if offering all Foundation capabilities) | - NHS login service (Foundation Solution Suppliers requirements) |

## Non-foundation capabilities {#InteroperabilityStandardV18.0.0-Non-foundationcapabilities}

### Communication Management {#InteroperabilityStandardV18.0.0-CommunicationManagement}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.6} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.6} |
| --- | --- |
| Email |  |

### Appointments Management - Citizen {#InteroperabilityStandardV18.0.0-AppointmentsManagement-Citizen}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.7} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.7} |
| --- | --- |
| IM1 - Interface Mechanism (Patient interface Consumer) | - [NHS login service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

### Prescription Ordering – Citizen {#InteroperabilityStandardV18.0.0-PrescriptionOrdering–Citizen}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.8} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.8} |
| --- | --- |
| IM1 - Interface Mechanism (Patient interface Consumer) | - [NHS login service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

### View Record - Citizen {#InteroperabilityStandardV18.0.0-ViewRecord-Citizen}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.9} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.9} |
| --- | --- |
| IM1 - Interface Mechanism (Patient interface Consumer) | - [NHS login service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

### Digital Diagnostics {#InteroperabilityStandardV18.0.0-DigitalDiagnostics}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.10} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.10} |
| --- | --- |
| Digital Diagnostics & Pathology Messaging | - [Messaging Exchange for Social Care and Health (MESH)](../../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |
| Screening messaging | - [Messaging Exchange for Social Care and Health (MESH)](../../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |

### Communicate with Practice - Citizen {#InteroperabilityStandardV18.0.0-CommunicatewithPractice-Citizen}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.11} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.11} |
| --- | --- |
| IM1 - Interface Mechanism (Patient interface Consumer) | - [NHS login service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

## Community Pharmacy Capabilities {#InteroperabilityStandardV18.0.0-CommunityPharmacyCapabilities}

### Consultation Management - Community Pharmacy {#InteroperabilityStandardV18.0.0-ConsultationManagement-CommunityPharmacy}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.12} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.12} |
| --- | --- |
| - GP Connect Access Record Structured (Consumer requirements) | - Personal Demographics Service (PDS) \* or Spine Mini Services   \*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution. |
| - GP Connect Update Record (Sender requirements) | - Interoperability Toolkit (ITK) - ITK3 Messaging Distribution - Messaging Exchange for Social Care and Health (MESH) - Personal Demographics Service (PDS) \* or Spine Mini Services   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| - NHSBSA Claims & Reporting |  |
| - Directory of Services (DoS) - Urgent and Emergency Care |  |

### Referral Management - Community Pharmacy {#InteroperabilityStandardV18.0.0-ReferralManagement-CommunityPharmacy}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.13} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.13} |
| --- | --- |
| - 111 | Without Using NHS 111 Report Adaptor  {#InteroperabilityStandardV18.0.0-WithoutUsingNHS111ReportAdaptor.1}  - Interoperability Toolkit (ITK) - Clinical Document Architecture (CDA) |
| - Booking and Referral Standard (BaRS) | - BaRS provides a list of prerequisites in the BaRS Implementation Guide |
| - Personal Demographics Service (PDS) | PDS FHIR API {#InteroperabilityStandardV18.0.0-PDSFHIRAPI.1} For Suppliers of new services or applications:   - Authentication and Access- using NHS Care Identity Service 2 API  2018 PDS Integration Requirements – v1.0 or older {#InteroperabilityStandardV18.0.0-2018PDSIntegrationRequirements–v1.0orolder.1} For Suppliers of services which ARE currently deployed into an operational environment:   - External Interface Specification (EIS) - NHS Messaging Implementation Manual (MIM) - Authentication and Access |

## Capabilities to support new ways of working {#InteroperabilityStandardV18.0.0-Capabilitiestosupportnewwaysofworking}

### Cross-organisation Appointment Booking {#InteroperabilityStandardV18.0.0-Cross-organisationAppointmentBooking}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.14} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.14} |
| --- | --- |
| GP Connect Appointment Management (Consumer requirements) | - Personal Demographics Service (PDS) \* or Spine Mini Services   \*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution. |

### Unified Care Record {#InteroperabilityStandardV18.0.0-UnifiedCareRecord}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.15} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.15} |
| --- | --- |
| - GP Connect Access Record HTML (Consumer requirements)   Or   - GP Connect Access Record Structured (Consumer requirements) | - Personal Demographics Service (PDS) \* or Spine Mini Services   \*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution. |

### Medicines Optimisation {#InteroperabilityStandardV18.0.0-MedicinesOptimisation}

| Interoperability Requirement {#InteroperabilityStandardV18.0.0-InteroperabilityRequirement.16} | Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.16} |
| --- | --- |
| - GP Connect Access Record Structured (Consumer requirements) | - Personal Demographics Service (PDS) \* or Spine Mini Services   \*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution. |

# Dependencies {#InteroperabilityStandardV18.0.0-Dependencies.17}

There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents

# Deprecated Standards {#InteroperabilityStandardV18.0.0-DeprecatedStandards}

There are currently no Deprecated Standards.

# Roadmap {#InteroperabilityStandardV18.0.0-Roadmap}

| **Items on the Roadmap which impact or relate to this Standard** |
| --- |
| | Title | | --- | | No content found. | |