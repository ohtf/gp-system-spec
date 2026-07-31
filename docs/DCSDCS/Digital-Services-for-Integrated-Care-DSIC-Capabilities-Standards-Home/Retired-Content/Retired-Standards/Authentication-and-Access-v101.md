---
page_id: "12491489319"
space: "DCSDCS"
title: "Authentication and Access v1.0.1"
version: 1
updated: "2023-07-27T12:42:17.943Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12491489319/Authentication+and+Access+v1.0.1"
labels: ["interop_standard_retired"]
---

# Authentication and Access v1.0.1

|  |  |
| --- | --- |
| ID | S54 |
| Version | 1.0.1 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 28 Apr 2022 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") - [DFOCVC](https://gpitbjss.atlassian.net/wiki/spaces/DFOCVCL) - [Vaccinations - Local/PCN Delivery](https://gpitbjss.atlassian.net/wiki/spaces/CVPDR) |

- [Introduction](#AuthenticationandAccessv1.0.1-Introduction)
- [Requirements](#AuthenticationandAccessv1.0.1-Requirements)
- [Compliance, Assurance and Testing](#AuthenticationandAccessv1.0.1-Compliance,AssuranceandTesting)
- [Documentation](#AuthenticationandAccessv1.0.1-Documentation)
  - [NHS Care Identity Service 2](#AuthenticationandAccessv1.0.1-NHSCareIdentityService2)
  - [CIS and Smartcards](#AuthenticationandAccessv1.0.1-CISandSmartcards)
- [Roadmap](#AuthenticationandAccessv1.0.1-Roadmap)

# Introduction

Identity and Access Management (IAM) provides a trusted digital identity service for health and care staff that authorises access to health and care information systems. This authentication allows the health and care professional to log on and access those systems securely through a range of access options.

The NHS Care Identity Service makes use of current technologies and Smartcards to allow health and care professionals in England to authenticate their identity when access national clinical information systems. This was previously implemented using CIS (Care Identity Service), but this is now replaced by NHS Care Identity Service 2.

The new NHS Care Identity Service 2 has a number of benefits:

- Allows the use of new authentication methods where a smartcard may not be appropriate
- Simplifies the effort needed to integrate an application with the authentication service
- Removes the need for outdated technology like IE11 or Java applets
- Allows the use of the latest operating systems and browsers

To enable these aims NHS Identity is providing an OpenID Connect (OIDC) solution. OIDC is an Internet Engineering Task Force (IETF) standard that defines a protocol for applications to request a user authentication from an Identity Provider (IdP) such as NHS Care Identity Service 2.

# Requirements

| Applicable Suppliers | Requirement | Level |
| --- | --- | --- |
| Suppliers of new services or applications (i.e. those which are NOT currently deployed into an operational environment) | NHS Care Identity Service 2 (NHS CIS2) to be used for authenticating staff by implementing and maintaining the latest specification version. | MUST |
| Suppliers of services which ARE currently deployed into an operational environment and have existing compliance. | CIS (Care Identity Service) or later version (e.g. NHS CIS2) to be used for authenticating staff. | MUST |

# Compliance, Assurance and Testing

Compliance and assurance is carried out as part of the overall IG assurance process when connecting to a national service (which is linked to the appropriate RBAC to access a service). Where Smartcards are used for accessing the local system, data compliance and assurance should be carried out to ensure that a user can only access services and patient information based on their allocated RBAC.

For Suppliers of new services or applications, see the Care Identity Service (CIS2) section on Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements.

# Documentation

### **NHS Care Identity Service 2**

Suppliers of new services or applications, see additional supporting documentation:

- Identity and Access Management - NHS Digital
- API authorisation

### **CIS and Smartcards**

Click here to view historical documentation

Documentation relating to CIS and Smartcards can be found at  NHS Digital Registration Authorities and Smartcard page.

Technical documentation is hosted at the NHS Identity pages on the NHS developer network.

# Roadmap

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Changes to Information Governance requirements](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/12569509907/Changes+to+Information+Governance+requirements) | [Information Governance](../../DSIC-Standards/Overarching-Standards/Information-Governance.md), [Authentication and Access](../../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md), [Baseline Assurance Standard](../../DSIC-Standards/Overarching-Standards/Baseline-Assurance-Standard.md) | Published | 23 Oct 2026 | Additions, removals and amendments to requirements in the Information Governance Standard | Uplift | Managed Capacity - Other |