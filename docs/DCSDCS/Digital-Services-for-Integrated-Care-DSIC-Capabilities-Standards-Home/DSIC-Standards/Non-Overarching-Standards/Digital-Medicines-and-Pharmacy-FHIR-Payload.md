---
page_id: "10752983078"
space: "DCSDCS"
title: "Digital Medicines and Pharmacy FHIR Payload"
version: 21
updated: "2026-07-21T14:23:30.514Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/10752983078/Digital+Medicines+and+Pharmacy+FHIR+Payload"
labels: ["standard"]
---

# Digital Medicines and Pharmacy FHIR Payload

|  |  |
| --- | --- |
| **ID** | S77 |
| **Version** | 7.0.0 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 30 Jun 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

/\*<![CDATA[\*/
div.rbtoc1785509308056 {padding: 0px;}
div.rbtoc1785509308056 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785509308056 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#DigitalMedicinesandPharmacyFHIRPayload-Introduction)
- [Requirements](#DigitalMedicinesandPharmacyFHIRPayload-Requirements)
- [Compliance, Assurance and Testing](#DigitalMedicinesandPharmacyFHIRPayload-Compliance,AssuranceandTesting)
- [Documentation](#DigitalMedicinesandPharmacyFHIRPayload-Documentation)
- [Dependencies](#DigitalMedicinesandPharmacyFHIRPayload-Dependencies)
- [Roadmap](#DigitalMedicinesandPharmacyFHIRPayload-Roadmap)

# Introduction

The Digital Medicines initiative aims to positively transform the way that Patients manage their medicines, promote new models of care as well as improve the medicines supply chain and the provision of medicines data. At a high-level, this all involves the adoption of digital Prescriptions to replace inefficient and cumbersome paper versions, utilising appropriate technologies to fully engage in the end-to-end Patient pathway, alongside supporting the adoption of technology to deliver a fully digitised medicines supply chain.

The Digital Medicines Specification utilises the [Generic FHIR Receiver](Generic-FHIR-Receiver.md) for receiving Solutions and supports the following requirements as part of its MVP.

# Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| GP Suppliers | DMPF1 | **Vaccination Administration**  Implement and maintain the vaccination [Digital Medicines and Pharmacy FHIR Payload](https://nhse-dsic.atlassian.net/wiki/download/attachments/10752983078/NHS%20England%20Digimeds%20Specification%20for%20Vaccination%20Event%20Data%20Flow%20Version%201.0%20APPROVED.docx?api=v2) inline with the latest specification version to receive notifications of the administration of vaccinations to a Patient at another Health or Care Organisation.  The following vaccinations to be supported:   - BCG - COVID-19 - Hep B - Hib/MenC - Human Papillomavirus (HPV) - Influenza (Flu) - Measles, Mumps, Rubella (MMR) - Measles, Mumps, Rubella, and Varicella (MMRV) - MenACWY - MenB - Pertussis - Pneumococcal - Respiratory Syncytial Virus (RSV) - Rotavirus - Shingles - 3 in 1 - 4 in 1 - 6 in 1 | MUST |
| GP Suppliers | DMPF2 | **GP Connect - Emergency Supply of Medications (ITK3)** - Receiver Implement and maintain the [GP Connect - Emergency Supply of Medications (ITK3) Payload](https://simplifier.net/guide/GP-Connect-DigiMeds-Emergency-Supply-of-Medicines/Home?version=1.3.0-public-beta) (formerly part of the Digital Medicines (DigiMeds) specification) inline with the latest specification version to receive notifications of emergency medication(s) supplied to a Patient at a Pharmacy. | MUST |
| Community Pharmacy Suppliers | DMPF3 | **GP Connect - Emergency Supply of Medications (ITK3)** - Sender Implement and maintain the [GP Connect - Emergency Supply of Medications (ITK3) Payload](https://simplifier.net/guide/GP-Connect-DigiMeds-Emergency-Supply-of-Medicines/Home?version=1.3.0-public-beta) (formerly part of the Digital Medicines (DigiMeds) specification) inline with the latest specification version to send notifications of emergency medication(s) supplied to a Patient at a Pharmacy to their registered GP Practice. | MUST |

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

- [Digital Medicine - FHIR](https://digital.nhs.uk/developer/api-catalogue/digital-medicine-fhir)
- [API and Integration Catalogue](https://digital.nhs.uk/developer/api-catalogue)
- [API Catalogue - Digital Medicine - FHIR](https://digital.nhs.uk/developer/api-catalogue/digital-medicine-fhir)
- [PRSB - Pharmacy information flows](https://theprsb.org/standards/pharmacyinformationflows/)

# Dependencies

Creating a compliant implementation requires GP Suppliers to implement the following dependent interface Standards:

- [Generic FHIR Receiver](Generic-FHIR-Receiver.md) - receiver Solutions

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Ingestion of Pharmacy First Urgent Medicine Supply information from Community Pharmacies into GP Solutions](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14715125761/Ingestion+of+Pharmacy+First+Urgent+Medicine+Supply+information+from+Community+Pharmacies+into+GP+Solutions) | [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Digital Medicines and Pharmacy FHIR Payload](Digital-Medicines-and-Pharmacy-FHIR-Payload.md), [Consultation Management - Community Pharmacy](../../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) | Published | 09 Oct 2026 | Render HTML and ingest structured Pharmacy First Urgent Medicine Supply information from Community Pharmacies into Patient Electronic Patient Records (EPRs) in GP Solutions | Uplift | Managed Capacity - Minor/Patch uplifts |

## Attachments

- [NHS England Digimeds Specification for Vaccination Event Data Flow Version 1.0 APPROVED.docx](../../../../.raw/DCSDCS/attachments/10752983078/att13394149388-NHS England Digimeds Specification for Vaccination Event Data Flow Version 1.0 APPROVED.docx)
