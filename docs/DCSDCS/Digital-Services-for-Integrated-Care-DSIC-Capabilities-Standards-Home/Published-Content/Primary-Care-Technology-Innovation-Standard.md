---
page_id: "11969953793"
space: "DCSDCS"
title: "Primary Care Technology Innovation Standard"
version: 5
updated: "2024-10-11T14:52:10.016Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11969953793/Primary+Care+Technology+Innovation+Standard"
labels: ["overarching_standard"]
---

# Primary Care Technology Innovation Standard

|  |  |
| --- | --- |
| ID | S81 |
| Version | 1.0.1 |
| Type | Overarching Standard |
| Status | Published |
| Effective Date | TBC |
| Contracting Vehicle(s) | [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

# Description

As part of our move to modernise core clinical systems for Primary Care, NHS Digital have been engaging Suppliers around our Modern Technology Standards. These standards and the [NHS Architecture Principles](https://digital.nhs.uk/about-nhs-digital/our-work/nhs-digital-architecture/principles) lay out the future ways of working and technology we want to see developing to serve the needs of Primary Care and simplify the complexity of healthcare systems provision.Why are we doing this:

- We have a clear strategy of Application and Data separation
- We want to leverage modern technology and ways of working to improve the resilience, scale, sustainability and the improvements for incremental continuous delivery that they enable
- Bring together an ecosystem of systems that work better together based around open standards
- Deliver systems that are a delight to use for users
- Help us be more responsive to the increasing demands of patient facing services
- Reduce the number of technical standards and data formats to drive standardisation and reduce our technical debt and cost of change
- Encourage systems that can be used on many devices across different care settings with minimal setup or change

# Requirements

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| PCTIS01 | **Internet First**  Solution Suppliers must make their systems accessible over the Public Internet. Any solution should not require either of the following for the user to operate:   - Direct HSCN connectivity (connectivity within the data centre is acceptable) - A secondary VPN   The user must be able to connect to the application over the Public Internet using SSL to an endpoint that presents an Extended Validation certificate for the supported browser [(Supported Browsers)](https://digital.nhs.uk/about-nhs-digital/standards-for-web-products/withdrawal-of-support-for-internet-explorer) trusted CA (Certificate Authority) with a minimum of a SHA-256 signature | MUST |
| PCTIS02 | **Public Cloud**  We have a cloud first strategy for the procurement of systems based upon tier one public cloud offerings e.g. AWS, Azure, GCP and other industry recognised providers with similar SLAs, rather than those based upon a community, hybrid or private deployment model.   Solution Suppliers must:   - Deliver a solution based entirely on a public cloud from a recognised industry vendor that can offer the benefits of public cloud in terms of SLA, scalability and deployment on demand and Pay-as-you-go pricing. - Follow [NHS Digital's cloud risk framework](https://digital.nhs.uk/data-and-information/looking-after-information/data-security-and-information-governance/nhs-and-social-care-data-off-shoring-and-the-use-of-public-cloud-services/cloud-risk-framework) guidelines depending on data risk classification. - Follow [NHS Digital's architecture principles](https://digital.nhs.uk/about-nhs-digital/our-work/nhs-digital-architecture/principles), service user requirements & provide evidence against them - Be able to evidence they can meet the objectives of a Well Architected Framework review (e.g. the AWS assessment tool [here](https://aws.amazon.com/well-architected-tool/)) of the application by addressing the goals outlined in that framework regardless of chosen public cloud vendor.   We are happy for Suppliers to chose their own preferred Public Cloud provider and go through an assessment against the criteria in the Well Architected Framework and ensure they can meet the criteria laid out in the WAF assessment of those platforms. To ease the assurance burden on suppliers of Public Cloud we have already assessed some of the larger ones e.g. Amazon AWS, Google GCP and Microsoft Azure for the provision of services.  Pre-assured Well Architected Frameworks for cloud providers:   - [Amazon AWS WAF](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc) - [Microsoft Azure WAF](https://docs.microsoft.com/en-us/azure/architecture/framework/) - [Google GCP WAF](https://cloud.google.com/architecture/framework)   Where the Solution Suppliers cloud provider does not provide a Well Architected Framework with the necessary coverage, the Solution Supplier may use one of the pre-assured cloud providers Well Architected Frameworks as a basis for evidence.  See also [NHS Cloud Hosting Standards & Guidance](../DSIC-Standards/Overarching-Standards/Hosting-Infrastructure.md) | MUST |
| PCTIS03 | **Browser Based Applications**  Solution Suppliers applications must be built to use a supported browser see [Spine technical information: Warranted Environment Specification (WES) - NHS Digital](https://digital.nhs.uk/services/spine/spine-technical-information-warranted-environment-specification-wes)  Solution Suppliers must follow the guidance laid out in the NHS Digital Standards for Web Products [NHS Digital Standards for Web Products](https://digital.nhs.uk/about-nhs-digital/standards-for-web-products)  Suppliers may also still provide Rich Client Applications, but the core functionality must be available via a browser based application. | MUST |
| PCTIS04 | **NHS Identity (CIS2)**  Solution Suppliers must utilise [CIS2](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) to provide a single system identity for clinical staff.  Note that both NHS login and CIS2 use the same standards - OIDC/Oauth2 | MUST |
| PCTIS05 | **NHS login for Patient Authentication**  Solution Suppliers must utilise NHS login for patient authentication to help:   - improve Patient experience and leverage trust in the NHS brand - Provide a single Identity across all services for patients based on open standards   See also [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) | MUST |
| PCTIS06 | **Modern User Experience**  We want to ensure that Solution Suppliers produce safe, easy to use systems that enhance the patient and clinician experience built to meet accessibility standards.   - Solution Suppliers must comply with [NHS Design and usability standards](https://digital.nhs.uk/about-nhs-digital/standards-for-web-products/accessibility-for-digital-services) and provide an independent 3rd party assessment by a recognised assessment provider e.g. RNIB, Digital Accessibility Centre etc. - The scope of the assessment should cover overall accessibility of the application and provide evidence against the [WCAG 2.1](https://www.w3.org/TR/WCAG21/) AA standard (and target future compliance against [WCAG 2.2](https://www.w3.org/TR/WCAG22/) as it becomes finalised) and solution Suppliers must make these reports available via the Buying Catalogue. - Solution Suppliers must have assessment reports refreshed upon major releases of their application, with a minimum refresh period of 18 months. - Solution Suppliers should conduct generative user research to identify the user needs that your solution is designed to meet and must show supporting evidence that user research has been conducted and that the implementation has been designed around the user needs and incorporates the output of user research. These should be supported by videos/screenshots of common workflows e.g. Appointments scheduling, Recording Consultations, Patient Registration, Prescribing and any Patient facing services. - Solution Suppliers should have a pattern library/design system for your product to drive consistency and usability | MUST |
| PCTIS07 | **Open APIs**  Moving to open APIs on API-M helps promote better interoperability and reduces the impact of changes on Solution Suppliers and Primary Care.  Solution Suppliers must not create integrations outside the existing framework, connection agreement and supporting standards. Any new APIs must be created via API-M unless an exception is granted in advance by NHS Digital.  As mandated by the appropriate Capabilities or associated Standards, Solution Suppliers must make any integrations using the following APIs:   - [SDS (Spine Directory Services) FHIR API](https://digital.nhs.uk/developer/api-catalogue/spine-directory-service-fhir) - [Electronic Prescription Service (EPS)](../DSIC-Standards/Non-Overarching-Standards/Electronic-Prescription-Service-EPS-Prescribing.md) - using EPS FHIR API - [e-Referrals Service (e-RS)](../DSIC-Standards/Non-Overarching-Standards/e-Referrals-Service-e-RS.md) - using e-RS FHIR API - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) - using PDS FHIR API | MUST |
| PCTIS08 | **NHS Development guidelines**  Solution Suppliers should follow the software development guidance laid out in the NHS Digital software engineering quality framework:  <https://github.com/NHSDigital/software-engineering-quality-framework> | SHOULD |

# Guidance

**Guidance**

This section describes how requirements may be assessed and provides background information to assist Suppliers

| Requirement | Guidance |
| --- | --- |
| PCTIS01 **Internet First** | This will be assessed visually using one of the [Supported Browsers](https://digital.nhs.uk/about-nhs-digital/standards-for-web-products/withdrawal-of-support-for-internet-explorer) by connecting to the application over the Public Internet and ensuring that the application presents an Extended Validation certificate from a trusted CA (Certificate Authority) with a minimum of a SHA-256 signature |
| PCTIS02 **Public Cloud** | Suppliers will need to provide evidence that they have followed [NHS Digital's cloud risk framework](https://digital.nhs.uk/data-and-information/looking-after-information/data-security-and-information-governance/nhs-and-social-care-data-off-shoring-and-the-use-of-public-cloud-services/cloud-risk-framework) guidelines, submit a WAF review report which they walkthrough responses with the assurance team |
| PCTIS03 **Browser Based Applications** | The application must work with all browsers stated in  [Spine technical information: Warranted Environment Specification (WES) - NHS Digital](https://digital.nhs.uk/services/spine/spine-technical-information-warranted-environment-specification-wes) |
| PCTIS04 **NHS Identity (CIS2)** | Users must be able to authenticate using their credentials in CIS2 without the need for a separate identity in the application |
| PCTIS05 **NHS login for Patient Authentication** | Patients must be able to authenticate using their credentials in NHS login without the need for a separate identity in the application |
| PCTIS06 **Modern User Experience** | Suppliers must provide an independent 3rd party assessment report that shows how they have followed the [NHS Design and usability standards](https://digital.nhs.uk/about-nhs-digital/standards-for-web-products/accessibility-for-digital-services) and reports compliance against the [WCAG 2.1](https://www.w3.org/TR/WCAG21/) AA standard (targeting future compliance against [WCAG 2.2](https://www.w3.org/TR/WCAG22/) as it becomes finalised). These reports may then be uploaded to the Buying Catalogue. |
| PCTIS07 **Open APIs** | Any connectivity through to SDS, EPS, e-RS and PDS must be evidenced using the FHIR APIs below:   - [SDS (Spine Directory Services) FHIR API](https://digital.nhs.uk/developer/api-catalogue/spine-directory-service-fhir) - [Electronic Prescription Service (EPS)](../DSIC-Standards/Non-Overarching-Standards/Electronic-Prescription-Service-EPS-Prescribing.md) - using EPS FHIR API - [e-Referrals Service (e-RS)](../DSIC-Standards/Non-Overarching-Standards/e-Referrals-Service-e-RS.md) - using e-RS FHIR API - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) - using PDS FHIR API |
| **PCTIS08** **NHS****Development guidelines** | Suppliers will need to demonstrate how they follow the engineering principles within the [Software Engineering Quality Framework](https://github.com/NHSDigital/software-engineering-quality-framework) and how they review software engineering quality using the review tool within the framework. If Suppliers do not follow the framework guidance, they will be asked to demonstrate their own equivalent software engineering principles and quality review approaches. |

# Capabilities

**Applicable Capabilities**

All Suppliers Solutions delivering any Capabilities for the Technology Innovation Framework will need to meet this Standard.

# Roadmap

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |