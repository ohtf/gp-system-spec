---
page_id: "13178896386"
space: "DCSDCS"
title: "Capabilities with Interoperability Relationships"
version: 20
updated: "2026-05-06T09:57:40.173Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/13178896386/Capabilities+with+Interoperability+Relationships"
labels: ["reference_page"]
---

# Capabilities with Interoperability Relationships

|  |  |
| --- | --- |
| ID | R10 |
| Version | 5.0.0 |
| Type | Reference |

- [Introduction](#CapabilitieswithInteroperabilityRelationships-Introduction)
  - [Foundation Capabilities](#CapabilitieswithInteroperabilityRelationships-FoundationCapabilities)
  - [Non-foundation Capabilities](#CapabilitieswithInteroperabilityRelationships-Non-foundationCapabilities)
  - [Community Pharmacy Capabilities](#CapabilitieswithInteroperabilityRelationships-CommunityPharmacyCapabilities)
  - [Digital Pathways Solution Registry Capabilities](#CapabilitieswithInteroperabilityRelationships-DigitalPathwaysSolutionRegistryCapabilities)

# Introduction

This page provides guidance to Suppliers to understand which interoperability requirements are associated with each Capability.

Some interdependencies between individual interface Standards exist. Creating a compliant implementation requires implementing all the required dependent interface Standards, as detailed in the 'Dependencies' column.

Note: this page is for guidance only and does not supersede what is mandated in the individual Capabilities and Standards. Suppliers need to comply with all of the requirements that are mandated by the Capability/Capabilities that the Supplier is offering.

## Foundation Capabilities

### [Appointments Management - GP](../DSIC-Capabilities/Appointments-Management-GP.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements (if offering all Foundation capabilities) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |
| [GP Connect Appointment Management](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Appointment-Management.md) (Provider requirements) | - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| [General Practice Appointments Data Reporting](../DSIC-Standards/Non-Overarching-Standards/General-Practice-Appointments-Data-Reporting.md) | - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md)   Or   - [Secure Electronic File Transfer (SEFT)](../DSIC-Standards/Non-Overarching-Standards/Secure-Electronic-File-Transfer-SEFT.md) |

### [Consultation Management - GP](../DSIC-Capabilities/Consultation-Management-GP.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements (if offering all Foundation capabilities) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |
| [Electronic Yellow Card Reporting](../DSIC-Standards/Non-Overarching-Standards/Electronic-Yellow-Card-Reporting.md) | There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |
| [eMED3 (Fit Notes)](../DSIC-Standards/Non-Overarching-Standards/eMED3-Fit-Notes.md) | - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |

### [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements (if offering all Foundation capabilities) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |
| [NHAIS HA/GP Links](../DSIC-Standards/Non-Overarching-Standards/NHAIS-HAGP-Links.md) | Creating a compliant implementation requires: MESH mailbox but [MESH](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) is implemented with adaptor |
| [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) | For Suppliers of new Solutions, Solutions which ARE currently deployed into an operational environment and have implemented the PDS FHIR API, and Community Pharmacy Solutions (using Healthcare worker access).  - [Authentication and Access](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API |
| [GP2GP](../DSIC-Standards/Non-Overarching-Standards/GP2GP.md) | For Suppliers of new Solutions and Solutions that have implemented the GP2GP FHIR Implementation:  - [GP2GP Requesting Adaptor](../DSIC-Standards/Non-Overarching-Standards/GP2GP-Requesting-Adaptor.md) - [GP2GP Sending Adaptor](../DSIC-Standards/Non-Overarching-Standards/GP2GP-Sending-Adaptor.md) - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) - using FHIR API - [Spine Directory Service - FHIR API](https://digital.nhs.uk/developer/api-catalogue/spine-directory-service-fhir) - [GP Connect Access Record Structured](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Access-Record-Structured.md) - Refer to ‘Migrate a Patient’s structured record' and ‘Migrate a document’ for more information - [GP Registrations Management Information API](https://digital.nhs.uk/developer/api-catalogue/gp-registrations-management-information) |
| [Summary Care Record (SCR)](../DSIC-Standards/Non-Overarching-Standards/Summary-Care-Record-SCR.md) | For Suppliers of new Solutions and Solutions that have implemented the SCR FHIR API:  - [Authentication and Access](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API |
| [GP Connect Access Record HTML](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Access-Record-HTML.md) (Provider requirements) | - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| [GP Connect Access Record Structured](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Access-Record-Structured.md) (Provider requirements) | - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| [GP Connect Send Document](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Send-Document.md) (Receiver requirements) | - [Interoperability Toolkit (ITK)](../DSIC-Standards/Non-Overarching-Standards/Interoperability-Toolkit-ITK.md) - ITK3 Messaging Distribution - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) - [Generic FHIR Receiver](../DSIC-Standards/Non-Overarching-Standards/Generic-FHIR-Receiver.md) (Receiver Solutions only) |
| [GP Connect Update Record](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Update-Record.md) (Receiver requirements) | - [Interoperability Toolkit (ITK)](../DSIC-Standards/Non-Overarching-Standards/Interoperability-Toolkit-ITK.md) - ITK3 Messaging Distribution - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| [GP Connect (Patient Facing) Access Record](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Access-Record.md) (Provider requirements) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |
| [GP Connect (Patient Facing) Prescriptions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Prescriptions.md) (Provider requirements) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |
| [GP Connect (Patient Facing) User Permissions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-User-Permissions.md) (Provider requirements) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |
| [111](../DSIC-Standards/Non-Overarching-Standards/111.md) | Using NHS 111 Report Adaptor There are no Interoperability Standards within the Capabilities and Standards model that are dependents. Without Using NHS 111 Report Adaptor Creating a compliant implementation requires implementing the following dependent interface standards:   - [Interoperability Toolkit (ITK)](../DSIC-Standards/Non-Overarching-Standards/Interoperability-Toolkit-ITK.md) - ITK3 Messaging Distribution - [Clinical Document Architecture (CDA)](../DSIC-Standards/Non-Overarching-Standards/Clinical-Document-Architecture-CDA.md) |
| [GPES Data Extraction](../DSIC-Standards/Non-Overarching-Standards/GPES-Data-Extraction.md) | - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |
| [Primary Care Clinical Terminology Usage Report](../DSIC-Standards/Non-Overarching-Standards/Primary-Care-Clinical-Terminology-Usage-Report.md) | - [Secure Electronic File Transfer (SEFT)](../DSIC-Standards/Non-Overarching-Standards/Secure-Electronic-File-Transfer-SEFT.md) |
| [Digital Medicines and Pharmacy FHIR Payload](../DSIC-Standards/Non-Overarching-Standards/Digital-Medicines-and-Pharmacy-FHIR-Payload.md) | - [Generic FHIR Receiver](../DSIC-Standards/Non-Overarching-Standards/Generic-FHIR-Receiver.md) - receiver Solutions |
| [National Data Opt-Out](../DSIC-Standards/Non-Overarching-Standards/National-Data-Opt-Out.md) | - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |
| [Transfer of Care FHIR Payload](../DSIC-Standards/Non-Overarching-Standards/Transfer-of-Care-FHIR-Payload.md) | - [Generic FHIR Receiver](../DSIC-Standards/Non-Overarching-Standards/Generic-FHIR-Receiver.md) |
| [National Events Management Service (NEMS)](../DSIC-Standards/Non-Overarching-Standards/National-Events-Management-Service-NEMS.md) | - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |
| [Multicast Notification Service (MNS)](../DSIC-Standards/Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) | - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) - if signals received via MESH |
| [Register with a GP Surgery Service](../DSIC-Standards/Non-Overarching-Standards/Register-with-a-GP-Surgery-Service.md) | - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) |
| [Vaccination Extract](../DSIC-Standards/Non-Overarching-Standards/Vaccination-Extract.md) | NHSE Daily Vaccination Events (In-bound) Extract For Suppliers of Solutions which ARE currently deployed into an operational environment and have implemented NHSE Daily Vaccination Events (In-bound) Extract:   - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |
| [Validated Relationship Service](../DSIC-Standards/Non-Overarching-Standards/Validated-Relationship-Service.md) | Creating a compliant implementation requires implementing the following dependent interface standards:  - [Authentication and Access](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API |

### [Prescribing](../DSIC-Capabilities/Prescribing.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements (if offering all Foundation capabilities) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |
| [Electronic Prescription Service (EPS) - Prescribing](../DSIC-Standards/Non-Overarching-Standards/Electronic-Prescription-Service-EPS-Prescribing.md) | For Suppliers of new Solutions and Solutions that have implemented the EPS FHIR API: Creating a compliant implementation requires implementing the following dependent interface standards:   - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) - using PDS FHIR API - [Authentication and Access](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API - [Digital Signature Service API](https://digital.nhs.uk/developer/api-catalogue/signing-service) |

### [Referral Management - GP](../DSIC-Capabilities/Referral-Management-GP.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements (if offering all Foundation capabilities) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |
| [e-Referral Service (eRS)](../DSIC-Standards/Non-Overarching-Standards/e-Referrals-Service-e-RS.md) | For Suppliers of new Solutions and Solutions that have implemented the e-RS FHIR API:  - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) - using PDS FHIR API - [Authentication and Access](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API |
| [Booking and Referral Standard (BaRS)](../DSIC-Standards/Non-Overarching-Standards/Booking-and-Referral-Standard-BaRS.md) | BaRS provides a list of prerequisites in the [BaRS Principles and Prerequisites](https://simplifier.net/guide/nhsbookingandreferralstandard/Home/About-BaRS/BaRS-Principles-and-Prerequisites?version=1.6.0) section of the implementation guide. There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |

### [Resource Management](../DSIC-Capabilities/Resource-Management.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Provider requirements (if offering all Foundation capabilities) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

## Non-foundation Capabilities

### [Appointments Management - Citizen](../DSIC-Capabilities/Appointments-Management-Citizen.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) (Patient interface Consumer) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

### [Communication Management](../DSIC-Capabilities/Communication-Management.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [Email](../DSIC-Standards/Non-Overarching-Standards/Email.md) | There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |

### [Cross-organisation Appointment Booking](../DSIC-Capabilities/Cross-organisation-Appointment-Booking.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [GP Connect Appointment Management](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Appointment-Management.md) (Consumer requirements) | - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |

### [Digital Diagnostics](../DSIC-Capabilities/Digital-Diagnostics.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [Digital Diagnostics & Pathology Messaging](../DSIC-Standards/Non-Overarching-Standards/Digital-Diagnostics-Pathology-Messaging.md) | - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |
| [Screening messaging](../DSIC-Standards/Non-Overarching-Standards/Screening-Messaging.md) | - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) |

### [Digital Dictation](../DSIC-Capabilities/Digital-Dictation.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) (Practice Consumer requirements) | There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |

### [Medical Reports](../DSIC-Capabilities/Medical-Reports.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [GP Connect Access Record HTML](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Access-Record-HTML.md) (Consumer requirements) | - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| [GP Connect Access Record Structured](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Access-Record-Structured.md) (Consumer requirements) | - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) (Practice Consumer requirements) | There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |

### [Prescription Ordering – Citizen](../DSIC-Capabilities/Prescription-Ordering-Citizen.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) (Patient interface Consumer)  Or  [GP Connect (Patient Facing) Prescriptions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Prescriptions.md) (Consumer requirements) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

### [Self-service Appointment Check-in](../DSIC-Capabilities/Self-service-Appointment-Check-in.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) (Practice Consumer requirements) | There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |

### [View Record - Citizen](../DSIC-Capabilities/View-Record-Citizen.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) (Patient interface Consumer)  Or  [GP Connect (Patient Facing) Access Record](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Access-Record.md) (Consumer requirements) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |

## Community Pharmacy Capabilities

### [Consultation Management - Community Pharmacy](../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) | For Suppliers of new Solutions, Solutions which ARE currently deployed into an operational environment and have implemented the PDS FHIR API, and Community Pharmacy Solutions (using Healthcare worker access).  - [Authentication and Access](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API |
| [GP Connect Access Record Structured](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Access-Record-Structured.md) (Consumer requirements) | - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| [Digital Medicines and Pharmacy FHIR Payload](../DSIC-Standards/Non-Overarching-Standards/Digital-Medicines-and-Pharmacy-FHIR-Payload.md) (Emergency Supply of Medications - Sender requirements) | There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |
| [GP Connect Update Record](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Update-Record.md) (Sender requirements) | - [Interoperability Toolkit (ITK)](../DSIC-Standards/Non-Overarching-Standards/Interoperability-Toolkit-ITK.md) - ITK3 Messaging Distribution - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| [NHSBSA Claims & Reporting](../DSIC-Standards/Non-Overarching-Standards/NHSBSA-Claims-Reporting.md) | There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |
| [Directory of Services (DoS) - Urgent and Emergency Care](../DSIC-Standards/Non-Overarching-Standards/Directory-of-Services-DoS-Urgent-and-Emergency-Care.md) | There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |
| [National Care Records Service (NCRS)](../DSIC-Standards/Non-Overarching-Standards/National-Care-Records-Service-NCRS.md) | There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |

### [Referral Management - Community Pharmacy](../DSIC-Capabilities/Referral-Management-Community-Pharmacy.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [111](../DSIC-Standards/Non-Overarching-Standards/111.md) | Using NHS 111 Report Adaptor There are no Interoperability Standards within the Capabilities and Standards model that are dependents. Without Using NHS 111 Report Adaptor Creating a compliant implementation requires implementing the following dependent interface standards:   - [Interoperability Toolkit (ITK)](../DSIC-Standards/Non-Overarching-Standards/Interoperability-Toolkit-ITK.md) - ITK3 Messaging Distribution - [Clinical Document Architecture (CDA)](../DSIC-Standards/Non-Overarching-Standards/Clinical-Document-Architecture-CDA.md) |
| [Booking and Referral Standard (BaRS)](../DSIC-Standards/Non-Overarching-Standards/Booking-and-Referral-Standard-BaRS.md) | BaRS provides a list of prerequisites in the [BaRS Principles and Prerequisites](https://simplifier.net/guide/nhsbookingandreferralstandard/Home/About-BaRS/BaRS-Principles-and-Prerequisites?version=1.6.0) section of the implementation guide. There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |

## Digital Pathways Solution Registry Capabilities

### [Care Navigation](../DSIC-Capabilities/Care-Navigation.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [NHS Notify](../DSIC-Standards/Non-Overarching-Standards/NHS-Notify.md) | - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) - For Suppliers of Solutions who use Messaging Exchange for Social Care and Health (MESH) to integrate with NHS Notify |
| [Booking and Referral Standard (BaRS)](../DSIC-Standards/Non-Overarching-Standards/Booking-and-Referral-Standard-BaRS.md) | BaRS provides a list of prerequisites in the [BaRS Principles and Prerequisites](https://simplifier.net/guide/nhsbookingandreferralstandard/Home/About-BaRS/BaRS-Principles-and-Prerequisites?version=1.6.0) section of the implementation guide. There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |
| [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) (Practice interface Consumer requirements) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |
| [GP Connect Access Record Structured](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Access-Record-Structured.md) (Consumer requirements) | - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| [GP Connect Access Record HTML](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Access-Record-HTML.md) (Consumer requirements) | - [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \* or [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md)   \*May be sourced indirectly by existing PDS interface provided by a Patient Information Maintenance - GP Solution, either via API to this Solution, or as a shared application resource if delivered as part of the same Solution. |
| [GP Connect Send Document](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Send-Document.md)(Sender Requirements) | - [Interoperability Toolkit (ITK)](../DSIC-Standards/Non-Overarching-Standards/Interoperability-Toolkit-ITK.md) - ITK3 Messaging Distribution - [Messaging Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) - [Generic FHIR Receiver](../DSIC-Standards/Non-Overarching-Standards/Generic-FHIR-Receiver.md) (Receiver Solutions only) |

### [Online Consultations and Online Patient Requests Reporting](../DSIC-Capabilities/Online-Consultations-and-Online-Patient-Requests-Reporting.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [Online Consultations and Video Consultations Reporting](../DSIC-Standards/Non-Overarching-Standards/Online-Consultations-and-Video-Consultations-Reporting.md)(Requirement OCVCR1) | There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents. |

### [Online Patient Consultation](../DSIC-Capabilities/Online-Patient-Consultation.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [NHS App](../DSIC-Standards/Non-Overarching-Standards/NHS-App.md) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |
| [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) | For Suppliers of new Solutions, Solutions which ARE currently deployed into an operational environment and have implemented the PDS FHIR API, and Community Pharmacy Solutions (using Healthcare worker access).  - [Authentication and Access](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API |

### [Online Patient Request](../DSIC-Capabilities/Online-Patient-Request.md)

| **Interoperability Requirement** | **Dependencies** |
| --- | --- |
| [NHS App](../DSIC-Standards/Non-Overarching-Standards/NHS-App.md) | - [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) |
| [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) | For Suppliers of new Solutions, Solutions which ARE currently deployed into an operational environment and have implemented the PDS FHIR API, and Community Pharmacy Solutions (using Healthcare worker access).  - [Authentication and Access](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) - using NHS Care Identity Service 2 API |