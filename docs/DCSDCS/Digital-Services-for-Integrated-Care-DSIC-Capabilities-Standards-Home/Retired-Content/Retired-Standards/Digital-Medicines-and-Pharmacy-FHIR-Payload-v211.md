---
page_id: "13392871425"
space: "DCSDCS"
title: "Digital Medicines and Pharmacy FHIR Payload v2.1.1"
version: 1
updated: "2024-10-18T09:24:10.761Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/13392871425/Digital+Medicines+and+Pharmacy+FHIR+Payload+v2.1.1"
labels: ["standard_retired"]
---

# Digital Medicines and Pharmacy FHIR Payload v2.1.1

|  |  |
| --- | --- |
| ID | S77 |
| Version | 2.1.1 |
| Type | Standard |
| Status | Retired |
| Effective Date | 22 Jul 2024 |
| Contracting Vehicle(s) | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

- [Introduction](#DigitalMedicinesandPharmacyFHIRPayloadv2.1.1-Introduction)
- [Requirements](#DigitalMedicinesandPharmacyFHIRPayloadv2.1.1-Requirements)
- [Compliance, Assurance and Testing](#DigitalMedicinesandPharmacyFHIRPayloadv2.1.1-Compliance,AssuranceandTesting)
- [Documentation](#DigitalMedicinesandPharmacyFHIRPayloadv2.1.1-Documentation)
- [Dependencies](#DigitalMedicinesandPharmacyFHIRPayloadv2.1.1-Dependencies)
- [Roadmap](#DigitalMedicinesandPharmacyFHIRPayloadv2.1.1-Roadmap)

# Introduction

The Digital Medicines initiative aims to positively transform the way that Patients manage their medicines, promote new models of care as well as improve the medicines supply chain and the provision of medicines data. At a high-level, this all involves the adoption of digital prescriptions to replace inefficient and cumbersome paper versions, utilising appropriate technologies to fully engage in the end-to-end Patient pathway, alongside supporting the adoption of technology to deliver a fully digitised medicines supply chain.

The Digital Medicines Specification utilises the Generic FHIR Receiver and supports the following requirements as part of its MVP.

# Requirements

| ID | Requirement | Level |
| --- | --- | --- |
| DMPF1 | **Pharmacy Immunisation Administration**  A FHIR Document used to notify a Patient’s registered GP Practice on the administration of immunisations to a Patient at a Pharmacy. | MUST |
| DMPF2 | **Pharmacy Emergency Medication Supply**  A FHIR Document used to notify a Patient’s registered GP Practice of emergency medication(s) supplied to a Patient at a Pharmacy. | MUST |

# Compliance, Assurance and Testing

The understanding that clinical risk and assurance responsibilities are formally acknowledged by System Suppliers and based on the knowledge that appropriate functional assurance will be performed by the Solutions Assurance team which is crucial to mitigating many of the clinical risks identified, the following clinical assurance approach is recommended:

1. **Clinical Safety** - All System Suppliers will be required to submit the required clinical safety documentation and sign off by their Clinical Safety Officer as per the Authority Clinical Safety Group (CSG) requirements.

2. **Test in Test** - A Digital Medicines clinician will, in the test environment via Webex, witness test the following scenarios to ensure the Systems are behaving as expected from a clinical perspective. The scenarios covered will be:

   1. The end to end process including the recording of a Patient consultation for a flu vaccination, where a vaccination has been administered and the subsequent transfer of that information to a GP Practice where it is acted upon.
   2. The end to end process including the recording of a NHS Urgent Medicines Supply Advanced Service (NUMSAS) consultation for a Patient where a supply is made, the subsequent transfer of that information to a GP Practice where it is acted upon.
3. **Test in Live** - Using test Patients, a Digital Medicines clinician will, in the live environment via Webex or in person, witness test the following scenarios to ensure the Systems are behaving as expected from a clinical perspective. The scenarios covered will be:

   1. The end to end process including the recording of a Patient consultation for a flu vaccination, where a vaccination has been administered and the subsequent transfer of that information to a GP Practice where it is acted upon.
   2. The end to end process including the recording of a NHS Urgent Medicines Supply Advanced Service (NUMSAS) consultation for a Patient where a supply is made, the subsequent transfer of that information to a GP Practice where it is acted upon.

The focus of the witness testing will be on the user workflow ensuring the positive and negative messages are prominent to the user and to provide a “sense check” of the PDF transformation of the message received by the GP System.

# Documentation

- The latest version of Digital Medicines specifications can be accessed here: Digital Medicine - FHIR (reference links: API and Integration Catalogue).
- The first stage of the Standard is now published and details the information that should be recorded for vaccinations administered and emergency medicines supplied by Community Pharmacists.
- The MVP states that Suppliers are expected to process the unstructured messages upon entry to the Contracting Vehicle in order to compliantly implement any use cases. However, there will be a future requirement for Suppliers to further enhance their Solutions to ensure the messages are processed in a structured format.

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- Generic FHIR Receiver

# Roadmap

| **Items on the Roadmap which impact or relate to this Standard** |
| --- |
| | Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route | | --- | --- | --- | --- | --- | --- | --- | | [Ingestion of Pharmacy First Urgent Medicine Supply information from Community Pharmacies into GP Solutions](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14715125761/Ingestion+of+Pharmacy+First+Urgent+Medicine+Supply+information+from+Community+Pharmacies+into+GP+Solutions) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Digital Medicines and Pharmacy FHIR Payload](../../DSIC-Standards/Non-Overarching-Standards/Digital-Medicines-and-Pharmacy-FHIR-Payload.md), [Consultation Management - Community Pharmacy](../../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) | Published | 09 Oct 2026 | Render HTML and ingest structured Pharmacy First Urgent Medicine Supply information from Community Pharmacies into Patient Electronic Patient Records (EPRs) in GP Solutions | Uplift | Managed Capacity - Minor/Patch uplifts | |