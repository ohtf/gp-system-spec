---
page_id: "12117573633"
space: "DCSDCS"
title: "NHS login service V1.0.0"
version: 1
updated: "2022-09-13T11:13:12.593Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12117573633/NHS+login+service+V1.0.0"
labels: ["interop_standard_retired"]
---

# NHS login service V1.0.0

|  |  |
| --- | --- |
| ID | S68 |
| Version | 1.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |
| Framework(s) | - GP IT Futures - Tech Innovation - DFOCVC - Vaccinations - Local/PCN Delivery |

- [Introduction](#NHSloginserviceV1.0.0-Introduction)
- [Documentation](#NHSloginserviceV1.0.0-Documentation)
- [Roadmap](#NHSloginserviceV1.0.0-Roadmap)

# Introduction {#NHSloginserviceV1.0.0-Introduction}

The NHS login Programme is developing a single, secure and easy-to-use system for verifying the identity of citizens and services requesting access to digital health records so that we can ensure people only access information about themselves and those in their care. Additional information can be found on the NHS login page on NHS Digital's website.

The very first stage of this development is to support the NHS App which will initially use existing IM1 interfaces to integrate with incumbent GP systems.  To enable this it is necessary for GP systems to provide a simple API for retrieval and/or creation of the "Linkage Key" (also known as "passphrase").

Future phases on the Roadmap (see below) will require GP Solutions to:

- consume the NHS login service instead of local authentication mechanisms.
- provision local identities directly into NHS login.

Please note this initiative was previously known as Citizen Identity.

# Documentation {#NHSloginserviceV1.0.0-Documentation}

## GP Linkage Key {#NHSloginserviceV1.0.0-GPLinkageKey}

Part of this work involves the development of a new simple interface to retrieve and create linkage keys for users, whereby the NHS login platform is used to register and verify users via an online process. As part of this process, the NHS login platform will obtain an NHS number (with appropriate consent) and validate this against PDS and GP Practice Codes (i.e. ODS Codes). This approach will allow the NHS login platform to retrieve linkage keys for users and allow the platform to generate new linkage keys for users where they do not already have one. The latest requirements set can be accessed below:

[Linkage Key API Specific…](../../../../attachments/DCSDCS/12117573633/att12117573652-Linkage Key API Specification v1.0.docx)

# Roadmap  {#NHSloginserviceV1.0.0-Roadmap}

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [NHS login interface - Provisioning](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/1391133536/NHS+login+interface+-+Provisioning) | [Interoperability Standard](../../DSIC-Standards/Overarching-Standards/Interoperability-Standard.md), [NHS login Service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md), [Appointments Management - Citizen](../../DSIC-Capabilities/Appointments-Management-Citizen.md), [Communicate With Practice - Citizen](../../Deprecated-Content/Deprecated-Capabilities/Communicate-With-Practice-Citizen.md), [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Prescription Ordering - Citizen](../../DSIC-Capabilities/Prescription-Ordering-Citizen.md), [View Record - Citizen](../../DSIC-Capabilities/View-Record-Citizen.md) | Draft | TBC | The provisioning interface enables GP solutions to provision new Citizen users on the NHS login platform, thus enabling Citizens to use one consistent account for Patient sign-in and ID verification. | Replace | Opportunity Item |

## Attachments

- [Linkage Key API Specification v1.0.docx](../../../../attachments/DCSDCS/12117573633/att12117573652-Linkage Key API Specification v1.0.docx)
