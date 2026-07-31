---
page_id: "12334170145"
space: "DCSDCS"
title: "GP2GP v3.0.0"
version: 3
updated: "2023-03-06T13:38:38.493Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12334170145/GP2GP+v3.0.0"
labels: ["interop_standard_retired"]
---

# GP2GP v3.0.0

|  |  |
| --- | --- |
| ID | S43 |
| Version | 3.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 31 Mar 2020 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

/\*<![CDATA[\*/
div.rbtoc1785509932898 {padding: 0px;}
div.rbtoc1785509932898 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785509932898 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#GP2GPv3.0.0-Introduction)
- [Compliance and Assurance](#GP2GPv3.0.0-ComplianceandAssurance)
- [Requirements](#GP2GPv3.0.0-Requirements)
  - [Message Fragments and Examples](#GP2GPv3.0.0-MessageFragmentsandExamples)
  - [Supplementary specifications](#GP2GPv3.0.0-Supplementaryspecifications)
- [Dependencies](#GP2GPv3.0.0-Dependencies)
- [Roadmap](#GP2GPv3.0.0-Roadmap)

# Introduction

The GP2GP record transfer mechanism enables a patient's record to be electronically transferred directly and securely when they move from one practice to another.

# Compliance and Assurance

The compliance baseline for GP2GP and document locations were correct at the time of original publication, but referenced documents can now be found embedded on this page, below. The exceptions to this are the references to the NHS Messaging Implementation Manual (MIM) and External Interface Specification (EIS) (follow these links for details).

[GP2GP 1.1a Compliance Mo…](GP2GP-v300.md)

The GP2GP assurance is split into 2 streams:

1. Compliance testing - this tests the spine messaging patterns and functionality
2. Interoperability Testing - the testing of the clinically semantic testing of the message payload between different systems

For advice and support on assurance please contact [businesspartners@nhs.net](mailto:businesspartners@nhs.net) or visit <https://digital.nhs.uk/services/nhs-business-partners>

# Requirements

| ID | Description | Level |
| --- | --- | --- |
| GP2GP00 | Suppliers must meet the requirements for GP2GP 1.1a | MUST |
| GP2GP01 | Suppliers must meet the requirements for GP2GP 2.2a  [HSCIC-PC-BLD-0068 26 GP2…](GP2GP-v300.md) | MUST |
| GP2GP02 | Suppliers must make available documentation to ensure that suppliers receiving GP2GP messages are fully able to interpret, consume and process the data to minimise data loss and degradation. This must include (but is not limited to):   - Structure of data - Any know issues or anomalies and how they should be handled - Code sets and associated meanings - Field specifications (types, lengths etc.) | MUST |
| GP2GP03 | Suppliers must provide support to receivers of GP2GP messages to resolve any issues with interpreting,consuming and processing received messages | MUST |
| GP2GP04 | Suppliers must meet the requirements for GP2GP 2.2b  [HSCIC-PC-BLD-0068 26 GP2…](GP2GP-v300.md) | MUST |

## Message Fragments and Examples

[NPFIT-FNT-TO-TIN-0562[1]…](GP2GP-v300.md)

## Supplementary specifications

The following supplemental specifications contain additional requirements and guidance for GP2GP implementation:

[NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-FNT-TO-TIN-1087.02%20GP2GP%20Supplementary%20Specification%20on%20Handling%20Medication%20Discontinuation.pdf?version=1&modificationDate=1678108066428&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0069%2024%20GP2GP%20Spine%20Technical%20Design%20v7.1.pdf?version=1&modificationDate=1678108066187&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0083.08%20GP2GP%20Response%20Codes.pdf?version=1&modificationDate=1678108065943&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0099.04%20GP2GP%20Handling%20Missing%20Attachments.pdf?version=1&modificationDate=1678108065690&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0132.03%20GP2GP%20Supplementary%20Specification%20on%20Structured%20Degrade%20Handling.pdf?version=1&modificationDate=1678108065472&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0133.02%20GP2GP%20Supplementary%20Spec%20-%20Handling%20and%20Propagation%20of%20Non%20Consultation%20Data.pdf?version=1&modificationDate=1678108065253&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0134.05%20GP2GP%20Supplementary%20Specification%20Representing%20PMIP%20Data%20in%20GP2GP%20Messages.pdf?version=1&modificationDate=1678108065021&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0158%20GP2GP%20Supplementary%20Specification%20Attachment%20References.pdf?version=1&modificationDate=1678108064796&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0163.02%20Topic%20and%20Category%20Handling%20in%20GP2GP.pdf?version=1&modificationDate=1678108064574&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0170.03%20GP2GP%20SS%20Handling%20Large%20Messages.pdf?version=1&modificationDate=1678108064351&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf](https://gpitbjss.atlassian.net/wiki/download/attachments/1391134336/NPFIT-PC-BLD-0171.02%20GP2GP%20SS%20Harvesting%20Management%20Information.pdf?version=1&modificationDate=1519839943050&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0172.02%20GP2GP%20UC1%20Transfer%20Electronic%20Health%20Record.pdf?version=1&modificationDate=1678108063889&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0173.01%20GP2GP%20UC%202%20Harvest%20and%20Prepare%20Management%20Information.pdf?version=1&modificationDate=1678108063676&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0175.03%20GP2GP%20SS%20Handling%20A-B-A%20Transfers%20v1.3.pdf?version=1&modificationDate=1678108063440&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0177.01%20GP2GP%20SS%20User%20Experience.pdf?version=1&modificationDate=1678108063201&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0178%2002%20GP2GP%20Coding%20Scheme%20Translation%20v1.1.pdf?version=1&modificationDate=1678108062963&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-0180.02%20GP2GP%20Transfer%20of%20Patient%20Facing%20Service%20Settings%2004.pdf?version=1&modificationDate=1678108062743&cacheVersion=1&api=v2)

[NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-PC-BLD-181.02%20GP2GP%20Handling%20the%20SCR%20indicator%20v03.pdf?version=1&modificationDate=1678108062522&cacheVersion=1&api=v2)

[NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-FNT-TO-IG-DES-0115.01%20Statement%20on%20Data%20Retention%20v1.0.pdf?version=1&modificationDate=1678108062312&cacheVersion=1&api=v2)

[NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-FNT-TO-TAR-0017.07%20Compliance%20Requirements%20for%20Patient%20Registration.pdf?version=1&modificationDate=1678108062077&cacheVersion=1&api=v2)

[NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/12334170145/NPFIT-FNT-TO-TIN-0289.08%20GP2GP%20Supplementary%20Specification%20on%20Handling%20Attachment%20Types.pdf?version=1&modificationDate=1678108061857&cacheVersion=1&api=v2)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)

# Roadmap

| Title |
| --- |
| No content found. |

## Attachments

- [HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170164-HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf)
- [NPFIT-FNT-TO-TIN-0379.03 System Walkthrough and Induction Pack.ppt](../../../../.raw/DCSDCS/attachments/12334170145/att12334170167-NPFIT-FNT-TO-TIN-0379.03 System Walkthrough and Induction Pack.ppt)
- [NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc](../../../../.raw/DCSDCS/attachments/12334170145/att12334170170-NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc)
- [NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170173-NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf)
- [NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170176-NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf)
- [NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170179-NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf)
- [NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170182-NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf)
- [NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170185-NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf)
- [NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170188-NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf)
- [NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170191-NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf)
- [NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170194-NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf)
- [NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170197-NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf)
- [NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170200-NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf)
- [NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170203-NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf)
- [NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170206-NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf)
- [NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170209-NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf)
- [NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170212-NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf)
- [NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170215-NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf)
- [NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170218-NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf)
- [NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170221-NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf)
- [NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170224-NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf)
- [NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170227-NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf)
- [NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170230-NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf)
- [NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf](../../../../.raw/DCSDCS/attachments/12334170145/att12334170233-NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf)
- [GP2GP 1.1a Compliance Module.doc](../../../../.raw/DCSDCS/attachments/12334170145/att12334170236-GP2GP 1.1a Compliance Module.doc)
