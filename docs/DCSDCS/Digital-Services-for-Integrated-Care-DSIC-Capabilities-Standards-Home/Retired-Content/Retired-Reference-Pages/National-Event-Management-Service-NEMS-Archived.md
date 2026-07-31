---
page_id: "1391135090"
space: "DCSDCS"
title: "National Event Management Service (NEMS) (Archived)"
version: 6
updated: "2024-06-07T09:51:43.713Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391135090/National+Event+Management+Service+NEMS+Archived"
labels: ["retired_reference_page"]
---

# National Event Management Service (NEMS) (Archived)

|  |  |
| --- | --- |
| ID | R5 |
| Version | 1.0.1 |
| Type | Reference |

# Summary

A decision was made to develop the Event Management Service (EMS) which will implement the publish/subscribe pattern to support the sharing of data across multiple health care settings. Initially, use cases around Child Health Services will pilot the service.

**Events Management Service (EMS)** - A service that facilitates the exchange of messages between publishers of event information and subscribers to that information. This service will provide the following:

- A method for allowing events to be published to the Event Hub.
- A mechanism for creating and viewing subscription rules, allowing interested parties to subscribe to events published to the Event Hub.
- A mechanism to allow events to be distributed to subscribers asynchronously (via MESH).

The EMS is a foundational interoperability service which will be used by programmes to meet their specific business requirements.

It is not the responsibility of the EMS to dictate how subscribers should process events, the responsibility of the EMS is limited to ensuring relevant events are delivered.

Specific use cases from Digital Child Health and Digital Maternity will require GP systems to integrate with the NEMS.

# Documentation

EMS API specification site on NHS Developer Network

EMS supports three functional interactions:

- Manage Subscriptions (synchronously via Subscription FHIR API)
- Publish Events (synchronously via Event Publication API)
- Receive Events (asynchronously via MESH with ITK3 wrapper)