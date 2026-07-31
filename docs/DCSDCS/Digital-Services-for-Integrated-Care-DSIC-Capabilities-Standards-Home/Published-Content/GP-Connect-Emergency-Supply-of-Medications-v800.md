---
page_id: "14715158529"
space: "DCSDCS"
title: "GP Connect Emergency Supply of Medications v8.0.0"
version: 2
updated: "2026-05-11T09:47:36.341Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14715158529/GP+Connect+Emergency+Supply+of+Medications+v8.0.0"
labels: ["standard"]
---

# GP Connect Emergency Supply of Medications v8.0.0

|  |  |
| --- | --- |
| **ID** | S77 |
| **Version** | 8.0.0 |
| **Type** | Standard |
| **Status** | Published |
| **Effective Date** | 09 Oct 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) |

/\*<![CDATA[\*/
div.rbtoc1785511518069 {padding: 0px;}
div.rbtoc1785511518069 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785511518069 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#GPConnectEmergencySupplyofMedicationsv8.0.0-Introduction)
- [Requirements](#GPConnectEmergencySupplyofMedicationsv8.0.0-Requirements)
  - [Data by Capability Mapping](#GPConnectEmergencySupplyofMedicationsv8.0.0-DatabyCapabilityMapping)
- [Compliance, Assurance and Testing](#GPConnectEmergencySupplyofMedicationsv8.0.0-Compliance,AssuranceandTesting)
- [Documentation](#GPConnectEmergencySupplyofMedicationsv8.0.0-Documentation)
- [Dependencies](#GPConnectEmergencySupplyofMedicationsv8.0.0-Dependencies)
- [Roadmap](#GPConnectEmergencySupplyofMedicationsv8.0.0-Roadmap)

# Introduction

The GP Connect Emergency Supply of Medications Standard, formerly part of the Digital Medicines (DigiMeds) specification, supports structured emergency medication information to be shared between Healthcare Organisations.

See [GP Connect - Emergency Supply of Medications (ITK3)](https://simplifier.net/guide/gp-connect-digimeds-emergency-supply-of-medicines/Home/Introduction/Introduction?version=1.3.0-public-beta) for further information.

# Requirements

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| Sender | GPCESM01 | Implement and maintain the [GP Connect - Emergency Supply of Medications (ITK3)](https://simplifier.net/guide/GP-Connect-DigiMeds-Emergency-Supply-of-Medicines/Home?version=1.3.0-public-beta) (formerly part of the Digital Medicines (DigiMeds) specification) inline with the latest specification version to send updates of emergency supplies of medication(s) for a Patient at a Community Pharmacy to their registered GP Practice, as per the Data by Capability Mapping section. | MUST |
| Receiver | GPCESM02 | Implement and maintain the [GP Connect - Emergency Supply of Medications (ITK3)](https://simplifier.net/guide/GP-Connect-DigiMeds-Emergency-Supply-of-Medicines/Home?version=1.3.0-public-beta) (formerly part of the Digital Medicines (DigiMeds) specification) inline with the latest specification version to receive updates of emergency supplies of medication(s) for a Patient at a Community Pharmacy. The HTML data will be rendered (e.g. as an HTML view or document), and structured information ingested as per the Data by Capability Mapping section as a minimum. | MUST |

## Data by Capability Mapping

| **Capability** | **Data Format** | **Allergies** | **Contact with Professionals** | **Consent (Legal Information)** | **GP Practice** | **History** | **Information and advice given** | **Medications and Medical devices** | **Patient Demographics** | **Plan and requested actions** | **Referral details** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Consultation Management - Community Pharmacy](../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) | HTML | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) |
| [Consultation Management - Community Pharmacy](../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) | Structured | (tick) | (tick) | (error) | (tick) | (error) | (error) | (tick) | (tick) | (error) | (error) |
| [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | HTML | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) | (tick) |
| [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) | Structured | (error) | (error) | (error) | (error) | (error) | (error) | (tick) | (error) | (error) | (error) |

# Compliance, Assurance and Testing

See the GP Connect Emergency Supply of Medications section on [Onboarding Overview of the Digital Services for Integrated Care (DSIC) Interoperability Standards and Requirements](../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

- [GP Connect - Emergency Supply of Medications (ITK3)](https://simplifier.net/guide/gp-connect-digimeds-emergency-supply-of-medicines/Home/Introduction/Introduction?version=1.3.0-public-beta)
- [Community Pharmacy Standard - PRSB](https://theprsb.org/standards/communitypharmacy/)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Generic FHIR Receiver](../DSIC-Standards/Non-Overarching-Standards/Generic-FHIR-Receiver.md)
- [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md)
- [Interoperability Toolkit (ITK)](../DSIC-Standards/Non-Overarching-Standards/Interoperability-Toolkit-ITK.md) - ITK3 Messaging Distribution

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Ingestion of Pharmacy First Urgent Medicine Supply information from Community Pharmacies into GP Solutions](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14715125761/Ingestion+of+Pharmacy+First+Urgent+Medicine+Supply+information+from+Community+Pharmacies+into+GP+Solutions) | [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Digital Medicines and Pharmacy FHIR Payload](../DSIC-Standards/Non-Overarching-Standards/Digital-Medicines-and-Pharmacy-FHIR-Payload.md), [Consultation Management - Community Pharmacy](../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) | Published | 09 Oct 2026 | Render HTML and ingest structured Pharmacy First Urgent Medicine Supply information from Community Pharmacies into Patient Electronic Patient Records (EPRs) in GP Solutions | Uplift | Managed Capacity - Minor/Patch uplifts |

## Attachments

- [NHS England Digimeds Specification for Vaccination Event Data Flow Version 1.0 APPROVED.docx](../../../.raw/DCSDCS/attachments/14715158529/att14715158547-NHS England Digimeds Specification for Vaccination Event Data Flow Version 1.0 APPROVED.docx)
