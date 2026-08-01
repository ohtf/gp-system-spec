---
page_id: "1391133660"
space: "DCSDCS"
title: "Non-Functional Questions v1.0.0"
version: 7
updated: "2019-08-01T13:15:38.081Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133660/Non-Functional+Questions+v1.0.0"
labels: ["overarching_standard_retired"]
---

# Non-Functional Questions v1.0.0

|  |  |
| --- | --- |
| ID | S63 |
| Version | 1.0.0 |
| Type | Overarching Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

# Description {#Non-FunctionalQuestionsv1.0.0-Description}

- [Non-Functional Questions Model](#Non-FunctionalQuestionsv1.0.0-Non-FunctionalQuestionsModel)
- [Non-Functional Categories](#Non-FunctionalQuestionsv1.0.0-Non-FunctionalCategories)

Non-functional requirements describe how the Solution works, not what the Solution should do, and serve as constraints or restrictions on the design of the Solution. The following non-functional questions are to enable NHS Digital to understand how the supplier Solution has implemented its non-functional requirements and how these requirements will fulfil the contractual SLAs.

## Non-Functional Questions Model {#Non-FunctionalQuestionsv1.0.0-Non-FunctionalQuestionsModel}

The non-functional questions (NFQs) model illustrated within Figure A attempts to show the relationships between the supplier Solution and the non-functional requirements (NFRs) required to satisfy the required service SLAs.

Suppliers are responsible for ensuring the non-functional elements of their Solutions are capable of meeting the defined service levels for specific capabilities provided as well as any other NFRs specified by NHS Digital across other standards. The NFQs are to allow the supplier to provide evidence to NHS Digital and Purchasers that their Solution will be able to satisfy the required SLAs. Suppliers will be required to demonstrate they understand the non functional landscape of the market they are selling into.

![](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133660/GP%20IT%20Futures%20-%20Standards%20v0.1.drawio-NFR%20Model.png?api=v2)

**Figure A - Non-Functional Questions Model**

## Non-Functional Categories {#Non-FunctionalQuestionsv1.0.0-Non-FunctionalCategories}

- [Usability](#Non-FunctionalQuestionsv1.0.0-Usability)
- [Performance and Scalability](#Non-FunctionalQuestionsv1.0.0-PerformanceandScalability)
- [Volume and Performance](#Non-FunctionalQuestionsv1.0.0-VolumeandPerformance)
- [Non Functional Testing](#Non-FunctionalQuestionsv1.0.0-NonFunctionalTesting)
- [Recoverability](#Non-FunctionalQuestionsv1.0.0-Recoverability)
- [Backup capability](#Non-FunctionalQuestionsv1.0.0-Backupcapability)
- [Availability](#Non-FunctionalQuestionsv1.0.0-Availability)
- [Resilience](#Non-FunctionalQuestionsv1.0.0-Resilience)
- [Information Governance](#Non-FunctionalQuestionsv1.0.0-InformationGovernance)
- [Security](#Non-FunctionalQuestionsv1.0.0-Security)
- [Service Management](#Non-FunctionalQuestionsv1.0.0-ServiceManagement)
- [Capacity Management](#Non-FunctionalQuestionsv1.0.0-CapacityManagement)
- [Legal Regulations, Compliance and Audit](#Non-FunctionalQuestionsv1.0.0-LegalRegulations,ComplianceandAudit)
- [Flexibility and Extensibility](#Non-FunctionalQuestionsv1.0.0-FlexibilityandExtensibility)
- [Interoperability / APIs](#Non-FunctionalQuestionsv1.0.0-Interoperability/APIs)
- [Integrity](#Non-FunctionalQuestionsv1.0.0-Integrity)
- [Mobile Working](#Non-FunctionalQuestionsv1.0.0-MobileWorking)

### Usability {#Non-FunctionalQuestionsv1.0.0-Usability}

| **ID** | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-U-1** | User roles | What are the expected user roles in the Solution? Who are the users? What are their needs? How do you know? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-U-2** | Physical user requirements | What do users require, e.g. headphones, specialist devices, card readers etc? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-U-3** | Supported browser versions | Which browsers are supported and what are the minimum and recommended versions?  How do you approach the deprecation and uplift of browser versions? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-U-4** | Required browser plugins or extensions | Are any specific browser plugins or extensions required? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-U-5** | Language support | Which non-English languages are supported? Which localisation settings are supported? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-U-6** | UI standards | What user interface standards does the Solution meet? Are you following [ISO 9241-210:2010](https://www.iso.org/obp/ui/#iso:std:iso:9241:-210:ed-1:v1:en) - the ‘six principles for human centred design'? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Performance and Scalability {#Non-FunctionalQuestionsv1.0.0-PerformanceandScalability}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-PS-1** | Number of named user accounts | What is the maximum number of individual named user accounts that can be supported? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-2** | Number of user groups | What is the maximum number of different user groups or roles of users that can be supported? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-3** | Number of concurrent sessions | What is the peak number of concurrent user sessions the Solution can support? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-4** | Average session length (login to logout) | What length of time is an average user session expected to last?  Provide Mode, Median & Mean values. | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-5** | Response times | What are the expected response times in a given percentage of cases for a given operation e.g. Login or Open Patient Record?  Provide different types of operation including command & query operations. | Provide values, show how the figures are derived, including any considerations which may impact these values. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-6** | Transactions per second | How many user transactions per second are supported?  Define what a user transaction consists of and how it is measured. | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-7** | Online service transaction volumes | How many online batch transactions per second are supported?  Define what a batch transaction consists of and how it is measured. | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-8** | Timeliness | What is the refresh time on updated data in a user view? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-9** | Query and reporting times | What is the average elapsed time for reports be made available to users after being requested?  Define what the reports consists of and how many records are included. | Provide values, show how the figures are derived, including any considerations which may impact these values. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-10** | Expected growth over time | What is the expected growth in number of users, transaction volumes, storage requirements etc.  per year? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-11** | System Response Times | Describe how measurements are calculated for system response times to meet SLAs. | Provide values, show how the figures are derived, including any considerations which may impact the values. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-12** | End User Interaction Timings | Describe how measurements are calculated for end user interaction timings to meet SLAs. | Provide values, show how the figures are derived, including any considerations which may impact the values. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-13** | Interface Mechanism Response Times | Describe how measurements are calculated for interface mechanism response times to meet SLAs. | Provide values, show how the figures are derived, including any considerations which may impact the values. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Volume and Performance {#Non-FunctionalQuestionsv1.0.0-VolumeandPerformance}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-VP-1** | Model | Describe what volumetric model(s) are provided to enable volume and performance tests encompassing load, ramp, stress and soak phases? | Provide model(s), show how the model(s) are derived, including any considerations which may impact the model(s). | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-VP-2** | V&P Performance | What V&P work has been undertaken to ensure the Solution will meet expected volume & performance SLAs. | Provide statement of  V&P assessment activities and associated test reports. | Demonstrate systematic approach of how the evidence is derived. |
| **GP-NFQ-VP-3** | Spine | What V & P testing of National Spine interactions (e.g. Personal Demographics Service, Summary Care Record, *e*-Referral Service, ..) is planned, to ensure supplier’s Solution has no impact on National Spine services? | Provide test plan. | Validate test coverage. |

### Non Functional Testing {#Non-FunctionalQuestionsv1.0.0-NonFunctionalTesting}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-T-1** | Test Plan | Describe what test plan and schedule of non-functional testing is in place and with what associated documentation? | Provide test plan to include sufficient details of scope and coverage. | Validate scope and non-functional test coverage. |
| **GP-NFQ-T-2** | Data Protection Testing | What Data Protection testing is in place to show legislation is met? | Provide test plan to include sufficient details of scope and coverage. | Validate scope and non-functional test coverage. |
| **GP-NFQ-T-3** | ITHC / Penetration Testing | What ITHC / penetration testing is planned? | Provide testing scope, documented process, and test, and corrective action evidence. | Validate scope, process & testing and any recommendations required corrective actions completed. acted upon. |
| **GP-NFQ-T-4** | Ready for Operations (RFO) Testing | What RFO testing is planned? | Provide details of RFO test coverage, examples:  • application / component failure and recovery  • monitoring and reporting of SLAs • Help Desk tools and processes • Testing to confirm the successful deployment process of the Solution | Validate test coverage. |

### Recoverability {#Non-FunctionalQuestionsv1.0.0-Recoverability}

| ID |  |  | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-R-1** | Disaster recovery point objective (RPO) | What RPO is possible with this Solution and how does that map to the required SLA? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-R-2** | Disaster recovery time objective (RTO) | What RTO is possible with this Solution and how does that map to the required SLA? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Backup capability {#Non-FunctionalQuestionsv1.0.0-Backupcapability}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-B-1** | Capability | Describe in detail what backup and recovery mechanisms are implemented. | Confirm formal processes and mechanisms are in place.  Provide design and documentation of implementation and operational processes. | Demonstrate systematic approach and rationale of design, implementation and processes. |
| **GP-NFQ-B-2** | Validation & Testing | Describe what testing has been undertaken to demonstrate the mechanism and processes support your operational requirements. | Confirm formal processes and mechanisms are in place.  Provide design and documentation of implementation and operational processes. | Demonstrate systematic approach and rationale of design, implementation and processes. |
| **GP-NFQ-B-3** | Periodic Testing | Describe what periodic testing of backup and recovery is undertaken? | Confirm formal processes and mechanisms are in place.  Provide design and documentation of implementation and operational processes. | Demonstrate systematic approach and rationale of design, implementation and processes. |

### Availability {#Non-FunctionalQuestionsv1.0.0-Availability}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-A-1** | Availability | What is your service availability during agreed service hours.  90% ("one nine") 36.5 days 72 hours 16.8 hours 99% ("two nines") 3.65 days 7.20 hours 1.68 hours 99.9% ("three nines") 8.76 hours 43.8 minutes 10.1 minutes 99.99% ("four nines") 52.56 minutes 4.32 minutes 1.01 minutes 99.999% ("five nines") 5.26 minutes 25.9 seconds 6.05 seconds | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-2** | Service hours | What are the standard business operating hours the Solution needs to be available for users? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-3** | Scheduled maintenance windows | What are the requirements for any scheduled periods of unavailability to perform Solution maintenance? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-4** | External system impacts | Does the availability of any external systems affect this Solution? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-5** | Fault tolerance | Describe any Single Points of Failure (SPOF) within the Solution or external that the Solution relies upon for operation. | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-6** | Degradability | Describe the ability of the solution to operate with reduced capacity or functionality in the event of an unexpected event, e.g. site failure | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-7** | Disaster recovery minimum recovery operating level (MROL) | In the event of a disaster what are the minimum business services that need to be recovered to continue operating? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Resilience {#Non-FunctionalQuestionsv1.0.0-Resilience}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-R-1** | Service Level Agreements (SLAs) | Describe how the hardware and software design supports the SLAs? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-R-2** | Hardware Design | Describe what level of resilience is provided in the hardware design? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-R-3** | Software Design | Describe what level of resilience is provided in the software design? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-R-4** | Business Impact of Service Incidents | Describe what mapping of business impacts of service incidents against levels of resilience has been undertaken? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-R-5** | Component Failure Impact Analysis | Describe what CIFA documentation has been produced? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Information Governance {#Non-FunctionalQuestionsv1.0.0-InformationGovernance}

| ID | Sub-category | Description | Evidence  Example | Assessment  Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-IG-1** | Data retention | What NHS Digital data retention policies are enforced by the Solution? See **GP-IG-14.2-4**in the Information Governance standard. | Provide documented evidence and rationale, including any impact considerations.  or  Provide list of policies | Demonstrate systematic approach and rationale of how evidence is derived.  or  How well do the policies map to requirements and legislation |
| **GP-NFQ-IG-2** | Data archiving | What data archiving policies must be enforced by the Solution? | Provide documented evidence and rationale, including any impact considerations.  or  Provide list of policies | Demonstrate systematic approach and rationale of how evidence is derived.  or  How well do the policies map to requirements and legislation |

### Security {#Non-FunctionalQuestionsv1.0.0-Security}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-S-1** | Data classification | What is the classification of data being processed by the Solution?  *Note: Refer to document for defining data classification used in Cloud & <https://www.gov.uk/government/publications/government-security-classifications>* | Completion of the risk assessment | Confirm classification of data is as expected |
| **GP-NFQ-S-2** | Encryption | Describe what encryption is implemented to protect data at rest and in transit and which standards are implemented? | Provide statement of encryption level | Confirm encryption is at minimum level |
| **GP-NFQ-S-3** | Authentication | Describe what authentication mechanisms are supported? | Provide list of authentication mechanisms supported | Confirm authentication is appropriate for given Solution/ data |
| **GP-NFQ-S-4** | Authentication retry limits and account locking | Describe how protection against unauthorised authentication is implemented? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-S-5** | Authorisation | Describe what authorisation for user and Solution actions is implemented? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-S-6** | Password Policy | What password policies are enforced by the Solution? | Provide documented evidence and rationale, including any impact considerations.  or  Provide list of policies | Demonstrate systematic approach and rationale of how evidence is derived.  or  How well do the policies map to requirements and legislation |
| **GP-NFQ-S-7** | Data redaction and obfuscation | Describe what mechanisms are in place for redaction and obfuscation of sensitive data? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-S-8** | Protection from exploits | Describe what protection from malicious use of the Solution is implemented, e.g. cross-site scripting, SQL injection prevention etc. | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Service Management {#Non-FunctionalQuestionsv1.0.0-ServiceManagement}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-SM-1** | Processes | Describe which ITIL aligned service management functions are operated. | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-SM-2** | Tooling | What Service management toolset is implemented. | Provide a list of tools and rationale for choosing. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-SM-3** | Monitoring | Describe what are the key resources, services and performance indicators that can be monitored? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-SM-4** | Alerting | Who is alerted if a resource or service is not meeting the agreed service levels? | Provide list of notified stakeholders and alerting thresholds. | List of appropriate stakeholders are notified. |
| **GP-NFQ-SM-5** | Service desk support hours | What are the standard hours for service desk support? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-SM-6** | Out of hours support | What support is available outside of service desk hours, e.g. forums, problem ticketing | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-SM-7** | Event logging | What events are logged? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-SM-8** | Documentation | Please provide all relevant Solution documentation. | Provide documentation of service processes and operations. | Documentation covers all appropriate levels of services. |

### Capacity Management {#Non-FunctionalQuestionsv1.0.0-CapacityManagement}

| ID | Sub-category | Description | Evidence  Example | Assessment  Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-CM-1** | Roadmap software | What is the Supplier roadmap for software releases and service deployment e.g. numbers per year? | Timeline of expected software changes and uplifts. | Roadmap demonstrates controlled and manageable plan of software changes over time. |
| **GP-NFQ-CM-2** | Roadmap Hardware | What is the Supplier roadmap for technology refresh/uplift points based on deployment numbers? | Timeline of expected hardware changes and uplifts. | Roadmap demonstrates controlled and manageable plan of hardware changes over time. |
| **GP-NFQ-CM-3** | Capacity Management toolset | What Capacity management toolset is implemented and what is the scope of information capture available | List of software and hardware tools used to measure and assess Solution capacity. | Tooling is comprehensive and effective and measuring and assessing Solution capacity. |
| **GP-NFQ-CM-4** | Capacity Management | Describe how the capacity of the Solution is managed and the what associated reports that are produced, include management and Solution process models . | Provide documented evidence and rationale, including any impact considerations.  Include report examples of specific metrics used with forecasts. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Legal Regulations, Compliance and Audit {#Non-FunctionalQuestionsv1.0.0-LegalRegulations,ComplianceandAudit}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-LCA-1** | Accessibility | Does your service/product comply with the Equality Act (<https://www.gov.uk/guidance/equality-act-2010-guidance>) and meet at least level AA of the Web Content Accessibility Guidelines (WCAG 2.0). For more guidance see the [NHS Digital Service Manual](https://beta.nhs.uk/service-manual/practices/make-your-service-accessible/). | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-LCA-2** | Legal regulations and guidelines | What legal regulations does your Solution comply with? | Provide a list of regulations the Solution complies with. | Required legal regulations are complied with. |
| **GP-NFQ-LCA-3** | Conformance to standards | What standards does your Solution comply with? | Provide a list of standards the Solution complies with. | Required standards are complied with. |
| **GP-NFQ-LCA-4** | Test and certifications | What evidence of compliance can be produced? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-LCA-5** | Support for external audit | What  independent audit of the implemented Solution has been undertaken? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-LCA-6** | Audited objects | What entities in the Solution are audited? | Provide a list of entities that are audited by the Solution. | Appropriate entities are audited. |
| **GP-NFQ-LCA-7** | Traceability | Which changes in the Solution are traceable, e.g. be able to tell what changed, who changed it and when? | Provide a list of changes that are traceable by the Solution. | Appropriate changes are traceable. |

### Flexibility and Extensibility {#Non-FunctionalQuestionsv1.0.0-FlexibilityandExtensibility}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-FE-1** | Adaptability | What changes is the Solution expected to be able to handle, e.g. without requiring re-development | Provide a list of changes that are handled by the Solution. | Appropriate changes are handled. |
| **GP-NFQ-FE-2** | Short notice changes | Are there elements which the business will need to change at short notice? | Provide a list of changes that will need to be handled at short notice by the Solution. | Appropriate elements are handled. |
| **GP-NFQ-FE-3** | Personalisation | Are there features which users can personalise, e.g. preferred visual theme? | Provide a list of features that can be personalised. | Appropriate features are able to be personalised. |
| **GP-NFQ-FE-4** | Customisation | Are there features which can be configured/customised without re-development? | Provide a list of features which can be configured without re-development. | Appropriate features are able to be configured. |

### Interoperability / APIs {#Non-FunctionalQuestionsv1.0.0-Interoperability/APIs}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-IA-1** | Security | Describe how security is applied to the Solutions APIs. | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-IA-2** | Standards | What standards do the Solutions APIs adhere to? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-IA-3** | Performance / Response Times | What is the expected response time of each API in a given percentage of cases for a given operation e.g. Login or Open Patient Record? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-IA-4** | MESH | What poll times are used for communicating with the MESH system? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Integrity {#Non-FunctionalQuestionsv1.0.0-Integrity}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-I-1** | Message Accuracy and Transfer | Describe how message accuracy and transfer is achieved and maintained. (e.g. how is the data guaranteed not to be corrupt) | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Mobile Working {#Non-FunctionalQuestionsv1.0.0-MobileWorking}

| ID | Sub-Category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-MW-1** | General | Describe how the Solution enables users the ability to work anywhere and at any time to access and update information from a supported mobile device and supporting improved productivity  e.g. a GP being able to work from home or using mobile devices to access real time information. | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-MW-2** | Availability | Describe how the Solution enables users to work "offline" when access to central services is not available.  e.g. when there is no network connection to central services from the remote device. | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-MW-3** | Data loss | Describe how the Solution prevents data loss when disconnection from central services occurs. | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-MW-4** | Data integrity | Describe how the Solution maintains data integrity when multiple devices have been "offline" and attempt to update the central services with conflicting information. | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |

# Capabilities {#Non-FunctionalQuestionsv1.0.0-Capabilities}

**Applicable Capabilities**

All suppliers Solutions delivering any Capabilities will need to meet this Standard.

# Roadmap {#Non-FunctionalQuestionsv1.0.0-Roadmap}

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [GP IT Futures - Standards v0.1.drawio-NFR Model.png](../../../../.raw/DCSDCS/attachments/1391133660/att1391158299-GP IT Futures - Standards v0.1.drawio-NFR Model.png)
