---
page_id: "1391133745"
space: "DCSDCS"
title: "Clinical Document Architecture (CDA)"
version: 16
updated: "2026-07-21T14:22:02.075Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133745/Clinical+Document+Architecture+CDA"
labels: ["standard"]
---

# Clinical Document Architecture (CDA)

|  |  |
| --- | --- |
| **ID** | S64 |
| **Version** | 1.0.0 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 01 Apr 2019 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#ClinicalDocumentArchitecture(CDA)-Introduction)
- [Requirements](#ClinicalDocumentArchitecture(CDA)-Requirements)
- [Dependencies](#ClinicalDocumentArchitecture(CDA)-Dependencies)
- [Roadmap](#ClinicalDocumentArchitecture(CDA)-Roadmap)

# Introduction

CDA is an XML-based HL7 standard for exchange of clinical information.

The only mandated use of CDA in general practice IT is receipt of [111](111.md) CDA referrals and reports.  However many localities have implemented solutions to ingest external documents in various formats including CDA.  For this reason suppliers may consider implementing CDA handling functionality for other use cases and payloads.

However it should be noted that NHS standards for structured clinical document transmission are now being developed around [FHIR](https://hl7.org/fhir) and [ITK3](Interoperability-Toolkit-ITK.md) and use of CDA is likely to be deprecated in the near future.

# Requirements

If a system sends or receives CDA messages it must comply with the requirements included in the CDA document set:

[HSCIC-FNT-TO-TAR-0082.02…](Clinical-Document-Architecture-CDA.md)

[HSCIC-FNT-TO-TAR-0081.03…](Clinical-Document-Architecture-CDA.md)

[HSCIC-FNT-TO-TAR-0080.03…](Clinical-Document-Architecture-CDA.md)

[HSCIC-FNT-TO-TAR-0079.03…](Clinical-Document-Architecture-CDA.md)

[HSCIC-FNT-TO-TAR-0095.02…](Clinical-Document-Architecture-CDA.md)

[HSCIC-FNT-TO-TAR-0092.04…](Clinical-Document-Architecture-CDA.md)

[HSCIC-FNT-TO-TAR-0083 02…](Clinical-Document-Architecture-CDA.md)

# Dependencies

There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents.

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [HSCIC-FNT-TO-TAR-0081.03 CDA Document Technical Requirements v2.1.docx](../../../../.raw/DCSDCS/attachments/1391133745/att1391138598-HSCIC-FNT-TO-TAR-0081.03 CDA Document Technical Requirements v2.1.docx)
- [HSCIC-FNT-TO-TAR-0092.04.01 CDA - Management Information v3.1.docx](../../../../.raw/DCSDCS/attachments/1391133745/att1391139040-HSCIC-FNT-TO-TAR-0092.04.01 CDA - Management Information v3.1.docx)
- [HSCIC-FNT-TO-TAR-0080.03 CDA Document Receiver Requirements V2.2.docx](../../../../.raw/DCSDCS/attachments/1391133745/att1391139041-HSCIC-FNT-TO-TAR-0080.03 CDA Document Receiver Requirements V2.2.docx)
- [HSCIC-FNT-TO-TAR-0095.02 Clinical Documents - Attachment Types v2.0 (1).docx](../../../../.raw/DCSDCS/attachments/1391133745/att1391139050-HSCIC-FNT-TO-TAR-0095.02 Clinical Documents - Attachment Types v2.0 (1).docx)
- [HSCIC-FNT-TO-TAR-0083 02 CDA Interoperability - Point to Point Error Codes v2.0.docx](../../../../.raw/DCSDCS/attachments/1391133745/att1391139073-HSCIC-FNT-TO-TAR-0083 02 CDA Interoperability - Point to Point Error Codes v2.0.docx)
- [HSCIC-FNT-TO-TAR-0082.02 CDA Interoperability - MHS Requirements v1.1.docx](../../../../.raw/DCSDCS/attachments/1391133745/att1391139097-HSCIC-FNT-TO-TAR-0082.02 CDA Interoperability - MHS Requirements v1.1.docx)
- [HSCIC-FNT-TO-TAR-0079.03 CDA Document Sender Requirements V2.1.docx](../../../../.raw/DCSDCS/attachments/1391133745/att1391139127-HSCIC-FNT-TO-TAR-0079.03 CDA Document Sender Requirements V2.1.docx)
