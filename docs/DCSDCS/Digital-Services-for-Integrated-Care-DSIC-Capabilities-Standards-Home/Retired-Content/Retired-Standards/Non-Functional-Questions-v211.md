---
page_id: "5180260945"
space: "DCSDCS"
title: "Non-Functional Questions v2.1.1"
version: 6
updated: "2023-04-11T11:40:58.493Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/5180260945/Non-Functional+Questions+v2.1.1"
labels: ["overarching_standard"]
---

# Non-Functional Questions v2.1.1

|  |  |
| --- | --- |
| ID | S63 |
| Version | 2.1.1 |
| Type | Overarching Standard |
| Status | Retired |
| Publication Date | 06 Jul 2022 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") - [DFOCVC](https://gpitbjss.atlassian.net/wiki/spaces/DFOCVCL) - [Vaccinations - Local/PCN Delivery](https://gpitbjss.atlassian.net/wiki/spaces/CVPDR) |

- [Non-Functional Questions Model](#Non-FunctionalQuestionsv2.1.1-Non-FunctionalQuestionsModel)
- [Non-Functional Categories](#Non-FunctionalQuestionsv2.1.1-Non-FunctionalCategories)

# Description {#Non-FunctionalQuestionsv2.1.1-Description}

Non-functional requirements describe how the Solution works, not what the Solution should do, and serve as constraints or restrictions on the design of the Solution. The following non-functional questions are to enable NHS Digital to assess the risk associated with the Compliance Assessment of the Solution against the overarching Service Management, Information Governance, Security, Testing, and Business Continuity and Disaster Recovery Standards. Supplier’s answers will also demonstrate they understand the non functional landscape of the market they are selling into.

## Non-Functional Questions Model {#Non-FunctionalQuestionsv2.1.1-Non-FunctionalQuestionsModel}

The non-functional questions (NFQs) model illustrated within Figure A attempts to show the relationships between the Supplier Solution and the non-functional requirements (NFRs) required to meet the Overarching Standards, provide appropriate levels of service and, where relevant, satisfy the required service SLAs.

Suppliers are responsible for ensuring the non-functional elements of their Solutions are capable of meeting any defined service levels for specific Capabilities provided, as well as any other NFRs specified by NHS Digital across other Standards.

Suppliers must provide an appropriate answer to the non-functional questions - the level of information and evidence required in the answer will depend on the Capabilities and scale of deployment of the Supplier’s Solution and this will be determined and specified in the guidance provided as part of the Capability Mapping and Standards Compliance On-Boarding process.

![](https://nhse-dsic.atlassian.net/wiki/download/attachments/5180260945/GP%20IT%20Futures%20-%20Standards%20v0.1.drawio-NFR%20Model.png?api=v2)

**Figure A - Non-Functional Questions Model**

## Non-Functional Categories {#Non-FunctionalQuestionsv2.1.1-Non-FunctionalCategories}

- [Usability](#Non-FunctionalQuestionsv2.1.1-Usability)
- [Performance and Scalability](#Non-FunctionalQuestionsv2.1.1-PerformanceandScalability)
- [Volume and Performance](#Non-FunctionalQuestionsv2.1.1-VolumeandPerformance)
- [Non Functional Testing](#Non-FunctionalQuestionsv2.1.1-NonFunctionalTesting)
- [Recoverability](#Non-FunctionalQuestionsv2.1.1-Recoverability)
- [Backup capability](#Non-FunctionalQuestionsv2.1.1-Backupcapability)
- [Availability](#Non-FunctionalQuestionsv2.1.1-Availability)
- [Resilience](#Non-FunctionalQuestionsv2.1.1-Resilience)
- [Information Governance](#Non-FunctionalQuestionsv2.1.1-InformationGovernance)
- [Security](#Non-FunctionalQuestionsv2.1.1-Security)
- [Service Management](#Non-FunctionalQuestionsv2.1.1-ServiceManagement)
- [Capacity Management](#Non-FunctionalQuestionsv2.1.1-CapacityManagement)
- [Legal Regulations, Compliance and Audit](#Non-FunctionalQuestionsv2.1.1-LegalRegulations,ComplianceandAudit)
- [Integrity](#Non-FunctionalQuestionsv2.1.1-Integrity)
- [Mobile Working](#Non-FunctionalQuestionsv2.1.1-MobileWorking)

### Usability {#Non-FunctionalQuestionsv2.1.1-Usability}

| **ID** | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-U-3** | Supported browser versions | Which browsers are supported and what are the minimum and recommended versions?  How do you approach the deprecation and uplift of browser versions? | Provide declaration and any supporting documented evidence and rationale. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-U-6** | UI standards | What user interface standards does the Solution meet? Are you following ISO 9241-210:2010 - the ‘six principles for human centred design'? | Provide declaration and any supporting documented evidence and rationale. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-U-7** | Supported devices | What devices are supported by the Solution that can be used and accessed by end users? | Provide type of devices supported, compatible with the Solution and any supporting documented evidence and rationale. | Demonstrate that the Solution is securely accessed and used by end users on supported devices through authentication and authorisation mechanisms in line with NHS Digital policies. |
| **GP-NFQ-U-8** | Accessibility | Describe how the Solution is accessed by / available to the end user? | Provide any supporting documents, and mechanism to access the Solution, for example, how to access the Solution in the event of interruption and how availability of the event is managed by the Solution | Demonstrate that the Solution is securely accessed by the end user via the provided mechanism.  Demonstrate the Solution is accessed and available to the end user via provided the mechanism if interrupted.  Demonstrate that event will be available for appropriate length of time. |

### Performance and Scalability {#Non-FunctionalQuestionsv2.1.1-PerformanceandScalability}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-PS-3** | Number of concurrent sessions | What is the peak number of concurrent user sessions the Solution can support? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-5** | Response times | What are the expected response times in a given percentage of cases for a given operation e.g. Login or Open Patient Record?  Provide different types of operation including command and query operations. | Provide values, show how the figures are derived, including any considerations which may impact these values. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-6** | Transactions per second | How many user transactions per second are supported?  Define what a user transaction consists of and how it is measured. | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-7** | Online service transaction volumes | How many online batch transactions per second are supported?  Define what a batch transaction consists of and how it is measured. | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-11** | System Response Times | Describe how measurements are calculated for system response times to meet SLAs. | Provide values, show how the figures are derived, including any considerations which may impact the values. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-12** | End User Interaction Timings | Describe how measurements are calculated for end user interaction timings to meet SLAs. | Provide values, show how the figures are derived, including any considerations which may impact the values. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-13** | Interface Mechanism Response Times | Describe how measurements are calculated for interface mechanism response times to meet SLAs. | Provide values, show how the figures are derived, including any considerations which may impact the values. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-PS-14** | Video and audio and picture / image quality | What are expected minimum requirements for good quality of video and audio and pictures / images sent via the system? | Provide minimum specification to get better quality of video and audio and pictures / images. | Demonstrate the following minimum requirements for better video / image, audio quality:  Minimum resolution of up to 720p or higher is required for HD ready.  End-to-end latency must be lower than 150 ms to avoid poor performance of image  Audio encoded at a minimum of 16 Kbit/s |

### Volume and Performance {#Non-FunctionalQuestionsv2.1.1-VolumeandPerformance}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-VP-1** | Model | Describe what volumetric model(s) are provided to enable volume and performance tests encompassing load, ramp, stress and soak phases? | Provide model(s), show how the model(s) are derived, including any considerations which may impact the model(s). | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-VP-2** | V&P Performance | What V&P work has been undertaken to ensure the Solution will meet expected volume & performance SLAs. | Provide statement of  V&P assessment activities and associated test reports. | Demonstrate systematic approach of how the evidence is derived. |
| **GP-NFQ-VP-3** | Spine | What V & P testing of National Spine interactions (e.g. Personal Demographics Service, Summary Care Record, *e*-Referral Service) is planned, to ensure Supplier’s Solution has no impact on National Spine services? | Provide statement of testing and test coverage | Validate test coverage. |

### Non Functional Testing {#Non-FunctionalQuestionsv2.1.1-NonFunctionalTesting}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-T-1** | Test Plan | Describe what test plan and schedule of non-functional testing is in place and with what associated documentation? | Provide test plan to include sufficient details of scope and coverage. | Validate scope and non-functional test coverage. |
| **GP-NFQ-T-2** | Data Protection Testing | What Data Protection testing is in place to show legislation is met? | Provide statement of test activity, the scope, coverage and attributable legislation | Validate scope and non-functional test coverage. |
| **GP-NFQ-T-3** | ITHC / Penetration Testing | What ITHC / penetration testing is planned?  Does the penetration test provider have one of these qualifications: Check, CREST or TIGER? | Provide statement of test activity, the scope, testing results and coverage | Validate scope, process and testing, testing results and any recommendations requiring corrective actions completed and acted upon. |
| **GP-NFQ-T-4** | Ready for Operations (RFO) Testing | What RFO testing is planned? | Provide details of RFO test coverage, examples:  • Application / component failure and recovery  • Monitoring and reporting of SLAs • Help Desk tools and processes • Testing to confirm the successful deployment process of the Solution | Validate test coverage. |

### Recoverability {#Non-FunctionalQuestionsv2.1.1-Recoverability}

| ID |  |  | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-R-1** | Disaster recovery point objective (RPO) | What RPO is possible with this Solution and how does that map to the required SLA? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-R-2** | Disaster recovery time objective (RTO) | What RTO is possible with this Solution and how does that map to the required SLA? | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Backup capability {#Non-FunctionalQuestionsv2.1.1-Backupcapability}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-B-1** | Capability | Describe in detail what backup and recovery mechanisms are implemented. | Confirm formal processes and mechanisms are in place.  Provide design and documentation of implementation and operational processes. | Demonstrate systematic approach and rationale of design, implementation and processes. |
| **GP-NFQ-B-2** | Validation and Testing | Describe what testing has been undertaken to demonstrate the mechanism and processes support your operational requirements. | Provide appropriate statement of test activity, coverage and outcomes | Demonstrate systematic approach and rationale of design, implementation and processes. |
| **GP-NFQ-B-3** | Periodic Testing | Describe what periodic testing of backup and recovery is undertaken? | Provide appropriate statement of test activity, coverage and outcomes. | Demonstrate systematic approach and rationale of design, implementation and processes. |

### Availability {#Non-FunctionalQuestionsv2.1.1-Availability}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-A-1** | Availability | What is your service availability during agreed service hours.  90% ("one nine") 36.5 days 72 hours 16.8 hours 99% ("two nines") 3.65 days 7.20 hours 1.68 hours 99.9% ("three nines") 8.76 hours 43.8 minutes 10.1 minutes 99.99% ("four nines") 52.56 minutes 4.32 minutes 1.01 minutes 99.999% ("five nines") 5.26 minutes 25.9 seconds 6.05 seconds | Provide a value, show how the figure is derived, including any considerations which may impact this value. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-2** | Service hours | What are the standard business operating hours the Solution needs to be available for users? | Provide details of service hours, where a solution may deliver a number of capabilities, a declaration of appropriate service hours is required. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-3** | Scheduled maintenance windows | What are the requirements for any scheduled periods of unavailability to perform Solution maintenance? | Provide statement, the underlying rationale and any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-4** | External system impacts | Does the availability of any external systems affect this Solution? | Provide statement, the underlying rationale and any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-5** | Fault tolerance | Describe any Single Points of Failure (SPOF) within the Solution or external that the Solution relies upon for operation. | Provide statement of any SPOF inherent within the Solution and where applicable, any associated mitigation.. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-6** | Degradability | Describe the ability of the solution to operate with reduced capacity or functionality in the event of an unexpected event, e.g. site failure | Provide details of any reduced operations capability, the levels of functionality and details of supporting documentation | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-A-7** | Disaster recovery minimum recovery operating level (MROL) | In the event of a disaster what are the minimum business services that need to be recovered to continue operating? | Provide details of any reduced operations capability, the levels of functionality and details of supporting documentation | Demonstrate systematic approach and rationale of how evidence is derived. |

### Resilience {#Non-FunctionalQuestionsv2.1.1-Resilience}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-RS-1** | Service Level Agreements (SLAs) | Describe how the hardware and software design supports the SLAs? | Provide details of how solution design supports the delivery of any SLA declaration, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-RS-2** | Hardware Design | Describe what level of resilience is provided in the hardware design? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-RS-3** | Software Design | Describe what level of resilience is provided in the software design? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-RS-4** | Business Impact of Service Incidents | Describe what mapping of business impacts of service incidents against levels of resilience has been undertaken? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-RS-5** | Component Failure Impact Analysis | Describe what CIFA documentation has been produced? | Confirm CFIA analysis has been completed, provide documented evidence of analysis. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-RS-6** | Network quality / performance | Describe what hardware / software requirements are supported for good quality of video, minimum resources required for good quality of video? | Provide minimum specification to get better quality of video, details of resources like data usage, costs associated to claim economic benefits of your Solution. | Demonstrate the following minimum requirements for better network quality: minimum call speed/bandwidth 500 Kbps  Upload and download speed: minimum 5 Mbps download and 2 Mbps upload speed  Confirm that data usage and cost associated is at minimum level. |

### Information Governance {#Non-FunctionalQuestionsv2.1.1-InformationGovernance}

| ID | Sub-category | Description | Evidence  Example | Assessment  Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-IG-1** | Data retention | What NHS Digital data retention policies are enforced by the Solution? See **GP-IG-14.2-4**in the Information Governance Standard. | Provide documented evidence and rationale, including any impact considerations.  or  Provide list of policies | Demonstrate systematic approach and rationale of how evidence is derived.  or  How well do the policies map to requirements and legislation |
| **GP-NFQ-IG-2** | Data archiving | What data archiving policies must be enforced by the Solution? | Provide documented evidence and rationale, including any impact considerations.  or  Provide list of policies | Demonstrate systematic approach and rationale of how evidence is derived.  or  How well do the policies map to requirements and legislation |

### Security {#Non-FunctionalQuestionsv2.1.1-Security}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-S-1** | Data classification | What is the classification of data being processed by the Solution?  *Note: Refer to document for defining data classification used in Cloud and https://www.gov.uk/government/publications/government-security-classifications* | Completion of the risk assessment | Confirm classification of data is as expected |
| **GP-NFQ-S-2** | Encryption | Describe what encryption is implemented to protect data at rest and in transit and which standards are implemented? | Provide statement of encryption level | Confirm encryption is at minimum level |
| **GP-NFQ-S-3** | Authentication | Describe what authentication mechanisms are supported? | Provide list of authentication mechanisms supported | Confirm authentication is appropriate for given Solution/ data |
| **GP-NFQ-S-4** | Authentication retry limits and account locking | Describe how protection against unauthorised authentication is implemented? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-S-5** | Authorisation | Describe what authorisation for user and Solution actions is implemented? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-S-6** | Password Policy | What password policies are enforced by the Solution? | Provide documented evidence and rationale, including any impact considerations.  or  Provide list of policies | Demonstrate systematic approach and rationale of how evidence is derived.  or  How well do the policies map to requirements and legislation |
| **GP-NFQ-S-7** | Data redaction and obfuscation | Describe what mechanisms are in place for redaction and obfuscation of sensitive data? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-S-8** | Protection from exploits | Describe what protection from malicious use of the Solution is implemented, e.g. cross-site scripting, SQL injection prevention etc. | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Service Management {#Non-FunctionalQuestionsv2.1.1-ServiceManagement}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-SM-1** | Processes | Describe which ITIL aligned service management functions are operated. | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-SM-2** | Tooling | What Service management toolset is implemented. | Provide a list of tools and rationale for choosing. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-SM-3** | Monitoring | Describe what are the key resources, services and performance indicators that can be monitored? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-SM-4** | Alerting | Who is alerted if a resource or service is not meeting the agreed service levels? | Provide list of notified stakeholders and alerting thresholds. | List of appropriate stakeholders are notified. |
| **GP-NFQ-SM-5** | Service desk support hours | What are the standard hours for service desk support? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-SM-6** | Out of hours support | What support is available outside of service desk hours, e.g. forums, problem ticketing | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-SM-7** | Event logging | What events are logged? | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Capacity Management {#Non-FunctionalQuestionsv2.1.1-CapacityManagement}

| ID | Sub-category | Description | Evidence  Example | Assessment  Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-CM-3** | Capacity Management toolset | What Capacity management toolset is implemented and what is the scope of information capture available | List of software and hardware tools used to measure and assess Solution capacity. | Tooling is comprehensive and effective and measuring and assessing Solution capacity. |
| **GP-NFQ-CM-4** | Capacity Management | Describe how the capacity of the Solution is managed and the what associated reports that are produced, include management and Solution process models . | Provide documented evidence and rationale, including any impact considerations.  Include report examples of specific metrics used with forecasts. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-CM-5** | Storage Capacity | Describe how solution is scalable and meets storage capacity needs? | Provide list of storage options, tools provided data transactions, scalability, and effective cost. | Demonstrate that proposed Solution has made provisions for "enough" storage and network capacity for the data transactions (as specified by the business) flow between hardware components of the proposed solution, especially at peak usage times. |

### Legal Regulations, Compliance and Audit {#Non-FunctionalQuestionsv2.1.1-LegalRegulations,ComplianceandAudit}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-LCA-1** | Accessibility | Does your service/product comply with the Equality Act (https://www.gov.uk/guidance/equality-act-2010-guidance) and meet at least level AA of the Web Content Accessibility Guidelines (WCAG 2.0)? For more guidance see the NHS Digital Service Manual. | Provide statement along with details of, and availability of, supporting documentation that can be provided to confirm statements. | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-LCA-5** | Support for external audit | What independent audit of the implemented Solution has been undertaken? | Provide Statement along with details of, and availability of, supporting documentation | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-LCA-6** | Audited objects | What entities in the Solution are audited? | Provide a list of entities that are audited by the Solution. | Appropriate entities are audited. |
| **GP-NFQ-LCA-7** | Traceability | Which changes in the Solution are traceable, e.g. be able to tell what changed, who changed it and when? | Provide a list of changes that are traceable by the Solution. | Appropriate changes are traceable. |

### Integrity {#Non-FunctionalQuestionsv2.1.1-Integrity}

| ID | Sub-category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-I-1** | Message Accuracy and Transfer | Describe how message accuracy and transfer is achieved and maintained. (e.g. how is the data guaranteed not to be corrupt) | Provide documented evidence and rationale, including any impact considerations. | Demonstrate systematic approach and rationale of how evidence is derived. |

### Mobile Working {#Non-FunctionalQuestionsv2.1.1-MobileWorking}

| ID | Sub-Category | Description | Evidence  Example | Assessment Criteria |
| --- | --- | --- | --- | --- |
| **GP-NFQ-MW-1** | General | Describe how the Solution enables users the ability to work anywhere and at any time to access and update information from a supported mobile device and supporting improved productivity  e.g. a GP being able to work from home or using mobile devices to access real time information. | Provide detailed statement along with details of, and availability of, any supporting documentation | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-MW-2** | Availability | Describe how the Solution enables users to work "offline" when access to central services is not available.  e.g. when there is no network connection to central services from the remote device. | Provide detailed statement along with details of, and availability of, any supporting documentation | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-MW-3** | Data loss | Describe how the Solution prevents data loss when disconnection from central services occurs. | Provide detailed statement along with details of, and availability of, any supporting documentation | Demonstrate systematic approach and rationale of how evidence is derived. |
| **GP-NFQ-MW-4** | Data integrity | Describe how the Solution maintains data integrity when multiple devices have been "offline" and attempt to update the central services with conflicting information. | Provide detailed statement along with details of, and availability of, any supporting documentation | Demonstrate systematic approach and rationale of how evidence is derived. |

# Capabilities {#Non-FunctionalQuestionsv2.1.1-Capabilities}

**Applicable Capabilities**

All Suppliers Solutions delivering any Capabilities will need to meet this Standard.

# Roadmap {#Non-FunctionalQuestionsv2.1.1-Roadmap}

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Changes to Non-Functional Questions Standard](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/12770967578/Changes+to+Non-Functional+Questions+Standard) | [Non-Functional Questions](../../DSIC-Standards/Overarching-Standards/Non-Functional-Questions.md) | Draft | TBC | Changes applied to Non-Functional Questions (NFQs) to uplift the content and Applicable Contracting Vehicle(s) | Uplift | Managed Capacity - Other |

## Attachments

- [GP IT Futures - Standards v0.1.drawio-NFR Model.png](../../../../.raw/DCSDCS/attachments/5180260945/att5180260948-GP IT Futures - Standards v0.1.drawio-NFR Model.png)
