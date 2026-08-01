---
page_id: "1391133752"
space: "DCSDCS"
title: "Digital Diagnostics & Pathology Messaging"
version: 26
updated: "2026-07-21T14:23:04.361Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133752/Digital+Diagnostics+Pathology+Messaging"
labels: ["standard"]
---

# Digital Diagnostics & Pathology Messaging

|  |  |
| --- | --- |
| **ID** | S34 |
| **Version** | 1.0.2 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#DigitalDiagnostics&PathologyMessaging-Introduction)
- [Requirements](#DigitalDiagnostics&PathologyMessaging-Requirements)
  - [Using Lab Results Adaptor](#DigitalDiagnostics&PathologyMessaging-UsingLabResultsAdaptor)
  - [Without using Lab results Adaptor](#DigitalDiagnostics&PathologyMessaging-WithoutusingLabresultsAdaptor)
- [Compliance, Assurance and Testing](#DigitalDiagnostics&PathologyMessaging-Compliance,AssuranceandTesting)
- [Documentation](#DigitalDiagnostics&PathologyMessaging-Documentation)
  - [Using Lab Results adaptor](#DigitalDiagnostics&PathologyMessaging-UsingLabResultsadaptor)
  - [Without using Lab Results adaptor](#DigitalDiagnostics&PathologyMessaging-WithoutusingLabResultsadaptor)
- [Dependencies](#DigitalDiagnostics&PathologyMessaging-Dependencies)
- [Roadmap](#DigitalDiagnostics&PathologyMessaging-Roadmap)

# Introduction {#DigitalDiagnostics&PathologyMessaging-Introduction}

Pathology messaging involves the electronic transmission of results of pathology tests to GP systems in response to a test request placed with laboratories.

# Requirements {#DigitalDiagnostics&PathologyMessaging-Requirements}

To comply with the Digital Diagnostics & Pathology Messaging Standard there are currently two implementation options:

1. Using Lab Results adaptor
2. Without using Lab Results adaptor

### **Using Lab Results Adaptor** {#DigitalDiagnostics&PathologyMessaging-UsingLabResultsAdaptor}

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| DDP05 | If implementing Digital Diagnostics & Pathology Messaging using the Lab Results adaptor (aka EDIFACT adaptor):   - Suppliers to Implement and maintain the adapter inline with the latest specification of the[Lab Results adaptor - NHS Digital](https://digital.nhs.uk/developer/api-catalogue/lab-results-adaptor)   The adaptor provides a pre-assured implementation of the Digital Diagnostics & Pathology Messaging Standard and covers requirements DDP02, DDP03 and DDP04 below. | MUST |

### **Without using Lab results Adaptor** {#DigitalDiagnostics&PathologyMessaging-WithoutusingLabresultsAdaptor}

|  |  |  |
| --- | --- | --- |
| **ID** | **Requirement** | **Level** |
| DDP02 | The system SHOULD continue to support the use of the v1.001 version (also known as MIG variant NHS002) of the (Pathology) Laboratory Service Report message. | SHOULD |
| DDP03 | Retransmission of a Pathology PMIP EDIFACT Acknowledgement message MUST be solely in response to a request from the receiving organisation: automatic retransmission is not acceptable. | MUST |
| DDP04 | The EDI management software for EDIFACT messages MUST comply with the requirements specified in 'Core Functional Requirements for EDI Management Software in the NHS', sections:   - General - Sending Interchanges - Receiving Interchanges | MUST |

#### NPFIT-FNT-TO-TAR-0103.01 Pathology Messaging - GP System Requirements {#DigitalDiagnostics&PathologyMessaging-NPFIT-FNT-TO-TAR-0103.01PathologyMessaging-GPSystemRequirements}

#### Introduction {#DigitalDiagnostics&PathologyMessaging-Introduction.1}

This document has been written as an update to the suite of pathology messaging documents published in 2000 by the Pathology Messaging Enabler Programme and subsequently the Pathology Messaging Implementation Programme.   
The previously published, and still mostly current, documentation comprises MS Word 232 files in 14 folders with many thousands of hyperlinks between the documents resulting in a 'pack' or approximately 32Mb. Since its publication, much of the messaging infrastructure used to carry messages between organisations has been replaced, the organisation who authored the requirements has been decommissioned and the tooling to generate and maintain the hyperlinks is also no longer available. Some of the requirements have also changed (e.g. the need to encrypt the messages).  
For convenience, and to align with common reference, the documentation is referred to as the 'PMIP Specs' and will be referred to as such within this document.

#### Document Purpose {#DigitalDiagnostics&PathologyMessaging-DocumentPurpose}

The purpose of this document is:

- to provide a description of the scope of the requirements in the various sections (folders) of documentation,
- to highlight any obsolete requirements and
- to document any changed requirements.

#### Audience {#DigitalDiagnostics&PathologyMessaging-Audience}

The intended audiences for this document are:

- GP System Suppliers
- Laboratory System Suppliers
- Laboratory 'Middleware' Suppliers
- Any NHS/DHSC Authority who is or may become the owner or custodian of these requirements

#### Document Scope {#DigitalDiagnostics&PathologyMessaging-DocumentScope}

The scope of the requirements is Laboratory to GP Practice Results Messaging for the following clinical disciplines:

- Haematology
- Biochemistry
- Microbiology (limited)

The requirements do NOT cover any other disciplines, lab to lab messaging or test requests/orders.

#### Description of Documentation {#DigitalDiagnostics&PathologyMessaging-DescriptionofDocumentation}

The PMIP Specs were published to GP system Suppliers under the 'RFA' scheme, the latest version being RFA99 v1.2. Within this release they were listed under the 'Clinical Messages' folder. At the time, the intention was to produce further clinical messaging requirements for domains such as Radiology and Discharge and so the requirements were written generically and structured in such as way as to allow other domains to be readily added with little change.  
Beneath the 'Clinical Messages' folder are 14 sub-folders, each of which is listed and described in the table below.

|  |  |
| --- | --- |
| **Folder Name** | **Description of Contents** |
| ACK | **NHS Standard for Acknowledgement of Clinical Messages – Message Specifications**  Contains the 'NHSACK' EDIFACT message specifications- information content (profile), implementation guidelines, change notes and message definition. |
| CEG | **Specification of Clinical EDI Functions for GP Systems**  Provides a framework for the description of the functional requirements of GP systems in relation to all clinical EDI information flows and specifically covers the functional requirements in relation to GP systems receiving pathology results reports from Laboratories and their acknowledgement. |
| CEP | **Pathology Messaging Requirements**  Provides a framework for the description of the functional requirements of Pathology systems in relation to all clinical EDI information flows and specifically covers the functional requirements in relation to Pathology Laboratory systems sending pathology results reports from to GPs and receiving their acknowledgements. |
| EDIG | **Core Functional Requirements for EDI Management Software in the NHS**  The requirements represent the generic set of EDI functional requirements for EDIFACT clinical messaging flows in the NHS. They represent a minimum set of requirements for EDI management software, including EDI gateways.  They do not cover   - Information flow (message) specific EDI software requirements. - Details of interfaces between EDI software and application software, messaging software or security software. |
| ISR | **IRM Solutions Register**  Contains a list of all the issues raised during the Pathology messaging 'pilots' together with the proposed resolutions. The IRM (Issues Resolution Mechanism) membership comprised Pathology laboratory staff, GPs, Suppliers |
| JCG | **Joint Computing Group** **of the** **Royal College of General Practitioners** **&** **General Medical Services Committee - EDI-RELATED** **APPLICATION FUNCTIONALITY** **IN GP CLINICAL SYSTEMS:** **USER REQUIREMENTS V1.0**  This document contains the General Practice user requirements upon which the requirements documented in the CEG folder are based. The document is intended for designers and developers of GP systems who wish to implement Clinical EDI. It aims to strike a balance between the need to ensure the provision of sufficient functionality to make early implementations of Clinical EDI useable by General Practitioners and their practice staff, while not asking the impossible of GP Systems Suppliers and as such the specifications describe to Suppliers the minimal functionality that they must provide.  Since it is in both Suppliers' and customers' interests that implementations are as useful as possible, this document also specifies functionality beyond the minimal set of requirements. |
| LSR | **NHS Standard for Pathology Reports - Laboratory Service Report Message Specifications**  Contains the 'MEDRPT' EDIFACT message specifications- information content (profile), implementation guidelines, change notes, message definition, code lists and UOM recommendations. |
| MREJ | **Potential Types of Error in Clinical Messaging and Requirements for their Detection and Rejection**  Provides an expandable framework for the description of potential error types in all clinical messaging; and in this version is populated solely to accommodate those messages associated with Pathology results reporting to General Practice.  It lists those errors which are applicable to the EDI messaging defined by PMEP and the types of error that are generic to both EDI messaging and to EDIFACT messages, and also those that are specific to the individual message types. |
| PMEP | **PMEP Technical Products**  This is the 'root' document that links to all the other folders and documents and is the 'point of entry' into the PMIP Specs. |
| RAD | **Version 1 Trial NHS Standard EDIFACT Messages for Radiology Requests and Reports**  This is essentially the same as the LSR folder but contains the raw message documentation without the detailed tailoring and implementation profiles that have been developed for Pathology through the Pathology Messaging Enabler Project. As such the Radiology Request and Report messaging Standards have never been officially sanctioned for use and remain as 'trial' Standards. |
| READ | **Laboratory Messaging Subset**  Defines the content and file structure of the set of Read codes used to uniquely identify the Pathology tested being reported and the timescales for implementing new versions of the subset. |
| SPEC | **Version 1 Trial NHS Standard EDIFACT Messages for GP-Hospital Specialist Service Request & Report**  This has the same status as the RAD folder, i.e. it contains the raw message documentation without the detailed tailoring and implementation profiles that have been developed for Pathology through the Pathology Messaging Enabler Project. As such the Hospital Specialist Service Request and Report messaging Standards have never been officially sanctioned for use and remain as 'trial' Standards. |
| SRID | **Using Sender/Recipient Identifiers**  Provides guidance to Suppliers/organisations on how to use Sender/Recipient Identifiers within the NHS EDI Naming Schema when implementing electronic messaging. |
| TCON | **Technical Messaging and Networking Requirements for Secure EDI**  Contains the technical messaging and networking requirements for Trusts and General Practice use of secure EDI. |

#### Terminology & High-Level Requirement Changes {#DigitalDiagnostics&PathologyMessaging-Terminology&High-LevelRequirementChanges}

The major changes to the Pathology messaging environment that have occurred since 2000 are described below. The impact of these changes varied with any consequential changes to messaging systems having been made and the systems have now been operating successfully without change for approximately 10 years. However, the PMIP Specs have not been updated to reflect these changes and it is therefore necessary to document the changes to enable a new reader to fully understand the requirements.

|  |  |
| --- | --- |
| **Ref:** | **Description of Change and its consequence** |
| 1 | Change: The NHS **Cryptography** Service has been decommissioned and there is therefore no longer a requirement for Laboratories to encrypt messages before sending to GPs or for GPs to decrypt messages upon receipt. |
|  | Consequence: All references to 'cryptography', 'encryption' and 'decryption' in the PMIP Specs should therefore be ignored. |
| 2 | Change: The **NHS X.400** messaging system, also referred to as the '**MMHS'**, was replaced by the 'Data Transfer Service' (DTS). DTS has subsequently been replaced by 'Message Exchange for Social Care and Health' (**MESH**). All pathology messages must now be sent over MESH. The requirements to audit the transport level delivery status of messages still remains – system must record the MESH delivery status instead of the X.400 delivery status. |
|  | Consequence: All references to 'X.400' shall be interpreted as references to 'MESH'. All references to 'MMHS' shall be interpreted as the 'message handling service' which is currently MESH. |
| 3 | Change: The '**NHSnet**' network has been replaced by the '**N3**' network which itself is undergoing a re-procurement. The N3 network is currently being transition to the next generation 'Health and Social Care Network' (**HSCN**) but will essentially remain the underlying network for the NHS. |
|  | Consequence: All references to 'NHSnet' shall be interpreted as references to 'N3/HSCN'. |
| 4 | Change: The '**Codesets**' (the allowable subset of Read codes that can be used for reporting) has become the 'Pathology Bounded Code List' or 'PBCL'. It is maintained by the UKTC (UK Terminology Centre) and updates are released every 6 months. Additional 'bonus' files now provide the equivalent CTV3 code for each Read2 code. |
|  | Consequence: The UKTC PBCL publications and associated documentation is the authoritative source of Pathology result 'Codeset' data and the 'READ' folder requirements are limited to the use of the codes only. |
| 5 | Change: The latest UKTC **PBCL** files contain a default **UOM** (Units of Measure) for most of the PBCL codes. This is a new development intended to improve clinical safety by the adoption of Standardised units across laboratories. |
|  | Consequence: GP Systems will receive less variability in UOMs which will enable greater potential for graphing (where this is not disallowed). System should also use these defaults when results are entered manually. |
| 6 | Change: Another recent change to the **PBCL** release is that each test is flagged to indicate whether it is safe to combine results (e.g. for graphing). |
|  | Consequence: Although there are no requirements to graph results it is known that Suppliers do provide such facilities in their systems. Where such facilities are provided, Suppliers should make any necessary changes to their systems to ensure they support these best clinical practice recommendations. |
| 7 | Change: Many of the folders have a document containing a **Glossary** and many of these glossary items no longer exist or are no longer applicable, for example   - GPnet - GPPL - Healthlink - NHSIA - NWN - OCS:this is now the Organisation Data Service - PMEP - PMIP - Project Connect |
|  | Consequence: These are historical projects or organisations and there are no materials from these entities that are required as part of the Pathology Messaging specifications and thus none need to be sought. |

#### Requirements Applicable to GP Systems {#DigitalDiagnostics&PathologyMessaging-RequirementsApplicabletoGPSystems}

The requirements applicable to GP systems are contained in the following subsections of the PMIP Specs:

- ACK
- CEG
- EDIG
- JCG
- LSR
- MREJ
- PMEP
- READ
- SRID
- TCON

Note: Some of the documents in the above sections will contain requirements for Laboratory systems as well as GP systems.  
**Of particular note** is the JCG section which contains a statement of GP User requirements from the Joint Computing Group of the RCGP and BMA. These requirements have been formally documented in the other sections and mostly in the CEG section. It is important to note the following:

- Some of the 'should' and 'may' requirements have since become 'shall' requirements as a result of requirements from other domains, e.g. the functional requirements for handling the receipt of CDA documents contain generic 'received report/document handling' requirements which apply equally to Pathology reports as they do CDA documents and any other received document. The CDA requirements also require systems to implement a common 'Inbox' or 'In-tray' containing all clinical communications, suitably categorised and identified to assist with user 'processing'.
- The patient matching algorithm specified in the CDA Functional Requirements – Receiver Requirements is different to that specified in CEG\_04\_C\_008. Systems should use the Patient matching rules stated in the CDA Functional Requirements rather than those used in the CEG requirements.

GP Suppliers will find it useful to read the CEP section which documents the requirements for Pathology laboratory systems as this provides useful information on how they populate messages.

#### High Level Requirements {#DigitalDiagnostics&PathologyMessaging-HighLevelRequirements}

|  |  |  |
| --- | --- | --- |
| **Req ID** | **Requirement Text** | **Level** |
| PM4.1.01 | System MUST meet all the requirements contained in the 'PMIP Specs' as listed at the beginning of this section ($5). | MUST |
| PM4.1.02 | Where conflicting, changed or expanded requirements are found in other GP system requirements documentation, including this document, the system MUST meet the requirement(s) stated in the latest published document. | MUST |
| PM4.1.02.1 | Systems MUST meet the Patient Matching (automatic and manual) requirements in the CDA Document Receiver Requirements in place of those listed in CEG\_04\_C\_008. | MUST |
| PM4.1.02.2 | System MUST support the 'Clinical Review' action (see CDA Document Receiver Requirements) instead of, or in addition to, the 'Viewed' status as specified in CEG\_04\_D\_008. A clinical user must now consciously indicate (by confirming that the action has taken place) that the report/document has been clinically reviewed rather than it being inferred by the system if the report/document has been displayed. | MUST |

#### Changes since initial publication of requirements {#DigitalDiagnostics&PathologyMessaging-Changessinceinitialpublicationofrequirements}

The main changes to the requirements since their initial publication are:

- The X.400 messaging systems has been decommissioned and was replaced by the Data Transfer Service (DTS), itself subsequently replace by 'Message Exchange for Social Care and Health' (MESH).
- The NHS Cryptography PKI Toolkit has been decommissioned and has not been replaced. Consequently there are no requirements to encrypt, decrypt or digitally stamp messages.
- NHSnet has been replaced by the N3 network. The N3 network is currently being transition to the next generation 'Health and Social Care Network' (**HSCN**)
- The 'Codelists' file, is now known at the Pathology Bounded Code List (PBCL) and is now subject to 6-monthly releases via TRUD along with a release note and an additional file providing mappings to CTV3 codes.

|  |  |  |
| --- | --- | --- |
| **Req ID** | **Requirement Text** | **Status** |
| PM4.2.01 | Systems MUST receive EDIFACT 'MEDRPT' (Pathology Result) messages, variant NHS003, over [MESH](Messaging-Exchange-for-Social-Care-and-Health-MESH.md) and MUST return acknowledgements over MESH. | MUST |
| PM4.2.01.1 | System MUST make the following 'translations' when reading the PMIP Specs:   - For 'MHS Address', read 'MESH Mailbox ID'. - For 'EDI Identifier' read 'MESH Sender/Recipient ID'. - For MMHS message ID, read MESH 'sequence identifier' (see MESH File Interface Specification) | MUST |
| PM4.2.02 | Systems MUST support the receiving and acknowledgement of unencrypted and not digitally stamped EDIFACT 'MEDRPT' (Pathology Result) messages.  Note: Systems SHOULD retain the ability to support encrypted Pathology messaging. | MUST |
| PM4.2.03 | Systems MUST use the Pathology Bounded Code List (see TRUD website) to validate received EDIFACT 'MEDRPT' (Pathology Result) messages. | MUST |
| PM4.2.03.1 | All implemented instances of the System MUST be updated with each new release of the PBCL by the implementation date for GP systems as documented in the PBCL Release Note. This will be no sooner than 1 month from the release date. | MUST |
| PM4.2.04 | Within LSR\_04\_C\_001.doc the Interchange number sequence should read 1..99,999,999 and not 1..999,999. Systems MUST restart Interchange numbering upon reaching 99,999,999 with the next Interchange being 1. | MUST |

#### Recent Changes {#DigitalDiagnostics&PathologyMessaging-RecentChanges}

During 2011-2012 a number of changes have been introduced into the Pathology Messaging domain. These have centred on the use of UOMs by laboratories. The changes are documented in the PBCL release documentation as published on TRUD and fall into three categories

1. A standard set of UOMs has been agreed by the pathology community and laboratories can only use UOM representations published in the Oct 2011 PBCL release pack.
2. Certain (Read-coded) tests/investigations have been assigned a default UOM and laboratories have been requested to adopt these defaults as soon as possible with effect from May 2012.
3. All (Read-coded) tests/investigations have also been assigned a 'combination' status – a status flag to indicate whether the results for a particular test can be safely combined, e.g. graphed. This is due to differences in the equipment used by different labs and thus the result (and reference range) from one lab may be legitimately different to that of another but they cannot be compared with each other.

The implications of these changes on GP systems will vary depending on the way in which GP systems function. There are no requirements for GP systems to validate UOMs or to use default UOMs when supporting manual entry of results or for systems to combine (e.g. graph) results, however, it is know that some GP systems do provide such functionality.

|  |  |  |
| --- | --- | --- |
| **Req ID** | **Requirement Text** | **Status** |
| PM4.3.01 | For manually entered pathology test results, the system SHOULD offer the default UOM for each test that has a default UOM assigned (see PBCL UOM Supplemental File – part of the PBCL release pack) | SHOULD |
| PM4.3.02 | Systems MAY validate received Pathology results against the UOM file to check for:   - A valid UOM (against the list of valid UOMs) - A correct UOM for the test (where a default UOM is specified)  If validation fails, the system MUST NOT change the onward processing of the message, i.e. it MUST continue to appear in the 'In-Tray' for the system. Such failed validations MAY be indicated to the user and SHOULD be logged in Audit Trails. | MAY  IF validation fails:  MUST , SHOULD |
| PM4.3.03 | Systems SHOULD NOT combine results (e.g. in graphical form) for a test if the PBCL\_CombinationCategory value for the test is '3' (Do not combine).  Note: Suppliers should seek latest documentation on combination category from the [PBCL Release Pack](https://isd.digital.nhs.uk/trud3/user/authenticated/group/0/pack/38) or other relevant source. | SHOULD NOT |

#### Detailed Requirement Changes & Errata {#DigitalDiagnostics&PathologyMessaging-DetailedRequirementChanges&Errata}

This section details errata and requirement changes in individual documents with the PMIP Specs.

#### ACK {#DigitalDiagnostics&PathologyMessaging-ACK}

None

#### CEG {#DigitalDiagnostics&PathologyMessaging-CEG}

|  |  |  |
| --- | --- | --- |
| **Filename** | **Section / Page** | **Description** |
| CEG\_01\_D\_007 | $2 | Ignore all references to cryptography and 'Digital Stamps'. |
| CEP\_02\_A\_007 | Various | Ignore all sections on and references to cryptography |
| CEG\_03\_C\_008 | $2 | Ignore all references to cryptography and 'Digital Stamps'.  For MHS Address, read MESH Mailbox ID. For EDI Identifier read MESH Sender/Recipient ID. |
| CEP\_04\_A\_008 | Various | Ignore all sections on and references to cryptography. |
| CEG\_04\_B\_007 | Various | Ignore all references to cryptography and 'Digital Stamps'. |
| CEG\_04\_C\_008 | $2   $3 | Ignore reference to "Intermittent dial-up connections via PSTN or ISDN" – systems are all permanently connected to N3/HSCN now. Ignore reference to "General (unstructured) E-mail".  Ignore all references to cryptography and 'Digital Stamps'. |
| CEP\_04\_D\_008 | Various | Ignore all references to cryptography and 'Digital Stamps'. |
| CEP\_04\_H\_007 | $2 | For 'Requirements for Accreditation … (RFA)" read 'GP Systems Compliance Module'. |
| CEP\_07\_A\_008 | Various | Ignore all sections on and references to cryptography. |
| CEG\_07\_B\_008 | $1  $2 | Ignore all references to cryptography and 'Digital Stamps'.  For MMHS message ID, read MESH 'sequence identifier' (see MESH File Interface Specification). For MHS Address, read MESH Mailbox ID. |
| CEG\_09\_A\_008 | $2 | MESH Identifiers are issued by The Authority. |

#### CEP {#DigitalDiagnostics&PathologyMessaging-CEP}

|  |  |  |
| --- | --- | --- |
| **Filename** | **Section / Page** | **Description** |
| CEP\_02\_C\_003 | p1 | Web link to leeds.ac.uk is no longer valid. For PBCL files go to TRUD (<https://isd.digital.nhs.uk/trud3/user/guest/group/0/home>)  Web link to doh.nhsweb are no longer valid. For Org and person code data see ODS web site ([https://digital.nhs.uk/organisation-data-service](https://digital.nhs.uk/services/organisation-data-service)) |
| CEP\_02\_D\_003 | pA1-3 | Web link to leeds.ac.uk is no longer valid. For PBCL files go to TRUD (<https://isd.digital.nhs.uk/trud3/user/guest/group/0/home>) |
| CEP\_03\_A\_003 | Table 2 | Ignore sections associated with 'Request to Lab'. |
| CEP\_03\_B\_003 | Various | Ignore all sections on and references to cryptography |
| CEP\_11\_A\_003 | Various | Ignore all sections on and references to cryptography |
| CEP\_12\_A\_003 | Various | Ignore all sections on and references to cryptography.  Note that MMHS references shall be read as MESH references, specifically MMHS notifications of delivery, non-delivery shall be read as MESH delivery/non-delivery notifications. Note that 'read-receipts' are not supported by MESH. |
| CEP\_13\_A\_003 | Various | Ignore all sections on and references to cryptography |
| CEP\_13\_B\_003 | Various  $2.5 | Ignore all sections on and references to cryptography  Note that it is not possible to request a read-receipt over MESH. Senders requiring this additional level of reporting must request an Acknowledgment message to be returned (see 2.4). |
| CEP\_13\_D\_003 | $3 | Note that it is not possible to request a read-receipt over MESH. Senders requiring this additional level of reporting must request an Acknowledgment message to be returned (as per CEP\_13\_B\_003) |
| CEP\_16\_B\_003 | Various | Ignore all references to cryptography and stamped for authentication. |
| CEP\_13\_C\_003 | Various | Ignore all sections on and references to cryptography |
| CEP\_17\_A\_003 | Various | Ignore all sections on and references to cryptography |
| CEP\_17\_B\_003 | Various | Ignore all references to cryptography and 'Digital Stamps'. |
| CEP\_21\_D\_003 | $3 | For MMHS Address, read MESH Mailbox ID.  For MMHS message ID, read MESH 'sequence identifier' (see MESH File Interface Specification) |
| CEP\_21\_E\_003 | $3 | For MMHS message ID, read MESH 'sequence identifier' (see MESH File Interface Specification) |

#### EDIG {#DigitalDiagnostics&PathologyMessaging-EDIG}

|  |  |  |
| --- | --- | --- |
| **Filename** | **Section / Page** | **Description** |
| EDIG\_03\_B\_005 | $2 | For "Health Authority message flows" read "NHAIS messaging". |
| EDIG\_04\_A\_005 | $1   $2 | Ignore whole of section 1.1 re X.400 and refer to MESH messaging specifications for details of construction of MESH messages.  Ignore references to "email" in section 1.2.  Ignore all references to "Read Receipts (RR)" – MESH does not support this functionality. |
| EDIG\_04\_B\_005 | All | Ignore the whole document. |
| EDIG\_05\_A\_005 | All | Ignore all references to cryptography and 'Digital Stamps'. |

#### ISR {#DigitalDiagnostics&PathologyMessaging-ISR}

This document provides a record of issues raised during development and early trials and provides an audit record and justification for changes resulting in the current PMIP Specs. There are several references to projects, organisations and technologies that have been superseded and which are documented elsewhere in this document. As the ISR document does not contain any requirements it has not been analysed and therefore revisions or interpretations have not been made. Readers should therefore not regard the contents of this document as authoritative in any way.

#### JCG {#DigitalDiagnostics&PathologyMessaging-JCG}

The JCG document is similar to the ISR document in that it does not contain any formal requirements for systems. It does, however, provide a useful reference to the original GP User Requirement and much of the content, aside from references to projects, organisations and technologies that have been superseded, is as valid today as it was when it was written. The user requirements therein are encapsulated elsewhere in the PMIP Specs and as such, any formal changes are captured in changes to other documents within the set.

#### LSR {#DigitalDiagnostics&PathologyMessaging-LSR}

|  |  |  |
| --- | --- | --- |
| **Filename** | **Section / Page** | **Description** |
| LSR 04-C-001 | $1 | Errata: Interchange number sequence 1..999,999 should be 1..99,999,999 |

None

#### MREJ {#DigitalDiagnostics&PathologyMessaging-MREJ}

None

#### PMEP {#DigitalDiagnostics&PathologyMessaging-PMEP}

None

#### READ {#DigitalDiagnostics&PathologyMessaging-READ}

|  |  |  |
| --- | --- | --- |
| **Filename** | **Section / Page** | **Description** |
| READ\_02\_A\_001 | $1  $2  $3  $4 | Web link to leeds.ac.uk is no longer valid. For PBCL files go to TRUD (<https://isd.digital.nhs.uk/trud3/user/guest/group/0/home>)  Ignore reference to "Labsetv1.002.txt", references to number of records, release dates, etc – see TRUD website for latest version.  Ignore section 3 – release dates and implementation timescales are contained in the PBCL release notes (See TRUD website).  Ignore this section. |

#### SRID {#DigitalDiagnostics&PathologyMessaging-SRID}

|  |  |  |
| --- | --- | --- |
| **Filename** | **Section / Page** | **Description** |
| SRID\_01\_A\_001 | $2    $4    $9 | Ignore reference to NHSIA Helpline. Contact NHS CFH Networking Address Registration Manager.  For "NHS Telecommunications Branch" read "Networking Address Registration Manager, NHS CFH".  Ignore reference to "Project Connect Tracking Database".  The "Project Connect Tracking Database" was replaced by "NHS CFH Tracking Database". This was subsequent 'formally discontinued' as the mechanism for email contact management. It was replaced with an NHSmail-only list mapping laboratories to email addresses. This is maintained by The Authority Solution Assurance Service Desk.  Ignore reference to NHSIA tel num. |

#### TCON {#DigitalDiagnostics&PathologyMessaging-TCON}

|  |  |  |
| --- | --- | --- |
| **Filename** | **Section / Page** | **Description** |
| TCON\_03\_A\_005 | Various | Ignore all sections on and references to cryptography and PKI. |
| TCON\_04\_A\_005 | Various | Ignore all sections on and references to cryptography. |
| TCON\_04\_B\_005 | Various  $3  $4 | Ignore all sections on and references to cryptography.  Ignore whole section.  Ignore whole section. |
| TCON\_04\_C\_005 | All | Ignore whole document. |

# Compliance, Assurance and Testing {#DigitalDiagnostics&PathologyMessaging-Compliance,AssuranceandTesting}

See the Digital Diagnostics and Pathology Messaging section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Documentation {#DigitalDiagnostics&PathologyMessaging-Documentation}

### **Using Lab Results adaptor** {#DigitalDiagnostics&PathologyMessaging-UsingLabResultsadaptor}

For Suppliers of new services or applications:

- [API Catalogue - Lab Results adaptor](https://digital.nhs.uk/developer/api-catalogue/lab-results-adaptor)
- [GP software developer guide](https://digital.nhs.uk/developer/guides-and-documentation/developer-guides/gp-software-developer-guide)

It is recommended to read GP software developer guide in conjunction with the adaptor documentation.

### **Without using Lab Results adaptor** {#DigitalDiagnostics&PathologyMessaging-WithoutusingLabResultsadaptor}

We are aware that there are older versions of PMIP documentation available online from archived websites. The links to the documentation provided on this site are the authoritative ones. So users are strongly recommended to use these versions in preference to any other versions.

- [Edifact\_Messaging\_Implementation\_Guidelines.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391133752/Edifact_Messaging_Implementation_Guidelines.pdf?version=1&modificationDate=1527853080733&cacheVersion=1&api=v2)
- [EDIFACT pathology messaging Standard ISB 1557](http://webarchive.nationalarchives.gov.uk/+/http://www.isb.nhs.uk/library/standard/217)

Note: the link above does not currently hold the EDIFACT message specifications themselves. They have now been uploaded to the[**NHS Developer Network**](https://developer.nhs.uk/downloads-data/pathology-message-specifications-pmep-pmip/)

# Dependencies {#DigitalDiagnostics&PathologyMessaging-Dependencies}

Creating a compliant implementation requires implementing the following dependent interface Standard:

- [Messaging Exchange for Social Care and Health (MESH)](Messaging-Exchange-for-Social-Care-and-Health-MESH.md)

# Roadmap {#DigitalDiagnostics&PathologyMessaging-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [ISB 1557 (PMEPv1.003).zip](../../../../.raw/DCSDCS/attachments/1391133752/att1391142738-ISB 1557 (PMEPv1.003).zip)
- [Edifact_Messaging_Implementation_Guidelines.pdf](../../../../.raw/DCSDCS/attachments/1391133752/att1391155565-Edifact_Messaging_Implementation_Guidelines.pdf)
- [image-20240715-115552.png](../../../../.raw/DCSDCS/attachments/1391133752/att13129646124-image-20240715-115552.png)
