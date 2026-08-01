---
page_id: "10886316215"
space: "DCSDCS"
title: "Generic FHIR Receiver"
version: 15
updated: "2026-07-21T15:11:24.998Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/10886316215/Generic+FHIR+Receiver"
labels: ["standard"]
---

# Generic FHIR Receiver

|  |  |
| --- | --- |
| **ID** | S76 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#GenericFHIRReceiver-Introduction)
- [Requirements](#GenericFHIRReceiver-Requirements)
- [Compliance, Assurance and Testing](#GenericFHIRReceiver-Compliance,AssuranceandTesting)
- [Dependencies](#GenericFHIRReceiver-Dependencies)
- [Roadmap](#GenericFHIRReceiver-Roadmap)

# Introduction {#GenericFHIRReceiver-Introduction}

The Generic FHIR Receiver is a component which will receive messages to the GP Practice which are:

- Delivered using [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md).
- Structured using [FHIR](http://hl7.org/fhir/summary.html)STU3 messages.
- Which meet the[ITK3](https://developer.nhs.uk/apis/itk3messagedistribution/) specification.

The Generic FHIR Receiver will obtain messages from the MESH Client or API depending on the Workflow ID within the MESH message header.

Various types of messages are received into GP Practices via MESH; some other component (referred to in the documentation as a Message Distributor) will usually handle all the incoming messages for the Practice MESH "mailbox", and distribute them to the appropriate handler for processing according to a workflow identifier and/or other metadata in the MESH header. The Generic FHIR Receiver will, therefore, receive its messages from this Message Distributor.

In summary, the responsibilities of the Generic FHIR Receiver are:

- Receive incoming ITK3 FHIR messages.
- Verify the message is a well-formed XML.
- Verify the message is a valid FHIR message conforming to the ITK3 specification.
- Match the message subject to a known Patient.
- Send Infrastructure and Business Acknowledgement messages (which are also FHIR messages which conform to the ITK3 specification) where these have been requested.
- Raise workflow tasks as appropriate using the data in the payload.

# Requirements {#GenericFHIRReceiver-Requirements}

Generic FHIR Receiver background and requirements:

[Generic FHIR Receiver In…](../../../../.raw/DCSDCS/attachments/10886316215/att10886316231-Generic FHIR Receiver Interop Capability - Specification v0_5.docx)

# Compliance, Assurance and Testing {#GenericFHIRReceiver-Compliance,AssuranceandTesting}

See the Generic FHIR Receiver section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Dependencies {#GenericFHIRReceiver-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md) - Message transport mechanism required to receive ITK3/FHIR messages asynchronously

# Roadmap {#GenericFHIRReceiver-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [Generic FHIR Receiver Interop Capability - Specification v0_5.docx](../../../../.raw/DCSDCS/attachments/10886316215/att10886316231-Generic FHIR Receiver Interop Capability - Specification v0_5.docx)
