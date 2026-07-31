---
page_id: "1933607010"
space: "DCSDCS"
title: "GP2GP v2.0.0"
version: 1
updated: "2020-04-02T09:53:00.182Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1933607010/GP2GP+v2.0.0"
labels: ["interop_standard_retired"]
---

# GP2GP v2.0.0

|  |  |
| --- | --- |
| ID | S43 |
| Version | 2.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 31 Dec 2019 |

- [Introduction](#GP2GPv2.0.0-Introduction)
- [Compliance and Assurance](#GP2GPv2.0.0-ComplianceandAssurance)
- [Requirements](#GP2GPv2.0.0-Requirements)
  - [Message Fragments and Examples](#GP2GPv2.0.0-MessageFragmentsandExamples)
  - [Supplementary specifications](#GP2GPv2.0.0-Supplementaryspecifications)
- [Dependencies](#GP2GPv2.0.0-Dependencies)
- [Roadmap](#GP2GPv2.0.0-Roadmap)

# Introduction

The GP2GP record transfer mechanism enables a patient's record to be electronically transferred directly and securely when they move from one practice to another.

# Compliance and Assurance

The compliance baseline for GP2GP and document locations were correct at the time of original publication, but referenced documents can now be found embedded on this page, below. The exceptions to this are the references to the NHS Messaging Implementation Manual (MIM) and External Interface Specification (EIS) (follow these links for details).

[GP2GP 1.1a Compliance Mo…](GP2GP-v200.md)

The GP2GP assurance is split into 2 streams:

1. Compliance testing - this tests the spine messaging patterns and functionality
2. Interoperability Testing - the testing of the clinically semantic testing of the message payload between different systems

For advice and support on assurance please contact [businesspartners@nhs.net](mailto:businesspartners@nhs.net) or visit https://digital.nhs.uk/services/nhs-business-partners

# Requirements

| ID | Description | Level |
| --- | --- | --- |
| GP2GP00 | Suppliers must meet the requirements for GP2GP 1.1a | MUST |
| GP2GP01 | Suppliers must meet the requirements for GP2GP 2.2a.   [HSCIC-PC-BLD-0068 26 GP2…](GP2GP-v200.md) | MUST |
| GP2GP02 | Suppliers must make available documentation to ensure that suppliers receiving GP2GP messages are fully able to interpret, consume and process the data to minimise data loss and degradation. This must include (but is not limited to):   - Structure of data - Any know issues or anomalies and how they should be handled - Code sets and associated meanings - Field specifications (types, lengths etc.) | MUST |
| GP2GP03 | Suppliers must provide support to receivers of GP2GP messages to resolve any issues with interpreting,consuming and processing received messages | MUST |
| GP2GP04 | Suppliers should meet the requirements for GP2GP 2.2b.  Suppliers should note these requirements will become MUST in the future, please see Roadmap for details.  [HSCIC-PC-BLD-0068 26 GP2…](GP2GP-v200.md) | SHOULD |

## Message Fragments and Examples

[NPFIT-FNT-TO-TIN-0562[1]…](GP2GP-v200.md)

## Supplementary specifications

The following supplemental specifications contain additional requirements and guidance for GP2GP implementation:

[NPFIT-FNT-TO-TIN-1087.02 GP2GP Supplementary Specification on Handling Medication Discontinuation.pdf](#)

[NPFIT-PC-BLD-0069 24 GP2GP Spine Technical Design v7.1.pdf](#)

[NPFIT-PC-BLD-0083.08 GP2GP Response Codes.pdf](#)

[NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf](#)

[NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf](#)

[NPFIT-PC-BLD-0133.02 GP2GP Supplementary Spec - Handling and Propagation of Non Consultation Data.pdf](#)

[NPFIT-PC-BLD-0134.05 GP2GP Supplementary Specification Representing PMIP Data in GP2GP Messages.pdf](#)

[NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf](#)

[NPFIT-PC-BLD-0163.02 Topic and Category Handling in GP2GP.pdf](#)

[NPFIT-PC-BLD-0170.03 GP2GP SS Handling Large Messages.pdf](#)

[NPFIT-PC-BLD-0171.02 GP2GP SS Harvesting Management Information.pdf](#)

[NPFIT-PC-BLD-0172.02 GP2GP UC1 Transfer Electronic Health Record.pdf](#)

[NPFIT-PC-BLD-0173.01 GP2GP UC 2 Harvest and Prepare Management Information.pdf](#)

[NPFIT-PC-BLD-0175.03 GP2GP SS Handling A-B-A Transfers v1.3.pdf](#)

[NPFIT-PC-BLD-0177.01 GP2GP SS User Experience.pdf](#)

[NPFIT-PC-BLD-0178 02 GP2GP Coding Scheme Translation v1.1.pdf](#)

[NPFIT-PC-BLD-0180.02 GP2GP Transfer of Patient Facing Service Settings 04.pdf](#)

[NPFIT-PC-BLD-181.02 GP2GP Handling the SCR indicator v03.pdf](#)

[NPFIT-FNT-TO-IG-DES-0115.01 Statement on Data Retention v1.0.pdf](#)

[NPFIT-FNT-TO-TAR-0017.07 Compliance Requirements for Patient Registration.pdf](#)

[NPFIT-FNT-TO-TIN-0289.08 GP2GP Supplementary Specification on Handling Attachment Types.pdf](#)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- External Interface Specification (EIS)
- NHS Messaging Implementation Manual (MIM)

# Roadmap

| Title |
| --- |
| No content found. |

## Attachments

- [HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf](../../../../.raw/DCSDCS/attachments/1933607010/att1931116791-HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2.pdf)
- [GP2GP 1.1a Compliance Module.doc](../../../../.raw/DCSDCS/attachments/1933607010/att1933541465-GP2GP 1.1a Compliance Module.doc)
- [NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc](../../../../.raw/DCSDCS/attachments/1933607010/att1933574229-NPFIT-FNT-TO-TIN-0562[1].02 GP2GP Message Fragments and Examples.doc)
