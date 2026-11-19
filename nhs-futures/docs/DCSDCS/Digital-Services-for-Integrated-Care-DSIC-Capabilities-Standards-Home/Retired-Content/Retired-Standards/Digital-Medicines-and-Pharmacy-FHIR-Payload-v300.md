---
page_id: "14325416012"
space: "DCSDCS"
title: "Digital Medicines and Pharmacy FHIR Payload v3.0.0"
version: 2
updated: "2025-09-01T15:09:32.310Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14325416012/Digital+Medicines+and+Pharmacy+FHIR+Payload+v3.0.0"
labels: ["standard_retired"]
---

# Digital Medicines and Pharmacy FHIR Payload v3.0.0

|  |  |
| --- | --- |
| ID {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-ID} | S77 |
| Version {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Version} | 3.0.0 |
| Type {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Type} | Standard |
| Status {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Status} | Retired |
| Effective Date {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-EffectiveDate} | 18 Oct 2024 |
| Contracting Vehicle(s) {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-ContractingVehicle(s)} | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

- [Introduction](#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Introduction)
- [Requirements](#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Requirements)
- [Compliance, Assurance and Testing](#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Compliance,AssuranceandTesting)
- [Documentation](#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Documentation)
- [Dependencies](#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Dependencies)
- [Roadmap](#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Roadmap)

# Introduction {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Introduction}

The Digital Medicines initiative aims to positively transform the way that Patients manage their medicines, promote new models of care as well as improve the medicines supply chain and the provision of medicines data. At a high-level, this all involves the adoption of digital Prescriptions to replace inefficient and cumbersome paper versions, utilising appropriate technologies to fully engage in the end-to-end Patient pathway, alongside supporting the adoption of technology to deliver a fully digitised medicines supply chain.

The Digital Medicines Specification utilises the Generic FHIR Receiver and supports the following requirements as part of its MVP.

# Requirements {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Requirements}

|  |  |  |
| --- | --- | --- |
| ID {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-ID.1} | Requirement {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Requirement} | Level {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Level} |
| DMPF1 {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-DMPF1} | **Vaccination Administration**  Implement and maintain the vaccination Digital Medicines and Pharmacy FHIR Payload inline with the latest specification version to receive notifications of the administration of vaccinations to a Patient at another Health or Care Organisation.  The following vaccinations to be supported:   - COVID-19 - Influenza - Pertussis - Respiratory Syncytial Virus (RSV) | MUST |
| DMPF2 {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-DMPF2} | **Pharmacy Emergency Medication Supply**  {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-PharmacyEmergencyMedicationSupply} Implement and maintain the Pharmacy Emergency Medication Supply Digital Medicines and Pharmacy FHIR Payload inline with the latest specification version to receive notifications of emergency medication(s) supplied to a Patient at a Pharmacy. | MUST |

# Compliance, Assurance and Testing {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Compliance,AssuranceandTesting}

The understanding that clinical risk and assurance responsibilities are formally acknowledged by System Suppliers and based on the knowledge that appropriate functional assurance will be performed by the Solutions Assurance team which is crucial to mitigating many of the clinical risks identified, the following clinical assurance approach is recommended:

1. **Clinical Safety** - All System Suppliers will be required to submit the required clinical safety documentation and sign off by their Clinical Safety Officer as per the Authority Clinical Safety Group (CSG) requirements.

2. **Test in Test** - A Digital Medicines clinician will, in the test environment via Webex, witness test the following scenarios to ensure the Systems are behaving as expected from a clinical perspective. The scenarios covered will be:

   1. The end to end process including the recording of a Patient consultation for a flu vaccination, where a vaccination has been administered and the subsequent transfer of that information to a GP Practice where it is acted upon.
   2. The end to end process including the recording of a NHS Urgent Medicines Supply Advanced Service (NUMSAS) consultation for a Patient where a supply is made, the subsequent transfer of that information to a GP Practice where it is acted upon.
3. **Test in Live** - Using test Patients, a Digital Medicines clinician will, in the live environment via Webex or in person, witness test the following scenarios to ensure the Systems are behaving as expected from a clinical perspective. The scenarios covered will be:

   1. The end to end process including the recording of a Patient consultation for a flu vaccination, where a vaccination has been administered and the subsequent transfer of that information to a GP Practice where it is acted upon.
   2. The end to end process including the recording of a NHS Urgent Medicines Supply Advanced Service (NUMSAS) consultation for a Patient where a supply is made, the subsequent transfer of that information to a GP Practice where it is acted upon.

The focus of the witness testing will be on the user workflow ensuring the positive and negative messages are prominent to the user and to provide a “sense check” of the PDF transformation of the message received by the GP System.

# Documentation {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Documentation}

- Digital Medicine - FHIR
- API and Integration Catalogue
- API Catalogue - Digital Medicine - FHIR
- PRSB - Pharmacy information flows

# Dependencies {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standards:

- Generic FHIR Receiver

# Roadmap {#DigitalMedicinesandPharmacyFHIRPayloadv3.0.0-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Ingestion of Pharmacy First Urgent Medicine Supply information from Community Pharmacies into GP Solutions](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14715125761/Ingestion+of+Pharmacy+First+Urgent+Medicine+Supply+information+from+Community+Pharmacies+into+GP+Solutions) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Digital Medicines and Pharmacy FHIR Payload](../../DSIC-Standards/Non-Overarching-Standards/Digital-Medicines-and-Pharmacy-FHIR-Payload.md), [Consultation Management - Community Pharmacy](../../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) | Published | 09 Oct 2026 | Render HTML and ingest structured Pharmacy First Urgent Medicine Supply information from Community Pharmacies into Patient Electronic Patient Records (EPRs) in GP Solutions | Uplift | Managed Capacity - Minor/Patch uplifts |

## Attachments

- [NHS England Digimeds Specification for Vaccination Event Data Flow Version 1.0 APPROVED.docx](../../../../attachments/DCSDCS/14325416012/att14325416027-NHS England Digimeds Specification for Vaccination Event Data Flow Version 1.0 APPROVED.docx)
