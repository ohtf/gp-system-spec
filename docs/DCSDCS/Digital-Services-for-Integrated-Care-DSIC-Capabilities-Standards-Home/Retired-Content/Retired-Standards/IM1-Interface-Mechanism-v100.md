---
page_id: "10612277465"
space: "DCSDCS"
title: "IM1 - Interface Mechanism v1.0.0"
version: 1
updated: "2020-12-31T11:29:23.202Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/10612277465/IM1+-+Interface+Mechanism+v1.0.0"
labels: []
---

# IM1 - Interface Mechanism v1.0.0

|  |  |
| --- | --- |
| ID | S47 |
| Version | 1.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

/\*<![CDATA[\*/
div.rbtoc1785509274439 {padding: 0px;}
div.rbtoc1785509274439 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785509274439 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#IM1-InterfaceMechanismv1.0.0-Introduction)
  - [Applicability](#IM1-InterfaceMechanismv1.0.0-Applicability)
- [Requirements](#IM1-InterfaceMechanismv1.0.0-Requirements)
  - [Generic Integration Requirements](#IM1-InterfaceMechanismv1.0.0-GenericIntegrationRequirements)
    - [Monitoring & Response Times](#IM1-InterfaceMechanismv1.0.0-Monitoring&ResponseTimes)
    - [Authentication and End Points](#IM1-InterfaceMechanismv1.0.0-AuthenticationandEndPoints)
    - [System Context & Invocation](#IM1-InterfaceMechanismv1.0.0-SystemContext&Invocation)
    - [Appropriate use of integration capability](#IM1-InterfaceMechanismv1.0.0-Appropriateuseofintegrationcapability)
    - [Interface Version Management](#IM1-InterfaceMechanismv1.0.0-InterfaceVersionManagement)
    - [Error & failure handling](#IM1-InterfaceMechanismv1.0.0-Error&failurehandling)
    - [Terminology & Coding Data Sets](#IM1-InterfaceMechanismv1.0.0-Terminology&CodingDataSets)
  - [Transaction or Practice Integration](#IM1-InterfaceMechanismv1.0.0-TransactionorPracticeIntegration)
    - [Patient Information Maintenance](#IM1-InterfaceMechanismv1.0.0-PatientInformationMaintenance)
    - [Appointments Management](#IM1-InterfaceMechanismv1.0.0-AppointmentsManagement)
    - [Consultation Management](#IM1-InterfaceMechanismv1.0.0-ConsultationManagement)
    - [Documents Management](#IM1-InterfaceMechanismv1.0.0-DocumentsManagement)
    - [Prescribing](#IM1-InterfaceMechanismv1.0.0-Prescribing)
    - [Referral Management](#IM1-InterfaceMechanismv1.0.0-ReferralManagement)
    - [Resource Management](#IM1-InterfaceMechanismv1.0.0-ResourceManagement)
    - [Communications Management](#IM1-InterfaceMechanismv1.0.0-CommunicationsManagement)
  - [Patient/Citizen Facing interfaces](#IM1-InterfaceMechanismv1.0.0-Patient/CitizenFacinginterfaces)
  - [Non Primary Care Settings](#IM1-InterfaceMechanismv1.0.0-NonPrimaryCareSettings)
  - [IM1 Refresh](#IM1-InterfaceMechanismv1.0.0-IM1Refresh)
  - [Bulk Extracts](#IM1-InterfaceMechanismv1.0.0-BulkExtracts)
  - [Deprecation of Interfaces](#IM1-InterfaceMechanismv1.0.0-DeprecationofInterfaces)
  - [Compliance & Assurance](#IM1-InterfaceMechanismv1.0.0-Compliance&Assurance)
  - [Important terms and definitions](#IM1-InterfaceMechanismv1.0.0-Importanttermsanddefinitions)
    - [Transient Data Definition](#IM1-InterfaceMechanismv1.0.0-TransientDataDefinition)
    - [Definition of Administration and Clinical Data](#IM1-InterfaceMechanismv1.0.0-DefinitionofAdministrationandClinicalData)
  - [Dependencies (Patient facing interface Only)](#IM1-InterfaceMechanismv1.0.0-Dependencies(PatientfacinginterfaceOnly))
- [Roadmap](#IM1-InterfaceMechanismv1.0.0-Roadmap)

# Introduction

IM1 is a mechanism for accessing data held in GP Systems (Systems providing one or more Capabilities as part of the GP IT Futures Framework). The interface mechanism should facilitate the following use-cases:

- **Patient** - real-time access to APIs exposed over the Internet supporting both read and limited write / transactional operations for the purposes of Patient/Citizen Facing Services (including registration and authentication of Citizens)
- **Bulk** - Bulk data extracts of all data held by the GP System Supplier
- **Practice** real-time APIs for integrating systems, which may operate locally

Provider Suppliers acting as consumers of their own interfaces must take note of requirements in the Interoperability Standard, particularly those relating to equitable access to functionality and data (Requirement: [ISNFR07](../../DSIC-Standards/Overarching-Standards/Interoperability-Standard.md))

Please also note that suppliers must be compliant with the overarching Commercial Standard, and comply with the Model Interface Licence contained within.

## Applicability

A system or application is required to **provide**IM1 interfaces if ANY of the following are true:

- It offered IM1 interfaces under GPSoC
- It offers ALL Foundation capabilities under GP IT Futures

Where a GP Connect interface capability is available, suppliers would be expected to develop against that, rather than developing a new bespoke or proprietary interface.

A system or application may wish to **consume** IM1 interfaces where they have a requirement to access data held in GP Systems.

# Requirements

This page describes integration requirements for systems which are required to be an IM1 interface provider and\or consumer.

The scope of this document includes:

- Generic requirements which allude to best practices in Applications integration, Extract Transformation Loading & API Management
- Requirements around some high level API Calls and its expected behaviour in generic terms
- Requirements around System Context, Authentication & Version Management

The following are not in scope:

- Low level Interface specifications and schema definitions. IM1 interfaces are not built to a standard specification and core system suppliers are currently free to implement in whatever way they see fit, however, suppliers should read the Principles section of the Interoperability Standard and ensure their approach is aligned accordingly. Where applicable they should be able to demonstrate adherence to Principles
- Commercial arrangements and charging
- Assurance and testing
- Mechanisms to get a Consumer Supplier on board and giving access to test environments

## Generic Integration Requirements

### Monitoring & Response Times

This pertains to individual requests and responses for each message interaction and how these are monitored.

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_resp\_001 | The Provider Integration Architecture must be capable of monitoring requests received by various Consumers, including the capture of response times required for processing the request within the confines of the Supplier Data Centre / Cloud boundary | Provider | Practice & Patient | MUST |

### Authentication and End Points

This refers to how Consumer Systems and Users are authenticated and mechanisms for Consumer systems to access the IM1 interfaces

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_auth\_001 | The Provider must provide a seamless process to authenticate Consumer systems and Users without any extra overhead or usability issues  User of a Consumer Solution can refer to a patient in case of Citizen Facing capabilities or refer to a healthcare professional or NHS Staff | Provider | All | MUST |
| im1\_auth\_002 | The access to Provider Endpoints should not be constrained by existence of a User Session on the Provider Solution | Provider | Practice | SHOULD |
| im1\_auth\_003 | For the Practice IM1 where feasible, the access to Provider Endpoints should not be constrained by requiring the Consumer integration components to be present within a Practice or within the GP's workstation/PC | Provider | Practice | SHOULD |
| im1\_auth\_004 | The access to Provider file Extracts must not be constrained by requiring the Consumer integration components to be present within a Practice or within the GP's workstation/PC for the Bulk IM | Provider | Bulk | SHOULD |

### System Context & Invocation

This refers to the context of the User Session within a Provider Solution and its visibility to the Consumer

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_context\_001 | The Provider Solution must provide mechanism for Consumer to be kept aware/notified of context information. At the very minimum notification should include   - user - patient   Note: Providers will notify Consumers of state/context changes; Consumers will not be required to poll or repeatedly call the Provider system to establish if there has been a change | Provider | Practice | SHOULD |
| im1\_context\_002 | In addition the Provider Solution context information must include, where appropriate (and where subscribed to / requested by Consumer):   - Complete set of changes (additions, deletions, amendments) to patient demographics where applicable - Functional state (e.g. prescribing module selected, add Appointment selected) - Data state (e.g. the drug selected, the problem/diagnosis selected) identified uniquely using the appropriate terminology | Provider | Practice | SHOULD |
| im1\_context\_003 | The Provider Solution should have a mechanism to launch the Consumer Solution, in a particular Context, by a User of the Provider Solution- This will be dependent on Consumer Solution providing a suitable link via which the Provider could launch / invoke the Consumer Solution | Provider | Practice | MAY |

### Appropriate use of integration capability

Ensuring the Provider Solution is not impacted by huge influx of request messages and how it handles such scenarios.

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_use\_001 | Provider must be capable of applying appropriate throttling techniques in order to spread the processing load of incoming requests or Extracts processing | Provider | All | MUST |
| im1\_use\_002 | Provider must be capable of notifying the Consumer of unavailability or delay of request processing (eg. during heavy usage of the Provider System) | Provider | All | MUST |
| im1\_use\_003 | If the Consumer supports non user-initiated actions/events that may affect either Provider or Consumer Solution performance then such actions/events must be capable of being scheduled at appropriate times | Consumer | All | MUST |
| im1\_use\_004 | Where a Provider includes mechanisms to retrieve large sets of data in real time, they must provide guidance on when to use each API call or method- The documentation that describes the supplier's IM1 must also indicate whether the use of any particular Interface Mechanism may adversely affect the performance of the system, e.g. extracting all the clinical data for all patients impedes general system performance and should be run during periods of low usage or when no users are using the system | Provider | Practice & Patient | MUST |
| im1\_use\_005 | The Consumer must ensure it displays the most up-to date information to its user - Where the information is not up-to date then it should be clearly notified to the User and the User should have visibility of date-time modified for the particular data item | Consumer | All | MUST |

### Interface Version Management

It is recognized that suppliers will need to update their interface mechanisms. These requirements ensure version updates are done in a standard manner giving enough notification to Consumers and also providing them the relevant details pertaining to changes.

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_ver\_001 | The version of the Interface Mechanism will be available to Consumer systems either via API calls or messages, or provided on request to Provider | Provider | All | MUST |
| im1\_ver\_003 | Provider implement updates in a manner that supports backward compatibility leaving existing interfaces working. Where an interface has to be retired then relevant requirement applies | Provider | All | MUST |
| im1\_ver\_004 | Deprecation of interfaces must only be carried out with agreements from Authority and Consumers by providing them with enough advanced notice | Provider | All | MUST |
| im1\_ver\_005 | Any interface change which would break existing Consumer App needs to be notified beforehand and Consumers should be given the opportunity to test their Solutions against it. | Provider | All | MUST |
| im1\_ver\_006 | Any new changes in an interface needs to be very clearly documented such that different between latest version and earlier version is very clear | Provider | All | MUST |
| im1\_ver\_007 | Consumers of IM1 will be notified of deprecated interfaces and will be given suitable notice in order for their Solution to be migrated away from deprecated interfaces and utilize the latest offering of IM1 from the Provider. Consumers must work to implement the latest version | Consumer | All | MUST |

### Error & failure handling

How errors in message processing should handled and notified to consumers.

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_error\_001 | Any error condition experienced by the Provider in processing a request needs to be clearly identified, captured and logged - The Consumer should get clear specific information as to what that error was | Provider | All | MUST |
| im1\_error\_002 | Error conditions must not result in abrupt disconnection or failure of the overall Provider interface. The provider should gracefully exit when errors occur and return meaningful error messages to the consumer | Provider & Consumer | All | MUST |
| im1\_error\_003 | Consumer must display the relevant specific error message to the end-user to give them a clear indication as to what went wrong | Consumer | Practice & Patient | MUST |

### Terminology & Coding Data Sets

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_code\_001 | Provide a mechanism for a Consumer Supplier to discover versions of any coding schemes used within the Provider Solution (including SNOMED-CT, DM+d, any other standard coding terms) | Provider | Practice and Bulk | MUST |

## Transaction or Practice Integration

Requirements are listed in terms of API Calls or Methods categorized by GP IT Futures Capabilities. For existing IM1 Providers none of the API calls should be removed unless an equivalent or an uplifted version is provided.

### Patient Information Maintenance

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_cap\_001 | Search Patient  Description: The Supplier must provide a mechanism that allows Consumer systems to search for a patient by providing patient demographic data items as search parameters. At the very minimum the Provider should provide search using the following fields used independently or used in combination:  first name, last name, dob, NHS Number and Provider should return the full set of demographics for the matching patient(s) | Provider | Practice | MUST |
| im1\_cap\_002 | Update Demographics  Description: The Supplier should provide a mechanism for Consumer systems to create a request for amending patient demographics via APIs, which can then be performed by a user of the Provider system | Provider | Practice | SHOULD |
| im1\_cap\_003 | Get Patient Demographics | Provider | Practice | MUST |
| im1\_cap\_004 | Get Full Medical Record | Provider | Practice | MUST |
| im1\_cap\_005 | File Data in Patient Record | Provider | Practice | MUST |

### Appointments Management

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_cap\_006 | Get Bookable Slots (Appointment)  **Note**: This should be met via GP Connect requirements as per Interoperability Standard | Provider | Practice | SHOULD |
| im1\_cap\_007 | Book Appointment  **Note**: This should be met via GP Connect requirements as per Interoperability Standard | Provider | Practice | SHOULD |
| im1\_cap\_008 | Cancel Appointment  **Note**: This should be met via GP Connect requirements as per Interoperability Standard | Provider | Practice | SHOULD |
| im1\_cap\_009 | Check in a Patient (on arrival) | Provider | Practice | SHOULD |

### Consultation Management

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_cap\_010 | Get Consultation Records for a Patient | Provider | Practice | SHOULD |
| im1\_cap\_011 | Create a new Consultation Record | Provider | Practice | SHOULD |
| im1\_cap\_012 | Add a document or attachment to a Consultation Record | Provider | Practice | SHOULD |

### Documents Management

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_cap\_013 | File Document into a Patient Record | Provider | Practice | MUST |
| im1\_cap\_014 | Retrieve Documents for a Patient | Provider | Practice | MUST |

### Prescribing

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_cap\_016 | Get All Current Medications | Provider | Practice | MUST |
| im1\_cap\_017 | Prescribe a Drug for a Patient | Provider | Practice | SHOULD |

### Referral Management

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_cap\_018 | Get All Referrals | Provider | Practice | SHOULD |
| im1\_cap\_019 | Create a Referral | Provider | Practice | SHOULD |

### Resource Management

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_cap\_021 | Get Details For Specific Staff | Provider | Practice | MUST |

### Communications Management

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_cap\_022 | Send Message to a Patient | Provider | Practice | MAY |

## Patient/Citizen Facing interfaces

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_pfs\_001 | The interface mechanism provided by the Solution must be sufficient to support the epics and requirements of the consumer Solutions that provide citizen online services as described in the Citizen capabilities. | Provider | Patient | MUST |
| im1\_pfs\_002 | The interface mechanism must support the query of services (capabilities) that are available with respect to a specified practice, and to a specific patient. | Provider | Patient | MUST |
| im1\_pfs\_003 | The interface mechanism must support the query of which patients are associated with a specific authenticated Verified User Account (VUA). | Provider | Patient | SHOULD |

## Non Primary Care Settings

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_nonpc\_001 | In an environment where Provider provides information-sharing across clinical settings, data provided to Practice Facing Consumer systems should include all data (including that from other settings) that is visible to the Provider Solution user.  Where such data is provided to Consumer systems, it must be made clear to the Consumer system which data is managed by the Provider Solution within the context of the Practice (Primary Care), and which is visible as a result of information-sharing mechanisms  Data provided to Patient Facing Consumer systems must only include data for which the Practice acts as Data Controller. | Provider | Practice | SHOULD |

## IM1 Refresh

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_refresh\_001 | The Provider needs to ensure all IM1 APIs are maintained to reflect relevant updates to the Providers Solution, for example new or amended data fields being collected and stored by the Provider.  IM1 release cycles should be aligned with overall Solution release cycle.  The appropriate API versioning should be applied as part of any new release.  This requirement is intended to cover changes initiated by the Provider as part of BAU product maintenance and is distinct from the change process for Minor and Patch Changes, which is intended to cover changes initiated by the Authority | Provider | All | SHOULD |

## Bulk Extracts

In order to support the needs of the Practice and its related organisations (e.g. commissioners, organisations responsible for public health) access to bulk clinical data that exists in Provider systems needs to be available, whilst being securely and appropriately controlled.

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_bulk\_001 | All data and entities which are part of the Data Model as defined by the Supplier, must be made available as required in the Extracts. These must include data for all patients for which the Practice is the data controller and should also include schema definitions, relationship diagrams (where applicable) and logical model in order for a Consumer to correctly interpret the extracts  The only exception is Transient data and if the Provider Supplier wishes these could be excluded. The definition of Transient data is provided further below in the page.  Bulk Schemas and consumer requests will be reviewed every 3 months and new entities or fields required for inclusion must incorporated as agreed & directed by the ‘Minor or patch changes’ section of the Change Management Process | Provider | Bulk | MUST |
| im1\_bulk\_002 | There must be at least one extract of bulk data in a 24 hr period | Provider | Bulk | MUST |
| im1\_bulk\_003 | Batch/bulk data extracts must include all data updates older than 30 minutes from the start of the extract process | Provider | Bulk | MUST |
| im1\_bulk\_005 | Provider must use a consistent Protocol / agreement for the transfer of Bulk extracts to relevant locations such that Consumer can consume it in a safe, complete manner | Provider | Bulk | MUST |
| im1\_bulk\_006 | Provider should have mechanisms of filtering Entities / Fields / Records based on Data Controller definitions before providing the Extracts | Provider | Bulk | MUST |
| im1\_bulk\_007 | The Provider must have an ability to log the full extraction process and various activities which takes place during the extraction process including capturing of response times for the extracts - In addition it should log start and stop events, errors & exceptions, statuses | Provider | Bulk | MUST |
| im1\_bulk\_008 | Provider should provide a capability for a Consumer to send a custom request for bulk extracts (for particular patient cohorts) to be processed by Provider. This request could be processed in an asynchronous manner (in a reasonable time frame not more than 2 or 3 hrs) | Provider | Bulk | MAY |
| im1\_bulk\_009 | Consumer must provide their approach and strategy for combining data from several different disparate sources and their adherence to Information Governance guidelines in terms of acquiring and access to this data | Consumer | Bulk | MUST |
| im1\_bulk\_010 | Consumer must be able to demonstrate their anonymisation and de-anonymisation processes ensuring they are in line with the Information Governance requirements | Consumer | Bulk | MUST |
| im1\_bulk\_011 | Consumer must have a mechanism to perform data quality checks on ingested data and have a process for highlighting corrupt data values or fields | Consumer | Bulk | MUST |
| im1\_bulk\_012 | Consumer Supplier must be able to demonstrate efficient mechanisms for data ingestion of Bulk extracts for both Full Bulk extracts and Delta drops | Consumer | Bulk | MUST |
| im1\_bulk\_013 | Consumer must provide an approach strategy for any transformations they plan to undertake, including a clear rationale explaining the transformations, before or during the Consumer's integration development | Consumer | Bulk | MUST |

## Deprecation of Interfaces

In relation to the planned deprecation of IM1 interfaces the following requirements will apply from the time that the interfaces are deprecated:

| ID | Requirement | Consumer or Provider | IM1 Type | Level |
| --- | --- | --- | --- | --- |
| im1\_dep\_001 | Deprecated interfaces must not be switched off, decommissioned or have service degraded while there are live consumers using the interface - Relevant SLA's still apply | Provider | All | MUST |
| im1\_dep\_002 | Deprecated interfaces may be decommissioned where:   1. The supplier has implemented into live a replacement as per the NHS Digital roadmap for the interface AND 2. There are no longer any live consumers of the deprecated interface | Provider | All | MUST |

## Compliance & Assurance

On boarding suppliers acting as providers or consumers will be required to evidence compliance against the IM1 interface line item requirements, as detailed on this page.

IM1 consuming suppliers will also need to complete the pairing process, before going live within the framework and this carries its own set of compliance and assurance requirements which currently lived outside of this framework.

The pairing process will remain the responsibility of the IM1 operations function. For advice and assistance from NHS Operations Function, please contact [im1.team@nhs.net](mailto:im1.team@nhs.net).

## Important terms and definitions

### Transient Data Definition

- Application log files for operational diagnostic trace, information, warnings and errors
- Completed message, scheduled historical operational/non patient record reports and other document correspondence Application archives
- Application user session data
- Application cache data
- Application help information
- Service configuration settings e.g. Firewall, VPN, SAN setup, Microsoft SQL Server settings, Microsoft IIS machine.config and web.config settings, batch scheduling settings

### Definition of Administration and Clinical Data

**Administrative**: Any data entities or objects which are involved in any aspect of administration of Patient Care and Management

**Clinical**: Any data entities or objects which contain data of clinical nature

Suppliers wishing to exclude data which falls within either of these definitions from the interfaces must agree this with the Authority.

## Dependencies (Patient facing interface Only)

Creating a compliant implementation of IM1 Patient interface requires implementing the following dependent interface standard:

- NHS login service

# Roadmap

| Roadmap Item |
| --- |
| No content found. |