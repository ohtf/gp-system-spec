---
page_id: "1391133525"
space: "DCSDCS"
title: "Spine Mini Services"
version: 20
updated: "2026-07-22T13:14:23.051Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133525/Spine+Mini+Services"
labels: ["standard"]
---

# Spine Mini Services

|  |  |
| --- | --- |
| **ID** | S66 |
| **Version** | 1.0.0 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 01 Apr 2019 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#SpineMiniServices-Introduction)
- [Requirements](#SpineMiniServices-Requirements)
- [Compliance, Assurance and Testing](#SpineMiniServices-Compliance,AssuranceandTesting)
- [Documentation](#SpineMiniServices-Documentation)
- [Dependencies](#SpineMiniServices-Dependencies)
- [Roadmap](#SpineMiniServices-Roadmap)

# Introduction

Spine Mini Services is a simplified read-only interface to some Spine Services, the most common one being [Personal Demographics Service (PDS)](Personal-Demographics-Service-PDS.md).

The Spine Mini Service Provider (SMSP) provides a security bridge to the Spine services and lower entry messaging specification which removes some of the complexity of the HL7 V3 interfaces e.g. It allows consumers to query information on Patients without having to develop the full PDS interface or go through the full Common Assurance Process.

It is also a mechanism to retrieve information on:

- [Child Protection Information Sharing (CPIS)](https://digital.nhs.uk/services/child-protection-information-sharing-service)
- [Summary Care Record (SCR)](Summary-Care-Record-SCR.md)
- [FGM Information Sharing (IS)](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/1391135139/FGM+Information+Sharing+IS)

A Solution that implements the core [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Capability is required to have full PDS integration. SMSP may be a suitable alternative to full PDS integration for some Solutions that are not tightly integrated into the core GP Solution and require a read-only source of demographics from PDS.

# Requirements

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| **SMS01** | Implement and maintain the 4 key requirement specifications below and the common requirements found here [Requirements pack and Supplier Conformance Assessment List (SCAL) template](https://digital.nhs.uk/services/spine/spine-mini-service-provider-for-personal-demographics-service/requirements-pack-and-supplier-conformance-assessment-list-template).   - The Interoperability Contracting Vehicle Common Provider Requirements - Included as the SMSP site documentation set - The Interoperability Contracting Vehicle Common Client Requirements -Included as the SMSP site documentation set - The Interoperability Service specific Provider Requirements e.g. FGM RIS, CPIS - The Interoperability Service Specific Client Requirements e.g. FGM RIS, CPIS | MUST |

# Compliance, Assurance and Testing

See the Spine Mini Services section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

- [Mini Services Introduction](https://digital.nhs.uk/services/spine/spine-mini-service-simplified-ways-to-connect-to-spine)

# Dependencies

There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents.

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |