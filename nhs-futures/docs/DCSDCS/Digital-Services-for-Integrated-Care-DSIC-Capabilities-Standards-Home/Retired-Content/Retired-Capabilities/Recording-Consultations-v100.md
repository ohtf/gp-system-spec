---
page_id: "1695285249"
space: "DCSDCS"
title: "Recording Consultations v1.0.0"
version: 2
updated: "2020-01-15T16:10:14.114Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1695285249/Recording+Consultations+v1.0.0"
labels: ["capability_retired"]
---

# Recording Consultations v1.0.0

|  |  |
| --- | --- |
| ID {#RecordingConsultationsv1.0.0-ID} | C15 |
| Version {#RecordingConsultationsv1.0.0-Version} | 1.0.0 |
| Type {#RecordingConsultationsv1.0.0-Type} | Capability |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

Full Capability status only. For this Capability, Solutions are required to meet all MUST EPICs and associated acceptance criteria.

# Description {#RecordingConsultationsv1.0.0-Description}

Supports the standardised recording of Consultations and other General Practice activities. Also supports the extraction of Female Genital Mutilation (FGM) data for the FGM data set.

# Outcomes {#RecordingConsultationsv1.0.0-Outcomes}

|  |  |
| --- | --- |
| For a Patient: | There is a detailed and standardised history of consultations including those between Healthcare Professionals that supports more efficient and timely diagnosis and treatment. |
| For General Practice: | Standardised recording and maintenance of accurate Consultation data. Enable timely and efficient access to Consultation data to support Patient care and safety. |
| For the wider NHS and social care system: | Enabling Healthcare Professionals from a variety of services and settings to access accurate and detailed Consultation data in support of decision making and provision of Patient services. |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### Epic 1 - record Consultation information {#RecordingConsultationsv1.0.0-Epic1-recordConsultationinformation}

As a Practice User

I want to record the information associated with a Consultation

So that the Consultation is recorded

#### Acceptance criterion 1: record Consultation information {#RecordingConsultationsv1.0.0-Acceptancecriterion1:recordConsultationinformation}

Given the Practice User is permitted to record Consultations

When the Practice User chooses to record information associated with a Consultation

Then the Consultation is recorded

#### Acceptance criterion 2: record Consultation using published form template {#RecordingConsultationsv1.0.0-Acceptancecriterion2:recordConsultationusingpublishedformtemplate}

Given the Practice User is permitted to record Consultations

When the Practice User chooses to record a Consultation using a published form template

Then the Consultation is recorded

#### Acceptance criterion 3: view Consultation information {#RecordingConsultationsv1.0.0-Acceptancecriterion3:viewConsultationinformation}

Given the Practice User is permitted to view Consultations

When the Practice User chooses to view to a Consultation

Then the Consultation is displayed

---

### Epic 2 - view report on calls and recalls {#RecordingConsultationsv1.0.0-Epic2-viewreportoncallsandrecalls}

As a Practice User

I want to view a report of Patient calls and recalls

So that I can view a report of Patient calls and recalls

#### Acceptance criterion 1: view report on calls and recalls {#RecordingConsultationsv1.0.0-Acceptancecriterion1:viewreportoncallsandrecalls}

Given the Practice User is permitted to view reports of Patient calls and recalls

When the Practice User chooses to view a report of Patient calls and recalls

Then the report is displayed

---

### Epic 3 - view report of Consultations {#RecordingConsultationsv1.0.0-Epic3-viewreportofConsultations}

As a Practice User

I want to view a report of Consultations

So that I can view a report of Consultations

#### Acceptance criterion 1: view a report of planned Consultations {#RecordingConsultationsv1.0.0-Acceptancecriterion1:viewareportofplannedConsultations}

Given the Practice User is permitted to view reports of planned Consultations

When the Practice User chooses to view a report of planned Consultations

Then the report is displayed

#### Acceptance criterion 2: view a report of unplanned Consultations {#RecordingConsultationsv1.0.0-Acceptancecriterion2:viewareportofunplannedConsultations}

Given the Practice User is permitted to view reports of unplanned Consultations

When the Practice User chooses to view a report of unplanned Consultations

Then the report is displayed

---

### Epic 4 - access Patient Record {#RecordingConsultationsv1.0.0-Epic4-accessPatientRecord}

As a Practice User

I want to access the Patient Record

So that I can access the Patient Record

#### Acceptance criterion 1: accessing Patient Record where identified {#RecordingConsultationsv1.0.0-Acceptancecriterion1:accessingPatientRecordwhereidentified}

Given a Patient Record is identified

And the Practice User is permitted to view the Patient Record

When the Practice User chooses to access the Patient Record

Then the Patient Record is accessed

---

### Epic 5 - manage Consultation form templates {#RecordingConsultationsv1.0.0-Epic5-manageConsultationformtemplates}

As a Practice User

I want to manage Consultation form templates

So that Practice Users can create Consultations from templates

#### Acceptance criterion 1: create Consultation form template {#RecordingConsultationsv1.0.0-Acceptancecriterion1:createConsultationformtemplate}

Given the Practice User is permitted to create Consultation form templates

When the Practice User chooses to create a Consultation form template

Then the Consultation form template is created

#### Acceptance criterion 2: view Consultation form template {#RecordingConsultationsv1.0.0-Acceptancecriterion2:viewConsultationformtemplate}

Given the Practice User is permitted to view Consultation form templates

When the Practice User chooses to view a Consultation form template

Then the Consultation form template is displayed

#### Acceptance criterion 3: amend Consultation form template {#RecordingConsultationsv1.0.0-Acceptancecriterion3:amendConsultationformtemplate}

Given the Practice User is permitted to amend Consultation form templates

When the Practice User chooses to amend a Consultation form template

Then the Consultation form template is amended

#### Acceptance criterion 4: delete Consultation form template {#RecordingConsultationsv1.0.0-Acceptancecriterion4:deleteConsultationformtemplate}

Given the Practice User is permitted to delete Consultation form templates

When the Practice User chooses to delete a Consultation form template

Then the Consultation form template is deleted

#### Acceptance criterion 5: view Consultation form template version history {#RecordingConsultationsv1.0.0-Acceptancecriterion5:viewConsultationformtemplateversionhistory}

Given the Practice User is permitted to view Consultation form templates

When the Practice User chooses to view the version history of a Consultation form template

Then the Consultation form template version history is displayed

#### Acceptance criterion 6: Consultation form template version roll back {#RecordingConsultationsv1.0.0-Acceptancecriterion6:Consultationformtemplateversionrollback}

Given the Practice User is permitted to amend Consultation form templates

And the Practice User is viewing the version history for the Consultation form template

And the template has a previous version

When the Practice User chooses to roll back to a previous version

Then the Consultation form template is rolled back

---

### Epic 6 - share Consultation form templates {#RecordingConsultationsv1.0.0-Epic6-shareConsultationformtemplates}

As a Practice User

I want to share Consultation form templates with other practices using this Recording Consultations solution

So that Consultation forms are available to other Practices that use this Recording Consultations solution

#### Acceptance criterion 1: share Consultation form templates {#RecordingConsultationsv1.0.0-Acceptancecriterion1:shareConsultationformtemplates}

Given the Practice User is permitted to share Consultation form templates

And there are other practices using this Recording Consultations solution

When the Practice User chooses to share the Consultation form template

Then the Consultation form template is shared

---

### Epic 7 - use supplier implemented national Consultation form templates {#RecordingConsultationsv1.0.0-Epic7-usesupplierimplementednationalConsultationformtemplates}

As a Practice User

I want to use Consultation form templates based on national forms that are provided by the supplier

So that I don't have to create these Consultation form templates myself and data for nationally contracted services can be recorded

#### Acceptance criterion 1: use supplier implemented form templates {#RecordingConsultationsv1.0.0-Acceptancecriterion1:usesupplierimplementedformtemplates}

Given the Practice User is permitted to create Consultation forms

When the Practice User chooses to create a Consultation form using a published template

Then they can choose to use a Consultation form template based on a national form provided by the supplier

---

### Epic 8 - extract Female Genital Mutilation data {#RecordingConsultationsv1.0.0-Epic8-extractFemaleGenitalMutilationdata}

As a Practice User

I want to extract Female Genital Mutilation data as required for the FGM data set

So that I can submit my practices Female Genital Mutilation data

#### Acceptance criterion 1: record Female Genital Mutilation data {#RecordingConsultationsv1.0.0-Acceptancecriterion1:recordFemaleGenitalMutilationdata}

Given the Practice User is permitted to extract data

When the Practice User chooses to extract the Female Genital Mutilation data

Then the Female Genital Mutilation data is extracted

**Capability Specific Standards**

Suppliers will have to attain compliance with these Standards during the compliance stage before they can be live on a framework with this Capability:

- Recording Consultations - Standard
- eMED3 (Fit Notes)
**Other Applicable Standards**

Suppliers will also have to attain compliance with these additional Standards during the compliance stage before they can be live on a framework with this Capability:

- Interoperability Standard
- Common Reporting
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |

|