---
page_id: "14924382209"
space: "DCSDCS"
title: "Patient Data Manager v0.1.1"
version: 2
updated: "2026-05-05T14:37:24.706Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14924382209/Patient+Data+Manager+v0.1.1"
labels: ["standard"]
---

# Patient Data Manager v0.1.1

|  |  |
| --- | --- |
| **ID** | S122 |
| **Version** | 0.1.1 |
| **Type** | Standard |
| **Status** | Draft |
| **Effective Date** | TBC |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

- [Introduction](#PatientDataManagerv0.1.1-Introduction)
- [Requirements](#PatientDataManagerv0.1.1-Requirements)
  - [Patient Data Manager FHIR API Operations](#PatientDataManagerv0.1.1-PatientDataManagerFHIRAPIOperations)
- [Compliance, Assurance and Testing](#PatientDataManagerv0.1.1-Compliance,AssuranceandTesting)
- [Documentation](#PatientDataManagerv0.1.1-Documentation)
- [Dependencies](#PatientDataManagerv0.1.1-Dependencies)
- [Roadmap](#PatientDataManagerv0.1.1-Roadmap)

# Introduction

The Patient Data Manager FHIR API enables NHS products to store, retrieve, and manage Patient health and care data in a standardised, interoperable format.

See [Patient Data Manager FHIR API](https://digital.nhs.uk/developer/api-catalogue/patient-data-manager) for further information.

# Requirements

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| GP Suppliers | PDM01 | Implement and maintain the [Patient Data Manager FHIR API](https://digital.nhs.uk/developer/api-catalogue/patient-data-manager) requirements inline with the latest specification version as per the Patient Data Manager FHIR API Operations section. | MUST |
| PDM02 | The Patient Data Manager FHIR API is called to get a specific FHIR resource when a notification event from the [Multicast Notification Service (MNS)](../DSIC-Standards/Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) is processed. | MUST |
| PDM03 | The Multicast Notification Service (MNS) notification event will be processed in an idempotent way. | MUST |
| PDM04 | After receipt, regardless of ingestion outcome of the FHIR resource, the Solution shall create a resource acknowledgement in the Patient Data Manager FHIR API according to the [FHIR Acknowledgement framework](https://simplifier.net/guide/Acknowledgement-Framework/Home?version=current).  The acknowledgement will cover both success and failure scenarios. | MUST |
| PDM05 | **Performance - Get a specific FHIR resource**  The Patient Data Manager FHIR API is called to retrieve a FHIR resource within 30 seconds of receiving the MNS event notification, measured end-to-end. | MUST |
| PDM06 | **Performance - Data Ingestion**  The ingested FHIR resource will be processed and made available in the GP IT Solution within 2 minutes of receipt of the FHIR resource from the Patient Data Manager FHIR API, measured end-to-end. | MUST |
| PDM07 | **Performance - Acknowledgements**  A resource acknowledgement shall be sent to the Patient Data Manager FHIR API within 5 minutes of FHIR resource ingestion. | MUST |
| PDM08 | **Reliability - Retry**  The system will attempt a minimum of 3 retries (with an option to extend to 5) before classifying a request as failed.  Each write operation should include an idempotency key. When retrying the same operation, use the same key to prevent duplicate processing.  As in line with PDM-009.  Examples may include, but are not limited to:   - Create a resource - Get a specific resource | MUST |
| PDM09 | **Reliability - Exponential Backoff Strategy**  Retry logic for failed request processing will follow an exponential backoff strategy to prevent system overload and ensure safe reprocessing.  Examples may include, but are not limited to:   - Create a resource - Get a specific resource | MUST |
| PDM10 | **Reliability - Dead Letter Queue (DLQ)**  Un-processable events or requests stemming from background processing to be published to a DLQ for investigation and out-of-band processing.  Examples may include, but are not limited to:   - Create a resource - Get a specific resource | MUST |
| PDM11 | **Reliability - DLQ Retry**  The cause of failure and events or requests in the dead letter queue (DLQ) to be retried after the cause of failure has been resolved, within 1 working days.  Examples may include, but are not limited to:   - Create a resource - Get a specific resource | MUST |

## Patient Data Manager FHIR API Operations

| **Capability** | **FHIR Resources** | **Post a bundle of operations** | **Search the datastore using GET** | **Update or create a specific resource based on conditions** | **Create a resource** | **Get a specific resource** | **Update or create a specific resource** | **Delete a specific resource** | **Search the datastore using POST** | **Post a Document bundle** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | [NHS Health Check online](https://nhsdigital.github.io/digital-health-checks-public/) | (tick) | (error) | (error) | (tick) | (tick) | (error) | (error) | (error) | (error) |

# Compliance, Assurance and Testing

See the Patient Data Manager FHIR API section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

- [Patient Data Manager FHIR API](https://digital.nhs.uk/developer/api-catalogue/patient-data-manager#overview--overview)
- [Patient Data Manager (PDM)](https://digital.nhs.uk/services/patient-data-manager)
- [NHS Health Check online Developer Documentation](https://nhsdigital.github.io/digital-health-checks-public/)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- [Authentication and Access](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API
- [Multicast Notification Service (MNS)](../DSIC-Standards/Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) Standard

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Title |
| --- |
| No content found. |