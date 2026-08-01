---
page_id: "11235426957"
space: "DCSDCS"
title: "GP Data for Planning and Research v1.0.1"
version: 16
updated: "2025-12-15T12:23:29.751Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11235426957/GP+Data+for+Planning+and+Research+v1.0.1"
labels: ["standard_retired"]
---

# GP Data for Planning and Research v1.0.1

|  |  |
| --- | --- |
| **ID** | S78 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Retired |
| **Effective Date** | 30 Oct 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) |

- [Introduction](#GPDataforPlanningandResearchv1.0.1-Introduction)
- [Requirements](#GPDataforPlanningandResearchv1.0.1-Requirements)
- [Compliance, Assurance and Testing](#GPDataforPlanningandResearchv1.0.1-Compliance,AssuranceandTesting)
- [Documentation](#GPDataforPlanningandResearchv1.0.1-Documentation)
- [Dependencies](#GPDataforPlanningandResearchv1.0.1-Dependencies)
- [Roadmap](#GPDataforPlanningandResearchv1.0.1-Roadmap)

# Introduction  {#GPDataforPlanningandResearchv1.0.1-Introduction}

This collection is called GP Data for Planning and Research (GPDfPR) and its purpose is to support the data needs of the health and social care system including policy development, public health, planning and commissioning of services and research. This new collection is designed to reduce the number of requests for access to data received by General Practice.

Once fully established, NHS Digital will undertake a managed transition from the General Practice Extraction Service (GPES) to the new GP data service. NHS Digital will also work with other organisations to enable transition from existing data flows to the new service.

More information about this data collection and the General Practice obligation to provide data for this purpose is contained in the Data Provision Notice issued by NHS Digital to GP Practices. The Data Provision Notice includes appendices which explain data minimisation, additional protections, pseudonymisation and the data collection specification.

The GPDfPR is a daily extract of both Patient and appointment data provided by GP Clinical Systems.

It is recognised that some Suppliers may deliver appointment modules only and will not collect clinical data. These Suppliers will still be required to provide the GPDfPR appointments feed. These Suppliers should contact NHS Digital so that only the relevant requirements are applied and an appropriate assurance model is put in place. For detail contact gpdata@nhs.net.

# Requirements {#GPDataforPlanningandResearchv1.0.1-Requirements}

The below document details the overarching high level requirements that must be assured against to be compliant with the Standard. This covers the operational management, different file feeds, timing of submissions, configuration items and messaging.

[GP Data for Secondary Uses Supplier Requirements.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/11235426957/GP%20Data%20for%20Secondary%20Uses%20Supplier%20Requirements.docx?version=1&modificationDate=1620904565693&cacheVersion=1&api=v2)

# Compliance, Assurance and Testing {#GPDataforPlanningandResearchv1.0.1-Compliance,AssuranceandTesting}

The [GPDPR Solution Assurance Approach](https://nhse-dsic.atlassian.net/wiki/download/attachments/11235426957/GPDPR%20Solution%20Assurance%20Approach%201.0.docx?version=1&modificationDate=1634648069646&cacheVersion=1&api=v2) describes the compliance, assurance and testing that Suppliers must complete to achieve compliance with the GPDPR Standard.

# Documentation {#GPDataforPlanningandResearchv1.0.1-Documentation}

The below GPDfPR Technical Output Specification is intended to provide a comprehensive technical view of the provider submission

[GPDfPR Technical Output Specification](https://nhse-dsic.atlassian.net/wiki/download/attachments/11235426957/General%20Practice%20Data%20for%20Planning%20and%20Research%20Technical%20Output%20Specification%20v0.77_06052021.xlsx?version=1&modificationDate=1620904564881&cacheVersion=1&api=v2)

The data set tables include attribute (data item) level detail necessary to construct an output data set suitable for submission. The data set tables also include additional information explaining:

1. Which attributes are mandatory/optional
2. Attribute’s format and type
3. Linkages between the tables
4. What attributes must be de-id at source

This document is also included in the GPDfPR Direction as an Annex for information to the public. However, for the contractual purposes of meeting the GPDfPR Standard Suppliers should use the copy published above.

#### Implementation Guidance  {#GPDataforPlanningandResearchv1.0.1-ImplementationGuidance}

The below document provides technical guidance for Suppliers generating and populating the GP data extract message and counterpart organisations receiving and processing GP data extract messages.

[GP Data Extract Supplier Implementation Guidance](https://nhse-dsic.atlassian.net/wiki/download/attachments/11235426957/GP%20Data%20Extract%20Supplier%20Implementation%20Guidance.docx?version=1&modificationDate=1620904565486&cacheVersion=1&api=v2)

#### Interface Specification {#GPDataforPlanningandResearchv1.0.1-InterfaceSpecification}

This document defines the technical interface and contact between the GP data extraction Subsystem within source systems and the Landing Platform, the component of DPS responsible for receiving, validating and processing GP data extracts prior to utilisation.

[GPDfSU GP Data Interface Specification.docx](https://nhse-dsic.atlassian.net/wiki/download/attachments/11235426957/GPDfSU%20GP%20Data%20Interface%20Specification.docx?version=1&modificationDate=1620904565287&cacheVersion=1&api=v2)

#### Schema  {#GPDataforPlanningandResearchv1.0.1-Schema}

The below zip file contains the xml Schema, Schematron and sample Patient, appointment and acknowledgement xml files.

[GP Data Schema.zip](https://nhse-dsic.atlassian.net/wiki/download/attachments/11235426957/GP%20Data%20Schema.zip?version=1&modificationDate=1620904565083&cacheVersion=1&api=v2)

# Dependencies  {#GPDataforPlanningandResearchv1.0.1-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standards:

- Messaging Exchange for Social Care and Health (MESH) - May alternatively use AWS Direct S3-S3 transfers as the secure transport mechanism
- De-identification is performed via an NHS Digital supplied de-identification toolkit. This process yields ‘transit pseudonyms’ which render the de-identified fields suitable for transmission across the organisational boundary between source system and NHS Digital landing platform. The transit pseudonym provides an encrypted wrapper which ensures the de-identified field is not persisted or processed as clear text within the data store.

To maintain security further information about Privitar and de-identification will be provided on request, although an overview can be found in the interface specification.

# Roadmap {#GPDataforPlanningandResearchv1.0.1-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [General Practice Data for Planning and Research Technical Output Specification v0.77_06052021.xlsx](../../../../.raw/DCSDCS/attachments/11235426957/att11235426972-General Practice Data for Planning and Research Technical Output Specification v0.77_06052021.xlsx)
- [GP Data Schema.zip](../../../../.raw/DCSDCS/attachments/11235426957/att11235426975-GP Data Schema.zip)
- [GPDfSU GP Data Interface Specification.docx](../../../../.raw/DCSDCS/attachments/11235426957/att11235426978-GPDfSU GP Data Interface Specification.docx)
- [GP Data Extract Supplier Implementation Guidance.docx](../../../../.raw/DCSDCS/attachments/11235426957/att11235426981-GP Data Extract Supplier Implementation Guidance.docx)
- [GP Data for Secondary Uses Supplier Requirements.docx](../../../../.raw/DCSDCS/attachments/11235426957/att11235426984-GP Data for Secondary Uses Supplier Requirements.docx)
- [GPDPR Solution Assurance Approach 1.0.docx](../../../../.raw/DCSDCS/attachments/11235426957/att11725340715-GPDPR Solution Assurance Approach 1.0.docx)
