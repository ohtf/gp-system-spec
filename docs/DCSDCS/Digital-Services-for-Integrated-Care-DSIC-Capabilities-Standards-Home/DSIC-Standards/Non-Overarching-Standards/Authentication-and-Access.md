---
page_id: "1391133913"
space: "DCSDCS"
title: "Authentication and Access"
version: 19
updated: "2026-07-20T14:50:55.350Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133913/Authentication+and+Access"
labels: ["standard"]
---

# Authentication and Access

|  |  |
| --- | --- |
| **ID** | S54 |
| **Version** | 2.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 09 Jul 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [DFOCVC](https://nhse-dsic.atlassian.net/wiki/spaces/DFOCVCL) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

/\*<![CDATA[\*/
div.rbtoc1785497910718 {padding: 0px;}
div.rbtoc1785497910718 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785497910718 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#AuthenticationandAccess-Introduction)
- [Requirements](#AuthenticationandAccess-Requirements)
- [Compliance, Assurance and Testing](#AuthenticationandAccess-Compliance,AssuranceandTesting)
- [Documentation](#AuthenticationandAccess-Documentation)
- [Dependencies](#AuthenticationandAccess-Dependencies)
- [Roadmap](#AuthenticationandAccess-Roadmap)

# Introduction

Identity and Access Management (IAM) provides a trusted digital identity service for Health and Care Professionals to authenticate their identity when accessing national clinical information systems. This authentication allows the Health and Care Professional to log on and access those systems securely through a range of access options.

The NHS Care Identity Service makes use of current technologies and Smartcards to allow Health and Care Professionals in England to authenticate their identity when accessing national clinical information systems. This was previously implemented using [CIS (Care Identity Service)](https://digital.nhs.uk/services/registration-authorities-and-smartcards#care-identity-service), but this is now replaced by [NHS Care Identity Service 2 (CIS2)](https://digital.nhs.uk/services/identity-and-access-management/nhs-care-identity-service-2).

NHS CIS2 has a number of main aims:

1. Allow the use of new authentication methods to support user’s workstyles
2. Simplify the effort needed to integrate an application with the authentication service
3. Remove the need for outdated technology like IE11 or Java applets
4. Allow the use of the latest operating systems and browsers

To enable these aims, the [CIS2 authentication service (CIA)](https://digital.nhs.uk/services/identity-and-access-management/nhs-care-identity-service-2/care-identity-authentication) is providing an [OpenID Connect (OIDC)](https://openid.net/developers/specs/) Solution. OIDC is an Internet Engineering Task Force (IETF) standard that defines a protocol for applications to request a user authentication from an Identity Provider (IdP) such as NHS CIS2.

# Requirements

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| AA01 | Implement and maintain the latest specification version of [NHS Care Identity Service 2 (NHS CIS2)](https://digital.nhs.uk/services/identity-and-access-management/nhs-care-identity-service-2/care-identity-authentication) for the authentication of Health or Care Professionals accessing NHS systems and national services | MUST |

# Compliance, Assurance and Testing

See the Care Identity Service (CIS2) section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation

- [NHS Care Identity Service 2](https://digital.nhs.uk/services/care-identity-service/applications-and-services/nhs-care-identity-service-2)
- [NHS CIS2 Authentication guidance for developers](https://digital.nhs.uk/services/care-identity-service/applications-and-services/cis2-authentication/guidance-for-developers)
- [OpenID Connect (OIDC) detailed guidance](https://digital.nhs.uk/services/identity-and-access-management/nhs-care-identity-service-2/care-identity-authentication/guidance-for-developers/detailed-guidance)
- [Onboard to NHS CIS2 Authentication](https://digital.nhs.uk/services/care-identity-service/applications-and-services/cis2-authentication/onboarding-journey)

# Dependencies

There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents.

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Changes to Information Governance requirements](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/12569509907/Changes+to+Information+Governance+requirements) | [Information Governance](../Overarching-Standards/Information-Governance.md), [Authentication and Access](Authentication-and-Access.md), [Baseline Assurance Standard](../Overarching-Standards/Baseline-Assurance-Standard.md) | Published | 23 Oct 2026 | Additions, removals and amendments to requirements in the Information Governance Standard | Uplift | Managed Capacity - Other |