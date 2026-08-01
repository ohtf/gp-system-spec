---
page_id: "12488474777"
space: "DCSDCS"
title: "Booking and Referral Standard (BaRS)"
version: 19
updated: "2026-07-20T15:02:44.161Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12488474777/Booking+and+Referral+Standard+BaRS"
labels: ["standard"]
---

# Booking and Referral Standard (BaRS)

|  |  |
| --- | --- |
| **ID** | S93 |
| **Version** | 2.0.2 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 06 May 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#BookingandReferralStandard(BaRS)-Introduction)
- [Requirements](#BookingandReferralStandard(BaRS)-Requirements)
  - [Capability to BaRS Core/Application(s) mapping](#BookingandReferralStandard(BaRS)-CapabilitytoBaRSCore/Application(s)mapping)
- [Compliance, Assurance and Testing](#BookingandReferralStandard(BaRS)-Compliance,AssuranceandTesting)
- [Documentation](#BookingandReferralStandard(BaRS)-Documentation)
- [Dependencies](#BookingandReferralStandard(BaRS)-Dependencies)
- [Roadmap](#BookingandReferralStandard(BaRS)-Roadmap)

# Introduction {#BookingandReferralStandard(BaRS)-Introduction}

The NHS Booking and Referral Standard (BaRS) is a set of instructions, rules and guidance on how to use the building blocks of FHIR to digitise workflows. BaRS offers a universal standard way to digitise workflows that support all cross service Patient journeys in the NHS.

See [NHS Booking and Referral Standard](https://simplifier.net/guide/nhsbookingandreferralstandard) for further information.

# Requirements {#BookingandReferralStandard(BaRS)-Requirements}

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **ID** | **Requirement** | **Level** |
| All | BARS01 | Implement and maintain the [NHS Booking and Referral Standard](https://simplifier.net/guide/nhsbookingandreferralstandard) inline with the latest specification version and as per the Capability to BaRS Core/Application(s) mapping. | MUST |

## Capability to BaRS Core/Application(s) mapping {#BookingandReferralStandard(BaRS)-CapabilitytoBaRSCore/Application(s)mapping}

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Capability** | **Core - Booking Sender** | **Core - Booking Receiver** | **Core - Referral Sender** | **Core - Referral Receiver** | **Application(s) - Sender** | **Application(s) - Receiver** |
| [Referral Management - GP](../../DSIC-Capabilities/Referral-Management-GP.md) | (error) | (error) | (tick) | (error) | Referrals into Pharmacy | N/A |
| [Referral Management - Community Pharmacy](../../DSIC-Capabilities/Referral-Management-Community-Pharmacy.md) | (error) | (error) | (error) | (tick) | N/A | Referrals into Pharmacy |
| [Care Navigation](../../DSIC-Capabilities/Care-Navigation.md) | (error) | (error) | (tick) | (error) | Referrals into Pharmacy | N/A |

# Compliance, Assurance and Testing {#BookingandReferralStandard(BaRS)-Compliance,AssuranceandTesting}

See the Booking and Referral Standard (BaRS) section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation {#BookingandReferralStandard(BaRS)-Documentation}

- [BaRS Overview](https://digital.nhs.uk/services/booking-and-referral-standard)
- [BaRS Implementation Guide](https://simplifier.net/guide/nhsbookingandreferralstandard/home)
- [API Catalogue - BaRS](https://digital.nhs.uk/developer/api-catalogue/booking-and-referral-fhir)

# Dependencies {#BookingandReferralStandard(BaRS)-Dependencies}

BaRS provides a list of prerequisites in the [BaRS Principles and Prerequisites](https://simplifier.net/guide/nhsbookingandreferralstandard/Home/About-BaRS/BaRS-Principles-and-Prerequisites?version=1.6.0) section of the implementation guide.

There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents.

# Roadmap {#BookingandReferralStandard(BaRS)-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../.raw/DCSDCS/attachments/12488474777/att12488474790-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
- [e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml](../../../../.raw/DCSDCS/attachments/12488474777/att12488474793-e-Referrals Service (e-RS) v2.0.1 - Digital Care Services (DCS) Capabilities & Standards - Confluence.mhtml)
- [NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx](../../../../.raw/DCSDCS/attachments/12488474777/att12488474796-NHS e-Referrals Service - Referrer Compliance Document v1.1 (1).docx)
