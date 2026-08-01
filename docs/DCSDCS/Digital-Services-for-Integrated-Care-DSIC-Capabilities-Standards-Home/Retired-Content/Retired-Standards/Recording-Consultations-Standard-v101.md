---
page_id: "1391134136"
space: "DCSDCS"
title: "Recording Consultations - Standard v1.0.1"
version: 11
updated: "2022-04-28T12:30:58.682Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391134136/Recording+Consultations+-+Standard+v1.0.1"
labels: ["capability_specific_retired"]
---

# Recording Consultations - Standard v1.0.1

|  |  |
| --- | --- |
| ID {#RecordingConsultations-Standardv1.0.1-ID} | S15 |
| Version | 1.0.1 |
| Type | Capability Specific Standard |
| Status {#RecordingConsultations-Standardv1.0.1-Status} | Retired |
| Effective Date {#RecordingConsultations-Standardv1.0.1-EffectiveDate} | 31 Dec 2019 |

# Requirements {#RecordingConsultations-Standardv1.0.1-Requirements}

| Sections |
| --- |
| Basic Data Recording & Reporting |
| Consultation Forms |
| FGM Enhanced Dataset |

---

| Epic Mapping | Requirement ID | Requirement Text | Level |
| --- | --- | --- | --- |
| Basic Data Recording & Reporting {#RecordingConsultations-Standardv1.0.1-BasicDataRecordingBasicDataRecording&Reporting} | | | |
| C15E1 | GP-05.3-01 {#RecordingConsultations-Standardv1.0.1-GP-05.3-01} | **Basic Data Recording - Data items**  Record for every Consultation whether planned or unplanned any number of data items including as a minimum:   - Start date/time - Staff Member(s) involved in the Consultation - Organisation - Location e.g. Practice, Patient’s home, hospital clinic   See Data Standards for coded data requirements, Appointments Management - GP - Standard for further requirements in relation to Consultations | MUST |
| C15E1 | GP-05.3-02 {#RecordingConsultations-Standardv1.0.1-GP-05.3-02GP-05.3-02} | **Basic Data Recording - Patient characteristics/interventions**  Ability to record Patient characteristics and interventions carried out to investigate or treat a Patient, including:   - Medical, family and social history - Symptoms, signs, observations and investigation results - Diagnoses, allergies, sensitivities and problems - Surgical, diagnostic and preventative procedures - Direct access services - Counselling and health education - Prescribing medicines and medical devices (see Prescribing - Standard v1.1.0)   The Solution will support the ability to record attachments  See Data Standards for coded data requirements | MUST |
| C15E1 | GP-RC-2-01 {#RecordingConsultations-Standardv1.0.1-GP-RC-2-01} | **Episode Recording**  Ability to record the episode type of coded data (e.g. Diagnoses) as New or Ongoing/Other.  See Good Practice Guidelines for GP electronic patient records Version 4 (2011) for further guidance | MUST |
| C15E1 | GP-05.3-03 {#RecordingConsultations-Standardv1.0.1-GP-05.3-03} | **Basic Data Recording - Information about **Patient Characteristics/Interventions****  Ability to record the following information about each Patient Characteristic and Intervention:   - A coded clinical term (e.g. SNOMED CT), where available, identifying the Characteristic or Intervention - A free text description - One or more structured (including numeric) values, where relevant to an observation or to the result of an investigation - The person carrying out the Intervention and their organisation (linked to Staff Member and cross-referencing Practice/related organisation) - The date and time on which, or dates and times between which, the Characteristic applied or Intervention took place - The date on which the Characteristic is to be reviewed   See Data Standards for coded data requirements, Appointments Management - GP - Standard for further requirements in relation to Consultations | MUST |
| C15E1 | GP-05.3-04 {#RecordingConsultations-Standardv1.0.1-GP-05.3-04GP-05.3-04} | **Basic Data Recording - Call/Recall processes**  Support the Practice in Call/Recall processes by:   - Recording that a Patient is subject to certain surveillance - Manually recording recall or review dates - Deriving and recording appropriate recall or review dates from other stored information (or lack thereof) such as demographic data and intervention start dates | MUST |
| C15E1 | **GP-PPFS-3.4-06** | **Child Competence Management**  Support a Competence Assessment of a Child by recording the following:   - Date (pre-populated with current date – amendable by Practice User) - Clinician (populated by a list of Practice Staff, default to logged on Practice User) - Competence Decision    - Not Competent (set as default)   - Competent - Notes (free text)   This Assessment can be carried out multiple times – the most recent Competence Decision is to be used to determine competence-based access and capabilities regarding Citizen Services. | MUST |
| C15E1 | **GP-RC-3-01** | **Child Competence Management - Child not registered at the Practice**  The Solution will support assessments of a Child where they are not registered at the Practice but has requested to become a Proxy for a Patient at the Practice. | MAY |
| C15E1 | **GP-PPFS-3.4-07B** | **'Not Competent' Child - Re-assessment timescale**  Upon recording a Competence Decision of ‘Not Competent’ for a Child, Clinician to be given the ability to suggest a timescale for re-assessment.  See GP-PPFS-3.4-06 for recording Child Competence and GP-PPFS-3.4-08 for recording Adult Capacity | MAY |
| C15E1 | **GP-PPFS-3.4-08** | **Adult Capacity Management**  Support the Capacity Assessment of a Patient (Adult) by recording the following:   - Date (pre-populated with current date – amendable by Practice User) - Clinician (populated by a list of Practice Staff, default to logged on Practice User) - Capacity Decision (Has Capacity (default), Lacks Capacity) - Notes (free text) | MUST |
| C15E2 | **GP-05.3-05** | **Call/Recall Reporting**  Ability to generate a Patient-based report on calls and recalls (e.g. list of Patients whose review or recall date is due/overdue) | MUST |
| C15E3 | **GP-05.3-06** | **Planned/Unplanned Consultations Reporting**  Ability to generate a report on:   - Planned Consultations (aggregate numbers of Consultations by service and/or organisation within a date range) - A Consultation with a Patient that is planned in advance, e.g. as the result of an Appointment. - Unplanned Consultations (aggregate numbers of Consultations by service and/or organisation within a date range) - A Consultation that was not planned in advance. Includes out of hours, accident and emergency, NHS 111, and walk in centre Consultations. | MUST |
| C15E4 | **GP-05.6-04** | **Access Patient Record**  Access a Patient Record where a Patient has been successfully identified, linked, listed or otherwise presented to the user. | MUST |
| Consultation Forms {#RecordingConsultations-Standardv1.0.1-ConsultationForms} | | | |
| C15E5 | GP-05.4-01 {#RecordingConsultations-Standardv1.0.1-GP-05.4-01GP-05.4-01} | **Consultation Forms - Templates**  Practice Users with appropriate system rights will have the ability to create, amend and delete Consultation form templates. Each template will have as a minimum:   - Unique identifier and/or name and version - Template status (whether draft, published / available for viewing and use across the Solution, or obsolete) - Basic business logic/rules, such as the ability to:   - include defaults e.g. current date   - auto-populate data items from within the Patient Record e.g. use of merge fields   - auto-populate data items based on other data within the form   - set mandatory data items | MUST |
| C15E5 | **GP-05.6-02** | ****Consultation** Forms - Template version history**  Ability for Practice User to view version history and version content for a template. | MUST |
| C15E5 | **GP-05.6-03** | ****Consultation** Forms - Template version roll back**  Ability to roll back to a previous version of a template. | MUST |
| C15E1 | GP-05.4-02 {#RecordingConsultations-Standardv1.0.1-GP-05.4-02} | ****Consultation** Forms - Create**  Create Consultation forms (using a published template - see GP-05.4-01) and launch other Consultation form templates from:   - Within the Patient Record - Other modules within the Solution including Patient registration | MUST |
| C15E1 | GP-05.4-03 {#RecordingConsultations-Standardv1.0.1-GP-05.4-03} | ****Consultation** Forms - View historical information**  View historical information when entering data items, including:   - Any data items previously recorded via a version of the form - Any pertinent data items previously recorded within the Patient Record | MUST |
| C15E1 | GP-05.4-04 {#RecordingConsultations-Standardv1.0.1-GP-05.4-04} | ****Consultation** Forms - Saving information**  Manage the completion and saving of a Consultation form. Practice User to have ability to:   - Save a partially completed form - View a saved instance of a form - Return to a saved form to continue data entry - Mark a data entry form as complete | MUST |
| C15E1 | GP-05.4-05 {#RecordingConsultations-Standardv1.0.1-GP-05.4-05} | ****Consultation** Forms - Obsolete forms**  When a form becomes obsolete, Practice User to be able to:   - Complete data entry when in progress (using latest version of form if obsoleted due to an update) - Access data previously recorded via the obsolete form template | MUST |
| C15E6 | GP-05.4-06 {#RecordingConsultations-Standardv1.0.1-GP-05.4-06} | ****Consultation** Forms - Sharing forms**  Support the sharing of Consultation form template(s) with other Practices on the same Solution.  For data entry form templates see GP-05.4-01 | MUST |
| C15E7 | **GP-RC-1-01** | ******Consultation** Forms -**Implement national forms**  Implement and update Consultation form templates to support nationally contracted services ensuring they are available throughout the lifetime of the relevant service. Including, but not limited to:   - QOF - GPES Data Extraction | MUST |
| FGM Enhanced Dataset {#RecordingConsultations-Standardv1.0.1-FGMEnhancedDataset} | | | |
| C15E1,  C15E8 | **FGM-ED-01** | **FGM Enhanced Dataset - SCCI2026**  Enable capture of FGM data, and submission of captured data in the Patient Record - in accordance with SCCI2026 - FGM Enhanced Dataset  See FGM Enhanced Dataset GP Approach, for specific requirements to support the ability to record, extract and upload the FGM Enhanced Dataset to the Clinical Audit Platform (CAP) | MUST |

# Capability {#RecordingConsultations-Standardv1.0.1-Capability}

**Applicable Capability**

All supplier Solutions will need to meet this Standard if they are delivering the Recording Consultations Capability

# Roadmap {#RecordingConsultations-Standardv1.0.1-Roadmap}

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [FGM Enhanced Dataset GP Approach.pdf](../../../../attachments/DCSDCS/1391134136/att1391149974-FGM Enhanced Dataset GP Approach.pdf)
