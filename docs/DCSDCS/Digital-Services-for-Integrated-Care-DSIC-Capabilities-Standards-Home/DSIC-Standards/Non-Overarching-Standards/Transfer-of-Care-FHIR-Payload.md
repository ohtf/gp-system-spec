---
page_id: "11888099337"
space: "DCSDCS"
title: "Transfer of Care FHIR Payload"
version: 13
updated: "2026-07-22T13:15:29.854Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11888099337/Transfer+of+Care+FHIR+Payload"
labels: ["standard"]
---

# Transfer of Care FHIR Payload

|  |  |
| --- | --- |
| **ID** | S79 |
| **Version** | 1.0.2 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#TransferofCareFHIRPayload-Introduction)
- [Requirements](#TransferofCareFHIRPayload-Requirements)
- [Compliance, Assurance and Testing](#TransferofCareFHIRPayload-Compliance,AssuranceandTesting)
- [Documentation](#TransferofCareFHIRPayload-Documentation)
- [Dependencies](#TransferofCareFHIRPayload-Dependencies)
- [Roadmap](#TransferofCareFHIRPayload-Roadmap)

# Introduction {#TransferofCareFHIRPayload-Introduction}

Patients move between care settings and responsibility for them is handed over from one Clinician to another. Transfer of Care messaging ensures that the clinical context and information about the Patient is transferred when this occurs.

To receive and process Transfer of Care FHIR documents, GP IT Suppliers are expected to provide their practice Solutions with a [Generic FHIR Receiver](Generic-FHIR-Receiver.md) capability. The Generic FHIR Receiver is a crucial common requirement across several of The Authority’s current programmes.

The scope for Transfer of Care currently covers:

- **Inpatient and Day Case Discharge Summary Document** – An ITK3 FHIR Document containing Transfer of Care information supporting inpatient and day case discharges typically between an acute hospital and GP Practice.
- **Emergency Care Discharge Summary Document** – An ITK3 FHIR Document containing Transfer of Care information supporting a discharge typically between an emergency care department and a GP Practice.
- **Inpatient and Day Case Discharge Summary (Mental Health) Document** – An ITK3 FHIR Document containing Transfer of Care information supporting a mental health adult discharge summary to a GP Practice.
- **Outpatient Clinic Letter Document** – An ITK3 FHIR Document containing Transfer of Care information between the hospital clinic and the GP and other relevant parties following a consultation in a clinic.

The four defined Transfer of Care messages uses the [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md) service for transport and the [Interoperability Toolkit (ITK)](Interoperability-Toolkit-ITK.md) version 3.0 specification as the message distribution specification.

Transfer of Care is about standardisation of the correspondence elements. As this is an interoperability piece of work, both Secondary Care and Primary Care need to support the standardisation changes. These are as follows:

- **CLINICAL CONTENT LAYER** – PRSB headings/sections & subheadings/elements
- **TERMINOLOGY LAYER** – SNOMED-CT and dm+d
- **TECHNOLOGY LAYER** – FHIR (HL-7) as the structure for carrying information
- **TRANSPORT LAYER** – MESH for direct electronic transfer to GP IT foundation systems
- **BUSINESS LAYER** – ITK3 Response Codes fed back to the Hospital from the GP IT foundation system confirming message has been processed and is relevant.

# Requirements {#TransferofCareFHIRPayload-Requirements}

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| **TCFHIR-01** | Implement and maintain the functionality needed to receive and process Transfer of Care FHIR documents. | MUST |

# Compliance, Assurance and Testing {#TransferofCareFHIRPayload-Compliance,AssuranceandTesting}

See the Transfer of Care (TOC) FHIR Payload section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation {#TransferofCareFHIRPayload-Documentation}

The latest FHIR specifications for the Transfer of Care payload can be accessed at <https://developer.nhs.uk/transfer-care-specification-versions/>.

Contextual detail and specifications pertaining to the MVP aspect of this work can be accessed via the Transfer of Care Payload V0.7 document below:

[Transfer of Care Payload…](../../../../attachments/DCSDCS/11888099337/att13201768454-Transfer of Care Payload V.07.docx)

The Transfer of Care FHIR messages will use the ITK3 (Interoperability Toolkit) specification available here <https://developer.nhs.uk/interoperability-tool-kit-itk-specification-versions/>. Suppliers should also consider the advice in the [Good Practice Guidelines for GP electronic patient records](https://www.england.nhs.uk/digital-gp-good-practice-guidance/).

# Dependencies {#TransferofCareFHIRPayload-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Generic FHIR Receiver](Generic-FHIR-Receiver.md)

# Roadmap {#TransferofCareFHIRPayload-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [Transfer of Care Payload V.07.docx](../../../../attachments/DCSDCS/11888099337/att13201768454-Transfer of Care Payload V.07.docx)
- [Transfer of Care - MVP Payload 0_7.docx](../../../../attachments/DCSDCS/11888099337/att13202063379-Transfer of Care - MVP Payload 0_7.docx)
