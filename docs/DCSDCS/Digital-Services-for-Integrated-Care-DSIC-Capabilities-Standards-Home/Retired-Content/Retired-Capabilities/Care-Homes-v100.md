---
page_id: "1686536581"
space: "DCSDCS"
title: "Care Homes v1.0.0"
version: 2
updated: "2020-01-15T16:24:14.899Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1686536581/Care+Homes+v1.0.0"
labels: ["capability_retired"]
---

# Care Homes v1.0.0

|  |  |
| --- | --- |
| ID | C21 |
| Version | 1.0.0 |
| Type | Capability |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description

The Care Home Capability supports the provision of health and care services to Residents who are residing in a Care Home.

The Capability supports the creation and maintenance of a Resident's record, ensuring an accurate, complete and up-to-date view of the Resident's health, care, personal and legal information. Providing the correct permissions are in place, the record can be made available to Care Home clinicians and other staff, external clinicians and any Proxies identified by the Resident.

The Capability has the potential to support a much wider range of operational and care-related processes including:

- Maintenance of staff records
- Scheduling and tracking of care-related tasks and activities (e.g. medication administration, exercise classes, pressure area assessments)
- Recording of incidents and adverse events

The Capability may also contribute to improvements in performance through provision of data for analysis.

# Outcomes

|  |  |
| --- | --- |
| Residents or their Proxies | - Peace of mind knowing that everyone involved in the Resident's care   - knows their personal needs   - is aware of their wishes and preferences regarding any delegated responsibilities to Proxies (e.g. friends, family)   - has access to any and all of the Resident's Care Plans (such as End of Life Care Plans)   - knows who is undertaking which activities and when |
| Care Home Clinical Staff | - Able to view and record information about the Resident including notes, care activities (e.g. medicines administration record (MAR chart), assessments, etc) in their record - Have access to each Resident's Care Plans and have up to date information regarding these plans (e.g. newly recorded data, progress or planned activities) - Record incidents and adverse events and communicate these with others as required |
| External Health or Care Professional | - Have full access to a Resident's Care Home record such as medication, interventions, test results and any applicable legal safeguards or care directions - Be able to record incidents and adverse events and to communicate these with other Care Workers involved in a Resident's care as required - Be notified of any incidents or adverse events that arise so they can participate in any decisions regarding mitigating actions |
| Care Home Administrators | - Schedule staff rotas and staff tasks efficiently utilising the most appropriate staff - Track actual versus scheduled tasks - Have access to a reporting system to monitor resource (e.g. staff) usage, analyse tasks, incidents and adverse events, and patient clinical data held in their local records - Maintain staff records |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### EpicCH1 - maintain Resident's Care Home Record

As a Health or Care Professional with a legitimate relationship to a Care Home Resident

I want to maintain a comprehensive record of the Resident and their care

So that I can ensure that a comprehensive record of their care is maintained and is accessible

#### Acceptance criterion 1: create Resident's record

Given the user has the correct permissions to create a Resident record

When a record for a Resident is required

Then the record for the Resident can be created

And details about the Resident can be recorded

#### Acceptance criterion 2: view Resident's record

Given a user (e.g. Health or Care Professional, Care Home Staff Member) has permissions to view the Resident's record

When they choose to view the Resident's record

Then they can view the Resident's record

#### Acceptance criterion 3: amend Resident's record

Given the user has the correct permissions to amend a Resident record

When an update to a Resident's record is required

Then the record for the Resident can be updated

#### Acceptance criterion 4: close Resident's record

Given the user has the correct permissions to close a Resident record

When a Resident's record is no longer required

Then the record for the Resident can be closed or made inactive

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### EpicCH2 - maintain Resident Proxy preferences

As a Care Home Manager

I want to maintain records of a Resident's consent preferences regarding a Proxy (e.g. spouse, relative, friend)

So that I can ensure a Resident's consent preferences are correct

#### Acceptance criterion 1: maintain Resident's preferences regarding Proxies

Given a Resident has nominated a Proxy

And has identified their preferences with respect to the Proxy (e.g. Proxy can view the Resident's record, Proxy can take decisions on behalf of the Resident)

When the user of the Care Home Solution accesses the Resident's record

Then they are able to view any existing preferences

And amend the record to reflect the details of the proxy

And record the Resident's preferences with regard to the Proxy and decision-making circumstances

#### Acceptance criterion 2: Proxy accesses Resident's record

Given a Resident has nominated a Proxy to have access to view their record

When the Resident's preferences regarding the Proxy are recorded

Then the Proxy can view the Resident's record

#### Acceptance criterion 3: treatment assent given by Proxy

Given a Resident's Care Plan requires agreement for a treatment to go ahead

And the Resident's record indicates a Proxy is in place for such decisions

When the Proxy provides assent to the treatment

Then details of the decision being made by the Proxy (rather than the Resident themselves) can be recorded

---

### EpicCH3 - view and maintain End of Life Care Plans

As a Care Home Manager

I want to ensure that everyone involved in a Resident's care can view and maintain an End of Life Care Plan

So that a Resident's wishes regarding End of Life Care are recorded and can be respected should the plan be enacted

#### Acceptance criterion 1: create an End of Life Care Plan for a Resident

Given the user has the correct permissions to create an End of Life Care Plan for a Resident

When an End of Life Care Plan is required for a Resident

Then an End of Life Care Plan for the Resident can be created

And the Resident's wishes and preferences can be recorded

And the Resident's record indicates that the plan exists

And the End of Life Care Plan's existence can be communicated to other interested parties (e.g. G.P.)

#### Acceptance criterion 2: view End of Life Care Plan for a Resident

Given a user (e.g. Health or Care Professional, Care Home Staff Member) has permissions to view the End of Life Care Plan

When they choose to view the End of Life Care Plan

Then they can view the Resident's End of Life Care Plan

#### Acceptance criterion 3: amend an End of Life Care Plan for a Resident

Given the user has the correct permissions to amend an End of Life Care Plan for a Resident

When a change is required to an End of Life Care Plan for a Resident

Then the End of Life Care Plan for the Resident can be amended

#### Acceptance criterion 4: close an End of Life Care Plan for a Resident

Given the user has the correct permissions to close an End of Life Care Plan for a Resident

When the End of Life Care Plan for a Resident is no longer required

Then the End of Life Care Plan for the Resident can be closed or made inactive

#### Acceptance criterion 5: record the existence of an externally held but accessible End of Life Care Plan for a Resident

Given a Record exists for a Resident

When the existence an End of Life Care Plan, held by another organisation, is identified for the Resident

Then information about the existing End of Life Care Plan can be recorded (e.g. where it is held, how it can be accessed)

---

### EpicCH4 - record incident and adverse events

As a Health or Care Professional providing a service to the Resident

I want to record details of any Resident-related incidents or adverse events and inform others involved in their care about them

So that I can ensure that others involved in their care can contribute to any immediate care decisions and any mitigating actions to prevent further occurrence of such events

#### Acceptance criterion 1: generate an incident or adverse event report

Given there is provision to record information about incident or adverse events

When an incident or adverse event occurs involving a Resident

Then a record of the incident or adverse event can be created

And the record can be maintained

#### Acceptance criterion 2: receive an automatic incident or adverse event report notification

Given an incident or adverse event has arisen concerning a Resident

And the Solution has been configured to identify who receives notifications about incidents and adverse events

When the details of an incident or adverse event are recorded

Then notifications are sent to the relevant recipients

---

### EpicCH5 - maintain Staff Records

As a Care Home Manager

I want to be able to maintain accurate records for Staff Members

So that I can use the information to generate schedules and assign appropriate staff to undertake activities related to Resident care

#### Acceptance criterion 1: maintain staff record

Given a record is required for Staff Members

And the user has the correct permissions to maintain the record

When the staff records option is selected

Then the record for a Staff Member can be maintained (created or updated)

And information about the Staff Member can be recorded

---

### EpicCH6 - maintain Staff Task schedules

As a Care Home Manager

I want to be able to create and maintain schedules

So that tasks relating to Resident care are delivered efficiently (i.e. right time) and effectively (i.e. right person and skills)

#### Acceptance criterion 1: create Staff schedules

Given care-related tasks are required (e.g. medication administration, dressing changes, bed changes, etc) for Residents at defined frequencies

And information relating to the required tasks in known (e.g. frequency, type of staff required)

And information relating to Staff Members is available (e.g. availability, skills and qualifications)

When a staff schedule is required

Then a schedule can be generated that allocates appropriate staff to each task

And reports on any unassigned tasks or conflicts

And the schedule can be saved

#### Acceptance criterion 2: manually amend Staff schedules

Given a schedule of tasks has been created

When changes are required (e.g. add ad hoc tasks, remove tasks, resolve conflicts)

Then the schedule can be manually amended

And the Solution notifies the user of any conflicts

And the changes to the schedule can be saved

---

### EpicCH7 - manage Tasks

As a Care Home Manager

I want to monitor the status of tasks assigned to members of staff

So that I can identify and respond to any issues with delivery of care tasks

#### Acceptance criterion 1: monitor Task progress

Given a schedule of routine tasks has been created

And there is a means for staff to identify when tasks are started and completed

And there is a means to track task progress

When the report or dashboard of progress is selected

Then information relating to the progress of tasks (e.g. start time, status) can be viewed

#### Acceptance criterion 2: generate Task reminder

Given a Staff Member has been assigned a task to commence at a scheduled time

When a task is due

Then a reminder is generated

And the reminder is sent to the assigned Staff Member

And a further reminder can be sent if the task becomes overdue

---

### EpicCH8 - reporting

As a Care Home Manager

I want to generate reports relating to the care provided to Residents

So that I can better plan and manage the delivery of care

#### Acceptance criterion 1: reports based on a range of selection criteria

Given that information relating to care of Residents is available (e.g. Resident records, information about care tasks or incidents or adverse events)

And this information is available to the reporting Solution

And selection rules have been defined to identify records meeting certain criteria (e.g. Residents taking a specific medication, tasks that took longer than expected)

When the report is run

Then only those records with matching values are output

And the output can be analysed to identify trends or performance

---

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