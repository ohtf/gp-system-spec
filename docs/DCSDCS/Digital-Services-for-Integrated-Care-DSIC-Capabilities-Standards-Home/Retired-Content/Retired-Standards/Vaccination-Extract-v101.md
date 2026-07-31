---
page_id: "14611054594"
space: "DCSDCS"
title: "Vaccination Extract v1.0.1"
version: 1
updated: "2026-01-05T11:12:50.137Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14611054594/Vaccination+Extract+v1.0.1"
labels: ["standard_retired"]
---

# Vaccination Extract v1.0.1

|  |  |
| --- | --- |
| **ID** | S116 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Retired |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

/\*<![CDATA[\*/
div.rbtoc1785511496704 {padding: 0px;}
div.rbtoc1785511496704 ul {list-style: none;margin-left: 0px;}
div.rbtoc1785511496704 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#VaccinationExtractv1.0.1-Introduction)
- [Requirements](#VaccinationExtractv1.0.1-Requirements)
  - [Vaccination Extract MESH Mailbox Configuration](#VaccinationExtractv1.0.1-VaccinationExtractMESHMailboxConfiguration)
- [Compliance, Assurance and Testing](#VaccinationExtractv1.0.1-Compliance,AssuranceandTesting)
- [Documentation](#VaccinationExtractv1.0.1-Documentation)
- [Dependencies](#VaccinationExtractv1.0.1-Dependencies)
- [Roadmap](#VaccinationExtractv1.0.1-Roadmap)

# Introduction

The Vaccination Extract Standard specifies the flow of vaccination-related information from healthcare settings to the Authority.

# Requirements

| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| GP Suppliers | VE01 | Implement and maintain the extraction of vaccination information inline with the latest NHSE Daily Vaccination Events (In-Bound) Extract specification version.  The following vaccination extracts to be supported on a daily basis:   - Influenza (Flu) - Respiratory Syncytial Virus (RSV) - Human Papillomavirus (HPV) - 3 in 1 - MenACWY   The following vaccination extracts to be supported on a daily or weekly basis:   - Measles, Mumps, Rubella (MMR) Vaccination data to be provided for Patients from 1 to 25 years old | MUST |

## Vaccination Extract MESH Mailbox Configuration

The table below outlines the MESH mailbox used for each vaccination.

| **MESH Mailbox** | **Message** |
| --- | --- |
| Data Processing Services (DPS) MESH mailbox | - Influenza (Flu) |
| Immunisation MESH mailbox | - Respiratory Syncytial Virus (RSV) - Measles, Mumps, Rubella (MMR) - Human Papillomavirus (HPV) - 3 in 1 - MenACWY |

# Compliance, Assurance and Testing

See the Vaccination Extract section on Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements.

# Documentation

- API Catalogue - Vaccination

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Messaging Exchange for Social Care and Health (MESH)](../../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md)

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Title | **Change Route** | **Change Type** | **Contracting Vehicle(s)** | **Date Added** | **Description** | **Effective Date** | **ID** | **Incentive / Funding Dates** | **Incentives / Funding** | **Publication Date** | **Standards and Capabilities** | **Status** | **Title** | **Type** | **Version** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Vaccinations data capture](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15219523600/Vaccinations+data+capture) | Managed Capacity - Other | Uplift | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) | 01 Jul 2026 | Mandatory data for vaccines to be recorded and available for extract from Electronic Patient Records (EPRs) | TBC | RM309 | N/A | No | TBC | [Prescribing](../../DSIC-Capabilities/Prescribing.md), [Vaccination Extract](../../DSIC-Standards/Non-Overarching-Standards/Vaccination-Extract.md) | Draft | Vaccinations data capture | Roadmap Item | 1.0.0 |

## Attachments

- [image-20250430-083744.png](../../../../.raw/DCSDCS/attachments/14611054594/att14611054606-image-20250430-083744.png)
