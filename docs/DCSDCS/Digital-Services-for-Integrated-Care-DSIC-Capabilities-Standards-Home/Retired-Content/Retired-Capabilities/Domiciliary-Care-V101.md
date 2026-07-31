---
page_id: "12750028801"
space: "DCSDCS"
title: "Domiciliary Care V1.0.1"
version: 1
updated: "2024-02-05T09:54:30.198Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12750028801/Domiciliary+Care+V1.0.1"
labels: ["capability_retired"]
---

# Domiciliary Care V1.0.1

|  |  |
| --- | --- |
| ID | C27 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description

A Domiciliary Care Capability enables Service Providers to effectively plan and manage Domiciliary Care services offered to Service Users. The Capability will allow for Domiciliary Care schedules to be produced that meet the needs of Service Users, efficiently roster staff and that allow Care Workers to manage their Appointments with Service Users.

The Domiciliary Care Capability may also allow Service Users and nominated individuals to view their Domiciliary Care schedule, allow remote access to Domiciliary Care schedules for Care Workers and for Domiciliary Care Organisations run reports on their Domiciliary Care data.

# Outcomes

|  |  |
| --- | --- |
| Service User | - Receive timely and appropriate Domiciliary Care - The right people have access to Domiciliary Care information |
| Domiciliary Care Organisation | - Centrally manage scheduling of Domiciliary Care services and rostering of staff - More flexibility and efficiency in handling staff leave - Gain insights into the Organisation with reporting |
| Care Worker | - Better organised as they can plan and track my care work schedule - Increased work efficiency as they can access the Domiciliary Care Plan and schedules during client visits and update them if required |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C27E1 - maintain Domiciliary Care schedules

As a Domiciliary Care Organisation

I want to maintain Domiciliary Care schedules for Service User visits by Care Workers

So that Service Users Appointments and care are planned

#### Acceptance criterion 1: create Domiciliary Care schedule

Given that the user is permitted to maintain Domiciliary Care schedules

And the requirements for the Domiciliary Care schedule have been defined

When the user chooses to create a Domiciliary Care schedule for Care Workers

Then the Domiciliary Care schedule is created

#### Acceptance criterion 2: view Domiciliary Care schedule

Given that the user is permitted to maintain Domiciliary Care schedules

And a Domiciliary Care schedule has been created

When the user chooses to view a Domiciliary Care schedule for Care Workers

Then the Domiciliary Care schedule is displayed

#### Acceptance criterion 3: amend Domiciliary Care schedule

Given that the user is permitted to maintain Domiciliary Care schedules

And a Domiciliary Care schedule has been created

When the user chooses to amend a Domiciliary Care schedule for Care Workers

Then the Domiciliary Care schedule is amended

#### Acceptance criterion 4: delete Domiciliary Care schedule

Given that the user is permitted to maintain Domiciliary Care schedules

And a Domiciliary Care schedule has been created

When the user chooses to delete a Domiciliary Care schedule for Care Workers

Then the Domiciliary Care schedule is deleted

#### Acceptance criterion 5: notification of Domiciliary Care schedule changes

Given that the Domiciliary Care schedule has been created

When there are changes in the Domiciliary Care schedule

Then the Care Worker is notified

---

### C27E2 - share Domiciliary Care schedules

As a Workforce Manager

I want to share Domiciliary Care schedules

So that I can communicate Domiciliary Care schedules to Staff Members

#### Acceptance criterion 1: share Domiciliary Care schedules

Given that the Domiciliary Care schedule has been created

When the user chooses to share the Domiciliary Care schedule

Then the Domiciliary Care schedule is shared with Staff Members

---

### C27E3 - manage Appointments

As a Care Worker

I want to manage Appointments for Service User visits

So that Service Users Appointments are planned and updated

#### Acceptance criterion 1: view Appointments

Given that the Care Worker is permitted to view Appointments

When the Care Worker chooses to view Appointments in their Domiciliary Care schedule

Then the Appointments in their Domiciliary Care schedule are displayed

#### Acceptance criterion 2: record Appointment details

Given that the Care Worker is permitted to record Appointment details

When the Care Worker chooses to record Appointment details (e.g. visit times, mileage, documentation)

Then the Appointment information is updated

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C27E4 - Service User manages their schedule for Domiciliary Care

As a Service User

I want to manage my Domiciliary Care schedule (including Appointment details)

So that I can view my Domiciliary Care schedule and inform staff of any changes

#### Acceptance criterion 1: Service User views Domiciliary Care schedule

Given that the Service User can view the Domiciliary Care schedule

When they choose to view their Domiciliary Care schedule

Then their Domiciliary Care schedule is displayed

#### Acceptance criterion 2: Service User informs Care Workers of changes

Given that the Service User is permitted to inform Care Workers of changes

And there is a change in circumstances (e.g. holidays, staying with a relative) that would impact their Domiciliary Care schedule

When they choose to inform Care Workers of changes in circumstances

Then the Care Workers are informed of changes in circumstances

---

### C27E5 - manage Care Plans for Service Users

As a Care Worker

I want to manage Care Plans for Service Users

So that I can ensure the Service User's Care Plan continues to reflect their needs

#### Acceptance criterion 1: Care Worker creates a Domiciliary Care Plan for the Service User

Given that the Care Worker has assessed the Domiciliary Care needs of the Service User

When they decide to create a Domiciliary Care Plan for the Service User

Then they can create the Domiciliary Care Plan

#### Acceptance criterion 2: Care Worker reviews Care Plan

Given that a Care Plan has been created for a Service User

When the Care Worker reviews the Care Plan

Then the Care Worker can record review details

 And the Care Worker can update the Care Plan details

#### Acceptance criterion 3: Care Worker closes the Care Plan

Given that a Care Plan has been created for a Service User

When it is decided that the Service User no longer needs Domiciliary Care services

Then the Care Plan can be closed or made inactive

#### Acceptance criterion 4: Care Worker shares the Service User's Domiciliary Care Plan with other Service Providers

Given that a Care Plan has been created for a Service User

When the Care Worker decides to share the Care Plan with another Service Provider

Then the Care Worker can share the Care Plan with other Service Providers

---

### C27E6 - remote access to Domiciliary Care schedule

As a Care Worker

I want to access Domiciliary Care schedules remotely

So that I can view and amend them anytime

#### Acceptance criterion 1: view Domiciliary Care schedule remotely

Given that the user is permitted to maintain Domiciliary Care schedules

And a Domiciliary Care schedule has been created

When the user chooses to view a Domiciliary Care schedule remotely

Then the Domiciliary Care schedule is displayed

#### Acceptance criterion 2: amend Domiciliary Care schedules remotely

Given that the user is permitted to maintain Domiciliary Care schedules

And a Domiciliary Care schedule has been created

When the user chooses to amend a Domiciliary Care schedule remotely

Then the Domiciliary Care schedule is amended

---

### C27E7 - receive notifications relating to Service User

As a Domiciliary Care Organisation

I want to be informed about changes that will affect a Service User's need for Domiciliary Care (e.g. that they have been admitted to or discharged from Hospital or a Care Home, other changes in domiciliary care needs)

So that I can make informed decisions about starting, modifying, suspending or re-instating their Domiciliary Care package

#### Acceptance criterion 1: Domiciliary Care Organisation is notified about change in Service User's needs

Given that Health or Care Professionals can send notifications in relation to a Service User

When the Health or Care Professional chooses to notify the Domiciliary Care Organisation (e.g. of changes to the Domiciliary Care required by the Service User)

Then the Domiciliary Care Organisation is notified

---

### C27E8 - reports

As a Domiciliary Care Organisation

I Want to run reports

So that I can get key insights into my business (e.g. staff mileage, time spent with Service Users)

#### Acceptance criterion 1: run reports

Given the user is permitted to run reports

When the user chooses to run a  report

Then the report is displayed

---

### C27E9 - nominated individuals to view Domiciliary Care schedule

As a Service User's nominated individual (e.g. proxy)

I want to be able to view Domiciliary Care information for the Service User

So that I have visibility of their Domiciliary Care Plan

#### Acceptance criterion 1: nominated individual views Domiciliary Care schedule information

Given that the nominated individual is permitted to view Domiciliary Care schedule information relating to the Service User

When the nominated individual wants to view Domiciliary Care schedule information

Then the Domiciliary Care schedule information is displayed

**Capability Specific Standards**

Suppliers will have to attain compliance with these Standards during the compliance stage before they can be live on a framework with this Capability:

None

**Other Applicable Standards**

Suppliers will have to attain compliance with these Standards during the compliance stage before they can be live on a framework with this Capability:

- Interoperability Standard
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |