---
page_id: "1391133874"
space: "DCSDCS"
title: "NHS login service"
version: 19
updated: "2026-07-22T13:07:51.721Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133874/NHS+login+service"
labels: ["standard"]
---

# NHS login service

|  |  |
| --- | --- |
| **ID** | S68 |
| **Version** | 2.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [DFOCVC](https://gpitbjss.atlassian.net/wiki/spaces/DFOCVCL) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

/\*<![CDATA[\*/
div.rbtoc1785497887633 {padding: 0px;}
div.rbtoc1785497887633 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785497887633 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#NHSloginservice-Introduction)
- [Requirements](#NHSloginservice-Requirements)
- [Compliance, Assurance and Testing](#NHSloginservice-Compliance,AssuranceandTesting)
- [Documentation](#NHSloginservice-Documentation)
  - [GP Linkage Key](#NHSloginservice-GPLinkageKey)
  - [Using NHS Login Integration](#NHSloginservice-UsingNHSLoginIntegration)
- [Dependencies](#NHSloginservice-Dependencies)
- [Roadmap](#NHSloginservice-Roadmap)

# Introduction

The NHS login Programme has developed a single, secure and easy-to-use system for verifying the identity of Citizens and Services requesting access to digital health records so that we can ensure people only access information about themselves and those in their care. Additional information can be found on the [NHS login page](https://www.nhs.uk/nhs-services/nhs-login/) on The Authority's website.

The very first stage of this development was to support the [NHS App](https://digital.nhs.uk/services/nhs-app) which initially used existing IM1 interfaces to integrate with incumbent GP systems. To enable this, it was necessary that GP systems provided a simple API for retrieval and/or creation of the "Linkage Key" (also known as "Passphrase"). The second stage of this development is for GP Citizen Services Solutions to consume the NHS Login Service.

Future phases on the Roadmap (see below) will require GP Solutions to:

- Provision local identities directly into NHS login.

Please note this initiative was previously known as Citizen Identity.

# Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| **Applicable Suppliers** | **Requirement ID** | **Requirement Text** | **Level** |
| Foundation Solution Suppliers | **NL01** | **GP Linkage Key**  Suppliers to provide an interface that allows the creation and retrieval of Linkage information when presented with an NHS Number. The Linkage Key information will then be used for subsequent IM1 interactions. | MUST |
| Citizen Services Solution Suppliers | **NL02** | **NHS Login Integration**  Suppliers to implement and maintain the NHS login integration inline with the latest documentation and offer the "Continue with NHS login" button on the front of Service for new and returning users. | MUST |

# Compliance, Assurance and Testing

See the NHS Login Service section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

## GP Linkage Key

Part of this work involves the development of a new simple interface to retrieve and create Linkage Keys for users, whereby the NHS login platform is used to register and verify users via an online process. As part of this process, the NHS login platform will obtain an NHS number (with appropriate consent) and validate this against PDS and GP Practice Codes (i.e. ODS Codes). This approach will allow the NHS login platform to retrieve Linkage Keys for users and allow the platform to generate new Linkage Keys for users where they do not already have one. The latest requirements set can be accessed below:

[Linkage Key API Specific…](NHS-login-service.md)

## Using NHS Login Integration

Full details of how to integrate with NHS login and if you are eligible can be found on the [Apply for NHS login - NHS Digital](https://digital.nhs.uk/services/nhs-login/nhs-login-for-partners-and-developers/nhs-login-integration-toolkit/apply-for-nhs-login) and [NHS login Integration Toolkit](https://digital.nhs.uk/services/nhs-login/nhs-login-for-partners-and-developers/nhs-login-integration-toolkit)

# Dependencies

There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents.

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [NHS login interface - Provisioning](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/1391133536/NHS+login+interface+-+Provisioning) | [Interoperability Standard](../Overarching-Standards/Interoperability-Standard.md), [NHS login Service](NHS-login-service.md), [Appointments Management - Citizen](../../DSIC-Capabilities/Appointments-Management-Citizen.md), [Communicate With Practice - Citizen](../../Deprecated-Content/Deprecated-Capabilities/Communicate-With-Practice-Citizen.md), [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Prescription Ordering - Citizen](../../DSIC-Capabilities/Prescription-Ordering-Citizen.md), [View Record - Citizen](../../DSIC-Capabilities/View-Record-Citizen.md) | Draft | TBC | The provisioning interface enables GP solutions to provision new Citizen users on the NHS login platform, thus enabling Citizens to use one consistent account for Patient sign-in and ID verification. | Replace | Opportunity Item |

## Attachments

- [Linkage Key API Specification v1.0.docx](../../../../.raw/DCSDCS/attachments/1391133874/att1391149290-Linkage Key API Specification v1.0.docx)
