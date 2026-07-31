---
page_id: "14127628289"
space: "DCSDCS"
title: "Vaccination Extract"
version: 6
updated: "2026-07-22T13:15:58.641Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14127628289/Vaccination+Extract"
labels: ["standard"]
---

# Vaccination Extract

|  |  |
| --- | --- |
| **ID** | S116 |
| **Version** | 3.0.0 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 30 Jun 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

/\*<![CDATA[\*/
div.rbtoc1785510974323 {padding: 0px;}
div.rbtoc1785510974323 ul {list-style: none;margin-left: 0px;}
div.rbtoc1785510974323 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#VaccinationExtract-Introduction)
- [Requirements](#VaccinationExtract-Requirements)
- [Supported Vaccines](#VaccinationExtract-SupportedVaccines)
- [Compliance, Assurance and Testing](#VaccinationExtract-Compliance,AssuranceandTesting)
- [Documentation](#VaccinationExtract-Documentation)
- [Dependencies](#VaccinationExtract-Dependencies)
  - [NHSE Daily Vaccination Events (In-bound) Extract](#VaccinationExtract-NHSEDailyVaccinationEvents(In-bound)Extract)
- [Roadmap](#VaccinationExtract-Roadmap)

# Introduction

The Vaccination Extract Standard specifies the flow of vaccination-related information from healthcare settings to the Authority.

# Requirements

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| Suppliers of Solutions which ARE currently deployed into an operational environment, and have implemented NHSE Daily Vaccination Events (In-Bound) Extract*.* | VE01 | Implement and maintain the extraction of vaccination information inline with the latest [NHSE Daily Vaccination Events (In-Bound) Extract](https://digital.nhs.uk/developer/api-catalogue/vaccination) specification version, and send vaccination event data for vaccines included in the [Supported Vaccines](Vaccination-Extract.md) list on a daily basis, via the IMMS-API MESH Mailbox. | MUST |
| - Suppliers of new Solutions (i.e. those which are NOT currently deployed into an operational environment with existing NHSE Daily Vaccination Events (In-Bound) Extract compliance. - Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented the Immunisation FHIR API. | VE02 | Implement and maintain the [Immunisation FHIR API](https://digital.nhs.uk/developer/api-catalogue/immunisation-fhir-api)inline with the latest specification version and send vaccination event data at the time of recording for vaccines included in the [Supported Vaccines](Vaccination-Extract.md) list. | MUST |

# Supported Vaccines

The following list outlines the vaccines for which vaccination event data is to be sent to the Authority:

- BCG
- COVID-19
- Hep B
- Hib/MenC
- Human Papillomavirus (HPV)
- Influenza (Flu)
- Measles, Mumps, Rubella (MMR)
- Measles, Mumps, Rubella, and Varicella (MMRV)
- MenACWY
- MenB
- Pertussis
- Pneumococcal
- Respiratory Syncytial Virus (RSV)
- Rotavirus
- Shingles
- 3 in 1
- 4 in 1
- 6 in 1

# Compliance, Assurance and Testing

For the Immunisation FHIR API, see the Vaccination Extract section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

For NHSE Daily Vaccination Events (In-Bound) Extract, Onboarding and Assurance information can be found [here](https://digital.nhs.uk/developer/api-catalogue/vaccination#onboarding).

# Documentation

- [Immunisation FHIR API](https://digital.nhs.uk/developer/api-catalogue/immunisation-fhir-api)
- [NHSE Daily Vaccination Events (In-Bound) Extract](https://digital.nhs.uk/developer/api-catalogue/vaccination)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

### NHSE Daily Vaccination Events (In-bound) Extract

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented NHSE Daily Vaccination Events (In-bound) Extract:

- [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md)

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Title | **Change Route** | **Change Type** | **Contracting Vehicle(s)** | **Date Added** | **Description** | **Effective Date** | **ID** | **Incentive / Funding Dates** | **Incentives / Funding** | **Publication Date** | **Standards and Capabilities** | **Status** | **Title** | **Type** | **Version** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Vaccinations data capture](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15219523600/Vaccinations+data+capture) | Managed Capacity - Other | Uplift | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) | 01 Jul 2026 | Mandatory data for vaccines to be recorded and available for extract from Electronic Patient Records (EPRs) | TBC | RM309 | N/A | No | TBC | [Prescribing](../../DSIC-Capabilities/Prescribing.md), [Vaccination Extract](Vaccination-Extract.md) | Draft | Vaccinations data capture | Roadmap Item | 1.0.0 |

## Attachments

- [image-20250430-083744.png](../../../../.raw/DCSDCS/attachments/14127628289/att14127628301-image-20250430-083744.png)
