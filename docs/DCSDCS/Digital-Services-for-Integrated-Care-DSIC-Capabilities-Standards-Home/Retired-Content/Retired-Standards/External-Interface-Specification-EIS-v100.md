---
page_id: "11963203670"
space: "DCSDCS"
title: "External Interface Specification (EIS) v1.0.0"
version: 1
updated: "2022-04-28T09:38:44.278Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11963203670/External+Interface+Specification+EIS+v1.0.0"
labels: ["interop_standard_retired"]
---

# External Interface Specification (EIS) v1.0.0

|  |  |
| --- | --- |
| ID | S40 |
| Version | 1.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

- [Introduction](#ExternalInterfaceSpecification(EIS)v1.0.0-Introduction)
  - [EIS - External Interface Specification](#ExternalInterfaceSpecification(EIS)v1.0.0-EIS-ExternalInterfaceSpecification)
- [Requirements](#ExternalInterfaceSpecification(EIS)v1.0.0-Requirements)
  - [Message Handling Service - EIS Part 2](#ExternalInterfaceSpecification(EIS)v1.0.0-MessageHandlingService-EISPart2)
    - [Direct messaging (Supplier to/from Spine)](#ExternalInterfaceSpecification(EIS)v1.0.0-Directmessaging(Supplierto/fromSpine))
      - [Web Service](#ExternalInterfaceSpecification(EIS)v1.0.0-WebService)
      - [ebXML Reliable Asynchronous](#ExternalInterfaceSpecification(EIS)v1.0.0-ebXMLReliableAsynchronous)
      - [Unreliable Asynchronous](#ExternalInterfaceSpecification(EIS)v1.0.0-UnreliableAsynchronous)
    - [Intermediary messaging (Supplier to/from Supplier via TMS)](#ExternalInterfaceSpecification(EIS)v1.0.0-Intermediarymessaging(Supplierto/fromSupplierviaTMS))
      - [Multi-hop End-Party Reliability](#ExternalInterfaceSpecification(EIS)v1.0.0-Multi-hopEnd-PartyReliability)
      - [Multi-hop Intermediary Reliability](#ExternalInterfaceSpecification(EIS)v1.0.0-Multi-hopIntermediaryReliability)
      - [Multi-hop No-Party Reliability](#ExternalInterfaceSpecification(EIS)v1.0.0-Multi-hopNo-PartyReliability)
    - [Message Structure](#ExternalInterfaceSpecification(EIS)v1.0.0-MessageStructure)
      - [ebXML (EIS11.6 section 2.5.4)](#ExternalInterfaceSpecification(EIS)v1.0.0-ebXML(EIS11.6section2.5.4))
      - [Web Service (EIS11.6 section 2.6.4)](#ExternalInterfaceSpecification(EIS)v1.0.0-WebService(EIS11.6section2.6.4))
  - [Message Interaction Map - EIS Part 3](#ExternalInterfaceSpecification(EIS)v1.0.0-MessageInteractionMap-EISPart3)
  - [Gazetteer Service - EIS Part 4](#ExternalInterfaceSpecification(EIS)v1.0.0-GazetteerService-EISPart4)
    - [Gazetteer Functions](#ExternalInterfaceSpecification(EIS)v1.0.0-GazetteerFunctions)
  - [SDS - Spine Directory Service - EIS Part 5](#ExternalInterfaceSpecification(EIS)v1.0.0-SDS-SpineDirectoryService-EISPart5)
    - [Example Usage](#ExternalInterfaceSpecification(EIS)v1.0.0-ExampleUsage)
  - [SSB - Spine Security Broker - EIS Part 6](#ExternalInterfaceSpecification(EIS)v1.0.0-SSB-SpineSecurityBroker-EISPart6)
    - [SSB Deployment Model](#ExternalInterfaceSpecification(EIS)v1.0.0-SSBDeploymentModel)
  - [SSB API - Spine Security Broker Application Interface - EIS Part 7](#ExternalInterfaceSpecification(EIS)v1.0.0-SSBAPI-SpineSecurityBrokerApplicationInterface-EISPart7)
  - [EIS Parts 8,9 and 10](#ExternalInterfaceSpecification(EIS)v1.0.0-EISParts8,9and10)
  - [ACS - Access Control Service - EIS Part 11](#ExternalInterfaceSpecification(EIS)v1.0.0-ACS-AccessControlService-EISPart11)
  - [One Click CSA - EIS Part 12](#ExternalInterfaceSpecification(EIS)v1.0.0-OneClickCSA-EISPart12)
  - [Appendix - EIS part A](#ExternalInterfaceSpecification(EIS)v1.0.0-Appendix-EISpartA)
  - [Errors - EIS Part B](#ExternalInterfaceSpecification(EIS)v1.0.0-Errors-EISPartB)
  - [Validation - EIS part C](#ExternalInterfaceSpecification(EIS)v1.0.0-Validation-EISpartC)
- [Roadmap](#ExternalInterfaceSpecification(EIS)v1.0.0-Roadmap)

# Introduction

## EIS - External Interface Specification

The External Interface Specification details how to connect to the NHS Digital Spine Services. It is made up of a number of parts detailing core spine subsystems and should be used alongside other specifications such as the NHS Message Implementation Manuals (MIMs), Domain Message Specifications (DMS’s) etc.

The EIS supports the legacy Interfaces to NHS Digital Spine and is currently being uplifted to the Spine-Core website for ease of access.

The EIS is made up of number individual documents, some of which have been deprecated hence will not be available. Each section is versioned separately at the last version of the EIS it was uplifted for its core content, with the whole compilation of documents uplifted to EIS 12.3 for NHS Digital rebranding.

This EIS describes the interfaces for the following national services:

- Electronic Transfer of Prescriptions (ETP)
- Electronic Referrals Service (e-RS).
- GP to GP (GP2GP)
- Gazetteer Service.
- Spine Directory Service (SDS).
- Spine Security Broker (SSB).
- Personal Demographics Service (PDS) – now known as Spine II Demographics.
- Legitimate Relationship Service (LRS).
- Personal Spine Information Services (PSIS) – now known as Spine II Clinicals
- Health and Social Care Initiative (HSCI)
- Child Protection Information Service (CPIS)

Note – EIS parts 8,9 and 10 have been withdrawn and are no longer in use and Part 1 is an introduction and covered here.

All amendments to each section of the EIS are documented in Part 1 The Introduction  EIS12.4--Part 1--Intro.doc

# Requirements

## Message Handling Service - EIS Part 2

Describes the behaviour and interface protocols for MHS nodes.  MHS nodes are responsible for reliable transport of HL7/XML messages to and from NHS Digital Spine.

The NHS Digital Message Handling Service (MHS) is the service that is responsible for handling all messages sent to Spine from local applications.  All senders/receivers of NHS digital XML documents and message interactions are required to implement an MHS.  The MHS supports both HL7 and non-HL7 XML, each type has differences in processing requirements.  The NHS Digital MHS historically referred to as the Transaction and Messaging service (TMS).

 The MHS section of the EIS describes the behaviour, protocols, message formats, and service contracts that represent an MHS node communicating with NHS Digital Spine.

For legacy services, the NHS Digital Spine MHS provides 2 modes of operation; ebXML mode, and web service mode.  Each mode varies in behaviour and header constructs.

Although the NHS Digital Spine interactions traversing the MHS are  [HL7-ebXML] and [HL7-WS], they are not wholly conformant with them.  There have been NHS-specific changes to meet specific needs.

Note the nomenclature,  [ebXML-MS] uses the term Message Service Handler (MSH) to describe an implementation of [ebXML-MS].  The term used in this specification is MHS.  The difference is to enforce the fact that MHS includes both ebXML MSH and web service functionality.  When this specification uses the term MSH, it is specifically referring to [ebXML-MS] only.

The core Message patterns in use are:

### Direct messaging (Supplier to/from Spine)

(*coming soon: message examples*)

#### Web Service

- Synchronous - business response returned over an open connection
- SOAP envelop and wrapper
- No reliability, no support for retry or duplicate elimination
- Typically used when:
  - a user is querying existing data
  - a user requires a quick answer
  - processing can be completed quickly (~350ms)
  - reliability is not important (if it fails, the user can try again)
  - the response is small (technically limited to 50kB in Spine 1, though some extension to 500kB for PSIS)

There are 3 types of synchronous messages for Web Service Mode :

- HL7 Messages – see EIS part 2 (MHS) section 2.6.4
- Non-HL7 Services – See EIS part 2 (MHS) section 2.6.5
- Pseudo HL7 Web Services – See EIS part 2 (MHS) section 2.6.6

Examples: PDS Simple Trace, PDS Retrieval, PSIS Event List Query

#### ebXML Reliable Asynchronous

- Asynchronous - signal level acknowledgement over the open connection, new return connection for the business response
- ebXML wrappers and MIME attachments
- Supports reliability (retry, persist duration, acknowledgements, duplicate elimination)
- Typically used when:
  - a user/system is informing Spine of an update/addition/removal to existing data
  - processing time is not critical (>1s is ok)
  - reliability is important (once acknowledged, the user can reasonably assume that the change will be made)
  - the response may be large (technically limited to 5MB in Spine 1)

Examples: All EPS messages, PDS Update, PSIS GP Summary

#### Unreliable Asynchronous

- Asynchronous
- ebXML wrappers and MIME attachments
- No reliability, no support for retry or duplicate elimination
- Typically used when:
  - a user is querying existing data
  - a user requires a quick answer
  - processing can be completed quickly (<1s) but not quickly enough for synchronous messaging
  - reliability is not important (if it fails, the user can try again)
  - the response may be large

### Intermediary messaging (Supplier to/from Supplier via TMS)

#### Multi-hop End-Party Reliability

- Asynchronous
- ebXML wrappers and MIME attachments
- Supports reliability, but managed by the end systems
- Typically used when:
  - a user/system is informing another system of an update/addition/removal to existing data
  - end-party availability is good
  - processing time is not critical (>1s is ok)
  - reliability is important
  - the response may be large

Examples: All Choose and Book R1 messages

#### Multi-hop Intermediary Reliability

- Asynchronous
- ebXML wrappers and MIME attachments
- Supports reliability, but managed by Spine (TMS accepts message from supplier then handles onward retries)
- Typically used when:
  - a user/system is informing another system of an update/addition/removal to existing data
  - end-party availability is poor or unknown
  - reliability is important
  - the response may be large

Examples: All Choose and Book R2 messages, GP2GP messages

#### Multi-hop No-Party Reliability

- Asynchronous
- ebXML wrappers and MIME attachments
- No support for reliability, but managed by Spine (TMS accepts message from supplier then handles onward retries)
- Typically used when:
  - a user/system is informing another system of an update/addition/removal to existing data
  - reliability is not important
  - the response may be large

Examples: All ERS  messages

### Message Structure

#### ebXML (EIS11.6 section 2.5.4)

The ebXML Message Service Specification defines a set of namespace-qualified SOAP Header and Body element extensions within the SOAP *Envelope*. These are packaged within MIME multipart attachments to allow payloads or other related attachments to be included with the SOAP extension elements.

The (HL7 or other) messages themselves are included in zero or more additional MIME parts in compliance with SOAP Messages with Attachments [SOAP-Att]. Implementations SHOULD ensure that attachments are compliant with [WSI-ATT].

There are two logical MIME parts within the Message Package:

- The first MIME part, referred to as the Header Container, containing one SOAP compliant XML message.
- Zero or more additional MIME parts, referred to as Payload Containers, containing application-level payloads. This is where NHS messages are

#### Web Service (EIS11.6 section 2.6.4)

The SOAP header contains [WS-A] elements, while the SOAP body contains the HL7 interaction message. The binding of HL7 elements to the [WS-A] structures were derived from [HL7-WSA]. For responses, the HL7 wrapper is wrapped in a *nasp* element in order to aid WSDL WS-I Basic Profile compliance. Please refer to [NASP-XML] for all messages that include the wrapping *nasp* element.

Additional details can be found in **EIS11.6--Part 2--MHS.doc** or the Spine Core site (coming soon)

## Message Interaction Map - EIS Part 3

This Message Interaction Map section of the EIS outlines HL7/Spine operational forms and message behaviour patterns of the  HL7 messages defined in the MIM or DMS. Local system implementations MUST support the MHS, HL7 and Spine non-HL7 behaviours defined in this section of the EIS. The details of the interface behaviour i.e. the contract properties used in ebXML are configured in the SDS and not defined in this section of the EIS.

Each subsection defines the behavioural elements for each MIM/Spine message domain implemented in Release 2008-B. For each domain, the following is provided:

- HL7/Spine non-HL7 Interaction. A message exchange begins with a specific interaction and a responding interaction. Some domains also require responses to responses. The interaction is described in its colloquial and normative form. The normative form is of the xxxx\_INnnnnnnUKvv form for HL7 interactions - Spine interactions are defined here and elsewhere within the EIS.
- MHS Message behaviour. This is the specific configured behaviour documented for MHS protocol implementations. The behaviour is described in the external document Message Behaviour Patterns. MHS implementations use Message Behaviour Patterns, as well as the MHS section of the MHS document, to specialise protocol behaviour left otherwise unconstrained by industry standard protocols (such as ebXML and web services). The following behaviours are adopted from Message Behaviour Patterns to the message domains:
  - Web Service
  - ebXML Reliable Asynchronous
  - Multi-hop End-Party Reliability
  - Multi-hop Intermediary Reliability
  - Unreliable Asynchronous
  - No-Party Reliability
- HL7 Forms of Operation. The HL7 behavioural forms describe how the layer above (the HL7 processor) behaves from a protocol perspective. This is documented in Part 2 of this specification. The two options supported by this specification are RIF Form and State Exchange Form.
- Error codes and messages have been removed from the MIM so that they may be described by each service owner. At this point, the domain error codes for services owned by NHS Digital are documented in this specification.

Full details can be found in **EIS12.4--Part 3--MessageInteractionMap.doc** or the Spine Core Site (coming soon)

## Gazetteer Service - EIS Part 4

(also known as Address Finder Service)

The Gazetteer Service supports the validation or retrieval of UK-based addresses. The service will fulfil requests coming from systems external to Spine as well as those from internal clients. It is an address validation service accessing a separate address list Postal Address File (PAF)

The service requires a relatively low level of reliability and as such will implement an MHS relationship with the client in web service mode.  The service will be provided via a SOAP web service defined by a WSDL.

The Gazetteer provides the following functionality to external systems:

- Validate and transform the address to PAF standard
- Search and return address list based on search criteria

### Gazetteer Functions

The Gazetteer service provides various functions for validating an address based on complete/partial address lines provided by the caller subsystems. This includes:

1. Single search result based on the house number/name and postcode.
2. Multiple search results on partial address inputs or wildcard searches.
3. Fuzzy searches based on the phonetics of words entered in address lines.
4. Intelligent postcode parsing to validate the underlying structure.
5. Return of the PAF address key for each delivery point.

Full details can be found in **EIS12.4--Part 4--Gazetteer Service.doc** or the Spine Core Site (coming soon)

## SDS - Spine Directory Service - EIS Part 5

SDS is a directory-structured facility for the maintenance and publication of reference data about

- NHS organisations (including independent organisations performing services to the NHS),
- Users (people e.g. NHS Staff) The user information includes detailed role-based access control data for use by all accredited systems.
- Services (accredited system endpoints that connect to Spine)

SDS is a vital component in the architecture that supports NHS Digital Spine systems and processes. As well as providing a straightforward user and services look-up facility, SDS provides accurate addressing of messaging between NHS systems. SDS interfaces with Spine functions such as SSB (Spine Security Broker - a single sign-on mechanism for NHS Digital Spine), CIS (Care Identity Service is previously known as Identity Management), and the ACS (Access Control Service) for Legitimate Relationships to provide authentication.

Individual modules of information stored within SDS can be combined to provide extended cross-domain functionality.

See  **Spine Core Site** for more details.

NB: message contract properties should be queried before an interaction is sent

### Example Usage

Reference data may be used by a system such as eRS (Electronic Referrals Service) when searching for an accredited system (service endpoint), by a Patient Administration System which needs to identify a user’s unique Spine identifier from their clinical code, or when a system needs to determine which GP Practice a GP is associated with based on their General Medical Practitioner Code.

Authentication functionality provided by SDS and CIS may be used by other systems such as eRS or other systems connecting to Spine to validate access to patient records.

Full details can be found in **2087 EIS11.8--Part 5--SDS.doc**  and practical guidance is here on the **Spine Core Site**

Some **Example SDS queries** for FHIR endpoint lookup can also be found on the Spine Core site.

## SSB - Spine Security Broker - EIS Part 6

The Spine Security Broker (SSB) interface Specification describes the external interfaces required by system implementers to provide for single sign-on.

The SSB provides services for the security needs of both Web-based and non-Web-based applications.  It is delivered in three main building blocks.

- The first is the Identity Server, which provides the core functionality of the central SSB Service.  The Identity Server serves up SSO Tokens and manages the sessions for users who have been successfully authenticated.
- The second is an Identity Agent (IA), which resides on the User Workstation.  The Identity Agent mediates the authentication transaction and serves subsequent User information on demand as part of the application-orientated authorisation process.
- The third is a Client Signing Interface, which provides client-side digital signing functions for the purposes of Content Commitment. This interface primarily uses cryptographic functions that execute on a user’s smart card.

User authentication may only occur if the User is formally registered to the Spine. User registration to the Spine includes the creation of a User profile, stored in the SDS, containing the User’s roles and other information that the Authority or Service deems necessary to make appropriate data access decisions.  The figure below of the SSB Deployment Model represents a deployment model of the SSB components and shows the interfaces described in this section.

### SSB Deployment Model

![SSB Deployment Model](https://nhse-dsic.atlassian.net/wiki/download/attachments/11963203670/SSD.png?api=v2)

Full details can be found in **2087 EIS12.2--Part 6--SSB.doc.**

## SSB API - Spine Security Broker Application Interface - EIS Part 7

The Spine Security Broker Application Interface details the formal specification of SSB Java and C APIs.

Full details can be found in **2087 EIS11.8--Part 7--SSB API.doc** or here **Spine Core Site - Smartcards** and there is information about the Warranted Environment Specification.

## EIS Parts 8,9 and 10

These have been withdrawn and are no longer in use.

## ACS - Access Control Service - EIS Part 11

The  ACS subsystem service part of the EIS specifically it covers the requirements for the web services to support resource-based access control maintenance and query.

The Service exposes authorisation information on Spines external interface via the following messages and is primarily used for SCR consent:

- SET\_RESOURCE\_PERMISSIONS\_INUK01
- GET\_RESOURCE\_PERMISSIONS\_INUK01
- GET\_RESOURCE\_PERMISSIONS\_RESPONSE\_INUK01
- HAS\_RESOURCE\_PERMISSIONS\_INUK01
- HAS\_RESOURCE\_PERMISSIONS\_RESPONSE\_INUK01

Full details can be found in **2087 EIS11.6--Part 11-- Access Control Service.doc**

## One Click CSA - EIS Part 12

SCRa is a general purpose non-business specific web application which will allow users to access a summary of a patient's Shared Patient Clinical Record clinical record.  The overall functionality of the service as required in the context of external systems will be limited to the following interface:

- IfiCSAoc

One-click provides a method for a client system to launch SCRa in a specific patient context. It allows systems not directly integrated to the Spine messaging systems to access to the Summary Care Record and related SCRa functionality in a relatively seamless manner. It allows access only to the single patient record that is supplied as part of the initial call to CSA One-click.

When invoked through this interface the SCRa will present the user with functionality that is appropriate to their role.

Note: this functionality will be limited to that described in the 2008B CSA Sub System Requirements Specification.

Full details can be found in **2087 EIS11.7--Part 12--One Click CSA.doc**

## Appendix - EIS part A

This is a general appendix, referenced by other sections of the External Interface Specification. It provides a list of references, acronyms and includes detailed information on message metadata.

Full details can be found in **2087 EIS11.6--Part A--Appendix.doc**

## Errors - EIS Part B

Provides a description of the Error Base process and how to interpret error bases.

This section of the EIS details two aspects of Spine Errors:

- the process around the creation of the Spine Error Base
- the detail on how to interpret the Error Base for individual domains

NHS Digital services require both an interface (the interaction in HL7 terminology) and an implementation supported by a Service Provider (this can be national or local services).  A service consumer holds a "service contract" with a particular version of the interface. However, the implementation can evolve independently.  Service Providers are required to ensure that an interface will return exception codes applicable to that interface version (as defined in the specifications that describe the interface ) unless the following events have occurred with the implementation:

- New NHS Digital agreed validation has been added to the implementation.
- NHS Digital has agreed on a change to existing validation of the implementation.
- NHS Digital has agreed to the removal of existing validation within the implementation.
- NHS Digital has agreed on validation changes resulting from agreed changes to the business process defined within the implementation.

Service consumers should implement a level of abstraction between the error code and text supplied by the service, and the user. This will allow the consumer to provide context-aware reporting to the user and consuming system logs.

Full details can be found in **2087 EIS11.6--Part B--Errors.doc**

## Validation - EIS part C

The validation section of the EIS  records the validation rules implemented by the service provider or intermediary where applicable (SPINE) on messages entering SPINE via core message patterns. These include:

- Multi-Hop End-Party Reliability Message AND Multi-Hop No-Party Reliability Patterns
- Multi-Hop Intermediary Reliability Message Pattern
- ebXML Reliable Asynchronous Message Pattern
- ebXML Unreliable Asynchronous Message Pattern
- Web Service (P1R1) Message Pattern
- Web Service (P1R2) Message Pattern

This information is provided to inform service consumers (local systems) as to the level of validation performed by the service provider (SPINE). To accurately and concisely describe validation rules XPath expressions have been maintained. Thus readers are assumed to be familiar with XPath and regular expressions.

Full details can be found in **2087 EIS11.6--Part C--Validation.doc**

# Roadmap

| Title |
| --- |
| No content found. |

## Attachments

- [EIS12.4--Part 3--MessageInteractionMap.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203687-EIS12.4--Part 3--MessageInteractionMap.doc)
- [EIS12.4--Part 1--Intro.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203690-EIS12.4--Part 1--Intro.doc)
- [EIS12.4--Part 4--Gazetteer Service.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203693-EIS12.4--Part 4--Gazetteer Service.doc)
- [2087 EIS11.6--Part C--Validation.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203696-2087 EIS11.6--Part C--Validation.doc)
- [2087 EIS11.6--Part B--Errors.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203699-2087 EIS11.6--Part B--Errors.doc)
- [2087 EIS11.6--Part A--Appendix.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203702-2087 EIS11.6--Part A--Appendix.doc)
- [2087 EIS11.7--Part 12--One Click CSA.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203705-2087 EIS11.7--Part 12--One Click CSA.doc)
- [2087 EIS11.6--Part 11-- Access Control Service.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203708-2087 EIS11.6--Part 11-- Access Control Service.doc)
- [2087 EIS11.8--Part 7--SSB API.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203711-2087 EIS11.8--Part 7--SSB API.doc)
- [2087 EIS12.2--Part 6--SSB.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203714-2087 EIS12.2--Part 6--SSB.doc)
- [2087 EIS11.8--Part 5--SDS.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203717-2087 EIS11.8--Part 5--SDS.doc)
- [EIS12.3--Part 3--MessageInteractionMap.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203720-EIS12.3--Part 3--MessageInteractionMap.doc)
- [EIS11.6--Part 2--MHS.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203723-EIS11.6--Part 2--MHS.doc)
- [EIS12.3--Part 1--Intro.doc](../../../../.raw/DCSDCS/attachments/11963203670/att11963203726-EIS12.3--Part 1--Intro.doc)
- [SSD.png](../../../../.raw/DCSDCS/attachments/11963203670/att11963203729-SSD.png)
