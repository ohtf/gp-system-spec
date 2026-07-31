---
page_id: "15212576769"
space: "DCSDCS"
title: "Vaccination Extract v2.0.0"
version: 1
updated: "2026-06-30T07:09:49.570Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/15212576769/Vaccination+Extract+v2.0.0"
labels: ["standard_retired"]
---

# Vaccination Extract v2.0.0

|  |  |
| --- | --- |
| **ID** | S116 |
| **Version** | 2.0.0 |
| **Type** | Standard |
| **Status** | Retired |
| **Effective Date** | 05 Jan 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

/\*<![CDATA[\*/
div.rbtoc1785511639634 {padding: 0px;}
div.rbtoc1785511639634 ul {list-style: none;margin-left: 0px;}
div.rbtoc1785511639634 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#VaccinationExtractv2.0.0-Introduction)
- [Requirements](#VaccinationExtractv2.0.0-Requirements)
- [Supported Vaccines](#VaccinationExtractv2.0.0-SupportedVaccines)
- [Compliance, Assurance and Testing](#VaccinationExtractv2.0.0-Compliance,AssuranceandTesting)
- [Documentation](#VaccinationExtractv2.0.0-Documentation)
- [Dependencies](#VaccinationExtractv2.0.0-Dependencies)
  - [NHSE Daily Vaccination Events (In-bound) Extract](#VaccinationExtractv2.0.0-NHSEDailyVaccinationEvents(In-bound)Extract)
- [Roadmap](#VaccinationExtractv2.0.0-Roadmap)

# Introduction

The Vaccination Extract Standard specifies the flow of vaccination-related information from healthcare settings to the Authority.

# Requirements

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| Suppliers of Solutions which ARE currently deployed into an operational environment, and have implemented NHSE Daily Vaccination Events (In-Bound) Extract*.* | VE01 | Implement and maintain the extraction of vaccination information inline with the latest NHSE Daily Vaccination Events (In-Bound) Extract specification version, and send vaccination event data for vaccines included in the Supported Vaccines list on a daily basis, via the IMMS-API MESH Mailbox. | MUST |
| - Suppliers of new Solutions (i.e. those which are NOT currently deployed into an operational environment with existing NHSE Daily Vaccination Events (In-Bound) Extract compliance. - Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented the Immunisation FHIR API. | VE02 | Implement and maintain the Immunisation FHIR API inline with the latest specification version and send vaccination event data at the time of recording for vaccines included in the Supported Vaccines list. | MUST |

# Supported Vaccines

The following list outlines the vaccines for which vaccination event data is to be sent to the Authority:

- COVID-19
- Human Papillomavirus (HPV)
- Influenza (Flu)
- Measles, Mumps, Rubella (MMR)
- Measles, Mumps, Rubella and Varicella (MMRV)
- MenACWY
- Pertussis
- Pneumococcal
- Respiratory Syncytial Virus (RSV)
- Shingles
- 3 in 1

# Compliance, Assurance and Testing

For the Immunisation FHIR API, see the Vaccination Extract section on Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements.

For NHSE Daily Vaccination Events (In-Bound) Extract, Onboarding and Assurance information can be found here.

# Documentation

- Immunisation FHIR API
- NHSE Daily Vaccination Events (In-Bound) Extract

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

### NHSE Daily Vaccination Events (In-bound) Extract

For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented NHSE Daily Vaccination Events (In-bound) Extract:

- Messaging Exchange for Social Care and Health (MESH)

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Title | **Change Route** | **Change Type** | **Contracting Vehicle(s)** | **Date Added** | **Description** | **Effective Date** | **ID** | **Incentive / Funding Dates** | **Incentives / Funding** | **Publication Date** | **Standards and Capabilities** | **Status** | **Title** | **Type** | **Version** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Vaccinations data capture](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15219523600/Vaccinations+data+capture) | Managed Capacity - Other | Uplift | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) | 01 Jul 2026 | Mandatory data for vaccines to be recorded and available for extract from Electronic Patient Records (EPRs) | TBC | RM309 | N/A | No | TBC | [Prescribing](../../DSIC-Capabilities/Prescribing.md), [Vaccination Extract](../../DSIC-Standards/Non-Overarching-Standards/Vaccination-Extract.md) | Draft | Vaccinations data capture | Roadmap Item | 1.0.0 |

## Attachments

- [image-20250430-083744.png](../../../../.raw/DCSDCS/attachments/15212576769/att15212576785-image-20250430-083744.png)
