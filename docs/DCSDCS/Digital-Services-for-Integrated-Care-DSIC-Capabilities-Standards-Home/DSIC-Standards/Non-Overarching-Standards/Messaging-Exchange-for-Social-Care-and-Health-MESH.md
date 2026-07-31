---
page_id: "1391133887"
space: "DCSDCS"
title: "Messaging Exchange for Social Care and Health (MESH)"
version: 17
updated: "2026-07-22T13:03:41.874Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133887/Messaging+Exchange+for+Social+Care+and+Health+MESH"
labels: ["standard"]
---

# Messaging Exchange for Social Care and Health (MESH)

|  |  |
| --- | --- |
| **ID** | S50 |
| **Version** | 1.0.2 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

/\*<![CDATA[\*/
div.rbtoc1785497896776 {padding: 0px;}
div.rbtoc1785497896776 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785497896776 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#MessagingExchangeforSocialCareandHealth(MESH)-Introduction)
- [Requirements](#MessagingExchangeforSocialCareandHealth(MESH)-Requirements)
  - [Messaging Architecture](#MessagingExchangeforSocialCareandHealth(MESH)-MessagingArchitecture)
  - [Connection Methods](#MessagingExchangeforSocialCareandHealth(MESH)-ConnectionMethods)
- [Compliance, Assurance and Testing](#MessagingExchangeforSocialCareandHealth(MESH)-Compliance,AssuranceandTesting)
- [Documentation](#MessagingExchangeforSocialCareandHealth(MESH)-Documentation)
- [Dependencies](#MessagingExchangeforSocialCareandHealth(MESH)-Dependencies)
- [Roadmap](#MessagingExchangeforSocialCareandHealth(MESH)-Roadmap)

# Introduction

The Message Exchange for Social Care and Health (MESH) is a centralised message transfer service provided by The Authority using the Spine Services Core infrastructure. This allows the service to benefit from the large-scale reliability of the Spine Services including its disaster recovery Capabilities and established service support.

The service supports the secure transfer of both clinical and business data flows between NHS Organisations and affiliated organisations. Sending organisations generate messages and “post” them to the central service from where they can then be “collected” by the recipient organisation. The principle of message transfer is “store and retrieve”. MESH is generally provided to end sites as part of Supplier provided Solutions although organisations can manage their interactions with the service directly themselves.

Information and technical documentation on use of the service can be found on The Authority’s website [here](https://digital.nhs.uk/services/message-exchange-for-social-care-and-health-mesh).

An on-line message tracking service is provided to enable Suppliers, end-sites and support organisations to trace messages. This Message On-line Enquiry Service (MOLES) supports the tracking of messages as they are transferred across the service in near real-time. Information on MOLES and its use are provided [here](https://digital.nhs.uk/services/message-exchange-for-social-care-and-health-mesh/message-tracking-the-mesh-online-enquiry-service-moles).

# Requirements

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| MR2.4.04 | **MESH Client**  Each new release of the MESH Client **MUST** be installed within 6 months of notification of its release by the MESH Service Team. Any mandatory functional or non-functional changes to any part(s) of the system that are required to be made in order to implement a new release **MUST** also be Deployed along with the new Client. | MUST |

## Messaging Architecture

MESH supports the transfer of data between organisations using the principle of “store and retrieve”. It utilises a mailbox-based messaging architecture. All registered endpoints have a mailbox. That mailbox can support the transfer and receipt of many different message types. Messages are uploaded and stored on the Central MESH Server from where they are then collected.

The service is agnostic in respect of the types of message payload that it can transfer. This includes the full range of potential data transfers from fully structured, such as FHIR, XML, EDIFACT etc to plain text. Message transfers must however comply with the published [MESH Interface Specification](https://digital.nhs.uk/developer/api-catalogue/message-exchange-for-social-care-and-health-api) to be accepted by MESH and transferred.

MESH supports the transfer of individual transfers up to 100MB in its standard form. It can support file transfers up to 20GB. To support transfers of this size (up to 20GB) an additional attribute is simply added for the specific transfer which informs the service to adopt a chunking process for that specific transfer.

MESH supports the transfer of data between organisations. It does NOT provide confirmation that end applications within those organisations are able to consume and appropriately process those transfers once they are collected from MESH. The service does record robust recording on transfers as they are transferred across the service, including error logging and non-collected reports. The readiness of end applications to consume message transfers is beyond the scope of MESH and is the responsibility of individual programmes, the standards they adopt and business rules and notifications that they define.

The [Interoperability Toolkit (ITK)](Interoperability-Toolkit-ITK.md) does address the MESH issues in respect of reliable messaging. It is not the only approach but implementations requiring this can develop in accordance with the ITK.

## Connection Methods

Access to MESH can be requested by submission of the appropriate [on-line form](https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdigital.nhs.uk%2Fservices%2Fmessage-exchange-for-social-care-and-health-mesh%2Fmessaging-exchange-for-social-care-and-health-apply-for-a-mailbox&data=05%7C02%7Crobyn.brooke1%40nhs.net%7Ce074bbf2d78f41931b7e08dca5880837%7C37c354b285b047f5b22207b48d774ee3%7C0%7C0%7C638567250871463385%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=YwJx3twGY0lz786zlTzftdDs9R0SdSUKam2HaIIGuiU%3D&reserved=0). Suppliers who are using products other than the Java MESH Client or the MESH User Interface to send/receive messages must first go through an [onboarding process](https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdigital.nhs.uk%2Fdeveloper%2Fapi-catalogue%2Fmessage-exchange-for-social-care-and-health-api%23overview--onboarding&data=05%7C02%7Crobyn.brooke1%40nhs.net%7Ce074bbf2d78f41931b7e08dca5880837%7C37c354b285b047f5b22207b48d774ee3%7C0%7C0%7C638567250871471790%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=P3oZBDUvxyhhGZKHuyjy0TuSQa%2Bbg0PzbgrDlox%2FsE0%3D&reserved=0) via the Digital Onboarding Service to show that their product conforms to the MESH API specifications.

There are 3 methods for connection to MESH, these are;

1. **MESH User Interface (UI)**

   1. Accessed via Spine Portal (web-enabled)
   2. Central configuration by NHS Digital
   3. Aimed at Low Tech End-Points (entry level)
   4. Smartcards required (2-factor authentication possible as alternative)
   5. Administrators in local organisations manage access
2. **MESH Client**

   1. Java-based client provided by NHS Digital (utilises the API)
   2. Supports interfacing with end applications
   3. Can be run as a service
   4. Controlled access to MESH with some level of local config
   5. Local Installation/development
   6. Aimed at Suppliers and Technical Organisations
3. **MESH Application Interface (API)**

   1. Allows integration to end applications
   2. High level of control
   3. Assurance Process must be completed
   4. Local Installation/development
   5. Aimed at Suppliers and Technical Organisations

The majority of the connections to MESH are currently supported by the MESH client. The expectation is that Suppliers and organisations will develop Solutions using the MESH client or the API. The choice of connection method is not prescribed by The Authority. The choice may be made based on the level of control or integration that Suppliers or organisations may prefer in their interaction with the service.

The MESH UI provides entry-level access to the service where there is little local support or Supplier involvement. It allows end users, individually or in teams, rather than end applications to interact with the MESH. This extends the use of MESH from pure application to application only.

If mandated Suppliers must use MESH in accordance to individual interface specifications.

# Compliance, Assurance and Testing

See the Message Exchange for Social Care and Health (MESH) section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

Technical documentation and file downloads are hosted at the [MESH download page](https://digital.nhs.uk/services/message-exchange-for-social-care-and-health-mesh/mesh-guidance-hub).

# Dependencies

There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents.

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |