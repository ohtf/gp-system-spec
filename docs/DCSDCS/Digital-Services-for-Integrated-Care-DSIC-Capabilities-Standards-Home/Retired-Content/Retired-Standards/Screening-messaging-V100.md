---
page_id: "11975327854"
space: "DCSDCS"
title: "Screening messaging V1.0.0"
version: 2
updated: "2022-05-10T10:53:04.385Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11975327854/Screening+messaging+V1.0.0"
labels: ["interop_standard_retired"]
---

# Screening messaging V1.0.0

|  |  |
| --- | --- |
| ID | S58 |
| Version | 1.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

/\*<![CDATA[\*/
div.rbtoc1785509684254 {padding: 0px;}
div.rbtoc1785509684254 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785509684254 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#ScreeningmessagingV1.0.0-Introduction)
- [Compliance and Assurance](#ScreeningmessagingV1.0.0-ComplianceandAssurance)
- [Requirements](#ScreeningmessagingV1.0.0-Requirements)
- [Documentation](#ScreeningmessagingV1.0.0-Documentation)
- [Dependencies](#ScreeningmessagingV1.0.0-Dependencies)
- [Roadmap](#ScreeningmessagingV1.0.0-Roadmap)

# Introduction

Some screening programmes use the Digital Diagnostics & Pathology Messaging standards to return results to GP systems. Variant NHS004 of the Medical Service Report (MEDRPT) message was created to enable it to carry screening results.

In addition to the minor changes to the message definition, the system is required to identify NHS004 messages as ‘screening messages’ rather than pathology messages and to present them as such to users for processing.

# Compliance and Assurance

For advice and support on assurance please contact businesspartners@nhs.net or visit https://digital.nhs.uk/services/nhs-business-partners

# Requirements

| Req ID | Requirement | Level |
| --- | --- | --- |
| SRN1 | The system MUST support MIG variant NHS004 of the EDIFACT Laboratory Service Report (MEDRPT) message. | MUST |
| SRN2 | The system MUST perform the same validation checks (e.g. EDIFACT constructs, Patient, Receiving Organisation, sender/recipient identifiers, etc) on a NHS004 message as a NHS003 message with the exception of the clinical code validation check. | MUST |
| SRN3 | The system MUST comply with the requirements contained in the following document: Cancer Screening - eGP-Comms GP Software Supplier Requirements v4.1.doc | MUST |
| SRN4 | From time to time the authority will provide updates to terminology code list and associated terminology mapping tables contained in the ‘Cancer Screening - eGP-Comms GP Software Supplier Requirements v4.1.doc’ requirement document (see SRN3 above)  Updates will be published as an addendum to the issued document and will additionally provide a schedule for implementation. Suppliers MUST be compliant with the updated code list aligned to the published schedule. The schedule will allow at least 3 months for implementation. | MUST |

# Documentation

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- Messaging Exchange for Social Care and Health (MESH)

# Roadmap

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [Cancer Screening - eGP-Comms GP Software Supplier Requirements v4.1.doc](../../../../.raw/DCSDCS/attachments/11975327854/att11975327871-Cancer Screening - eGP-Comms GP Software Supplier Requirements v4.1.doc)
