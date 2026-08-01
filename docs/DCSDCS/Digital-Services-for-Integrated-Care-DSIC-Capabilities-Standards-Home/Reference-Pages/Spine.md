---
page_id: "1391133543"
space: "DCSDCS"
title: "Spine"
version: 9
updated: "2024-03-08T09:46:29.480Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133543/Spine"
labels: ["reference_page"]
---

# Spine

|  |  |
| --- | --- |
| ID | R1 |
| Version | 1.0.2 |
| Type | Reference |

- [Introduction](#Spine-Introduction)
  - [Spine Demographics host:](#Spine-SpineDemographicshost:)
  - [Spine Clinicals host](#Spine-SpineClinicalshost)
  - [Other Spine Services include:](#Spine-OtherSpineServicesinclude:)
- [Compliance, Assurance and Testing](#Spine-Compliance,AssuranceandTesting)
  - [Using MHS Adaptor](#Spine-UsingMHSAdaptor)
- [Documentation](#Spine-Documentation)
  - [Using MHS Adaptor](#Spine-UsingMHSAdaptor.1)

# Introduction {#Spine-Introduction}

The NHS Spine supports national services such as the  Personal Demographics Service (PDS), e-Referrals Service (e-RS), Electronic Prescription Service (EPS) and the Summary Care Record (SCR). To provide secure access to these systems Spine hosts an number of subsystems which are defined in the External Interface Specification (EIS). The FHIR services guidance is accessible at  Spine FHIR APIs.  There are also a number of supporting artefacts that needed for development to enable Spine access. The migration from Spine to Spine 2 has seen an uplift and renaming of some services, which is defined as the DIP (Digital Interoperability Platform). A representation of the DIP can be seen below:

[2017-05-22 - DIP Diagram…](../../../attachments/DCSDCS/1391133543/att1391149316-2017-05-22 - DIP Diagram.pdf)

There are two core patient information repositories Spine Clinicals and Spine Demographics, where a service sits is determined by the sensitivity of the data, currently

## Spine Demographics host: {#Spine-SpineDemographicshost:}

- Personal Demographics Service (PDS)
- [Visitors and Migrants](https://nhsconnect.github.io/visitor-and-migrants/index.html)
- [National Data Opt Outs](https://developer.nhs.uk/apis/optout/)

## Spine Clinicals host {#Spine-SpineClinicalshost}

- Summary Care Record (SCR)
- Female Genital Mutilation Risk Indicator System - F[GM RIS](https://nhsconnect.github.io/fgm-risk-indication-service/)
- Child Projection Information Service - [CP-IS](https://digital.nhs.uk/services/child-protection-information-sharing-project)
- Flags - such as Reasonable Adjustments (in development)

## Other Spine Services include: {#Spine-OtherSpineServicesinclude:}

- Spine Directories - [ODS](https://digital.nhs.uk/services/organisation-data-service), [CIS](https://digital.nhs.uk/services/registration-authorities-and-smartcards/care-identity-service), [Pathways DOS](https://digital.nhs.uk/services/directory-of-services-dos). eRS Directory, Choices Directory, MESH endpoints
- [National Events Management Service](https://developer.nhs.uk/apis/ems-beta/)
- [National Record Locator Service](https://developer.nhs.uk/apis/nrls/)
- Strategic Authorisation [National Identity](https://developer.nhs.uk/apis/national-authentication/)
- Message Exchange for Social Care and Health - [MESH](https://digital.nhs.uk/services/message-exchange-for-social-care-and-health-mesh)
- [Spine Secure Proxy](https://developer.nhs.uk/apis/gpconnect-0-5-0/integration_spine_security_proxy.html)
- [Spine Mini Service](https://digital.nhs.uk/services/spine/spine-mini-service-simplified-ways-to-connect-to-spine)
- [API Gateway](https://developer.nhs.uk/apis/) which includes the functionality of the legacy Transaction and Messaging Service (TMS)
- Message Handling System via [MHS Adaptor](https://digital.nhs.uk/developer/api-catalogue/mhs)

# Compliance, Assurance and Testing {#Spine-Compliance,AssuranceandTesting}

Compliance and Assurance is carried out by the [Solution Assurance](https://digital.nhs.uk/services/solution-assurance) Team for access to each individual Spine Service. Local Systems accessing Spine services must meet the [Spine WES](https://digital.nhs.uk/services/spine/spine-technical-information-warranted-environment-specification-wes) and the minimum set of IG requirements defined by each service.

When developing healthcare applications, they can be tested by connecting them to the Spine test environment [OpenTest](https://digital.nhs.uk/services/spine/open-access-test-environment-for-spine-opentest). It contains clinical and demographic test data and gives access to a real Spine 2 core instance and all spine based national NHS services.

The is supporting guidance for accessing [Spine FHIR APIs](https://developer.nhs.uk/apis/spine-core/) is currently in draft format and should be checked regularly for further additions

### **Using MHS Adaptor** {#Spine-UsingMHSAdaptor}

MHS adapter has been developed and pre-assured by the Authority.

More information on integrating can be found [here](https://digital.nhs.uk/developer/api-catalogue/mhs)

# Documentation {#Spine-Documentation}

Additional supporting documentation:

- The [Supported Cipher Suite](https://confluence.digital.nhs.uk/download/attachments/48835039/Approved%20Crypto%20v4.pdf?version=1&modificationDate=1524127638333&api=v2)
- [End Point Access](http://www.assurancesupport.digital.nhs.uk/files/2018-09/nhs-digital-endpoint-directaccess-to-spine-services-v9.4.docx) guidance
- General [Spine Access guidance](https://digital.nhs.uk/developer/guides-and-documentation)
- [NPFIT-FNT-TO-SCG-0005 SCG clarification on timezone v1.1.doc](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133543/NPFIT-FNT-TO-SCG-0005%20SCG%20clarification%20on%20timezone%20v1.1.doc?version=1&modificationDate=1541000859127&cacheVersion=1&api=v2)
- [NPFIT-FNT-TO-SCG-0005 App3 v2.xls](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133543/NPFIT-FNT-TO-SCG-0005%20App3%20v2.xls?version=1&modificationDate=1542296301812&cacheVersion=1&api=v2)
- Organisation Data Service [ODS](https://digital.nhs.uk/services/organisation-data-service) and  codes can be accessed by the [ODS API Suite](https://directory.spineservices.nhs.uk/ODSAPISuite)
- [Spine101.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133543/Spine101.pdf?version=1&modificationDate=1542296437605&cacheVersion=1&api=v2)

### **Using MHS Adaptor** {#Spine-UsingMHSAdaptor.1}

It is recommended to read [GP software developer guide](https://digital.nhs.uk/developer/guides-and-documentation/developer-guides/gp-software-developer-guide) in conjunction with the adaptor documentation

- [API Catalogue - MHS adaptor](https://digital.nhs.uk/developer/api-catalogue/mhs)
- [GP software developer guide](https://digital.nhs.uk/developer/guides-and-documentation/developer-guides/gp-software-developer-guide)

## Attachments

- [2017-05-22 - DIP Diagram.vsd](../../../attachments/DCSDCS/1391133543/att1391149087-2017-05-22 - DIP Diagram.vsd)
- [NPFIT-FNT-TO-SCG-0005 App3 v2.xls](../../../attachments/DCSDCS/1391133543/att1391149166-NPFIT-FNT-TO-SCG-0005 App3 v2.xls)
- [Spine101.pdf](../../../attachments/DCSDCS/1391133543/att1391149205-Spine101.pdf)
- [2017-05-22 - DIP Diagram.pdf](../../../attachments/DCSDCS/1391133543/att1391149316-2017-05-22 - DIP Diagram.pdf)
- [NPFIT-FNT-TO-SCG-0005 SCG clarification on timezone v1.1.doc](../../../attachments/DCSDCS/1391133543/att1391158150-NPFIT-FNT-TO-SCG-0005 SCG clarification on timezone v1.1.doc)
