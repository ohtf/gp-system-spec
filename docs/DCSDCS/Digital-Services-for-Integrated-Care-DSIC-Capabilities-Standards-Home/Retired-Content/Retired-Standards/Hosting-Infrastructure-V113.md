---
page_id: "14160658433"
space: "DCSDCS"
title: "Hosting & Infrastructure V1.1.3"
version: 1
updated: "2025-05-27T09:36:12.584Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14160658433/Hosting+Infrastructure+V1.1.3"
labels: ["overarching_standard_retired"]
---

# Hosting & Infrastructure V1.1.3

|  |  |
| --- | --- |
| ID {#Hosting&InfrastructureV1.1.3-ID} | S29 |
| Version {#Hosting&InfrastructureV1.1.3-Version} | 1.1.3 |
| Type {#Hosting&InfrastructureV1.1.3-Type} | Overarching Standard |
| Status {#Hosting&InfrastructureV1.1.3-Status} | Retired |
| Effective Date {#Hosting&InfrastructureV1.1.3-EffectiveDate} | 16 Dec 2024 |
| Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ContractingVehicle(s)} | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [DFOCVC](https://nhse-dsic.atlassian.net/wiki/spaces/DFOCVCL) - [Vaccinations - Local/PCN Delivery](https://nhse-dsic.atlassian.net/wiki/spaces/CVPDR) |

- [Introduction](#Hosting&InfrastructureV1.1.3-Introduction)
  - [NHS Cloud Hosting Standards & Guidance](#Hosting&InfrastructureV1.1.3-NHSCloudHostingStandards&Guidance)
  - [The Authority's Associated Cloud Guidance Links:](#Hosting&InfrastructureV1.1.3-TheAuthority'sAssociatedCloudGuidanceLinks:)
  - [Co-location and Provider Data Centre Hosting & Infrastructure Requirements](#Hosting&InfrastructureV1.1.3-Co-locationandProviderDataCentreHosting&InfrastructureRequirements)
  - [Scope](#Hosting&InfrastructureV1.1.3-Scope)
- [Requirements - External Standards](#Hosting&InfrastructureV1.1.3-Requirements-ExternalStandards)
  - [Physical Aspects](#Hosting&InfrastructureV1.1.3-PhysicalAspects)
  - [Power](#Hosting&InfrastructureV1.1.3-Power)
  - [IT Infrastructure](#Hosting&InfrastructureV1.1.3-ITInfrastructure)
  - [Servers](#Hosting&InfrastructureV1.1.3-Servers)
  - [Network](#Hosting&InfrastructureV1.1.3-Network)
  - [Management of Services and Infrastructure](#Hosting&InfrastructureV1.1.3-ManagementofServicesandInfrastructure)
  - [Asset Management](#Hosting&InfrastructureV1.1.3-AssetManagement)
  - [Service Monitoring](#Hosting&InfrastructureV1.1.3-ServiceMonitoring)
  - [Device Management](#Hosting&InfrastructureV1.1.3-DeviceManagement)
  - [Data Storage](#Hosting&InfrastructureV1.1.3-DataStorage)
  - [Security](#Hosting&InfrastructureV1.1.3-Security)
  - [Reporting & Documentation](#Hosting&InfrastructureV1.1.3-Reporting&Documentation)
    - [Additional Information](#Hosting&InfrastructureV1.1.3-AdditionalInformation)
- [Applicable Capabilities](#Hosting&InfrastructureV1.1.3-ApplicableCapabilities)
- [Roadmap](#Hosting&InfrastructureV1.1.3-Roadmap)

# Introduction {#Hosting&InfrastructureV1.1.3-Introduction}

Supports best practices for infrastructure and hosting of systems. For example, ensuring that systems are cost effective, secure, reliable, resilient, safe, manageable and energy efficient.

It is essential that Solutions delivered under the Catalogue and Contracting Vehicles follow standards and guidance.

The previous GPSoC infrastructure requirements pulled together best practice from recognised standards and industry guidance, however, feedback from Suppliers and other stakeholders identified that these requirements were complex and challenging to evidence as part of the assurance process.

In addition it is a Supplier's responsibility to ensure they fully understand industry standards & best practice and cannot rely on The Authority explicitly defining requirements at a point in time. The previous requirements documents were developed at a point in time and technology and security vulnerabilities change rapidly.

Whilst UK Government has promoted a Cloud First policy, it is only recently (2018) that the hosting within public cloud has become a reality for health based services. The Technology Strategy has a fundamental principle of delivery of services via cloud provision and specifically the architecting of Solutions to be cloud native. The Authority recognises that cloud hosting may not be appropriate for some services e.g. based on the sensitive and scale of data or the manner in which the service is architected.

Fundamentally there are three core options for hosting services:-

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s)} | Hosting Option {#Hosting&InfrastructureV1.1.3-HostingOption} | Description {#Hosting&InfrastructureV1.1.3-Description} | Preference Status {#Hosting&InfrastructureV1.1.3-PreferenceStatus} | Level {#Hosting&InfrastructureV1.1.3-Level} | Section {#Hosting&InfrastructureV1.1.3-Section} |
| All | Cloud – Public or Private | The Public / Private cloud provider offers self-managed virtualised, elastic/on demand scalable infrastructure as a service where the cloud provider owns the underlying datacentres and physical infrastructure. The Supplier rents the use of the virtualised infrastructure. | Strongly Preferred | Suppliers SHOULDhost Solutions via one of these options. | NHS Cloud Hosting Standards & Guidance |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | Colocation | The physical infrastructure is owned by the Supplier and hosting of the physical infrastructure is provided within the Colo providers datacentres, The management of the infrastructure can be done by the Colo provider, a 3rd party or the Supplier themselves. | Preferred | Co location & Provider Datacentre Standards |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | Provider own facilities | The datacentres and physical infrastructure are owned by the Supplier. The management of the infrastructure can be done by a 3rd party or the Supplier themselves. | Not recommended |

The Authority does not recommend the Suppliers should attempt to host services themselves due to the cost and complexity of providing data centre capabilities that meet the necessary requirements.

Previously the GPSoC framework provided a set of requirements for local hosting of services. Given the security and service risks of this form of infrastructure the Catalogue and Contracting Vehicles will not formally assure local hosting of services. Buyers purchasing services which are locally hosted will be required to satisfy themselves that the security and service risks are mitigated and managed appropriately.

The standards to support infrastructure and hosting are split into two sections, depending on the mechanism being deployed:-

- Cloud – Based on published NHS wide risk assessments and guidance
- Co-Location / provider facilities – specific requirements & assurance processes

## NHS Cloud Hosting Standards & Guidance {#Hosting&InfrastructureV1.1.3-NHSCloudHostingStandards&Guidance}

The following is a summary of the "NHS and social care data: off-shoring and the use of public cloud services" gathered from cloud guidance information published by the Authority. It makes clear what evidence is to be sought from a Supplier, where it is deemed necessary to assure compliance with the 4 step process.

Some key points of note:

- All decisions in relation to the security of data are the responsibility of the data controller(s). Also, in many cases organisations will have a SIRO responsible for data and cyber security
- Where a professional body exists, there is certainly merit in seeking their approval for the migration of data to cloud, but ultimately the data controller remains the key approver
- Data Controllers need to understand the risks of moving to cloud, and any impact
- Data controllers must take into account the standard CIA triad (confidentiality, Integrity, Availability), and also other relevant factors, including, but not limited to, cost, security, resilience, capability and funding

The 4 steps to inform the data controller on a risk based decision are detailed below.

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).1} | Step {#Hosting&InfrastructureV1.1.3-Step} | Step Description {#Hosting&InfrastructureV1.1.3-StepDescription} | Evidence {#Hosting&InfrastructureV1.1.3-Evidence} |
| All | Step 1 - Understand the data {#Hosting&InfrastructureV1.1.3-Step1-Understandthedata} | All data managed by NHS and social care organisations should be treated as OFFICIAL or OFFICIAL-SENSITIVE data, in line with the Government Security Classification Policy.  The Authority has further elaborated the very broad classifications. The Health and Social Care Cloud Risk Model is more granular than the Government Security Classification Policy. | EVIDENCE requested for step 1: {#Hosting&InfrastructureV1.1.3-EVIDENCErequestedforstep1:}  1. The Supplier needs to provide evidence that they have identified all data, data types, and attributes, and assessed it against the model. 2. Binary objects identified within the data set, such as JPEG, PDF, etc, can still be classified by their content. The Supplier needs to evidence an understanding of the percentage splits between data types, which may alter the overall the classification. |
| All | Step 2- Assess the Risks {#Hosting&InfrastructureV1.1.3-Step2-AssesstheRisks} | The Authority's Health and Social Care data risk framework and associated data risk model are both used to establish the risk level of the data. Typically Personally Identifiable Data (PID) would be Level 5. Please refer to the link NHS and social care data: off-shoring and the use of public cloud services for latest versions of Cloud risk framework and Health and social care data risk model. | EVIDENCE requested for step 2: {#Hosting&InfrastructureV1.1.3-EVIDENCErequestedforstep2:}  1. Completed risk model indicating the risk level established from the data detailed in step 1. 2. The Health and Social Care Cloud Risk Model also considers service classification (Bronze/Silver/Gold/Platinum), and Suppliers will need a statement to back-up their selection of the classification. |
| All | Step 3 - Implement the appropriate controls {#Hosting&InfrastructureV1.1.3-Step3-Implementtheappropriatecontrols} | Care organisations, such as GPs, retain the data controller responsibilities and they are therefore ultimately responsible for ensuring that proportionate controls are put in place to mitigate all risks. The data controllers may rightly request to see these controls (proposed by the Supplier) before considering any migration to cloud. | EVIDENCE requested for step 3: {#Hosting&InfrastructureV1.1.3-EVIDENCErequestedforstep3:}  1. The Supplier will provide evidence against section 8. Appendix A - detailed advice and guidance from the latest version of "Cloud security good practice guide" present in NHS and social care data: off-shoring and the use of public cloud services with a statement (or linked evidence) against each guidance line item which is applicable for the data classification level identified at step 2. 2. Prior to implementation - where there are many data controllers using a Solution (such as a GP system), the Authority would request evidence of the comms strategy to inform all data controllers, seeking any dissent based on the identified risk. 3. Prior to implementation - consideration around GDPR: The Supplier should state they have completed and provide if requested to the Catalogue Authority, a Data Protection Impact Assessment (DPIA), plus confirm adherence to the relevant data protection legislation. |
| All | Step 4 - Monitoring the Implementation {#Hosting&InfrastructureV1.1.3-Step4-MonitoringtheImplementation} | All cloud providers take on data processor responsibilities, with Care organisations (e.g. GP practices) retaining the data controller responsibilities, and they must ensure the selected cloud provider remains fit for purpose. | EVIDENCE requested for step 4: {#Hosting&InfrastructureV1.1.3-EVIDENCErequestedforstep4:}  1. For Contracting Vehicles, Suppliers will be obliged to evidence any external accreditations at the point of renewal. This will include those external standards evidenced during step 3. |

## The Authority's Associated Cloud Guidance Links: {#Hosting&InfrastructureV1.1.3-TheAuthority'sAssociatedCloudGuidanceLinks:}

- NHS and social care data: off-shoring and the use of public cloud services

## Co-location and Provider Data Centre Hosting & Infrastructure Requirements {#Hosting&InfrastructureV1.1.3-Co-locationandProviderDataCentreHosting&InfrastructureRequirements}

- Scope
- Requirements - External Standards
- Physical Aspects
- Power
- IT Infrastructure
- Servers
- Network
- Management of Services and Infrastructure
- Asset Management
- Service Monitoring
- Device Management
- Data Storage
- Security
- Reporting & Documentation

## Scope {#Hosting&InfrastructureV1.1.3-Scope}

The scope of this document covers the infrastructure requirements a Supplier must meet when providing services where a Supplier has co located their service & infrastructure within a data centre providers facilities OR where the Supplier is using their own facilities. The requirements will cover a number of aspects including but not limited to:

- Provision of power and cooling
- Networking and IT Infrastructure
- Management of the Data Centre
- Physical presence of the data centre and the IT build processes
- Racks
- Mechanical and electrical plant
- Data Floor
- Operating Systems / Virtualisation
- Software (Solution Management)
- Business practices
- Security

For the avoidance of doubt these requirements do not cover cloud provision.

#### Required Evidence {#Hosting&InfrastructureV1.1.3-RequiredEvidence}

**Unless stated otherwise, the evidence expected for each requirement is to provide formal confirmation of compliance to the requirement.**

# Requirements - External Standards {#Hosting&InfrastructureV1.1.3-Requirements-ExternalStandards}

In addition to the below requirements the following standards (or equivalent) MUST be adhered to and where appropriate, accreditation achieved with a valid certificate and a Statement of Applicability (SoA) and documented scope provided.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).2} | Req. ID {#Hosting&InfrastructureV1.1.3-Req.ID} | Standard {#Hosting&InfrastructureV1.1.3-Standard} | Name {#Hosting&InfrastructureV1.1.3-Name} | Description {#Hosting&InfrastructureV1.1.3-Description.1} | Level {#Hosting&InfrastructureV1.1.3-Level.1} | Evidence {#Hosting&InfrastructureV1.1.3-Evidence.1} |
| All | ES1.0 {#Hosting&InfrastructureV1.1.3-ES1.0} | NHS and social care data: off-shoring and the use of public cloud services guidance | NHS and social care data: off-shoring and the use of public cloud services guidance | The geographical location (or specific range of locations) of the clinical data at rest and service management activities at any given time are to be known and communicated to the Authority.  Operating the Solution or elements of the Solution outside of England will be with the permission of the Authority, the data controllers and their representative organisations.  **Note:** There are no absolute barriers to the off-shoring of data or services, although the requirements of UK Government IA policy must be able to be met in the overseas location. See Data Protection Act and Offshoring for statements on the offshoring of information. | MUST | Provide formal confirmation of compliance to requirement. |
| All | ES2.0 {#Hosting&InfrastructureV1.1.3-ES2.0} | Sanctions, embargoes and restrictions | Sanctions, embargoes and restrictions | The Supplier will require approval from the Authority for any part of the Solution that is hosted or communicates with services outside of England.  The communication between systems will not be made to those countries or states prohibited by Government Policy. | MUST | Provide formal confirmation of compliance to requirement. |
| All | ES3.0 {#Hosting&InfrastructureV1.1.3-ES3.0} | Cyber Essentials Plus | Certified cyber security | Protect your organisation against cyber attack Cyber Essentials helps you to guard against the most common cyber threats and demonstrate your commitment to cyber security. | MUST | Supplier should have a valid Cyber Essential Plus Certificate. |
| All | ES4.0 {#Hosting&InfrastructureV1.1.3-ES4.0} | ISO 27001 - IT Security Management Systems | ISO/IEC 27001 | ISO/IEC 27001 specifies the requirements for establishing, implementing, maintaining and continually improving an information security management system within the context of the organisation. It also includes requirements for the assessment and treatment of information security risks tailored to the needs of the organisation.  The requirements set out in ISO/IEC 27001 are generic and are intended to be applicable to all organisations, regardless of type, size or nature. | SHOULD | **ISO/IEC 27001 Accreditation**  A valid ISO 27001 Certificate is required from a UKAS-registered accreditation organisation, **or IAF registered accreditation organisation in exceptional circumstances**. |
| All | ES5.0 {#Hosting&InfrastructureV1.1.3-ES5.0} | ISO 9001 - Quality management systems | ISO 9001:2015 | ISO 9001:2015 specifies requirements for a quality management system when an organisation:  a) needs to demonstrate its ability to consistently provide products and services that meet customer and applicable statutory and regulatory requirements, and  b) aims to enhance customer satisfaction through the effective application of the system, including processes for improvement of the system and the assurance of conformity to customer and applicable statutory and regulatory requirements.  All the requirements of ISO 9001:2015 are generic and are intended to be applicable to any organisation, regardless of its type or size, or the products and services it provides. | MUST | **Data Centre Provider -**Valid ISO 9001:2015 Certificate or evidence of compliance with Quality Management procedures aligned to ISO 9001. |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES7.0 {#Hosting&InfrastructureV1.1.3-ES7.0} | ISO 14001 Environmental management systems | ISO 14001:2015 | ISO 14001:2015 specifies the requirements for an environmental management system that an organisation can use to enhance its environmental performance. ISO 14001:2015 is intended for use by an organisation seeking to manage its environmental responsibilities in a systematic manner that contributes to the environmental pillar of sustainability.  ISO 14001:2015 helps an organisation achieve the intended outcomes of its environmental management system, which provide value for the environment, the organisation itself and interested parties. Consistent with the organisation 's environmental policy, the intended outcomes of an environmental management system include:  · enhancement of environmental performance  · fulfilment of compliance obligations  · achievement of environmental objectives  ISO 14001:2015 is applicable to any organisation, regardless of size, type and nature, and applies to the environmental aspects of its activities, products and services that the organisation determines it can either control or influence considering a life cycle perspective. ISO 14001:2015 does not state specific environmental performance criteria.  ISO 14001:2015 can be used in whole or in part to systematically improve environmental management. Claims of conformity to ISO 14001:2015, however, are not acceptable unless all its requirements are incorporated into an organisation 's environmental management system and fulfilled without exclusion. | MAY | **Data Centre Provider** - Valid ISO 14001:2015 Certificate or evidence of compliance with Environmental Management procedures aligned to ISO 14001. |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES8.0 {#Hosting&InfrastructureV1.1.3-ES8.0} | ISO 50001 Energy management systems | ISO 50001:2018 | This document specifies requirements for establishing, implementing, maintaining and improving an energy management system (EnMS). The intended outcome is to enable an organisation to follow a systematic approach in achieving continual improvement of energy performance and the EnMS.  This document:  a) is applicable to any organisation regardless of its type, size, complexity, geographical location, organisation al culture or the products and services it provides  b) is applicable to activities affecting energy performance that are managed and controlled by the organisation  c) is applicable irrespective of the quantity, use, or types of energy consumed  d) requires demonstration of continual energy performance improvement, but does not define levels of energy performance improvement to be achieved  e) can be used independently, or be aligned or integrated with other management systems  Annex A provides guidance for the use of this document. Annex B provides a comparison of this edition with the previous edition | MAY | **Data Centre Provider** - Valid ISO 50001:2018 Certificate or evidence of compliance with Energy Management procedures aligned to 50001. |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES9.0 {#Hosting&InfrastructureV1.1.3-ES9.0} | BS6701 Telecommunications equipment and telecommunications cabling. Specification for installation, operation and maintenance | BS 6701:2010 | If you work in the telecommunications industry, and are responsible for installing, operating or the administration and maintenance of copper or optical fiber cabling or equipment, then this newly-revised standard will be of interest.  Conformance to specific aspects of BS 6701 is a requirement of the Wiring Regulations (BS 7671) and is applicable in virtually all premises. In addition, it addresses cabling external to buildings and should be followed by anyone installing cabling.  Correctly specified and installed cable management systems ensure that telecommunication cabling performs at its best – so it is important that cable management be considered from the start of a project.  In addition to specifying the requirements beyond the scope of the BS EN 50174 series of standards for telecommunications cabling, BS 6701 provides requirements for installing telecommunications equipment. The application of BS 6701 will ensure that equipment is properly set up, which means the customer will be reassured their risk-managed cabling installations work to optimum performance, thus assuring more profitable business practice.  As one of the few national standards that are directly linked to the EN 50174 series, BS 6701 could also be used in other countries. It supports all cabling media. | SHOULD | **Data Centre Provider** - A valid BS 6701:2010 Certificate required from UKAS registered accreditation organisation. |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES10.0 {#Hosting&InfrastructureV1.1.3-ES10.0} | EU Code of Conduct | EUCoC | This Code of Conduct has been created in response to the increasing energy consumption in data centres and the need to reduce the related environmental, economic and energy supply security impacts. The aim is to inform and stimulate data centre operators and owners to reduce energy consumption in a cost-effective manner without hampering the mission critical function of data centres. The Code of Conduct aims to achieve this by improving understanding of energy demand within the data centre, raising awareness, and recommending energy efficient best practices and targets. | SHOULD | Provide formal confirmation of compliance to requirement. |
| All | ES11.0 {#Hosting&InfrastructureV1.1.3-ES11.0} | General Data Protection Regulation  Data Protection Act 2018 | GDPR / DPA 2018 | The Guide to the GDPR explains the provisions of the GDPR to help organisations comply with its requirements. It is for those who have day-to-day responsibility for data protection.  The GDPR forms part of the data protection regime in the UK, together with the new Data Protection Act 2018 (DPA 2018). The main provisions of this apply, like the GDPR, from 25 May 2018. | MUST | Provide formal confirmation of compliance to requirement. |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES13.0 {#Hosting&InfrastructureV1.1.3-ES13.0} | BS EN 50600-2-1:2014. Building construction  (Minimum availability class 3) | BS EN 50600-2-1:2014 | The unrestricted access to internet-based information demanded by the information society has led to an exponential growth of both internet traffic and the volume of stored/retrieved data. Data Centres are housing and supporting the information technology and network telecommunications equipment for data processing, data storage and data transport. They are required both by network operators (delivering those services to customer premises) and by enterprises within those customer premises.  Data Centres need to provide modular, scalable and flexible facilities and infrastructures to easily accommodate the rapidly changing requirements of the market. In addition, energy consumption of data centres has become critical both from an environmental point of view (reduction of carbon footprint) and with respect to economical considerations (cost of energy) for the data centre operator.  The implementation of data centres varies in terms of: a) purpose (enterprise, co-location, co-hosting or network operator facilities) b) security level c) physical size d) accommodation (mobile, temporary and permanent constructions)  The needs of data centres also vary in terms of availability of service, the provision of security and the objectives for energy efficiency. These needs and objectives influence the design of data centres in terms of building construction, power distribution, environmental control and physical security. Effective management and operational information is required to monitor achievement of the defined needs and objectives.  This series of European Standards specifies requirements and recommendations to support the various parties involved in the design, planning, procurement, integration, installation, operation and maintenance of facilities and infrastructures within data centres. These parties include:   1. owners, facility managers, ICT managers, project managers, main contractors 2. consultants, architects, building designers and builders, system and installation designers 3. Suppliers of equipment 4. installers, maintainers | SHOULD | Suppliers MUST be able to provide evidence to demonstrate alignment with the scope and aims of BS EN 50600.  **Note.**Formal accreditation (when available) will become a mandatory requirement as detailed in the Standards Roadmap. |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES14.0 {#Hosting&InfrastructureV1.1.3-ES14.0} | BS EN 50600-2-2:2014. Power distribution  (Minimum availability class 3) | BS EN 50600-2-2:2014 | SHOULD |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES15.0 {#Hosting&InfrastructureV1.1.3-ES15.0} | BS EN 50600-2-3:2014. Environmental control  (Minimum availability class 3) | BS EN 50600-2-3:2014 | SHOULD |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES16.0 {#Hosting&InfrastructureV1.1.3-ES16.0} | BS EN 50600-2-4:2015. Telecommunications cabling infrastructure  (Minimum availability class 3) | BS EN 50600-2-4:2015 | SHOULD |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES17.0 {#Hosting&InfrastructureV1.1.3-ES17.0} | BS EN 50600-2-5:2016. Security systems  (Minimum availability class 3) | BS EN 50600-2-5:2016 | SHOULD |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES18.0 {#Hosting&InfrastructureV1.1.3-ES18.0} | BS EN 50600-3-1:2016. Management and operational information  (Minimum availability class 3) | BS EN 50600-3-1:2016 | SHOULD |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES19.0 {#Hosting&InfrastructureV1.1.3-ES19.0} | BS EN 50600-4-1:2016. Overview of and general requirements for key performance indicators  (Minimum availability class 3) | BS EN 50600-4-1:2016 | SHOULD |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | ES20.0 {#Hosting&InfrastructureV1.1.3-ES20.0} | BS EN 50600-4-2:2016. Power Usage Effectiveness  (Minimum availability class 3) | BS EN 50600-4-2:2016 | SHOULD |

## Physical Aspects {#Hosting&InfrastructureV1.1.3-PhysicalAspects}

This section is concerned with the physical aspects of a Data Centre including where the Data Centre is located, some of its physical attributes and factors near that data centre which could affect its operation and security.

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).3} | ID {#Hosting&InfrastructureV1.1.3-ID.1} | Requirement {#Hosting&InfrastructureV1.1.3-Requirement} | Level {#Hosting&InfrastructureV1.1.3-Level.2} |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HPA4.0 {#Hosting&InfrastructureV1.1.3-HPA4.0} | Data Centre Locations:  The Supplier will provide the data centre address and the current data centre owner’s / operator’s details, to the Authority. | MUST |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HPA5.0 {#Hosting&InfrastructureV1.1.3-HPA5.0} | Data Centre Build:  The Supplier will provide the build date of the data centre, its current age and any planned or expected data centre services uplift or refit covering but not limited to:   - Power - Space - Cooling - Security - Construction | MUST |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HPA16.1 {#Hosting&InfrastructureV1.1.3-HPA16.1} | Data Centre Intrusion Detection:  The Supplier will ensure that the data centre perimeter is protected by an IDS (Intrusion Detection System) compliant to BS EN 50131-1:2006. | SHOULD |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HPA25.0 {#Hosting&InfrastructureV1.1.3-HPA25.0} | Data Centre Vehicle Access:  The Supplier’s data centre will have arrangements such that a vehicle is unable to enter the site before all the checking of the vehicle and driver has been completed.The gate will prevent the tail gating of vehicles. | MUST |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HPA32.0 {#Hosting&InfrastructureV1.1.3-HPA32.0} | Data Centre - declaration of Resilience:  The Supplier’s Solution will provide at a minimum two separate geographically physical locations to hold the data and capability to run the services. The distance between the two locations will be such that they cannot both be affected by concurrent loss due to overlapping items on the Location Risk Assessment. | MUST |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HPA34.0 {#Hosting&InfrastructureV1.1.3-HPA34.0} | Data Centre Access Declaration:  The Supplier will provide permanent access to the data centre and equipment, supported by an access request process of 24hrs notice for normal maintenance requests and 1hr for emergency access, with unlimited frequency, for the purpose of maintaining the systems and services.  **Note:** If the hosting provider is a 3rd party / sub-contractor to the Supplier and escorted access is the policy enforced then permanent access to the data centre will still be provided. | MUST |

## Power {#Hosting&InfrastructureV1.1.3-Power}

This section covers the power to the Data Centre, Data Hall and cabinets.

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).4} | ID {#Hosting&InfrastructureV1.1.3-ID.2} | Requirement {#Hosting&InfrastructureV1.1.3-Requirement.1} | Level {#Hosting&InfrastructureV1.1.3-Level.3} |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HPW11.0 {#Hosting&InfrastructureV1.1.3-HPW11.0} | Data Centre Standby Operation:  Refuelling of the tanks for the generators will be possible with the generators in use. | MUST |

## IT Infrastructure {#Hosting&InfrastructureV1.1.3-ITInfrastructure}

This section is concerned with the physical infrastructure that makes up the service, how it is built and the policies around its setup.

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).5} | ID {#Hosting&InfrastructureV1.1.3-ID.3} | Requirement {#Hosting&InfrastructureV1.1.3-Requirement.2} | Level {#Hosting&InfrastructureV1.1.3-Level.4} |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HI2.0 {#Hosting&InfrastructureV1.1.3-HI2.0} | Log File Timestamp:  The Supplier to ensure that log files written, even if the device is passive, will write the log with the synchronised time to NHS Network and written in UTC but can be displayed in the Supplier’s application in local time. | MUST |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HI3.0 {#Hosting&InfrastructureV1.1.3-HI3.0} | Time Synchronisation:  The Supplier will ensure the infrastructure’s time is synchronised with a NHS & National Apps, Cloud / CNSP NTP service, delivered as a minimum, by a stratum 3 service. | MUST |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HI5.0 {#Hosting&InfrastructureV1.1.3-HI5.0} | The Supplier to ensure that message time stamping is performed using UTC, for all infrastructure, but can be displayed in the Suppliers supported applications in local time.  **Note:** This requirements scope is the infrastructure; see IG Requirements for further related time stamping and representation. This requirement is to ensure that there is a consistent time stamping policy across all infrastructures and messaging so that correlation can occur locally, between Suppliers and also national applications. The requirement is to ensure that the raw date use is of the format defined. Local support applications (Applications used to manage the service) can represent the date in their local time if required and in line with the IG Requirements. | MUST |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HI9.0 {#Hosting&InfrastructureV1.1.3-HI9.0} | Support Agreement Confirmation:  The Supplier to ensure that all hardware, devices, servers and components have support agreements in place to replace faulty items if they fail. The replacing of components will not impact live service and meet SLA and planned down time agreements. | MUST |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HI13.0 {#Hosting&InfrastructureV1.1.3-HI13.0} | Live Service Separation:  The Supplier will ensure that Live environments are segregated from the development activity by using processors, virtual servers, domains and partitions that are not in use by live and by storing development utilities away from the live environment. | MUST |

## Servers {#Hosting&InfrastructureV1.1.3-Servers}

This section is concerned with servers that provide clinical applications, including operating systems and use of virtualisation.

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).6} | ID {#Hosting&InfrastructureV1.1.3-ID.4} | Requirement {#Hosting&InfrastructureV1.1.3-Requirement.3} | Level {#Hosting&InfrastructureV1.1.3-Level.5} |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HS9.0 {#Hosting&InfrastructureV1.1.3-HS9.0} | Server Operational Design: Hardening:  The Supplier will ensure that all operating systems and applications have undergone a hardening process to ensure only the necessary services are in place, within their domain of responsibility in the equipment and services they provide.  **Note:** Hardening is the process of securing a system reducing its vulnerability, through the use of patching, removal of unnecessary software and services.  Good Practice guidance can be found on The Authority's website  The Supplier to ensure that due diligence to hardening is performed for their domains of responsibility.  If the Supplier is responsible for the hardware / OS then this hardening will be performed on the hardware and OS.  If the Supplier only provides application software then the necessary hardening will have been performed on that application software.  If the mobile device hardware (Phone, Medical Device, mobile appliance) is provided by the Supplier as part of their Solution then hardening on the components they have provided will have been performed.  Where a BYO device is used the Supplier will ensure their application is hardened to protect the data and application. | MUST |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HS20.0 {#Hosting&InfrastructureV1.1.3-HS20.0} | Server Operational Design: Application Security:  The Supplier will ensure that servers are configured to disable or restrict:   - non-essential or redundant services (e.g. X Windows, Open Windows, fingered and web browsers) - communication services that are inherently susceptible to abuse (e.g. tftp, RPC, rlogin, rsh or rexec) - communication protocols that are prone to abuse, where not required (e.g. HTTP, HTTPS, SSH, FTP, SMTP, Telnet and UUCP) - execute permissions on sensitive commands or scripts (e.g. rlogin, rcp, rsh, remsh, tstp and trtp) - powerful utilities (e.g. Windows ‘Registry Editor’) or ‘control panels’ - run commands or command processors (e.g. Perl or Tcl) | MUST |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HS24.0 {#Hosting&InfrastructureV1.1.3-HS24.0} | Server Operational Design: Virtualisation:  The Supplier to ensure that physical servers hosting virtual instances are protected from resource overload (e.g. excessive use of the CPU, memory, hard disk and network). | MUST |

## Network {#Hosting&InfrastructureV1.1.3-Network}

This section covers the use of networks in the provision of the Supplier’s service. The NHS Wide Area Network is now known as HSCN; referred to as the “NHS Network” below.

The Health and Social Care Network (HSCN) is the successor to N3. In 2018 N3 was already closed to new implementations when The Authority published its 'Internet First' strategy. The strategy mandates that health systems should be designed to use the Internet rather than HSCN.

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).7} | ID {#Hosting&InfrastructureV1.1.3-ID.5} | Requirement {#Hosting&InfrastructureV1.1.3-Requirement.4} | Level {#Hosting&InfrastructureV1.1.3-Level.6} |
| All | HNT1.0 {#Hosting&InfrastructureV1.1.3-HNT1.0} | External Networking:  The Supplier’s data centre to be connected to the Internet and the NHS Network, for clinical services holding PID that are accessed from either an Internet or NHS Network attached end point. | MUST |
| All | HNT1.1 {#Hosting&InfrastructureV1.1.3-HNT1.1} | External Networking Termination:  If the Suppliers data centre are connected to the NHS Network termination will be from an approved termination point. | MUST |
| All | HNT1.2 {#Hosting&InfrastructureV1.1.3-HNT1.2} | External Networking - Spine Services:  The Supplier’s data centre to be connected to the Internet and the NHS Network, for services that communicate with national systems. (PDS, TMS, etc.) | MUST |
| All | HNT1.3 {#Hosting&InfrastructureV1.1.3-HNT1.3} | Network Security:  The Supplier will respond to the Authorities request for information around security, network settings and ports used, from time to time, in how their services operate across the NHS Network, to support the NHS Network QoS Policy over HSCN. | MUST |
| All | HNT2.0 {#Hosting&InfrastructureV1.1.3-HNT2.0} | Network - QoS:  Communications in and out of the data centre will adhere to the HSCN connection Agreement and NHS Network QoS policy for the classification of data across the network, to enable network traffic prioritisation and ‘class of service’ to reduce network latency. The Supplier will evidence their adherence to the QoS policy, to the Authority, for changes to the system in how it communicates across the NHS Network, prior to release.  **Note:**  See HSCN Quality of Service overview  See HCSN Technical Guidance | MUST |
| All | HNT2.1 {#Hosting&InfrastructureV1.1.3-HNT2.1} | NHS Network Connectivity:  The Supplier’s NHS Network connections to be compliant with the HSCN Connection Agreement and compliant with the DNS and IP addressing policies for the network, where HSCN is used.  See The Authority's HSCN Page | MUST |
| All | HNT3.1 {#Hosting&InfrastructureV1.1.3-HNT3.1} | NHS Networking Compliance:  The Supplier to provide evidence that the system complies with the requirements and best practice operating principals and guidance when operating over the NHS Network. Specifically the system to:   - Comply with the NHS Network QoS (Quality of Service) Policy - Performs adequately within the network latency constraints - Performs adequately within the typical bandwidth (downstream and upstream) provided to consumers - Collaborate with the Authority and relevant network providers to resolve escalated performance issues which could include installing diagnostic probes into the DC environment | MUST |
| All | HNT4.0 {#Hosting&InfrastructureV1.1.3-HNT4.0} | QoS Policy Acceptance:  The Supplier will have completed a NHS Network QoS Policy review, where the Suppliers application makes use of or is accessed across the NHS Network, have demonstrated the application and services adhere to the NHS Network policy. NHS Network QoS rules may need to be amended as a part of this review. Updates to refreshed QoS policies to be applied as required.  See HSCN Quality of Service overview | MUST |
| All | HNT6.0 {#Hosting&InfrastructureV1.1.3-HNT6.0} | Data Centre Network Connectivity:  The Supplier will provide the details of any carriers and the redundancy of all communications utilised in and out of the data centre as part of the Solution. This is to include but not limited to:   - Internet Connections - NHS Network Connections - Intra Site communication - Management / Support Connections | MUST |
| All | HNT7.0 {#Hosting&InfrastructureV1.1.3-HNT7.0} | Data Centre Network Resilience:  The data centre will have dual Internet and dual NHS Network connections via two exchanges, where available. | MUST |
| All | HNT21.0 {#Hosting&InfrastructureV1.1.3-HNT21.0} | Remote Application Connectivity:  The Supplier to ensure that all connections to remote servers and applications are authenticated. | MUST |
| All | HNT22.0 {#Hosting&InfrastructureV1.1.3-HNT22.0} | Remote Management Connectivity:  The Supplier to ensure that access to diagnostic ports for network and server components are securely controlled. | MUST |
| All | HNT23.0 {#Hosting&InfrastructureV1.1.3-HNT23.0} | Network Segregation:  The Supplier will segregate the networks that support deployments from other unrelated services to ensure the appropriate level of service. | MUST |
| All | HNT30.0 {#Hosting&InfrastructureV1.1.3-HNT30.0} | Network Access User Security:  The Supplier to ensure network devices are restricted to authorised network staff, using access controls that support individual accountability, and protected from unauthorised access / configuration / updates. | MUST |
| All | HNT31.0 {#Hosting&InfrastructureV1.1.3-HNT31.0} | Network Device Security:  The Supplier to ensure network devices that perform routing (e.g. routers and switches) are configured to prevent unauthorised or incorrect updates by:   - verifying the source of routing updates Verifying the destination of routing updates (e.g. by transmitting updates only to specific routers) - protecting the exchange of routing information (e.g. by using passwords) - encrypting the routing information being exchanged | MUST |
| All | HNT36.0 {#Hosting&InfrastructureV1.1.3-HNT36.0} | Wireless Network Design:  The Supplier to ensure there are documented standards / procedures at the appropriate level and implemented for controlling wireless access to the network, which cover:   - placement and configuration of wireless access points (hardware devices that provide interfaces between the wireless network and a wired network) - methods of limiting access to authorised users - use of encryption (e.g. Wi-Fi Protected Access II (WPA2)) for protecting information in transit - detection of unauthorised wireless access points and wireless devices | MUST |
| All | HNT38.0 {#Hosting&InfrastructureV1.1.3-HNT38.0} | The Supplier to ensure that new services or applications are accessible from the internet. New services or applications are those which are NOT currently deployed into an operational environment. | MUST |
| All | HNT39.0 {#Hosting&InfrastructureV1.1.3-HNT39.0} | The Supplier to ensure existing services or applications are transitioned to comply with the Internet First strategy in line with the Authority's published guidance (see Standards Road map). | MAY |
| All | HNT40.0 {#Hosting&InfrastructureV1.1.3-HNT40.0} | The Supplier to ensure HSCN connectivity is procured where there are any systems or services the Supplier needs to reach that are only on the HSCN network. | MUST |

## Management of Services and Infrastructure {#Hosting&InfrastructureV1.1.3-ManagementofServicesandInfrastructure}

This section details the requirements in relation to how ICT services provided by a Supplier are managed. The optimisation of resources and improved performance are achieved by adopting best practices for fault monitoring and management, configuration management, security management, bandwidth management, accounting management, etc.

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).8} | ID {#Hosting&InfrastructureV1.1.3-ID.6} | Requirement {#Hosting&InfrastructureV1.1.3-Requirement.5} | Level {#Hosting&InfrastructureV1.1.3-Level.7} |
| All | HMI9.0 {#Hosting&InfrastructureV1.1.3-HMI9.0} | Operational Systems Access:  The Supplier will ensure that encrypted administrative access to information systems, network devices and telecommunications equipment (e.g. by using secure management consoles or secure remote login shells such as ssh), is used. | MUST |
| All | HMI10.0 {#Hosting&InfrastructureV1.1.3-HMI10.0} | Operational Systems -Access Policy:  The Supplier will ensure access to critical systems and networks by external individuals for remote maintenance purposes (e.g. remote diagnosis / testing, software maintenance) should be managed by:   - defining and agreeing the objectives and scope of planned work - authorising sessions individually - restricting access rights so that they do not exceed those required to meet the objectives and scope of planned work - logging all activity undertaken - revoking access rights and changing passwords immediately after agreed maintenance is complete - performing an internal independent review of remote maintenance activity | MUST |
| All | HMI12.0 {#Hosting&InfrastructureV1.1.3-HMI12.0} | Operational Systems Patching Governance:  The Supplier to ensure a patch management process is established to govern the application of patches to:   - business applications, operating system software and firmware (e.g. on servers, mobile devices and consumer devices) - computer equipment - consumer devices (including tablets and smartphones) - virtual systems (e.g. virtual servers and virtual desktops) - network storage systems (including Storage Area Network (SAN) and Network-Attached Storage (NAS)) - network equipment (e.g. routers, switches, wireless access points and firewalls) | MUST |
| All | HMI13.0 {#Hosting&InfrastructureV1.1.3-HMI13.0} | Operational Systems Patching Process:  The Supplier to ensure that the patch management process will:   - specify methods of validating patches (e.g. ensuring that the patch is from an authorised source) - assess the business impact of implementing patches (or not implementing a particular patch) - ensure patches are tested against known criteria - describe methods of deploying patches in a timely manner (e.g. grouping multiple patches and using software distribution tools) - provide methods of deploying patches to systems that are not connected to the network (e.g. standalone computers) or devices that connect to the network infrequently (e.g. travelling staff) - report on the status of patch deployment across the organisation - include methods of dealing with the failed deployment of a patch (e.g. redeployment of the patch | MUST |

## Asset Management {#Hosting&InfrastructureV1.1.3-AssetManagement}

This section is concerned with the recording of the assets within the data centre.

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).9} | ID {#Hosting&InfrastructureV1.1.3-ID.7} | Requirement {#Hosting&InfrastructureV1.1.3-Requirement.6} | Level {#Hosting&InfrastructureV1.1.3-Level.8} |
| All | HCM1.0 {#Hosting&InfrastructureV1.1.3-HCM1.0} | Configuration Management Data Base:  A CMDB (Configuration Management Data Base) will be maintained and contain all CI’s, including but not limited to:   - Software versions - Licenses with expiry and type e.g. Open Source, Seat, GPL, SSL - Certificates and their expiry - Portable devices - Appliances - Version of CI - Location - Hardware components - Install applications and versions - Network connections - Network devices - Authentication tokens and devices - CI (Configuration Item) relationships - Location Details - Virtualisation deployment and state - Service related to (parent and Child)   The level of detail within the CMDB will be of sufficient detail at the CI level to be able to support the change and incident process.  The Supplier will ensure that a consistent naming convention (e.g. computer / server addresses, network device names, terminal locations and user identifiers) is used and recorded within the CMDB.  The Supplier to ensure that CIs that are used as part of the definition of configuration or an asset are held in the CMDB and DSL.This could include but is not limited to:   - Network configuration - Patches - Scripts | MUST |
| All | HCM4.0 {#Hosting&InfrastructureV1.1.3-HCM4.0} | Data Centre Audit Reporting:  The Supplier to make the results of its data centre audits available to the Authority on request along with any work off plans. | MUST |

## Service Monitoring {#Hosting&InfrastructureV1.1.3-ServiceMonitoring}

This section is concerned with how the service is monitored to understand its current state and how it is performing.

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).10} | ID {#Hosting&InfrastructureV1.1.3-ID.8} | Requirement {#Hosting&InfrastructureV1.1.3-Requirement.7} | Level {#Hosting&InfrastructureV1.1.3-Level.9} |
| All | HSM1.0 {#Hosting&InfrastructureV1.1.3-HSM1.0} | Monitoring Toolsets:  The Supplier to implement a toolset to be able to monitor capacity and utilisation of equipment, to support the capacity planning and incident process. This could include but not limited to:   - Disk IO and Space - CPU and Memory - Active user sessions - Messaging throughput - Key transaction performance both front door and intra-subsystem | MUST |
| All | HSM2.0 {#Hosting&InfrastructureV1.1.3-HSM2.0} | Service Management Tools:  The Supplier to implement service management tools and procedures within the sub-system including but not limited to:   - systems monitoring (disk, CPU, memory, utilisation) - audit and logging (time stamped) - messaging throughput and queue management - maintenance - backup and recovery - deployment of services and patches - altering at set thresholds below servicing impacting levels | MUST |
| All | HSM4.0 {#Hosting&InfrastructureV1.1.3-HSM4.0} | Capacity Monitoring:  The Supplier to implement a toolset to be able to benchmark the performance of the infrastructure and software assets to be able to understand the deviation from the normal operation. Note: This measurement will include but not limited to, memory, CPU, bandwidth (Tx/Rx), timing points and throughput. | MUST |
| All | HSM5.0 {#Hosting&InfrastructureV1.1.3-HSM5.0} | New Hardware Provisioning:  For technology uplifts and new services on new hardware provisions the Supplier will select hardware that enables equipment power and temperature to be monitored through standard interfaces allowing integration with the Supplier’s management system.  Note: This could be through the use of but not limited to:   - SNMP – Simple Network Management Protocol - IPMI – Intelligent Platform Management Interface - DCMI – Data Centre Manageability Interface | MUST |
| All | HSM6.0 {#Hosting&InfrastructureV1.1.3-HSM6.0} | Application Provider - NMS Access:  The Supplier will allow the Authority's supported method of integration with NMS. | SHOULD |

## Device Management {#Hosting&InfrastructureV1.1.3-DeviceManagement}

This section is concerned with how a device can be managed remotely.

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).11} | ID {#Hosting&InfrastructureV1.1.3-ID.9} | Requirement {#Hosting&InfrastructureV1.1.3-Requirement.8} | Level {#Hosting&InfrastructureV1.1.3-Level.10} |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HDM1.0 {#Hosting&InfrastructureV1.1.3-HDM1.0} | Lights Out Policy:  The Supplier will provide a ‘lights out’ operational model for the systems with specific processes to allow named engineer access to the environment. | MUST |
| - GP IT Futures - DFOCVC - Vaccinations - Local/PCN Delivery | HDM4.0 {#Hosting&InfrastructureV1.1.3-HDM4.0} | Remote Systems Maintenance:  It will be possible for the Supplier to perform software related maintenance and upgrade remotely without requiring physical access to the data hall. | MUST |

## Data Storage {#Hosting&InfrastructureV1.1.3-DataStorage}

This section is concerned with how data is protected when a failure occurs within the Solution. This covers both clinical and non-clinical data.

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).12} | ID {#Hosting&InfrastructureV1.1.3-ID.10} | Requirement {#Hosting&InfrastructureV1.1.3-Requirement.9} | Level {#Hosting&InfrastructureV1.1.3-Level.11} |
| All | HDP1.0 {#Hosting&InfrastructureV1.1.3-HDP1.0} | Data Access Protection:  The Supplier to ensure protection of clinical data at the storage level through the use of RAID, block snapshot, replication or mirroring technology within a single data centre / data hall. | MUST |
| All | HDP2.0 {#Hosting&InfrastructureV1.1.3-HDP2.0} | Data Loss protection:  The Supplier to ensure clinical data is protected using methods against up to two disk or media failures, within any one device configuration offering a discrete storage service. | MUST |
| All | HDP3.0 {#Hosting&InfrastructureV1.1.3-HDP3.0} | Data Integrity Implementation:  The Supplier will provide Transactional Integrity for clinical data by the use of a 2nd physical location for storing of data.  Note: The 2nd site could be a DR Site, Active 2nd site or a site used for storage replication. | MUST |
| All | HDP5.0 {#Hosting&InfrastructureV1.1.3-HDP5.0} | Data Handling Conformance:  The clinical data transferred to additional locations will be stored in accordance of the Authority’s data handling policies. | MUST |
| All | HDP6.0 {#Hosting&InfrastructureV1.1.3-HDP6.0} | Data Integrity Approach:  The Supplier’s approach to Transaction Integrity to securing data to at least two separate physical locations to be communicated to and assured by the Authority at the Suppliers design stage. | MUST |
| All | HDP7.0 {#Hosting&InfrastructureV1.1.3-HDP7.0} | Data Storage - BCDR standards:  The Supplier to ensure that Data Protection is performed in line with the Disaster Recovery and Business Continuity standard. | MUST |
| All | HDP9.0 {#Hosting&InfrastructureV1.1.3-HDP9.0} | Data Replication:  The Supplier will ensure that the clinical data applied to the primary site and sent to the 2nd site is processed in time order of how the data was applied to the primary site. Thus ensuring a consistent data set across the two sites and to maintain the application integrity. | MUST |
| All | HDP10.0 {#Hosting&InfrastructureV1.1.3-HDP10.0} | The Supplier to provide a “Data Management Policy”, to the Authority, detailing the data retention and level of resilience / protection needed. | MUST |
| All | HDP11.0 {#Hosting&InfrastructureV1.1.3-HDP11.0} | Data Protection Legislation:  The Supplier will demonstrate, if requested by the Authority, that functions/elements provided to meet Data Protection Legislation are operating in accordance with the Authority’s Requirements and the Design Documents. | MUST |
| All | HDP12.0 {#Hosting&InfrastructureV1.1.3-HDP12.0} | Data Disposal:  The Supplier will ensure that during disposal of equipment all data is removed from devices before they are passed to a 3rd party or reused in line with the “Disposal and Destruction of Sensitive Data Good Practice Guideline”.  See: Guidelines for Media Sanitization | MUST |

## Security {#Hosting&InfrastructureV1.1.3-Security}

Due to the sensitive nature of the information in this section, the details are held in the file "Co-location and Provider Data Centre Hosting & Infrastructure Requirements - Security" and can be requested by emailing gpitfutures@nhs.net.

## Reporting & Documentation {#Hosting&InfrastructureV1.1.3-Reporting&Documentation}

|  |  |  |  |
| --- | --- | --- | --- |
| Applicable Contracting Vehicle(s) {#Hosting&InfrastructureV1.1.3-ApplicableContractingVehicle(s).13} | ID {#Hosting&InfrastructureV1.1.3-ID.11} | Requirement {#Hosting&InfrastructureV1.1.3-Requirement.10} | Level {#Hosting&InfrastructureV1.1.3-Level.12} |
| All | HD1.0 {#Hosting&InfrastructureV1.1.3-HD1.0} | Documentation:  The Supplier will provide documentation which represents the non-functional technical architecture of the Solution, including but not limited to: data centre design, local and wide network architecture, and physical technology models. Documentation should include diagrams, and associated textual descriptions, as necessary to enable effective assurance of key Solution aspects as noted below: Non-Functional Specification Defines the non-functional aspects of the system including but not limited to:   - Details of any relevant contract service schedule(s) - Business continuity and disaster recovery design - Data Centre resilience design - Backup and Recovery Processes - Configuration Management including identification, control and verification - Performance monitoring design including categorisation of transactions and design of monitoring software including links into the Authority Solutions where relevant e.g. National Monitoring System (NMS) - Overall systems security design - Migration design showing design for process and data, details of any tools developed to support migration, details of duration and outages required to perform migration and data cleansing strategy - Capacity management design incorporating an indicative sizing model, a business transaction data forecast, an impact assessment on existing infrastructure and a baseline capacity plan - Availability Management design, including Component Failure Impact Assessment and monitoring - Services impact assessment including expected service management processes, helpdesk, maintenance, performance management and reporting changes - Support Model design, including dependencies on third parties (including NHS National Service Desk), support hours, escalation model and incident severity guidelines   **Note**: Document artefacts to be concise with a preference for diagrammatical form where the Supplier utilises as much of their own internal documentation as possible to reduce extra document production. | MUST |
| All | HD3.0 {#Hosting&InfrastructureV1.1.3-HD3.0} | Capacity Reporting:  The Supplier to provide memory, CPU, network and disk utilisation grouping by the sub systems utilising the resources as part of a capacity performance and planning review. | MUST |
| All | HD5.0 {#Hosting&InfrastructureV1.1.3-HD5.0} | The Supplier to provide a Hosting strategy roadmap to the Authority detailing where new technology advances could be exploited within the hosting arena.  **Note:** This could include advances in IaaS, SaaS, PaaS that may become viable within the term of the contract. | MUST |

### Additional Information {#Hosting&InfrastructureV1.1.3-AdditionalInformation}

See Recommended Best Practices

# Applicable Capabilities {#Hosting&InfrastructureV1.1.3-ApplicableCapabilities}

All Suppliers Solutions delivering any Capabilities will need to meet this Standard.

# Roadmap {#Hosting&InfrastructureV1.1.3-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Updates to external standards in Hosting and Infrastructure](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15315795970/Updates+to+external+standards+in+Hosting+and+Infrastructure) | [Hosting & Infrastructure](../../DSIC-Standards/Overarching-Standards/Hosting-Infrastructure.md), [Baseline Assurance Standard](../../DSIC-Standards/Overarching-Standards/Baseline-Assurance-Standard.md) | Draft | 14 Aug 2026 | Updating hyperlinks to external standards to the most recent version and removing references to specific editions | Uplift | Managed Capacity - Minor/Patch uplifts |