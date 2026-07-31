---
page_id: "1391133681"
space: "DCSDCS"
title: "Interoperability Standard"
version: 43
updated: "2026-07-20T10:32:51.762Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133681/Interoperability+Standard"
labels: ["overarching_standard"]
---

# Interoperability Standard

|  |  |
| --- | --- |
| **ID** | S32 |
| **Version** | 18.2.6 |
| **Type** | Interoperability Standard |
| **Status** | Effective |
| **Effective Date** | 20 Jul 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [DFOCVC](https://nhse-dsic.atlassian.net/wiki/spaces/DFOCVCL) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#InteroperabilityStandard-Introduction)
- [Notes on quality and consistency of interface documentation](#InteroperabilityStandard-Notesonqualityandconsistencyofinterfacedocumentation)
- [Interoperability principles](#InteroperabilityStandard-Interoperabilityprinciples)
- [Baseline Assurance Standard Requirements](#InteroperabilityStandard-BaselineAssuranceStandardRequirements)
  - [Interoperability non-functional requirements](#InteroperabilityStandard-Interoperabilitynon-functionalrequirements)
  - [Minimum non-functional requirements for interfaces built to the Authority's specifications](#InteroperabilityStandard-Minimumnon-functionalrequirementsforinterfacesbuilttotheAuthority'sspecifications)
- [Further Requirements](#InteroperabilityStandard-FurtherRequirements)
- [Capability-independent interoperability Standards](#InteroperabilityStandard-Capability-independentinteroperabilityStandards)
- [Capabilities with Interoperability Relationships](#InteroperabilityStandard-CapabilitieswithInteroperabilityRelationships)
- [Roadmap](#InteroperabilityStandard-Roadmap)

# Introduction

Defines overarching Interoperability requirements and interfaces to be implemented, including quality and principles to be followed for Supplier Solutions.

# Notes on quality and consistency of interface documentation

There are a large number of interfaces that Solutions need to implement. These interfaces, and their documentation have been created over a very long period of time by a number of different organisations and programmes. The static nature of the Solutions market means that historically there has been limited justification and appetite for modernising or standardising existing documentation. This means that the format, quality and consistency of interface documentation is currently extremely variable.

Until these issues can be addressed Suppliers and system implementers should expect to encounter issues with interface documentation. These could include:

- Inconsistencies in how optionality of requirements is expressed, e.g. MoSCoW ratings (Must Have/Should Have/Could Have/Won’t Have)
- References to obsolete or outdated externalities, e.g. in-force legal frameworks, organisations or systems
- Descriptions of 'upcoming' or planned future phases which may or may not have actually occurred
- Broken links
- Referenced documents that have been included elsewhere in this Standard rather than in the indicated location
- Referenced documents that interface owners have advised are no longer relevant
- Unavailable information relating to the impact of upcoming roadmap changes
- Verbose and/or difficult to follow documentation compared to modern best practices for interface documentation
- Unavailable sample files or test data

Suppliers should contact the Authority at [gpitfutures@nhs.net](mailto:gpitfutures@nhs.net) to resolve any documentation issues which block them from delivering compliant implementations.

# Interoperability principles

Suppliers are expected to adhere to the interoperability principles wherever possible. Whilst adherence will not be assessed in Onboarding, the Authority will expect any deviation from these principles to be supported by a valid rationale on delivery of interfaces.

Detailed guidance is available from gov.uk [Technology Code of Practice](https://www.gov.uk/guidance/the-technology-code-of-practice), [API Technical & Data Standards Guidance](https://www.gov.uk/guidance/gds-api-technical-and-data-standards) & [API Design Guidance](https://www.gov.uk/government/collections/api-design-guidance)

# Baseline Assurance Standard Requirements

The Baseline Assurance Standard (BAS) provides a proportionate, risk-based assurance approach for Solutions; balancing safety against efficiency by combining a minimum set of essential Requirements from the [DSIC Overarching Standards](index.md). Completing the BAS is the first step to achieving full assurance with the Overarching Standards allowing Supplier Solutions to be published on the Buying Catalogue. Upon meeting this Standard, Solutions are required to meet any remaining Further Requirements in the Overarching Standards in the timeframe applicable to the Contracting Vehicle.

All Baseline Assurance Requirements can be found [here.](Baseline-Assurance-Standard.md) Each Solution will be assigned a category of A, B or C that determines the level of assurance applied to that Solution. See the relevant category column to understand the assurance required for each Requirement. For information on Solution Categories see [Solution Categories for Assurance in DSIC](../../Reference-Pages/Baseline-Assurance-Standard-and-Solution-Categories-for-Assurance-in-DSIC-Guidance.md).

The following table of Requirements are the Requirements in the Baseline Assurance Standard related to the Interoperability Standard.

## Interoperability non-functional requirements

The following overarching requirements apply to all interfaces in the scope of the Interoperability Standard which are offered by a Solution.

| **Applicable Contracting Vehicle(s)** | **ID** | **Requirement** | **Level** | **Category A** | **Category B** | **Category C** |
| --- | --- | --- | --- | --- | --- | --- |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | ISNFR01 | Suppliers will implement uplifts to the message & API specifications included within the interoperability Standard as agreed & directed by the ‘Minor or patch changes’ section of the [Change Management Process](https://gpitbjss.atlassian.net/wiki/spaces/GPITF/pages/1391133471/Change+Management+Process+and+Roadmap+Introduction#ChangeManagementProcessandRoadmapIntroduction-HowwillversionupliftsbehandledthroughtheChangeprocess?). | MUST | **Self-certification** | **Self-certification** | **Self-certification** |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | ISNFR03 | Suppliers will provide the full documentation for all currently live or in development and available-to-consumers interfaces, under a [Creative Commons Attribution-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nd/4.0/). Documentation must include, but is not limited to:   - Full details of all available endpoints - Message structures - Code sets - Intended interface behaviour, including any sequencing of calls, with pseudo code reference exemplars - Requirements on Consumers - Error handling - Authentication and authorisation requirements - Encryption, transport layer security and certificate requirements | MUST | **Full Assessment**  Supporting evidence to include:   - URL of the public location where the documentation resides. - Documentation that covers all aspects listed within the Requirement. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - URL of the public location where the documentation resides. | **Self-certification** |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | ISNFR04 | For all currently live or in development and available-to-consumers interfaces, Suppliers will provide mock versions of the interfaces to support Consumer development and testing. Mocks must meet the following criteria:   1. They must cover the full scope of behaviour of the interface 2. They must offer sufficient fidelity to the live interface to fully support Consumer development and testing     1. Test data/scenarios must be publicly documented, e.g. Consumers will be clearly signposted which data they must submit in order to test a particular endpoint, error handling scenario or particular behaviour of the interface | MUST | **Self-certification** | **Self-certification** | **Self-certification** |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | ISNFR05 | Discrepancies discovered between ISNFR04 test mocks and behaviour of live interfaces will be rectified within two working days of first notification to the interface Provider. | SHOULD | **Self-certification** | **Self-certification** | **Self-certification** |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | ISNFR06 | Discrepancies discovered between ISNFR03 documentation and actual interfaces will be rectified within 5 working days of first notification to the interface Provider. | MUST | **Self-certification** | **Self-certification** | **Self-certification** |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | ISNFR07 | Within the scope of interfaces specified within the Standard, Suppliers must not offer differential service, e.g. all API functionality and behaviour will be equally available to all API Consumers, including the API Provider's own applications. | MUST | **Self-certification** | **Self-certification** | **Self-certification** |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | ISNFR08 | Suppliers should not offer multiple APIs for the same purpose, e.g. there should not be multiple, different Appointments Booking APIs. Suppliers are free to offer APIs to different Consumers under different commercial terms if permitted by the contract and Contracting Vehicle, but they should offer only one technical API for each purpose. | SHOULD | **Self-certification** | **Self-certification** | **Self-certification** |

## Minimum non-functional requirements for interfaces built to the Authority's specifications

Where an interface/extract is built to the Authority's functional specifications, e.g. IM1 - Interface Mechanism or GP Connect, the following requirements apply to the production implementation. For requirements relating to performance and availability Suppliers should refer to the [Service Levels](Service-Management.md)*.*

| **Applicable Contracting Vehicle(s)** | **ID** | **Requirement** | **Level** | **Category A** | **Category B** | **Category C** |
| --- | --- | --- | --- | --- | --- | --- |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | ASNFR01 | Data currency. Updates to systems made through non-API mechanisms (e.g. user interface) should be available on APIs in real time, i.e. as soon as the update transaction is committed. | SHOULD | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Detailed response including technical and data architecture design evidence that demonstrates compliance. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Detailed response including technical and data architecture design evidence that demonstrates compliance. | **Self-certification** |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | ASNFR02 | Data currency. Updates made through APIs must be available on APIs in real time, i.e. as soon as the update transaction is committed. | MUST | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Detailed response including technical and data architecture design evidence that demonstrates compliance. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Detailed response including technical and data architecture design evidence that demonstrates compliance. | **Self-certification** |

# Further Requirements

Suppliers will not be required to meet any Further Requirements to achieve full compliance with the Interoperability Standard.

# Capability-independent interoperability Standards

This section lists the interoperability requirements which are not linked to specific Capabilities. Where a requirement mandates compliance with specific Interoperability Standard(s), there is no alternative implementation. These are typically (but not exclusively) supporting Standards such as communications protocols or related technical Standards.

| **Applicable Contracting Vehicle(s)** | **Interoperability Standard** | **Description** | **Category A** | **Category B** | **Category C** |
| --- | --- | --- | --- | --- | --- |
| - GP IT Futures - Tech Innovation - DFOCVC - Digital Primary Care | [IM1 - Interface Mechanism](../Non-Overarching-Standards/IM1-Interface-Mechanism.md) | IM1 - Interface Mechanism is a mechanism for accessing data held in GP Systems (Systems providing one or more Foundation Capabilities). The interface mechanism facilitates three use-cases (Patient, Bulk and Practice) which are detailed within the IM1 - Interface Mechanism Standard.  A system or application is required to **provide**IM1 interfaces if it offered IM1 interfaces under GP IT Futures and/or if implementing an IM1 interface is mandated within the Capabilities and Standards.  Where a GP Connect interface capability is available, Provider Suppliers would be expected to develop against that, rather than developing a new bespoke or proprietary interface.  A system or application may wish to **consume** IM1 interfaces where they have a requirement to access data held in GP Systems and the Provider Solution does not offer a GP Connect interface. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - IM1 Standard Assurance sign off. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - IM1 Standard Assurance sign off. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - IM1 Standard Assurance sign off. |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Primary Care | [Authentication & Access](../Non-Overarching-Standards/Authentication-and-Access.md) | Standard for controlling Health or Care Professional access to services or specific resources. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Authentication and Access Standard Assurance sign off. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Authentication and Access Standard Assurance sign off. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Authentication and Access Standard Assurance sign off. |
| - GP IT Futures - Tech Innovation - DFOCVC - Digital Primary Care | [NHS Login Service](../Non-Overarching-Standards/NHS-login-service.md) | Standard for confirming the identity of Patients/Service Users. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - NHS Login Service Standard Assurance sign off. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - NHS Login Service Standard Assurance sign off. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - NHS Login Service Standard Assurance sign off. |
| - GP IT Futures - Tech Innovation - DFOCVC - Digital Primary Care | [Email](../Non-Overarching-Standards/Email.md) | Standard for Health and care systems that send and receive email; to ensure their email service meets the secure email standard. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Email Standard Assurance sign off. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Email Standard Assurance sign off. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Email Standard Assurance sign off. |
| - GP IT Futures - Tech Innovation - Digital Primary Care | [Generic FHIR Receiver](../Non-Overarching-Standards/Generic-FHIR-Receiver.md) | A component which will receive messages into the GP Practice Solution. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Generic FHIR Receiver Standard Assurance sign off. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Generic FHIR Receiver Standard Assurance sign off. | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Generic FHIR Receiver Standard Assurance sign off. |

# Capabilities with Interoperability Relationships

See [Capabilities with Interoperability Relationships](../../Reference-Pages/Capabilities-with-Interoperability-Relationships.md) for guidance on the interoperability requirements which are associated with each Capability.

Note: this page is for guidance only and does not supersede what is mandated in the individual Capabilities and Standards.

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [National Proxy Service](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15035203759/National+Proxy+Service) | [Patient Information Maintenance - GP](https://nhse-dsic.atlassian.net/wiki/x/5AXrUg), [Validated Relationship Service](../Non-Overarching-Standards/Validated-Relationship-Service.md), [GP Connect (Patient Facing) User Permissions](../Non-Overarching-Standards/GP-Connect-Patient-Facing-User-Permissions.md), [GP Connect (Patient Facing) Access Record](../Non-Overarching-Standards/GP-Connect-Patient-Facing-Access-Record.md), [GP Connect (Patient Facing) Prescriptions](../Non-Overarching-Standards/GP-Connect-Patient-Facing-Prescriptions.md), [Multicast Notification Service (MNS)](../Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) | Published | 20 Apr 2027 | Integrate with the National Proxy Service | New | Managed Capacity - Other |
| [Ingestion of Pharmacy First Urgent Medicine Supply information from Community Pharmacies into GP Solutions](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14715125761/Ingestion+of+Pharmacy+First+Urgent+Medicine+Supply+information+from+Community+Pharmacies+into+GP+Solutions) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Digital Medicines and Pharmacy FHIR Payload](../Non-Overarching-Standards/Digital-Medicines-and-Pharmacy-FHIR-Payload.md), [Consultation Management - Community Pharmacy](../../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) | Published | 09 Oct 2026 | Render HTML and ingest structured Pharmacy First Urgent Medicine Supply information from Community Pharmacies into Patient Electronic Patient Records (EPRs) in GP Solutions | Uplift | Managed Capacity - Minor/Patch uplifts |
| [Patient Flags Service - Female Genital Mutilation (FGM) Flag](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14101676093/Patient+Flags+Service+-+Female+Genital+Mutilation+FGM+Flag) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), Patient Flags Service | Published | 08 Mar 2027 | Enable national sharing and management of Female Genital Mutilation Flag data via the Patient Flags Service - FHIR API | Uplift | Managed Capacity - Other |
| [Patient Flags Service - Child Protection - Information Sharing (CP-IS) Flag](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14101446658/Patient+Flags+Service+-+Child+Protection+-+Information+Sharing+CP-IS+Flag) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), Patient Flags Service | Published | 08 Feb 2027 | Enable national sharing and management of Patients Child Protection - Information Sharing Flags via the Patient Flags Service - FHIR API | Uplift | Managed Capacity - Other |
| [Patient Flags Service - Reasonable Adjustments (RA) Flag](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/12194349077/Patient+Flags+Service+-+Reasonable+Adjustments+RA+Flag) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Multicast Notification Service (MNS)](../Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) | Published | 08 Jan 2027 | Enable national sharing and management of Patients Reasonable Adjustments Flag via the Patient Flags Service - FHIR API | New | Managed Capacity - Other |
| [Update GP Connect Access Record Structured Requirements to include Allergies](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14634254337/Update+GP+Connect+Access+Record+Structured+Requirements+to+include+Allergies) | [GP Connect Access Record Structured](../Non-Overarching-Standards/GP-Connect-Access-Record-Structured.md) | Draft | TBC | Update the GP Connect Access Record Structured Standard to include the consumption of data for the Allergies clinical area | Uplift | Managed Capacity - Other |
| [NHS login interface - Provisioning](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/1391133536/NHS+login+interface+-+Provisioning) | [Interoperability Standard](Interoperability-Standard.md), [NHS login Service](../Non-Overarching-Standards/NHS-login-service.md), [Appointments Management - Citizen](../../DSIC-Capabilities/Appointments-Management-Citizen.md), [Communicate With Practice - Citizen](../../Deprecated-Content/Deprecated-Capabilities/Communicate-With-Practice-Citizen.md), [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Prescription Ordering - Citizen](../../DSIC-Capabilities/Prescription-Ordering-Citizen.md), [View Record - Citizen](../../DSIC-Capabilities/View-Record-Citizen.md) | Draft | TBC | The provisioning interface enables GP solutions to provision new Citizen users on the NHS login platform, thus enabling Citizens to use one consistent account for Patient sign-in and ID verification. | Replace | Opportunity Item |
| [Improved GP contract indicators for Index of Deprivation](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/12361236539/Improved+GP+contract+indicators+for+Index+of+Deprivation) | [GPES Data Extraction](../Non-Overarching-Standards/GPES-Data-Extraction.md), [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | Draft | TBC | Uplifts to the GPES Data Extraction and indicators for GP Index of Deprivation | Uplift | Managed Capacity - Minor/Patch uplifts |
| [GP Connect Appointments Practitioner Role Update](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/12690849794/GP+Connect+Appointments+Practitioner+Role+Update) | [GP Connect Appointment Management](../Non-Overarching-Standards/GP-Connect-Appointment-Management.md) | Draft | TBC | Expand the Job Roles (known as Care Connect SDS-Job Roles) the GP Practice Solution provides to each of the appointment slots it makes available via GP Connect Appointment Management API | Uplift | Managed Capacity - Other |
| [Data environment for OpenSAFELY](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/12591300609/Data+environment+for+OpenSAFELY) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | Draft | TBC | GP system Supplier data environment Standard for OpenSAFELY | New | Managed Capacity - Other |