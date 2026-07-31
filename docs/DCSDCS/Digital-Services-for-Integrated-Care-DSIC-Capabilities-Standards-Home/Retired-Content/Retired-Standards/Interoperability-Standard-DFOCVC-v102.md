---
page_id: "12576653313"
space: "DCSDCS"
title: "Interoperability Standard (DFOCVC) v1.0.2"
version: 1
updated: "2023-10-16T15:17:12.533Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12576653313/Interoperability+Standard+DFOCVC+v1.0.2"
labels: ["overarching_standard_retired"]
---

# Interoperability Standard (DFOCVC) v1.0.2

|  |  |
| --- | --- |
| **ID** | S74 |
| **Version** | 1.0.1 |
| **Type** | Interoperability Standard |
| **Status** | Retired |
| **Effective Date** | 30 Aug 2023 |
| **Framework(s)** | [DFOCVC](#) |

/\*<![CDATA[\*/
div.rbtoc1785510305925 {padding: 0px;}
div.rbtoc1785510305925 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785510305925 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#InteroperabilityStandard(DFOCVC)v1.0.2-Introduction)
- [Notes on quality and consistency of interface documentation](#InteroperabilityStandard(DFOCVC)v1.0.2-Notesonqualityandconsistencyofinterfacedocumentation)
- [Interoperability principles](#InteroperabilityStandard(DFOCVC)v1.0.2-Interoperabilityprinciples)
  - [Interoperability non-functional requirements](#InteroperabilityStandard(DFOCVC)v1.0.2-Interoperabilitynon-functionalrequirements)
  - [Minimum non-functional requirements for interfaces built to the Authority's specifications](#InteroperabilityStandard(DFOCVC)v1.0.2-Minimumnon-functionalrequirementsforinterfacesbuilttotheAuthority'sspecifications)
- [Capability-independent interoperability standards](#InteroperabilityStandard(DFOCVC)v1.0.2-Capability-independentinteroperabilitystandards)
  - [Spine](#InteroperabilityStandard(DFOCVC)v1.0.2-Spine)
  - [IM1 - Interface Mechanism](#InteroperabilityStandard(DFOCVC)v1.0.2-IM1-InterfaceMechanism)
  - [Authentication and authorisation](#InteroperabilityStandard(DFOCVC)v1.0.2-Authenticationandauthorisation)
  - [Communications](#InteroperabilityStandard(DFOCVC)v1.0.2-Communications)
  - [Roadmap](#InteroperabilityStandard(DFOCVC)v1.0.2-Roadmap)

# Introduction

This Standard provides a single place for system Suppliers to find out which interfaces they need to implement and to access the required documentation.

Future changes to interfaces will be communicated via the Roadmap.

# Notes on quality and consistency of interface documentation

There are a large number of interfaces that systems need to implement. These interfaces, and their documentation, have been created over a very long period of time by a number of different organisations and programmes. The static nature of the systems market (no new entrants needing to implement) means that historically there has been limited justification and appetite for modernising or standardising existing documentation. This means that the format, quality and consistency of interface documentation is currently extremely variable.

Until these issues can be addressed suppliers and system implementers should expect to encounter issues with interface documentation. These could include:

- Inconsistencies in how optionality of requirements is expressed, e.g. MoSCoW ratings
- References to obsolete or outdated externalities, e.g. in-force legal frameworks, organisations or systems
- Descriptions of 'upcoming' or planned future phases which may or may not have actually occurred
- Broken links
- Referenced documents that have been included elsewhere in this standard rather than in the indicated location
- Referenced documents that interface owners have advised are no longer relevant
- Unavailable information relating to the impact of upcoming roadmap changes, e.g. where the replacement of existing VUA/OSA/LOSA based patient accounts by NHS login could impact an interface implementation
- Verbose and/or difficult to follow documentation compared to modern best practices for interface documentation
- Unavailable sample files or test data

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

| **Req ID** | **Requirement Text** | **Level** |
| --- | --- | --- |
| ISNFR01 | Suppliers will implement uplifts to the message & API specifications included within the interoperability standard as agreed & directed by the ‘Minor or patch changes’ section of the Change Management Process. | MUST |
| ISNFR02 | The system will provide comprehensive audit facilities for ALL messages, including acknowledgements, over ALL transports and using ALL message types/syntax in order to satisfy general IG requirements and specific message flow requirements to ensure that support desks have access to the required information when investigating incidents/issues. | MUST |
| ISNFR03 | Suppliers will publicly publish full documentation for all currently live or in development and available-to-consumers interfaces, under a Creative Commons Attribution-NoDerivatives 4.0 International License. Documentation must include, but is not limited to:   - Full details of all available endpoints - Message structures - Code sets - Intended interface behaviour, including any sequencing of calls, with pseudo code reference exemplars. - Requirements on consumers - Error handling - Authentication and authorisation requirements - Encryption, transport layer security and certificate requirements | MUST |
| ISNFR04 | For all currently live or in development and available-to-consumers interfaces, suppliers will make available public, mock versions of the interfaces to support consumer development and testing. Mocks must meet the following criteria:   1. They must cover the full scope of behaviour of the interface 2. They must offer sufficient fidelity to the live interface to fully support consumer development and testing     1. Test data/scenarios must be publicly documented, e.g. consumers will be clearly signposted which data they must submit in order to test a particular endpoint, error handling scenario or particular behaviour of the interface | MUST |
| ISNFR05 | Discrepancies discovered between ISNFR04 test mocks and behaviour of live interfaces will be rectified within two working days of first notification to the interface provider | SHOULD |
| ISNFR06 | Discrepancies discovered between ISNFR03 documentation and actual interfaces will be rectified within 5 working days of first notification to the interface provider | MUST |
| ISNFR07 | Within the scope of interfaces specified within the standard, Suppliers must not offer differential service, e.g all API functionality and behaviour will be equally available to all API consumers, including the API provider's own apps. | MUST |
| ISNFR08 | Suppliers should not offer multiple APIs for the same purpose, e.g. there should not be multiple, different Appointments Booking APIs. Suppliers are free to offer APIs to different consumers under different commercial terms if permitted by the contract and framework, but they should offer only one technical API for each purpose. | SHOULD |
| ISNFR09 | Suppliers to provide Patient/Service User level data about a specific Patient/Service User upon request from the healthcare organisation. | MUST |

## Minimum non-functional requirements for interfaces built to the Authority's specifications

Where an interface/extract is built to the Authority's functional specifications, e.g. IM1 - Interface Mechanism, GP Connect the following requirements apply to the production implementation. For requirements relating to performance and availability suppliers should refer to the Service Level Agreement.

| **Req ID** | **Requirement Text** | **Level** |
| --- | --- | --- |
| ASNFR01 | Data currency. Updates to systems made through non-API mechanisms (e.g. user interface) should be available on APIs in real time, i.e. as soon as the update transaction is committed. | SHOULD |
| ASNFR02 | Data currency. Updates made through APIs must be available on APIs in real time, i.e. as soon as the update transaction is committed. | MUST |

# Capability-independent interoperability standards

This section lists the interoperability requirements which are not linked to single capabilities, they do not offer an alternative to implement a requirement that mandates compliance with specific Interoperability Standard(s). These are typically (but not exclusively) supporting standards such as communications protocols or related technical standards.

## Spine

The NHS Spine provides national interoperability infrastructure as well as specific national services, for example the Personal Demographics Service (PDS).

Two specific Spine components are key supporting standards for a number of the interop standards, they are:

- External Interface Specification (EIS) describes how to connect to NHS Spine services
- NHS Messaging Implementation Manual (MIM) describes the message formats used for Spine interactions

## IM1 - Interface Mechanism

IM1 - Interface Mechanism is a mechanism for accessing data held in GP Systems (Systems providing one or more Capabilities as part of the GP IT Futures Framework). The interface mechanism facilitates three use-cases (Patient, Bulk and Practice) which are detailed within the IM1 page.

A system or application may wish to **consume** IM1 interfaces where they have a requirement to access data held in GP Systems.

## Authentication and authorisation

Standards for confirming the identity of service users and controlling their access to services or specific resources.

- Authentication and Access
- NHS login service

## Communications

- Email (system accounts for automated sending for purposes such as notifications)

## Roadmap

| **Items on the Roadmap which impact or relate to this Capability** |
| Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding   | Roadmap Item | | --- | | No content found. | |