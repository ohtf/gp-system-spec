---
page_id: "1841397861"
space: "DCSDCS"
title: "GP2GP v1.0.0"
version: 3
updated: "2020-03-02T16:28:03.995Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1841397861/GP2GP+v1.0.0"
labels: ["interop_standard_retired"]
---

# GP2GP v1.0.0

|  |  |
| --- | --- |
| ID | S43 |
| Version | 1.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

- [Introduction](#GP2GPv1.0.0-Introduction)
- [Compliance and Assurance](#GP2GPv1.0.0-ComplianceandAssurance)
- [Requirements](#GP2GPv1.0.0-Requirements)
  - [Message Fragments and Examples](#GP2GPv1.0.0-MessageFragmentsandExamples)
  - [Supplementary specifications](#GP2GPv1.0.0-Supplementaryspecifications)
- [Dependencies](#GP2GPv1.0.0-Dependencies)
- [Roadmap](#GP2GPv1.0.0-Roadmap)

# Introduction {#GP2GPv1.0.0-Introduction}

The GP2GP record transfer mechanism enables a patient's record to be electronically transferred directly and securely when they move from one practice to another.

# Compliance and Assurance {#GP2GPv1.0.0-ComplianceandAssurance}

The compliance baseline for GP2GP and document locations were correct at the time of original publication, but referenced documents can now be found embedded on this page, below. The exceptions to this are the references to the NHS Messaging Implementation Manual (MIM) and External Interface Specification (EIS) (follow these links for details).

[GP2GP 1.1a Compliance Mo…](../../../../.raw/DCSDCS/attachments/1841397861/att1841397936-GP2GP 1.1a Compliance Module.doc)

The GP2GP assurance is split into 2 streams:

1. Compliance testing - this tests the spine messaging patterns and functionality
2. Interoperability Testing - the testing of the clinically semantic testing of the message payload between different systems

For advice and support on assurance please contact [businesspartners@nhs.net](mailto:businesspartners@nhs.net) or visit https://digital.nhs.uk/services/nhs-business-partners

# Requirements {#GP2GPv1.0.0-Requirements}

| ID | Description | Level |
| --- | --- | --- |
| GP2GP00 | Suppliers must meet the requirements for GP2GP 1.1a | MUST |
| GP2GP01 | Suppliers should meet the requirements for GP2GP 2.2 (a and b).  Suppliers should note these requirements will become MUST in the future, please see Roadmap for details.  [HSCIC-PC-BLD-0068 26 GP2…](../../../../.raw/DCSDCS/attachments/1841397861/att1841397933-HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf) | SHOULD |
| GP2GP02 | Suppliers must make available documentation to ensure that suppliers receiving GP2GP messages are fully able to interpret, consume and process the data to minimise data loss and degradation. This must include (but is not limited to):   - Structure of data - Any know issues or anomalies and how they should be handled - Code sets and associated meanings - Field specifications (types, lengths etc.) | MUST |
| GP2GP03 | Suppliers must provide support to receivers of GP2GP messages to resolve any issues with interpreting,consuming and processing received messages | MUST |

## Message Fragments and Examples {#GP2GPv1.0.0-MessageFragmentsandExamples}

[NPFIT-FNT-TO-TIN-0562[1]…](../../../../.raw/DCSDCS/attachments/1841397861/att1841397867-NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc)

## Supplementary specifications {#GP2GPv1.0.0-Supplementaryspecifications}

The following supplemental specifications contain additional requirements and guidance for GP2GP implementation:

[NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-FNT-TO-TIN-1087.02%20GP2GP%20Supplementary%20Specification%20on%20Handling%20Medication%20Discontinuation.pdf?version=1&modificationDate=1583164812963&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0069%2024%20GP2GP%20Spine%20Technical%20Design%20v7.1.pdf?version=1&modificationDate=1583164812734&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0083.08%20GP2GP%20Response%20Codes.pdf?version=1&modificationDate=1583164812513&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0099.04%20GP2GP%20Handling%20Missing%20Attachments.pdf?version=1&modificationDate=1583164812275&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0132.03%20GP2GP%20Supplementary%20Specification%20on%20Structured%20Degrade%20Handling.pdf?version=1&modificationDate=1583164812043&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0133.02%20GP2GP%20Supplementary%20Spec%20-%20Handling%20and%20Propagation%20of%20Non%20Consultation%20Data.pdf?version=1&modificationDate=1583164811782&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0134.05%20GP2GP%20Supplementary%20Specification%20Representing%20PMIP%20Data%20in%20GP2GP%20Messages.pdf?version=1&modificationDate=1583164811441&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0158%20GP2GP%20Supplementary%20Specification%20Attachment%20References.pdf?version=1&modificationDate=1583164811206&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0163.02%20Topic%20and%20Category%20Handling%20in%20GP2GP.pdf?version=1&modificationDate=1583164810904&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0170.03%20GP2GP%20SS%20Handling%20Large%20Messages.pdf?version=1&modificationDate=1583164810675&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0171.02%20GP2GP%20SS%20Harvesting%20Management%20Information.pdf?version=1&modificationDate=1583164810417&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0172.02%20GP2GP%20UC1%20Transfer%20Electronic%20Health%20Record.pdf?version=1&modificationDate=1583164810157&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0173.01%20GP2GP%20UC%202%20Harvest%20and%20Prepare%20Management%20Information.pdf?version=1&modificationDate=1583164809913&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0175.03%20GP2GP%20SS%20Handling%20A-B-A%20Transfers%20v1.3.pdf?version=1&modificationDate=1583164809679&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0177.01%20GP2GP%20SS%20User%20Experience.pdf?version=1&modificationDate=1583164809449&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0178%2002%20GP2GP%20Coding%20Scheme%20Translation%20v1.1.pdf?version=1&modificationDate=1583164809213&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-0180.02%20GP2GP%20Transfer%20of%20Patient%20Facing%20Service%20Settings%2004.pdf?version=1&modificationDate=1583164808973&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-PC-BLD-181.02%20GP2GP%20Handling%20the%20SCR%20indicator%20v03.pdf?version=1&modificationDate=1583164808733&cacheVersion=1&api=v2)

[NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-FNT-TO-IG-DES-0115.01%20Statement%20on%20Data%20Retention%20v1.0.pdf?version=1&modificationDate=1583164808495&cacheVersion=1&api=v2)

[NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-FNT-TO-TAR-0017.07%20Compliance%20Requirements%20for%20Patient%20Registration.pdf?version=1&modificationDate=1583164808238&cacheVersion=1&api=v2)

[NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1841397861/NPFIT-FNT-TO-TIN-0289.08%20GP2GP%20Supplementary%20Specification%20on%20Handling%20Attachment%20Types.pdf?version=1&modificationDate=1583164807908&cacheVersion=1&api=v2)

# Dependencies {#GP2GPv1.0.0-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface standards:

- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)

# Roadmap {#GP2GPv1.0.0-Roadmap}

| Title |
| --- |
| No content found. |

## Attachments

- [NPFIT-FNT-TO-TIN-0379.03 System Walkthrough and Induction Pack.ppt](../../../../.raw/DCSDCS/attachments/1841397861/att1841397864-NPFIT-FNT-TO-TIN-0379.03 System Walkthrough and Induction Pack.ppt)
- [NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc](../../../../.raw/DCSDCS/attachments/1841397861/att1841397867-NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc)
- [NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397870-NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf)
- [NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397873-NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf)
- [NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397876-NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf)
- [NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397879-NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf)
- [NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397882-NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf)
- [NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397885-NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf)
- [NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397888-NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf)
- [NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397891-NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf)
- [NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397894-NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf)
- [NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397897-NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf)
- [NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397900-NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf)
- [NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397903-NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf)
- [NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397906-NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf)
- [NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397909-NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf)
- [NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397912-NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf)
- [NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397915-NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf)
- [NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397918-NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf)
- [NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397921-NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf)
- [NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397924-NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf)
- [NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397927-NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf)
- [NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397930-NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf)
- [HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf](../../../../.raw/DCSDCS/attachments/1841397861/att1841397933-HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf)
- [GP2GP 1.1a Compliance Module.doc](../../../../.raw/DCSDCS/attachments/1841397861/att1841397936-GP2GP 1.1a Compliance Module.doc)
