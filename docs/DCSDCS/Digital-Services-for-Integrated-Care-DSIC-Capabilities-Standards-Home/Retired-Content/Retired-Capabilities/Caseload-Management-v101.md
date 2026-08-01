---
page_id: "13813678081"
space: "DCSDCS"
title: "Caseload Management v1.0.1"
version: 1
updated: "2025-02-14T09:36:19.831Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/13813678081/Caseload+Management+v1.0.1"
labels: ["capability_retired"]
---

# Caseload Management v1.0.1

|  |  |
| --- | --- |
| ID | C22 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Contracting Vehicle(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description {#CaseloadManagementv1.0.1-Description}

The Caseload Management Capability supports the allocation of appropriate Health and Care Professionals to Patients/Service Users who are in need of healthcare or support.

It ensures that Health and Care Professionals are assigned a manageable number of 'cases' (Patients/Service Users and their healthcare or support needs) and that Patient/Service Users receive care from a Professional with the correct skills and equipment, ensuring efficient use of resources.

The Capability applies a number of factors (e.g. case urgency, Patient/Service User location, technology support requirements, skill requirements) in generating caseloads (the 'active' cases allocated over a period of time across the team of Health and Care Professionals) and contact schedules (the timetable of contacts with Patients/Service Users for an individual Health or Care Professional): this allows work to be effectively planned and managed and changes (e.g. new demand) to be responded to.

By enabling case records to be maintained, the Capability ensures that the right information is available to support the process and that a complete record of care is created.

Although the Capability is not about maintaining a clinical or care record for the Patient/Service User, it may allow integration with other health and care Solutions, allowing information to be shared and a more complete picture of the Patient/Service User's health and care to be maintained.

It may also support delivery of service improvements through reporting and analysis and the use of care pathways and packages.

# Outcomes {#CaseloadManagementv1.0.1-Outcomes}

|  |  |
| --- | --- |
| Caseload Manager | - Able to centrally manage scheduling and caseload resourcing - Able to make the best use of available staff and other resources in meeting the care needs of Patients/Service Users - More efficiency in handling change (e.g. new demand or staff absence) - Able to plan contact with Patients/Service Users so that the correct staff and equipment are available with the right duration and frequency of contact |
| Health or Care Professional | - Able to create an accurate record of care that has been delivered - Able to use contact schedules to plan and manage workload |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C22E1 - manage Cases {#CaseloadManagementv1.0.1-C22E1-manageCases}

As a Caseload Manager

I want to capture details of Patient/Service User cases (e.g. Referrals and Service Requests)

So that I can understand demand and use these to generate Caseloads and contact schedules

#### Acceptance criterion 1: create Case {#CaseloadManagementv1.0.1-Acceptancecriterion1:createCase}

Given that Referrals and Service Requests can be made

And that the user is permitted to create cases

When a new Referral or Service Request is received

Then the case can be created

And information about the case can be captured

#### Acceptance criterion 2: view Case {#CaseloadManagementv1.0.1-Acceptancecriterion2:viewCase}

Given the user is permitted to view cases

When they choose to view a Patient/Service User's case

Then the Patient/Service User's case is displayed

#### Acceptance criterion 3: amend Case {#CaseloadManagementv1.0.1-Acceptancecriterion3:amendCase}

Given the user is permitted to amend cases

When a change to a Patient/Service User's case is required

Then the Patient/Service User's case can be amended

#### Acceptance criterion 4: close Case {#CaseloadManagementv1.0.1-Acceptancecriterion4:closeCase}

Given the user is permitted to close cases

When a case is no longer required

Then the case can be closed or made inactive

---

### C22E2 - maintain Caseloads {#CaseloadManagementv1.0.1-C22E2-maintainCaseloads}

As a Caseload Manager

I want to maintain Caseloads

So that staff and equipment are allocated to cases efficiently and Patients/Service Users receive optimum care

#### Acceptance criterion 1: create Caseload {#CaseloadManagementv1.0.1-Acceptancecriterion1:createCaseload}

Given that the user is permitted to create Caseloads

And the requirements for the Caseload have been defined (e.g. cases to be included and their priority, staff or equipment requirements)

When the user chooses to create a Caseload to support Patient/Service User care

Then the Caseload is created

#### Acceptance criterion 2: view Caseload {#CaseloadManagementv1.0.1-Acceptancecriterion2:viewCaseload}

Given that the user is permitted to view Caseloads

And Caseloads have been created

When the user chooses to view a Caseload

Then the Caseload is displayed

#### Acceptance criterion 3: amend Caseload {#CaseloadManagementv1.0.1-Acceptancecriterion3:amendCaseload}

Given that the user is permitted to amend Caseloads

When a change to the Caseload is required (e.g. additional cases added)

Then the Caseload can be amended

#### Acceptance criterion 4: delete Caseload {#CaseloadManagementv1.0.1-Acceptancecriterion4:deleteCaseload}

Given that the user is permitted to delete Caseloads

When the user chooses to delete a Caseload

Then the Caseload is deleted

#### Acceptance criterion 5: share Caseload with Health and Care Professionals {#CaseloadManagementv1.0.1-Acceptancecriterion5:shareCaseloadwithHealthandCareProfessionals}

Given that the Caseload has been created

When the user chooses to share the Caseload

Then the Caseload can be shared with the relevant Health and Care Professionals

---

### C22E3 - generate and manage contact schedules {#CaseloadManagementv1.0.1-C22E3-generateandmanagecontactschedules}

As a Caseload Manager

I want to generate individual contact schedules

So that Health and Care Professionals can understand and manage their workload

#### Acceptance criterion 1: create contact schedule {#CaseloadManagementv1.0.1-Acceptancecriterion1:createcontactschedule}

Given that the user is permitted to create contact schedules

And the requirements for the contact schedule has been defined (e.g. applicable Staff Member, case contact frequency and duration of service)

When the user chooses to create a contact schedule for a Health or Care Professional

Then the contact schedule is created

#### Acceptance criterion 2: view contact schedule {#CaseloadManagementv1.0.1-Acceptancecriterion2:viewcontactschedule}

Given that the user is permitted to view contact schedules

And a contact schedule has been created

When the user chooses to view a contact schedule for a Health or Care Professional

Then the contact schedule is displayed

#### Acceptance criterion 3: amend contact schedule {#CaseloadManagementv1.0.1-Acceptancecriterion3:amendcontactschedule}

Given that the user is permitted to amend contact schedules

And a contact schedule has been created

When the user chooses to amend the contact schedule for a Health or Care Professional

Then the contact schedule is amended

#### Acceptance criterion 4: delete contact schedule {#CaseloadManagementv1.0.1-Acceptancecriterion4:deletecontactschedule}

Given that the user is permitted to delete contact schedules

And a contact schedule has been created

When the user chooses to delete the contact schedule for a Health or Care Professional

Then the contact schedule is deleted

---

### C22E4 - update Case details {#CaseloadManagementv1.0.1-C22E4-updateCasedetails}

As a Health or Care Professional

I want to be able to update the details for cases assigned to me

So that there is an accurate record of the case (e.g. contacts, status, outcome)

#### Acceptance criterion 1: update Case details {#CaseloadManagementv1.0.1-Acceptancecriterion1:updateCasedetails}

Given a case has been assigned to a Health or Care Professional

And the Health or Care Professional is permitted to update cases assigned to them

When the Health or Care Professional views a case

Then they are able to update the details held about the case

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C22E5 - review and comment on Caseload {#CaseloadManagementv1.0.1-C22E5-reviewandcommentonCaseload}

As a Health or Care Professional

I want to be able to view and comment on my Caseload

So that I understand the cases assigned to me and can raise any issues

#### Acceptance criterion 1: view and comment on Caseload {#CaseloadManagementv1.0.1-Acceptancecriterion1:viewandcommentonCaseload}

Given a Caseload has been assigned to a Health or Care Professional

And the Health or Care Professional is permitted to view their caseload

When the Health or Care Professional views their Caseload

Then they are able to comment on the elements of the Caseload

---

### C22E6 - review and comment on contact schedule {#CaseloadManagementv1.0.1-C22E6-reviewandcommentoncontactschedule}

As a Health or Care Professional

I want to view and comment on my contact schedule

So that I can manage my workload and can raise any issues

#### Acceptance criterion 1: view and comment on contact schedule {#CaseloadManagementv1.0.1-Acceptancecriterion1:viewandcommentoncontactschedule}

Given a contact schedule has been assigned to a Health or Care Professional

And the Health or Care Professional is permitted to view their contact schedule

When the Health or Care Professional views their contact schedule

Then they are able to comment on the elements of the contact schedule

---

### C22E7 - view and update Patient/Service User's Health or Care Record {#CaseloadManagementv1.0.1-C22E7-viewandupdatePatient/ServiceUser'sHealthorCareRecord}

As a Health or Care Professional

I want to be able to view and updated the health or care record for a Patient/Service User held by another Service Provider

So that I can use the information to better understand their needs and can contribute to a more complete and accurate record of their healthcare

#### Acceptance criterion 1: view Health or Care Record {#CaseloadManagementv1.0.1-Acceptancecriterion1:viewHealthorCareRecord}

Given a Patient/Service User has health or care records held by other Service Providers

And one or more of these records can be accessed using the Caseload Management Solution

When the Patient/Service User's record is accessed

Then the record(s) held by other Service Providers can be viewed

#### Acceptance criterion 2: update Health or Care Record {#CaseloadManagementv1.0.1-Acceptancecriterion2:updateHealthorCareRecord}

Given a Patient/Service User has health or care records held by other Service Providers

And one or more of these records can be updated using the Caseload Management Solution

When the Patient/Service User's record is accessed

Then the record(s) held by other Service Providers can be updated

---

### C22E8 - reporting {#CaseloadManagementv1.0.1-C22E8-reporting}

As a Caseload Manager

I want to generate reports relating to cases and Caseload

So that I can better manage and plan the delivery of care for Patients/Service Users

#### Acceptance criterion 1: report based on a range of selection criteria {#CaseloadManagementv1.0.1-Acceptancecriterion1:reportbasedonarangeofselectioncriteria}

Given that information is available relating to cases and caseloads

When the report is run

Then the results are output

And the output can be analysed to identify trends or performance

---

### C22E9 - Care Pathway templates {#CaseloadManagementv1.0.1-C22E9-CarePathwaytemplates}

As a Caseload Manager

I want to be able to define Care Pathway templates

So that I can standardise delivery of care and create a more consistent experience for Patients/Service Users

#### Acceptance criterion 1: create Care Package template {#CaseloadManagementv1.0.1-Acceptancecriterion1:createCarePackagetemplate}

Given the Caseload Manager is permitted to create Care Package templates

When the need for a new Care Package template is identified

Then a new Care Package template can be defined (e.g. number and frequency of contacts, duration, services provided)

And the template can be used to plan care for Patients/Service Users

**Capability Specific Standards**

Suppliers will have to attain compliance with these Standards during the compliance stage before they can be live on a Contracting Vehicle with this Capability:

None

**Other Applicable Standards**

Suppliers will have to attain compliance with these Standards during the compliance stage before they can be live on a Contracting Vehicle with this Capability:

- Interoperability Standard
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |