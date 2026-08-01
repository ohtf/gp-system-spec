---
page_id: "11963203865"
space: "DCSDCS"
title: "Authentication and Access V1.0.0"
version: 1
updated: "2022-04-28T09:55:42.257Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11963203865/Authentication+and+Access+V1.0.0"
labels: ["interop_standard_retired"]
---

# Authentication and Access V1.0.0

|  |  |
| --- | --- |
| ID | S54 |
| Version | 1.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

- [Introduction](#AuthenticationandAccessV1.0.0-Introduction)
- [Compliance and Assurance](#AuthenticationandAccessV1.0.0-ComplianceandAssurance)
- [Testing](#AuthenticationandAccessV1.0.0-Testing)
- [Documentation](#AuthenticationandAccessV1.0.0-Documentation)
- [Roadmap](#AuthenticationandAccessV1.0.0-Roadmap)

# Introduction {#AuthenticationandAccessV1.0.0-Introduction}

Authentication and access to systems and national services is managed via Smartcards using CIS (Care Identity Service).  Smartcards are manually issued to staff by their local Registration Authority (RA) Team. A system users access is determined by their Role Based Access Codes (RBAC), the national RBAC table can be downloaded from the NHS Digital Registration Authorities and Smartcard page along with all the associated policies and forms to apply for a Smartcard.

RBAC is used at both local and national level and the codes are supported for both environments.

The CIS will be replaced by the NHS Identity Service (previously known as Strategic Authentication) which is an implementation of OpenID Connect. It enables internet based, platform agnostic authentication with alternatives to (as well as) Smartcards. Once this migration has completed, all new implementations will need to use the NHS Identity service for authenticating staff.

# Compliance and Assurance {#AuthenticationandAccessV1.0.0-ComplianceandAssurance}

Compliance and assurance is carried out as part of the overall IG assurance process when connecting to a national service (which is linked to the appropriate RBAC to access a service). Where Smartcards are used for accessing the local system, data compliance and assurance should be carried out to ensure that a user can only access services and patient information based on their allocated RBAC.

# Testing {#AuthenticationandAccessV1.0.0-Testing}

Testing is carried out by the Solution Assurance Test And Assurance Service and supported by the Technical Support Service. The RBAC access MUST be tested as part of the individual service requirements testing e.g. Access to PDS, SCR.

# Documentation {#AuthenticationandAccessV1.0.0-Documentation}

Documentation relating to CIS and Smartcards can be found at  NHS Digital Registration Authorities and Smartcard page.

Technical documentation is hosted at the NHS Identity pages on the NHS developer network.

# Roadmap {#AuthenticationandAccessV1.0.0-Roadmap}

| Roadmap Item |
| --- |
| No content found. |