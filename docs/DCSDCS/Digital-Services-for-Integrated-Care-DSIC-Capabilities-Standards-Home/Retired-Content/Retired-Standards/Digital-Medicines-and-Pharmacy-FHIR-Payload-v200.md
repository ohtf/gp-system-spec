---
page_id: "12337315841"
space: "DCSDCS"
title: "Digital Medicines and Pharmacy FHIR Payload  v2.0.0"
version: 1
updated: "2023-04-12T13:15:20.605Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12337315841/Digital+Medicines+and+Pharmacy+FHIR+Payload+v2.0.0"
labels: ["interop_standard_retired"]
---

# Digital Medicines and Pharmacy FHIR Payload  v2.0.0

|  |  |
| --- | --- |
| ID | S77 |
| Version | 2.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Published Date | 08 Mar 2023 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

- [Introduction](#DigitalMedicinesandPharmacyFHIRPayloadv2.0.0-Introduction)
- [Requirements](#DigitalMedicinesandPharmacyFHIRPayloadv2.0.0-Requirements)
- [Compliance, Assurance and Testing](#DigitalMedicinesandPharmacyFHIRPayloadv2.0.0-Compliance,AssuranceandTesting)
  - [Summary of Recommendations](#DigitalMedicinesandPharmacyFHIRPayloadv2.0.0-SummaryofRecommendations)
- [Documentation](#DigitalMedicinesandPharmacyFHIRPayloadv2.0.0-Documentation)
- [Dependencies](#DigitalMedicinesandPharmacyFHIRPayloadv2.0.0-Dependencies)
- [Roadmap](#DigitalMedicinesandPharmacyFHIRPayloadv2.0.0-Roadmap)

# Introduction

The Digital Medicines initiative aims to positively transform the way that Patients manage their medicines, promote new models of care as well as improve the medicines supply chain and the provision of medicines data. At a high-level, this all involves the adoption of digital prescriptions to replace inefficient and cumbersome paper versions, utilising appropriate technologies to fully engage in the end-to-end Patient pathway, alongside supporting the adoption of technology to deliver a fully digitised medicines supply chain.

The Digital Medicines Specification utilises the Generic FHIR Receiver and supports the following care communications as part of its MVP:

- **Pharmacy Immunisation Administration** – A FHIR Document used to notify a Patient’s registered GP Practice on the administration of immunisations to a Patient at a Pharmacy.
- **Pharmacy Emergency Medication Supply** – A FHIR Document used to notify a Patient’s registered GP Practice of emergency medication(s) supplied to a Patient at a Pharmacy.

# Requirements

| ID | Requirement | Level |
| --- | --- | --- |
| **DMPF1** | **Pharmacy Immunisation Administration**  A FHIR Document used to notify a Patient’s registered GP Practice on the administration of immunisations to a Patient at a Pharmacy. | MUST |
| **DMPF2** | **Pharmacy Emergency Medication Supply**   A FHIR Document used to notify a Patient’s registered GP Practice of emergency medication(s) supplied to a Patient at a Pharmacy. | MUST |
| **DMPF3** | **Pharmacy Minor Illnesses**  A FHIR Document used to notify a Patient’s registered GP Practice of a minor illness consultation a Patient has received at a Pharmacy. | MUST |

# Compliance, Assurance and Testing

## Summary of Recommendations

The understanding that clinical risk and assurance responsibilities are formally acknowledged by system Suppliers and based on the knowledge that appropriate functional assurance will be performed by the NHS Digital Solutions Assurance team which is crucial to mitigating many of the clinical risks identified, the following clinical assurance approach is recommended:

**1. Clinical Safety**

All system Suppliers will be required to submit the required clinical safety documentation and sign off by their Clinical Safety Officer as per the NHS Digital Clinical Safety Group (CSG) requirements

**2**.**Test in Test**

A Digital Medicines clinician will, in the test environment via Webex, witness test the following scenarios to ensure the systems are behaving as expected from a clinical perspective. The scenarios covered will be:

a. The end to end process including the recording of a Patient consultation for a flu vaccination, where a vaccination has been administered and the subsequent transfer of that information to a GP Practice where it is acted upon.

b. The end to end process including the recording of a NUMSAS consultation for a Patient where a supply is made, the subsequent transfer of that information to a GP Practice where it is acted upon.

**3. Test in Live**

Using test Patients, a Digital Medicines clinician will, in the live environment via Webex or in person, witness test the following scenarios to ensure the systems are behaving as expected from a clinical perspective. The scenarios covered will be:

a. The end to end process including the recording of a Patient consultation for a flu vaccination, where a vaccination has been administered and the subsequent transfer of that information to a GP Practice where it is acted upon.

b. The end to end process including the recording of a NUMSAS consultation for a Patient where a supply is made, the subsequent transfer of that information to a GP Practice where it is acted upon.

The focus of the witness testing will be on the user workflow ensuring the positive and negative messages are prominent to the user and to provide a “sense check” of the PDF transformation of the message received by the GP system.

# Documentation

The latest version of Digital Medicines specifications can be accessed here: https://developer.nhs.uk/apis/digitalmedicines-1.2.5-private-beta/. (Reference links: https://developer.nhs.uk/apis/ and https://digital.nhs.uk/developer/api-catalogue/digital-medicine-fhir).

The first stage of the standard is now published and details the information that should be recorded for vaccinations administered and emergency medicines supplied by community pharmacists.

The MVP states that Suppliers are expected to process the unstructured messages upon entry to the framework in order to compliantly implement any use cases. However, there will be a future requirement for Suppliers to further enhance their Solutions to ensure the messages are processed in a structured format.

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- Generic FHIR Receiver

# Roadmap

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Ingestion of Pharmacy First Urgent Medicine Supply information from Community Pharmacies into GP Solutions](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14715125761/Ingestion+of+Pharmacy+First+Urgent+Medicine+Supply+information+from+Community+Pharmacies+into+GP+Solutions) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Digital Medicines and Pharmacy FHIR Payload](../../DSIC-Standards/Non-Overarching-Standards/Digital-Medicines-and-Pharmacy-FHIR-Payload.md), [Consultation Management - Community Pharmacy](../../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) | Published | 09 Oct 2026 | Render HTML and ingest structured Pharmacy First Urgent Medicine Supply information from Community Pharmacies into Patient Electronic Patient Records (EPRs) in GP Solutions | Uplift | Managed Capacity - Minor/Patch uplifts |