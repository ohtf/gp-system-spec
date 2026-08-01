---
page_id: "12667027525"
space: "DCSDCS"
title: "Community Pharmacy Clinical Services"
version: 15
updated: "2025-11-11T11:48:54.430Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12667027525/Community+Pharmacy+Clinical+Services"
labels: ["supp_care_standard"]
---

# Community Pharmacy Clinical Services

|  |  |
| --- | --- |
| **ID** | SCS1 |
| **Version** | 3.0.0 |
| **Type** | Supplementary Care Standard |
| **Status** | Effective |
| **Effective Date** | 10 Nov 2025 |
| **Contracting Vehicle(s)** | [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) |

# Description {#CommunityPharmacyClinicalServices-Description}

Supports Referrals to Community Pharmacy and the management of Community Pharmacy Consultations. Also supports the submission of data to the NHS Business Services Authority (NHSBSA) for payment purposes.

This Standard mandates the requirements for systems used to deliver the following Clinical Services:

- Pharmacy First

  - Minor Illness
  - Urgent Medicines
  - Clinical Pathways
- Pharmacy Contraception
- Pharmacy Blood Pressure Check

# Functional Requirements {#CommunityPharmacyClinicalServices-FunctionalRequirements}

| **Requirement ID** | **Requirement** | **Level** |
| --- | --- | --- |
| SCSCP01 | Adhere to the following Epics in the [Consultation Management - Community Pharmacy](../../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) Capability:   - E00645 - search for a Patient on the Personal Demographics Service (PDS) - E00761 - record Patient Consent for Community Pharmacy Consultations - E00624 - record Patient Consent to share Consultation Information for Community Pharmacy Contraception Consultations - E00625 - manage Pharmacy First Consultation Information for Patients - E00756 - manage Pharmacy Contraception Consultation Information for Patients - E00757 - manage Pharmacy Blood Pressure Check Consultation Information for Patients - E00626 - view information from the GP Practice Electronic Patient Record (EPR) of the Patient during Community Pharmacy Consultations - E00627 - record medication for Patients for Community Pharmacy Consultations - E00628 - print NHS FP10DT for Patients medication for Pharmacy First Consultations - E00629 - Alert Health or Care Professional to provide Safety-Netting Advice to Patients for Pharmacy First Consultations - E00631 - submit records of Pharmacy First Consultations for Patients to their registered GP Practice - E00758 - submit records of Pharmacy Blood Pressure Check Consultations for Patients to their registered GP Practice - E00759 - submit records of Pharmacy Contraception Consultations for Patients to their registered GP Practice - E00632 - submit records of Community Pharmacy Consultations for Patients to NHS Business Services Authority (NHSBSA) - E00633 - view Community Pharmacy details using Directory of Services (DoS) for Community Pharmacy Consultations - E00763 - launch the National Care Record Service (NCRS) for a Patient during Community Pharmacy Consultations - E00634 - launch the Electronic Prescription Service (EPS) Prescription Tracker page for Community Pharmacy Consultations - E00635 - launch the NICE Clinical Knowledge Summaries (CKS) page for Community Pharmacy Consultations - E00636 - launch shared decision making tools for Pharmacy Contraception Consultations - E00637 - launch Patient Group Directions (PGDs), Clinical Protocols and Clinical Pathways for Pharmacy First Consultations - E00760 - launch Patient Group Directions (PGDs) for Pharmacy Contraception Consultations - E00638 - view a Body Mass Index (BMI) calculator for Community Pharmacy Consultations | MUST |
| SCSCP02 | Adhere to the following Epics in the [Referral Management - Community Pharmacy](../../DSIC-Capabilities/Referral-Management-Community-Pharmacy.md) Capability:   - E00639 - view Community Pharmacy Inbound Referrals from NHS 111 for Patients - E00674 - view Community Pharmacy Inbound Referrals from GP Practices for Patients - E00641 - manually create Community Pharmacy Inbound Referrals for Patients - E00643 - amend status of Community Pharmacy Inbound Referrals for Patients - E00640 - notify Health or Care Professional of new Community Pharmacy Inbound Referrals for Patients - E00642 - sort Community Pharmacy Inbound Referrals for Patients - E00644 - flag overdue Community Pharmacy Inbound Referrals for Patients | MUST |

# Secondary Artefacts {#CommunityPharmacyClinicalServices-SecondaryArtefacts}

| **ID** | **Theme** | **Requirement** | **Level** |
| --- | --- | --- | --- |
| SCSCPA01 | Baseline Assurance Standard | Adhere to all the Requirements in the [Baseline Assurance Standard](../Overarching-Standards/Baseline-Assurance-Standard.md) Standard applicable to Community Pharmacy Clinical Services Suppliers | MUST |
| SCSCPA02 | Business Continuity and Disaster Recovery | Adhere to all the Requirements in the [Further Requirements](../Overarching-Standards/Business-Continuity-and-Disaster-Recovery.md) applicable to Community Pharmacy Clinical Services Suppliers within 12 months of being listed on the Buying Catalogue | MUST |
| SCSCPA03 | Information Governance | Adhere to all the Requirements in the [Further Requirement](../Overarching-Standards/Information-Governance.md) applicable to Community Pharmacy Clinical Services Suppliers within 12 months of being listed on the Buying Catalogue | MUST |

# Roadmap {#CommunityPharmacyClinicalServices-Roadmap}

Items on the Roadmap which impact or relate to this Supplementary Care Standard

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Community Pharmacy Consultation Blood Pressure Reading Validation and Enhancements to Hypertension Case Finding Service](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15179644930/Community+Pharmacy+Consultation+Blood+Pressure+Reading+Validation+and+Enhancements+to+Hypertension+Case+Finding+Service) | [Community Pharmacy Clinical Services](Community-Pharmacy-Clinical-Services.md), [Consultation Management - Community Pharmacy](../../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md) | Published | 05 Oct 2026 | Introduction of blood pressure reading validation to Community Pharmacy Consultations and the updating of the Blood Pressure Check Service to the Hypertension Case Finding Service, including improved ABPM reporting and hypertension risk assessment ratings | Uplift | Managed Capacity - Other |
| [New Medicine Service (NMS) for Community Pharmacy](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14308966401/New+Medicine+Service+NMS+for+Community+Pharmacy) | [Consultation Management - Community Pharmacy](../../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md), [NHSBSA Claims & Reporting](../Non-Overarching-Standards/NHSBSA-Claims-Reporting.md), [Community Pharmacy Clinical Services](Community-Pharmacy-Clinical-Services.md) | Draft | TBC | Introducing the Pharmacy New Medicine Service to the Community Pharmacy Clinical Services Supplementary Care Standard | Uplift | Managed Capacity - Minor/Patch uplifts |
| [Update GP Connect Access Record Structured Requirements to include Allergies](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14634254337/Update+GP+Connect+Access+Record+Structured+Requirements+to+include+Allergies) | [GP Connect Access Record Structured](../Non-Overarching-Standards/GP-Connect-Access-Record-Structured.md) | Draft | TBC | Update the GP Connect Access Record Structured Standard to include the consumption of data for the Allergies clinical area | Uplift | Managed Capacity - Other |
| [Introducing the Pharmacy Smoking Cessation Service to the Community Pharmacy Clinical Services Supplementary Care Standard](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14601224206/Introducing+the+Pharmacy+Smoking+Cessation+Service+to+the+Community+Pharmacy+Clinical+Services+Supplementary+Care+Standard) | [Community Pharmacy Clinical Services](Community-Pharmacy-Clinical-Services.md), [Consultation Management - Community Pharmacy](../../DSIC-Capabilities/Consultation-Management-Community-Pharmacy.md), [NHSBSA Claims & Reporting](../Non-Overarching-Standards/NHSBSA-Claims-Reporting.md) | Draft | TBC | Introducing the Pharmacy Smoking Cessation Service to the Community Pharmacy Clinical Services Supplementary Care Standard | Uplift | Managed Capacity - Minor/Patch uplifts |

## Attachments

- [SNOMED_CT_Inactives_Fact_sheet_v1.0.pdf](../../../../.raw/DCSDCS/attachments/12667027525/att12667027534-SNOMED_CT_Inactives_Fact_sheet_v1.0.pdf)
- [AA4 GPSoC Allergy Archetype GP Connect Allergy Guidance v1.docx](../../../../.raw/DCSDCS/attachments/12667027525/att12667027537-AA4 GPSoC Allergy Archetype GP Connect Allergy Guidance v1.docx)
- [AA3 Implementing the Allergy Archetype in FHIR v1.docx](../../../../.raw/DCSDCS/attachments/12667027525/att12667027540-AA3 Implementing the Allergy Archetype in FHIR v1.docx)
- [AA2 Implementing the Allergy Archetype in the GP2GP Message v1.docx](../../../../.raw/DCSDCS/attachments/12667027525/att12667027543-AA2 Implementing the Allergy Archetype in the GP2GP Message v1.docx)
- [AA1 GPSoC Allergy Archetype Implementation Guidance v1.docx](../../../../.raw/DCSDCS/attachments/12667027525/att12667027546-AA1 GPSoC Allergy Archetype Implementation Guidance v1.docx)
