---
page_id: "1391135052"
space: "DCSDCS"
title: "Co location and Provider Data Centre Hosting & Infrastructure Requirements"
version: 14
updated: "2020-10-29T17:04:18.899Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391135052/Co+location+and+Provider+Data+Centre+Hosting+Infrastructure+Requirements"
labels: []
---

# Co location and Provider Data Centre Hosting & Infrastructure Requirements

- [Introduction](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Introduction)
- [External Standards](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-ExternalStandards)
- [Physical Aspects](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-PhysicalAspects)
- [Power](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Power)
- [IT Infrastructure](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-ITInfrastructure)
- [Servers](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Servers)
- [Network](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Network)
- [Management of Services and Infrastructure](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-ManagementofServicesandInfrastructure)
- [Asset Management](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-AssetManagement)
- [Service Monitoring](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-ServiceMonitoring)
- [Device Management](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-DeviceManagement)
- [Data Storage](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-DataStorage)
- [Security](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Security)
- [Reporting & Documentation](#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Reporting&Documentation)

# Introduction {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Introduction}

The scope of this document covers the infrastructure requirements a supplier must meet when providing services where a supplier has co located their service & infrastructure within a data centre providers facilities OR where the supplier is using their own facilities. The requirements will cover a number of aspects including but not limited to:

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

Required Evidence

**Unless stated otherwise, the evidence expected for each requirement is to provide formal confirmation of compliance to the requirement.**

# External Standards {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-ExternalStandards}

In addition to the below requirements the following standards (or equivalent) MUST be adhered to and where appropriate, accreditation achieved with a valid certificate and a Statement of Applicability (SoA) and documented scope provided.

| Req. ID | Standard | Name | Description | Level | Evidence |
| --- | --- | --- | --- | --- | --- |
| ES1.0 | NHS and social care data: off-shoring and the use of public cloud services guidance | NHS and social care data: off-shoring and the use of public cloud services guidance | The geographical location (or specific range of locations) of the clinical data at rest and service management activities at any given time are to be known and communicated to NHS Digital.  Operating the Solution or elements of the Solution outside of England will be with the permission of NHS Digital, the data controllers and their representative organisations..  **Note:**  There are no absolute barriers to the off-shoring of data or services, although the requirements of UK Government IA policy must be able to be met in the overseas location.  See Data Protection Act and Offshoring for statements on the offshoring of information. | MUST | Provide formal confirmation of compliance to requirement |
| ES2.0 | Sanctions, embargoes and restrictions | Sanctions, embargoes and restrictions | The supplier will require approval from NHS Digital of any part of the Solution that is hosted or communicates with services outside of England.  The communication between systems will not be made to those countries or states prohibited by Government Policy. | MUST | Provide formal confirmation of compliance to requirement |
| ES3.0 | Cyber Essentials Plus | Certified cyber security | Protect your organisation against cyber attack Cyber Essentials helps you to guard against the most common cyber threats and demonstrate your commitment to cyber security | MUST | Valid Cyber Essentials Plus Certificate |
| ES4.0 | ISO 27001 - IT Security Management Systems | ISO/IEC 27001:2013 | ISO/IEC 27001:2013 specifies the requirements for establishing, implementing, maintaining and continually improving an information security management system within the context of the organisation. It also includes requirements for the assessment and treatment of information security risks tailored to the needs of the organisation.  The requirements set out in ISO/IEC 27001:2013 are generic and are intended to be applicable to all organisations, regardless of type, size or nature. | SHOULD | A valid ISO 27001:2013 Certificate is required from a UKAS accredited and registered certification organisation. |
| ES5.0 | ISO 9001 - Quality management systems | ISO 9001:2015 | ISO 9001:2015 specifies requirements for a quality management system when an organisation:  a) needs to demonstrate its ability to consistently provide products and services that meet customer and applicable statutory and regulatory requirements, and  b) aims to enhance customer satisfaction through the effective application of the system, including processes for improvement of the system and the assurance of conformity to customer and applicable statutory and regulatory requirements.  All the requirements of ISO 9001:2015 are generic and are intended to be applicable to any organisation, regardless of its type or size, or the products and services it provides. | MUST | **Data Centre Provider -**Valid ISO 9001:2015 Certificate or evidence of compliance with Quality Management procedures aligned to ISO 9001 |
| ES7.0 | ISO 14001 Environmental management systems | ISO 14001:2015 | ISO 14001:2015 specifies the requirements for an environmental management system that an organisation can use to enhance its environmental performance. ISO 14001:2015 is intended for use by an organisation seeking to manage its environmental responsibilities in a systematic manner that contributes to the environmental pillar of sustainability.  ISO 14001:2015 helps an organisation achieve the intended outcomes of its environmental management system, which provide value for the environment, the organisation itself and interested parties. Consistent with the organisation 's environmental policy, the intended outcomes of an environmental management system include:  · enhancement of environmental performance;  · fulfilment of compliance obligations;  · achievement of environmental objectives.  ISO 14001:2015 is applicable to any organisation , regardless of size, type and nature, and applies to the environmental aspects of its activities, products and services that the organisation determines it can either control or influence considering a life cycle perspective. ISO 14001:2015 does not state specific environmental performance criteria.  ISO 14001:2015 can be used in whole or in part to systematically improve environmental management. Claims of conformity to ISO 14001:2015, however, are not acceptable unless all its requirements are incorporated into an organisation 's environmental management system and fulfilled without exclusion. | MAY | **Data Centre Provider** - Valid ISO 14001:2015 Certificate or evidence of compliance with Environmental Management procedures aligned to ISO 14001 |
| ES8.0 | ISO 50001 Energy management systems | ISO 50001:2018 | This document specifies requirements for establishing, implementing, maintaining and improving an energy management system (EnMS). The intended outcome is to enable an organisation to follow a systematic approach in achieving continual improvement of energy performance and the EnMS.  This document:  a) is applicable to any organisation regardless of its type, size, complexity, geographical location, organisation al culture or the products and services it provides;  b) is applicable to activities affecting energy performance that are managed and controlled by the organisation ;  c) is applicable irrespective of the quantity, use, or types of energy consumed;  d) requires demonstration of continual energy performance improvement, but does not define levels of energy performance improvement to be achieved;  e) can be used independently, or be aligned or integrated with other management systems.  Annex A provides guidance for the use of this document. Annex B provides a comparison of this edition with the previous edition. | MAY | **Data Centre Provider** - Valid ISO 50001:2018 Certificate or evidence of compliance with Energy Management procedures aligned to 50001 |
| ES9.0 | BS6701 Telecommunications equipment and telecommunications cabling. Specification for installation, operation and maintenance | BS 6701:2010 | If you work in the telecommunications industry, and are responsible for installing, operating or the administration and maintenance of copper or optical fibre cabling or equipment, then this newly-revised standard will be of interest.  Conformance to specific aspects of BS 6701 is a requirement of the Wiring Regulations (BS 7671) and is applicable in virtually all premises.  In addition, it addresses cabling external to buildings and should be followed by anyone installing cabling.  Correctly specified and installed cable management systems ensure that telecommunication cabling performs at its best – so it is important that cable management be considered from the start of a project.  In addition to specifying the requirements beyond the scope of the BS EN 50174 series of standards for telecommunications cabling, BS 6701 provides requirements for installing telecommunications equipment. The application of BS 6701 will ensure that equipment is properly set up, which means the customer will be reassured their risk-managed cabling installations work to optimum performance, thus assuring more profitable business practice.  As one of the few national standards that are directly linked to the EN 50174 series, BS 6701 could also be used in other countries. It supports all cabling media. | SHOULD | A valid ISO 27001:2013 Certificate is required from a UKAS accredited and registered certification organisation. |
| ES10.0 | EU Code of Conduct | EUCoC | This Code of Conduct has been created in response to the increasing energy consumption in data centres and the need to reduce the related environmental, economic and energy supply security impacts. The aim is to inform and stimulate data centre operators and owners to reduce energy consumption in a cost-effective manner without hampering the mission critical function of data centres. The Code of Conduct aims to achieve this by improving understanding of energy demand within the data centre, raising awareness, and recommending energy efficient best practices and targets.  TBD: May be put on the roadmap. | SHOULD | Provide formal confirmation of compliance to requirement |
| ES11.0 | General Data Protection Regulation  Data Protection Act 2018 | GDPR / DPA 2018 | The Guide to the GDPR explains the provisions of the GDPR to help organisations comply with its requirements. It is for those who have day-to-day responsibility for data protection.  The GDPR forms part of the data protection regime in the UK, together with the new Data Protection Act 2018 (DPA 2018). The main provisions of this apply, like the GDPR, from 25 May 2018. | MUST | Provide formal confirmation of compliance to requirement |
| ES13.0 | BS EN 50600-2-1:2014. Building construction  (Minimum availability class 3) | BS EN 50600-2-1:2014 | The unrestricted access to internet-based information demanded by the information society has led to an exponential growth of both internet traffic and the volume of stored/retrieved data. Data centres are housing and supporting the information technology and network telecommunications equipment for data processing, data storage and data transport. They are required both by network operators (delivering those services to customer premises) and by enterprises within those customer premises.  Data centres need to provide modular, scalable and flexible facilities and infrastructures to easily accommodate the rapidly changing requirements of the market. In addition, energy consumption of data centres has become critical both from an environmental point of view (reduction of carbon footprint) and with respect to economical considerations (cost of energy) for the data centre operator.  The implementation of data centres varies in terms of: a) purpose (enterprise, co-location, co-hosting or network operator facilities); b) security level; c) physical size; d) accommodation (mobile, temporary and permanent constructions).  The needs of data centres also vary in terms of availability of service, the provision of security and the objectives for energy efficiency. These needs and objectives influence the design of data centres in terms of building construction, power distribution, environmental control and physical security. Effective management and operational information is required to monitor achievement of the defined needs and objectives.  This series of European Standards specifies requirements and recommendations to support the various parties involved in the design, planning, procurement, integration, installation, operation and maintenance of facilities and infrastructures within data centres. These parties include: 1) owners, facility managers, ICT managers, project managers, main contractors; 2) consultants, architects, building designers and builders, system and installation designers; 3) suppliers of equipment; 4) installers, maintainers. | SHOULD | Formal accreditation against BS EN 50600 will not be available until mid 2019 therefore suppliers MUST be able to provide evidence to demonstrate alignment with the scope and aims of BS EN 50600.  **Note.**  Formal accreditation (when available) will become a mandatory requirement as detailed in the standards road map |
| ES14.0 | BS EN 50600-2-2:2014. Power distribution  (Minimum availability class 3) | BS EN 50600-2-2:2014 | SHOULD |
| ES15.0 | BS EN 50600-2-3:2014. Environmental control  (Minimum availability class 3) | BS EN 50600-2-3:2014 | SHOULD |
| ES16.0 | BS EN 50600-2-4:2015. Telecommunications cabling infrastructure  (Minimum availability class 3) | BS EN 50600-2-4:2015 | SHOULD |
| ES17.0 | BS EN 50600-2-5:2016. Security systems  (Minimum availability class 3) | BS EN 50600-2-5:2016 | SHOULD |
| ES18.0 | BS EN 50600-3-1:2016. Management and operational information  (Minimum availability class 3) | BS EN 50600-3-1:2016 | SHOULD |
| ES19.0 | BS EN 50600-4-1:2016. Overview of and general requirements for key performance indicators  (Minimum availability class 3) | BS EN 50600-4-1:2016 | SHOULD |
| ES20.0 | BS EN 50600-4-2:2016. Power Usage Effectiveness  (Minimum availability class 3) | BS EN 50600-4-2:2016 | SHOULD |

# Physical Aspects {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-PhysicalAspects}

This section is concerned with the physical aspects of a Data Centre including where the Data Centre is located, some of its physical attributes and factors near that data centre which could affect its operation and security.

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **HPA4.0** | The supplier will provide the data centre address and the current data centre owner’s / operator’s details, to NHS Digital. | MUST |
| **HPA5.0** | The supplier will provide the build date of the data centre, its current age and any planned or expected Data Centre services uplift or refit covering but not limited to:   - Power - Space - Cooling - Security - Construction | MUST |
| **HPA16.1** | The supplier will ensure that the Data Centre perimeter is protected by an IDS (Intrusion Detection System) compliant to BS EN 50131-1:2006 | SHOULD |
| **HPA25.0** | The supplier’s Data Centre will have arrangements such that a vehicle is unable to enter the site before all the checking of the vehicle and driver has been completed.  The gate will prevent the tail gating of vehicles. | MUST |
| **HPA32.0** | The supplier’s Solution will provide at a minimum two separate geographically physical locations to hold the data and capability to run the services.  The distance between the two locations will be such that they cannot both be affected by concurrent loss due to overlapping items on the Location Risk Assessment. | MUST |
| **HPA34.0** | The supplier will provide permanent access to the Data Centre and equipment, supported by an access request process of 24hrs notice for normal maintenance requests and 1hr for emergency access, with unlimited frequency, for the purpose of maintaining the systems and services  **Note:** If the hosting provider is a 3rd party / sub-contractor to the supplier and escorted access is the policy enforced then permanent access to the Data Centre will still be provided. | MUST |

# Power {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Power}

This section covers the power to the Data Centre, Data Hall and cabinets.

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **HPW11.0** | Refuelling of the tanks for the generators will be possible with the generators in use. | MUST |

# IT Infrastructure {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-ITInfrastructure}

This section is concerned with the physical infrastructure that makes up the service, how it is built and the policies around its setup.

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **HI2.0** | The supplier to ensure that log files written, even if the device is passive, will write the log with the synchronised time to NHS Network and written in UTC but can be displayed in the supplier’s application in local time. | MUST |
| **HI3.0** | The supplier will ensure the infrastructure’s time is synchronised with a NHS & National Apps, Cloud / CNSP NTP service, delivered as a minimum, by a stratum 3 service | MUST |
| **HI5.0** | The supplier to ensure that message time stamping is performed using UTC, for all infrastructure, but can be displayed in the suppliers supported applications in local time.    **Note:** This requirements scope is the infrastructure; see IG Requirements for further related time stamping and representation. This requirement is to ensure that there is a consistent time stamping policy across all infrastructures and  messaging so that correlation can occur locally, between suppliers and also national applications. The requirement is to ensure that the raw date use is of the format defined.  Local support applications (Applications used to manage the service) can represent the date in their local time if required and in line with the IG Requirements. | MUST |
| **HI9.0** | The supplier to ensure that all hardware, devices, servers and components have support agreements in place to replace faulty items if they fail.  The replacing of components will not impact live service and meet SLA and planned down time agreements. | MUST |
| **HI13.0** | The supplier will ensure that Live environments are segregated from the development activity by using processors, virtual servers, domains and partitions that are not in use by live and by storing development utilities away from the live environment. | MUST |

# Servers {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Servers}

This section is concerned with servers that provide clinical applications, including operating systems and use of virtualisation.

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **HS9.0** | The supplier will ensure that all operating systems and applications have undergone a hardening process to ensure only the necessary services are in place, within their domain of responsibility in the equipment and services they provide.  **Note:** Hardening is the process of securing a system reducing its vulnerability, through the use of patching, removal of unnecessary software and services.  Good Practice guidance can be found on the NHS Digital Web Site  The supplier to ensure that due diligence to hardening is performed for their domains of responsibility.  If the supplier is responsible for the hardware / OS then this hardening will be performed on the hardware and OS.  If the supplier only provides application software then the necessary hardening will have been performed on that application software.  If the mobile device hardware (Phone, Medical Device, mobile appliance) is provided by the supplier as part of their Solution then hardening on the components they have provided will have been performed.  Where a BYO device is used the supplier will ensure their application is hardened to protect the data and application. | MUST |
| **HS20.0** | The supplier will ensure that servers are configured to disable or restrict:   - non-essential or redundant services (eg X Windows, Open  Windows, fingered and web browsers) - communication services that are inherently susceptible to abuse (e.g. tftp, RPC, rlogin, rsh or rexec) - communication protocols that are prone to abuse, where not required (e.g. HTTP, HTTPS, SSH, FTP, SMTP, Telnet and UUCP) - execute permissions on sensitive commands or scripts (e.g. rlogin, rcp, rsh, remsh, tstp and trtp) - powerful utilities (e.g. Windows ‘Registry Editor’) or ‘control panels’ - run commands or command processors (e.g. Perl or Tcl). | MUST |
| **HS24.0** | The supplier to ensure that physical servers hosting virtual instances are protected from resource overload (e.g. excessive use of the CPU, memory, hard disk and network). | MUST |

# Network {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Network}

This section covers the use of networks in the provision of the supplier’s service. The NHS Wide Area Network is now known as HSCN; referred to as the “NHS Network” below.

The Health and Social Care Network (HSCN) is the successor to N3. In 2018 N3 was already closed to new implementations when NHS Digital published its 'Internet First' strategy. The strategy mandates that health systems should be designed to use the Internet rather than HSCN.

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **HNT1.0** | The supplier’s data centre to be connected to the Internet and the NHS Network, for clinical services holding PID that are accessed from either an Internet or NHS Network attached end point. | MUST |
| **HNT1.1** | If the suppliers Data Centre are connected to the NHS Network termination will be from an approved termination point. | MUST |
| **HNT1.2** | The supplier’s data centre to be connected to the Internet and the NHS Network, for services that communicate with national systems. (PDS, TMS, etc) | MUST |
| **HNT1.3** | The supplier will respond to the Authorities request for information around security, network settings and ports used, from time to time, in how their services operate across the NHS Network, to support the NHS Network QoS Policy over HSCN. | MUST |
| **HNT2.0** | Communications in and out of the Data Centre will adhere to the HSCN connection Agreement and NHS Network QoS policy for the classification of data across the network, to enable network traffic prioritisation and ‘class of service’ to reduce network latency.  The supplier will evidence their adherence to the QoS policy, to NHS Digital, for changes to the system in how it communicates across the NHS Network, prior to release.  **Note:**  See HSCN Quality of Service overview  See HCSN Technical Guidance | MUST |
| **HNT2.1** | The supplier’s NHS Network connections to be compliant with the HSCN Connection Agreement and compliant with the DNS and IP addressing policies for the network, where HSCN is used  See NHS digital HCSN Page | MUST |
| **HNT3.1** | The supplier to provide evidence that the system complies with the requirements and best practice operating principals and guidance when operating over the NHS Network.  Specifically the system to:   - Comply with the NHS Network QoS (Quality of Service) Policy - Performs adequately within the network latency constraints - Performs adequately within the typical bandwidth (downstream and upstream) provided to consumers - Collaborate with NHS Digital and relevant network providers to resolve escalated performance issues which could include installing diagnostic probes into the DC environment. | MUST |
| **HNT4.0** | The supplier will have completed a NHS Network QoS Policy review, where the suppliers application makes use of or is accessed across the NHS Network, have demonstrated the application and services adhere to the NHS Network policy.  NHS Network QoS rules may need to be amended as a part of this review. Updates to refreshed QoS policies to be applied as required.  See HSCN Quality of Service overview | MUST |
| **HNT6.0** | The supplier will provide the details of any carriers and the redundancy of all communications utilised in and out of the data centre as part of the Solution. This is to include but not limited to:   - Internet Connections - NHS Network Connections - Intra Site communication - Management / Support Connections | MUST |
| **HNT7.0** | The Data Centre will have dual Internet and dual NHS Network connections via two exchanges, where available. | MUST |
| **HNT21.0** | The supplier to ensure that all connections to remote servers and applications are authenticated. | MUST |
| **HNT22.0** | The supplier to ensure that access to diagnostic ports for network and server components are securely controlled. | MUST |
| **HNT23.0** | The supplier will segregate the networks that support deployments from other unrelated services to ensure the appropriate level of service. | MUST |
| **HNT30.0** | The supplier to ensure network devices are restricted to authorised network staff, using access controls that support individual accountability, and protected from unauthorised access / configuration / updates. | MUST |
| **HNT31.0** | The supplier to ensure network devices that perform routing (e.g. routers and switches) are configured to prevent unauthorised or incorrect updates by:   - verifying the source of routing updates Verifying the destination of routing updates (e.g. by transmitting updates only to specific routers) - protecting the exchange of routing information (e.g. by using passwords) - encrypting the routing information being exchanged. | MUST |
| **HNT36.0** | The supplier to ensure there are documented standards / procedures at the appropriate level and implemented for controlling wireless access to the network, which cover:   - placement and configuration of wireless access points (hardware devices that provide interfaces between the wireless network and a wired network) - methods of limiting access to authorised users - use of encryption (e.g. Wi-Fi Protected Access II (WPA2)) for protecting information in transit - detection of unauthorised wireless access points and wireless devices.   **Note:**  See NHS Digital's Good practice Guidance on Wi-Fi | MUST |
| **HNT38.0** | The supplier to ensure that new services or applications are accessible from the internet.  New services or applications are those which are NOT currently deployed into an operational environment. | MUST |
| **HNT39.0** | The supplier to ensure existing services or applications are transitioned to comply with the Internet First strategy in line with NHS Digital published guidance (see Standards Road map). | MAY |
| **HNT40.0** | The supplier to ensure HSCN connectivity is procured where there are any systems or services the supplier needs to reach that are only on the HSCN network. | MUST |

# Management of Services and Infrastructure {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-ManagementofServicesandInfrastructure}

This section details the requirements in relation to how ICT services provided by a supplier are managed.  The optimisation of resources and improved performance are achieved by adopting best practices for fault monitoring and management, configuration management, security management, bandwidth management, accounting management, etc.

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **HMI9.0** | The supplier will ensure that encrypted administrative access to information systems, network devices and telecommunications equipment (e.g. by using secure management consoles or secure remote login shells such as ssh), is used. | MUST |
| **HMI10.0** | The supplier will ensure access to critical systems and networks by external individuals for remote maintenance purposes (e.g. remote diagnosis / testing, software maintenance) should be managed by:   - defining and agreeing the objectives and scope of planned work - authorising sessions individually - restricting access rights so that they do not exceed those required to meet the objectives and scope of planned work - logging all activity undertaken - revoking access rights and changing passwords immediately after agreed maintenance is complete - performing an internal independent review of remote maintenance activity | MUST |
| **HMI12.0** | The supplier to ensure a patch management process is established to govern the application of patches to:   - business applications, operating system software and firmware (eg on servers, mobile devices and consumer devices) - computer equipment - consumer devices (including tablets and smartphones) - virtual systems (e.g. virtual servers and virtual desktops) - network storage systems (including Storage Area Network (SAN) and Network-Attached Storage (NAS)) - network equipment (e.g. routers, switches, wireless access points and firewalls) | MUST |
| **HMI13.0** | The supplier to ensure that the patch management process will:   - specify methods of validating patches (e.g. ensuring that the patch is from an authorised source) - assess the business impact of implementing patches (or not implementing a particular patch) - ensure patches are tested against known criteria - describe methods of deploying patches in a timely manner (e.g. grouping multiple patches and using software distribution tools) - provide methods of deploying patches to systems that are not connected to the network (e.g. standalone computers) or devices that connect to the network infrequently (e.g. travelling staff) - report on the status of patch deployment across the organisation - include methods of dealing with the failed deployment of a patch (e.g. redeployment of the patch). | MUST |

# Asset Management {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-AssetManagement}

This section is concerned with the recording of the assets within the Data Centre.

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **HCM1.0** | A CMDB (Configuration Management Data Base) will be maintained and contain all CI’s, including but not limited to:   - Software versions - Licenses with expiry and type e.g. Open Source, Seat, GPL, SSL - Certificates and their expiry - Portable devices - Appliances - Version of CI - Location - Hardware components - Install applications and versions - Network connections - Network devices - Authentication tokens and devices - CI (Configuration Item) relationships - Location Details - Virtualisation deployment and state - Service related to (parent and Child)   The level of detail within the CMDB will be of sufficient detail at the CI level to be able to support the change and incident process.  The supplier will ensure that a consistent naming convention (e.g. computer / server addresses, network device names, terminal locations and user identifiers) is used and recorded within the CMDB.  The supplier to ensure that CIs that are used as part of the definition of configuration or an asset are held in the CMDB and DSL.  This could include but is not limited to:   - Network configuration - Patches - Scripts | MUST |
| **HCM4.0** | The supplier to make the results of its data centre audits available to NHS Digital on request along with any work off plans. | MUST |

# Service Monitoring {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-ServiceMonitoring}

This section is concerned with how the service is monitored to understand its current state and how it is performing.

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **HSM1.0** | The supplier to implement a toolset to be able to monitor capacity and utilisation of equipment, to support the capacity planning and incident process.   This could include but not limited to:   - Disk IO and Space - CPU and Memory - Active user sessions - Messaging throughput - Key transaction performance both front door and intra-subsystem. | MUST |
| **HSM2.0** | The supplier to implement service management tools and procedures within the sub-system including but not limited to:   - systems monitoring (disk, CPU, memory, utilisation) - audit and logging (time stamped) - messaging throughput and queue management - maintenance - backup and recovery - deployment of services and patches - altering at set thresholds below servicing impacting levels | MUST |
| **HSM4.0** | The supplier to implement a toolset to be able to benchmark the performance of the infrastructure and software assets to be able to understand the deviation from the normal operation.  Note: This measurement will include but not limted to, memory, CPU, bandwidth (Tx/Rx), timing points and throughput. | MUST |
| **HSM5.0** | For technology uplifts and new services on new hardware provisions the supplier will select hardware that enables equipment power and temperature to be monitored through standard interfaces allowing integration with the supplier’s management system.  ***Note:*** This could be through the use of but not limited to :   - SNMP – Simple Network Management Protocol - IPMI – Intelligent Platform Management Interface - DCMI – Data Centre Manageability Interface | MUST |
| **HSM6.0** | **Application Provider** - NMS Access:  The supplier will allow an NHS Digital supported method of integration with NMS. | SHOULD |

# Device Management {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-DeviceManagement}

This section is concerned with how a device can be managed remotely.

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **HDM1.0** | The supplier will provide a ‘lights out’ operational model for the systems with specific processes to allow named engineer access to the environment. | MUST |
| **HDM4.0** | It will be possible for the supplier to perform software related maintenance and upgrade remotely without requiring physical access to the data hall. | MUST |

# Data Storage {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-DataStorage}

This section is concerned with how data is protected when a failure occurs within the Solution.  This covers both clinical and non-clinical data.

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **HDP1.0** | The supplier to ensure protection of clinical data at the storage level through the use of RAID, block snapshot, replication or mirroring technology within a single data centre / data hall. | MUST |
| **HDP2.0** | The supplier to ensure clinical data is protected using methods against up to two disk or media failures, within any one device configuration offering a discrete storage service. | MUST |
| **HDP3.0** | The supplier will provide Transactional Integrity for clinical data by the use of a 2nd physical location for storing of data.  **Note:** The 2nd site could be a DR Site, Active 2nd site or a site used for storage replication. | MUST |
| **HDP5.0** | The clinical data transferred to additional locations will be stored in accordance of NHS Digital’s data handling policies. | MUST |
| **HDP6.0** | The supplier’s approach to Transaction Integrity to securing data to at least two separate physical locations to be communicated to and assured by NHS Digital at the suppliers design stage. | MUST |
| **HDP7.0** | The supplier to ensure that Data Protection is performed in line with the Business Continuity and Disaster Recovery Standard. | MUST |
| **HDP9.0** | The supplier will ensure that the clinical data applied to the primary site and sent to the 2nd site is processed in time order of how the data was applied to the primary site. Thus ensuring a consistent data set across the two sites and to maintain the application integrity. | MUST |
| **HDP10.0** | The supplier to provide a “Data Management Policy”, to NHS Digital, detailing the data retention and level of resilience / protection needed. | MUST |
| **HDP11.0** | The supplier will demonstrate, if requested by NHS Digital, that functions/elements provided to meet Data Protection Legislation are operating in accordance with NHS Digital's Requirements and the Design Documents. | MUST |
| **HDP12.0** | The supplier will ensure that during disposal of equipment all data is removed from devices before they are passed to a 3rd party or reused in line with the “Disposal and Destruction of Sensitive Data Good Practice Guideline”.  See: Guidelines for Media Sanitization | MUST |

# Security {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Security}

Due to the sensitive nature of the information in this section, the details are held on Bravo in the file "Co location and Provider Data Centre Hosting & Infrastructure Requirements - Security".

# Reporting & Documentation {#ColocationandProviderDataCentreHosting&InfrastructureRequirements-Reporting&Documentation}

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **HD1.0** | The supplier will provide documentation which represents the non-functional technical architecture of the Solution, including but not limited to: data centre design, local and wide network architecture, and physical technology models. Documentation should include diagrams, and associated textual descriptions, as necessary to enable effective assurance of key Solution aspects as noted below: Non-Functional Specification Defines the non-functional aspects of the system including but not limited to:   - Details of any relevant contract service schedule(s) - Business continuity and disaster recovery design - Data centre resilience design - Backup and Recovery Processes - Configuration Management including identification, control and verification - Performance monitoring design including categorisation of transactions and design of monitoring software including links into NHS Digital Solutions where relevant e.g. National Monitoring System (NMS) - Overall systems security design - Migration design showing design for process and data, details of any tools developed to support migration, details of duration and outages required to perform migration and data cleansing strategy - Capacity management design incorporating an indicative sizing model,  a business transaction data forecast, an impact assessment on existing infrastructure and a baseline capacity plan - Availability Management design, including Component Failure Impact Assessment and monitoring - Services impact assessment including expected service management processes, helpdesk, maintenance, performance management and reporting changes - Support Model design, including dependencies on third parties (including NHS National Service Desk), support hours, escalation model and incident severity guidelines.   **Note:** Document artefacts to be concise with a preference for diagrammatical form where the supplier utilises as much of their own internal documentation as possible to reduce extra document production. | MUST |
| **HD3.0** | The supplier to provide memory, CPU, network and disk utilisation grouping by the sub systems utilising the resources as part of a capacity performance and planning review. | MUST |
| **HD5.0** | The supplier to provide a Hosting strategy roadmap to NHS Digital detailing where new technology advances could be exploited within the hosting arena.  **Note:** This could include advances in IaaS, SaaS, PaaS that may become viable within the term of the contract. | MUST |