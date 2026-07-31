---
page_id: "14715125791"
space: "DCSDCS"
title: "Vaccination Administration (DigiMeds) v1.0.0"
version: 2
updated: "2026-05-11T09:49:04.295Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14715125791/Vaccination+Administration+DigiMeds+v1.0.0"
labels: ["standard"]
---

# Vaccination Administration (DigiMeds) v1.0.0

|  |  |
| --- | --- |
| **ID** | S123 |
| **Version** | 1.0.0 |
| **Type** | Standard |
| **Status** | Published |
| **Effective Date** | 09 Oct 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

- [Introduction](#VaccinationAdministration(DigiMeds)v1.0.0-Introduction)
- [Requirements](#VaccinationAdministration(DigiMeds)v1.0.0-Requirements)
- [Compliance, Assurance and Testing](#VaccinationAdministration(DigiMeds)v1.0.0-Compliance,AssuranceandTesting)
- [Dependencies](#VaccinationAdministration(DigiMeds)v1.0.0-Dependencies)
- [Roadmap](#VaccinationAdministration(DigiMeds)v1.0.0-Roadmap)

# Introduction

The Vaccinations Administration (DigiMeds) Standard supports updates to a Patient’s registered GP Practice about vaccinations administered at another Health or Care Organisation.

# Requirements

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| GP Suppliers | DMPF01 | Implement and maintain the [DigiMeds specification for Vaccination Event Data Flow](https://nhse-dsic.atlassian.net/wiki/download/attachments/10752983078/NHS%20England%20Digimeds%20Specification%20for%20Vaccination%20Event%20Data%20Flow%20Version%201.0%20APPROVED.docx?api=v2) inline with the latest specification version to receive updates of the administration of vaccinations to a Patient at another Health or Care Organisation.  The following vaccinations to be supported:   - BCG - COVID-19 - Hep B - Hib/MenC - Human Papillomavirus (HPV) - Influenza (Flu) - Measles, Mumps, Rubella (MMR) - Measles, Mumps, Rubella, and Varicella (MMRV) - MenACWY - MenB - Pertussis - Pneumococcal - Respiratory Syncytial Virus (RSV) - Rotavirus - Shingles - 3 in 1 - 4 in 1 - 6 in 1 | MUST |

# Compliance, Assurance and Testing

See the Vaccinations Administration (DigiMeds) section on [Onboarding Overview of the Digital Services for Integrated Care (DSIC) Interoperability Standards and Requirements](../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Generic FHIR Receiver](../DSIC-Standards/Non-Overarching-Standards/Generic-FHIR-Receiver.md)
- [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md)

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Record Vaccination Events for GP Payments](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15219523585/Record+Vaccination+Events+for+GP+Payments) | [Vaccination Administration Service (DigiMeds)](Vaccination-Administration-DigiMeds-v100.md) | Draft | TBC | Ensure that vaccination events are automatically attributed to the Patient’s registered GP Practice. | Uplift | Managed Capacity - Other |