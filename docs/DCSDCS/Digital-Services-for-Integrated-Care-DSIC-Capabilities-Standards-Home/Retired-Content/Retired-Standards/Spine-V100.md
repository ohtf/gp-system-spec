---
page_id: "11975327795"
space: "DCSDCS"
title: "Spine V1.0.0"
version: 1
updated: "2022-05-10T10:08:38.980Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11975327795/Spine+V1.0.0"
labels: ["retired_reference_page"]
---

# Spine V1.0.0

|  |  |
| --- | --- |
| ID | R1 |
| Version | 1.0.0 |
| Type | Reference |

- [Introduction](#SpineV1.0.0-Introduction)
  - [Spine Demographics host:](#SpineV1.0.0-SpineDemographicshost:)
  - [Spine Clinicals host](#SpineV1.0.0-SpineClinicalshost)
  - [Other Spine Services include:](#SpineV1.0.0-OtherSpineServicesinclude:)
- [Compliance and Assurance](#SpineV1.0.0-ComplianceandAssurance)
- [Testing](#SpineV1.0.0-Testing)
- [Documentation](#SpineV1.0.0-Documentation)

# Introduction {#SpineV1.0.0-Introduction}

The NHS Digital Spine supports national services such as the  Personal Demographics Service (PDS), e-Referrals Service (e-RS), Electronic Prescription Service (EPS) and the Summary Care Record (SCR). To provide secure access to these systems Spine hosts an number of subsystems which are defined in the External Interface Specification (EIS). The FHIR services guidance is accessible at  Spine FHIR APIs.  There are also a number of supporting artefacts that needed for development to enable Spine access. The migration from Spine to Spine 2 has seen an uplift and renaming of some services, which is defined as the DIP (Digital Interoperability Platform). A representation of the DIP can be seen below:

[2017-05-22 - DIP Diagram…](../../../../attachments/DCSDCS/11975327795/att11975327829-2017-05-22 - DIP Diagram.pdf)

There are two core patient information repositories Spine Clinicals and Spine Demographics, where a service sits is determined by the sensitivity of the data, currently

## Spine Demographics host: {#SpineV1.0.0-SpineDemographicshost:}

- Personal Demographics Service (PDS)
- Visitors and Migrants
- National Data Opt Outs

## Spine Clinicals host {#SpineV1.0.0-SpineClinicalshost}

- Summary Care Record (SCR)
- Female Genital Mutilation Risk Indicator System - FGM RIS
- Child Projection Information Service - CP-IS
- Flags - such as Reasonable Adjustments (in development)

## Other Spine Services include: {#SpineV1.0.0-OtherSpineServicesinclude:}

- Spine Directories - ODS, CIS, Pathways DOS. eRS Directory, Choices Directory, MESH endpoints
- National Events Management Service
- National Record Locator Service
- Strategic Authorisation National Identity
- Message Exchange for Social Care and Health - MESH
- Spine Secure Proxy
- Spine Mini Service
- API Gateway which includes the functionality of the legacy Transaction and Messaging Service (TMS)

# Compliance and Assurance {#SpineV1.0.0-ComplianceandAssurance}

Compliance and Assurance is carried out by the Solution Assurance Team for access to each individual Spine Service. Local Systems accessing Spine services must meet the Spine WES and the minimum set of IG requirements defined by each service.

# Testing {#SpineV1.0.0-Testing}

 When developing healthcare applications, they can be tested by connecting them to the Spine test environment OpenTest. It contains clinical and demographic test data and gives access to a real Spine 2 core instance and all spine based national NHS services.

The is supporting guidance for accessing Spine FHIR APIs is currently in draft format and should be checked regularly for further additions

# Documentation {#SpineV1.0.0-Documentation}

Additional supporting documentation:

- The Supported Cipher Suite
- End Point Access guidance
- General Spine Access guidance
- NPFIT-FNT-TO-SCG-0005 SCG clarification on timezone v1.1.doc
- NPFIT-FNT-TO-SCG-0005 App3 v2.xls
- Organisation Data Service [ODS](https://digital.nhs.uk/services/organisation-data-service) and  codes can be accessed by the ODS API Suite
- Spine101.pdf

## Attachments

- [2017-05-22 - DIP Diagram.pdf](../../../../attachments/DCSDCS/11975327795/att11975327829-2017-05-22 - DIP Diagram.pdf)
- [2017-05-22 - DIP Diagram.vsd](../../../../attachments/DCSDCS/11975327795/att11975327832-2017-05-22 - DIP Diagram.vsd)
- [Spine101.pdf](../../../../attachments/DCSDCS/11975327795/att11975327835-Spine101.pdf)
- [NPFIT-FNT-TO-SCG-0005 App3 v2.xls](../../../../attachments/DCSDCS/11975327795/att11975327838-NPFIT-FNT-TO-SCG-0005 App3 v2.xls)
- [NPFIT-FNT-TO-SCG-0005 SCG clarification on timezone v1.1.doc](../../../../attachments/DCSDCS/11975327795/att11975327841-NPFIT-FNT-TO-SCG-0005 SCG clarification on timezone v1.1.doc)
