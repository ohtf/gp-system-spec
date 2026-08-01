---
page_id: "11963531299"
space: "DCSDCS"
title: "Appointments Management - GP v1.0.1"
version: 1
updated: "2022-04-28T11:31:42.394Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11963531299/Appointments+Management+-+GP+v1.0.1"
labels: ["capability_retired"]
---

# Appointments Management - GP v1.0.1

|  |  |
| --- | --- |
| ID | C5 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |

Full Capability status only. For this Capability, Solutions are required to meet all MUST EPICs and associated acceptance criteria.

# Description {#AppointmentsManagement-GPv1.0.1-Description}

Supports the administration, scheduling, resourcing and reporting of Appointments.

# Outcomes {#AppointmentsManagement-GPv1.0.1-Outcomes}

|  |  |
| --- | --- |
| For a Patient: | The ability to access medical services as and when they are needed. |
| For General Practice: | The effective management of time, personnel, and resources to ensure all Patients have timely access to appropriate medical services, and that staff members can undertake their responsibilities efficiently. |
| For the wider NHS and social care system: | The efficient management of Appointments, allocation of resources and movement of Patients across Primary Care to best support the needs of all Patients. |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C5E1 - manage Session templates {#AppointmentsManagement-GPv1.0.1-C5E1-manageSessiontemplates}

As a Practice User

I want to manage Session templates

So that Practice Users can create Sessions from templates

#### Acceptance criterion 1: create Session template {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion1:createSessiontemplate}

Given the Practice User is permitted to create Session templates

When they choose to create a Session template

Then the Session template is created

#### Acceptance criterion 2: amend Session template {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion2:amendSessiontemplate}

Given the Practice User is permitted to amend Session templates

When they choose to amend a Session template

Then the Session template is amended

#### Acceptance criterion 3: delete Session template {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion3:deleteSessiontemplate}

Given the Practice User is permitted to delete Session templates

When they choose to delete a Session template

Then the Session template is deleted

---

### C5E2 - manage Sessions {#AppointmentsManagement-GPv1.0.1-C5E2-manageSessions}

As a Practice User

I want to manage Sessions

So that Practice Users can manage Sessions for the General Practice

#### Acceptance criterion 1: assign Session templates {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion1:assignSessiontemplates}

Given the Practice User is permitted to assign Session templates

When they choose to assign a Session template

Then the Session template is assigned

#### Acceptance criterion 2: create a Session {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion2:createaSession}

Given the Practice User is permitted to create a Session

When they choose to create a Session

Then the Session is created

#### Acceptance criterion 3: amend a Session {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion3:amendaSession}

Given the Practice User is permitted to amend a Session

When they choose to amend a Session

Then the Session is amended

#### Acceptance criterion 4: cancel a Session {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion4:cancelaSession}

Given the Practice User is permitted to cancel a Session

When they choose to cancel a Session

Then the Session is cancelled

#### Acceptance criterion 5: view a Session {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion5:viewaSession}

Given the Practice User is permitted to view a Session

When they choose to view a Session

Then the Session is displayed

#### Acceptance criterion 6: export a Session {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion6:exportaSession}

Given the Practice User is permitted to export a Session

When they choose to export a Session

Then the Session is exported

---

### C5E3 - configure Appointments {#AppointmentsManagement-GPv1.0.1-C5E3-configureAppointments}

As a Practice User

I want to configure Sessions and Slots

So that they can be used for Appointments

#### Acceptance criterion 1: configure Sessions {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion1:configureSessions}

Given the Practice User is permitted to configure Sessions

When they choose to configure a Session

Then the Session is configured

#### Acceptance criterion 2: configure Slots {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion2:configureSlots}

Given the Practice User is permitted to configure Slots

When they choose to configure a Slot

Then the Slot is configured

---

### C5E4 - Practice configuration {#AppointmentsManagement-GPv1.0.1-C5E4-Practiceconfiguration}

As a Practice User

I want to configure Appointment rules at a Practice level

So that they can be used for Appointments

#### Acceptance criterion 1: configure Appointment rules {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion1:configureAppointmentrules}

Given the Practice User is permitted to configure Appointment rules at a Practice level

When they define a rule

Then the rule is applied to all Appointments

---

### C5E5 - manage Appointments {#AppointmentsManagement-GPv1.0.1-C5E5-manageAppointments}

As a Practice User

I want to manage Appointments

So that Patients have access to medical services

#### Acceptance criterion 1: book Appointments  {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion1:bookAppointments}

Given the Practice User is permitted to book Appointments

When they choose to book an Appointment

Then the Appointment is booked

#### Acceptance criterion 2: cancel Appointments  {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion2:cancelAppointments}

Given the Practice User is permitted to cancel Appointments

When they choose to cancel an Appointment

Then the Appointment is cancelled

#### Acceptance criterion 3: update Appointments  {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion3:updateAppointments}

Given the Practice User is permitted to update Appointments

When they choose to update an Appointment

Then the Appointment is updated

#### Acceptance criterion 4: view Appointments  {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion4:viewAppointments}

Given the Practice User is permitted to view Appointments

When they choose to view an Appointment

Then the Appointment is displayed

#### Acceptance criterion 5: search Appointments  {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion5:searchAppointments}

Given the Practice User is permitted to search for Appointments

When they search Appointments

Then the search results are displayed

#### Acceptance criterion 6: alerts on Appointments  {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion6:alertsonAppointments}

Given the Practice User is permitted to receive alerts

When the management of an Appointment requires an alert to be displayed

Then the alert is displayed

---

### C5E6 - view Appointment reports {#AppointmentsManagement-GPv1.0.1-C5E6-viewAppointmentreports}

As a Practice User

I want to view Appointment reports

So that I can see Appointment activity

#### Acceptance criterion 1: view Appointment reports {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion1:viewAppointmentreports}

Given the Practice User is permitted to view Appointment reports

When the Practice User chooses to view an Appointment report

Then the report is displayed

---

### C5E7 - access Patient Record {#AppointmentsManagement-GPv1.0.1-C5E7-accessPatientRecord}

As a Practice User

I want to access the Patient Record

So that I can access the Patient Record

#### Acceptance criterion 1: accessing Patient Record where identified {#AppointmentsManagement-GPv1.0.1-Acceptancecriterion1:accessingPatientRecordwhereidentified}

Given a Patient Record is identified

And the Practice User is permitted to view the Patient Record

When the Practice User chooses to access the Patient Record

Then the Patient Record is accessed

**Capability Specific Standards**

Suppliers will have to attain compliance with these Standards during the compliance stage before they can be live on a framework with this Capability:

- Appointments Management - GP - Standard
- General Practice Appointments Data Reporting
**Other Applicable Standards**

Suppliers will also have to attain compliance with these additional Standards during the compliance stage before they can be live on a framework with this Capability:

- Interoperability Standard
- Common Reporting v2.0.0
- Management Information (MI) Reporting
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

| Roadmap Item |
| --- |
| No content found. |