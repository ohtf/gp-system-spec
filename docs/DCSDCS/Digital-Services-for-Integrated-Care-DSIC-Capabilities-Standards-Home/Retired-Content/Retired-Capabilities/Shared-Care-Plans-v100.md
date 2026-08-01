---
page_id: "1692893641"
space: "DCSDCS"
title: "Shared Care Plans v1.0.0"
version: 2
updated: "2020-01-15T16:38:56.037Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1692893641/Shared+Care+Plans+v1.0.0"
labels: ["capability_retired"]
---

# Shared Care Plans v1.0.0

|  |  |
| --- | --- |
| ID | C36 |
| Version | 1.0.0 |
| Type | Capability |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description {#SharedCarePlansv1.0.0-Description}

Shared Care Plans support a Patient-centred approach to care. It allows Health and Care Professionals to view and maintain a single, shared Plan for the Patient/Service User rather than holding separate and disconnected Plans within the individual health and care organisations. It encourages a collaborative approach to supporting Patients/Service Users to meet their health and care needs, including Patients/Service Users with long-term conditions or in residential care. Health or Care Professionals with appropriate access rights involved in delivering care for the Patient/Service User can see and contribute to a Patient/Service User's Care Plan. Guardians, Caregivers with appropriate access rights or the Patient/Service User can also view and update them.

In integrated care settings, all members of the Care Team should have access to the same information and can build upon the Shared Care Plan. Team members act in coordination towards a common goal to provide integrated care and avoid errors. A Shared Care Plan functions as a living document that members of the Care Team refer to or update on an ongoing basis. Service Providers must also be able to seamlessly share and access Shared Care Plans across health or care settings that use different IT systems.

Examples of Care Plans include:

- End of Life Care - contains a Patient/Service User's preferences and wishes for their end of life care
- Urgent Care Plan - contains a Patient/Service User's preferences and wishes in an urgent care setting
- Transitional Care - contains anticipated changes in a Patient/Service User's health status, helping them manage key transition periods in their lives and their care trajectory
- Advanced Care Plan - Following a discussion with the individual about their future wishes and priorities regarding the type of care they would wish to receive and where they wish to be cared for, the plan may be enacted if they lose capacity or are unable to express a preference in the future
- Escalation Plan - contains the support the Patient/Service User would receive in managing potential future events relating to their condition(s). It may cover what to do when Patient/Service User's condition deteriorates and may include instructions for emergency care professionals (e.g. paramedics)

# Outcomes {#SharedCarePlansv1.0.0-Outcomes}

|  |  |
| --- | --- |
| Patient/Service User | - I have a better experience as I do not have to repeat my health condition and Shared Care Plan information to different Health or Care Professionals - I have a say in my health and care plans as I can contribute to the Shared Care Plan and help in setting goals and outcomes that I would like to achieve |
| Care Team (Care Coordinator, nurses, health professionals, Carer (family or friend), GP) | - The sharing of information helps me work collaboratively with other members of the Care Team - I can make informed decisions as the Patient/Service User’s Shared Care Plan information is shared, up to date and real-time - I am better informed as have easy access to information about the Patient/Service User, progress of the Shared Care Plan in achieving outcomes and my own work |
| Other Organisations (e.g. NHS111, Hospitals, Community Service Providers, Schools). | - I can make informed decisions for the well-being of the Patient/Service User as I can view up-to-date Shared Care Plan information for the Patient/Service User |
| Family members, friends and other Carers | - I am informed and involved as I can view or contribute to the Shared Care Plan of the person I care for |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### EpicSC1 - create Shared Care Plan  {#SharedCarePlansv1.0.0-EpicSC1-createSharedCarePlan}

As a Care Team Member

I want to be able to create Shared Care Plans

So that I can collaborate with other Care Team Members in delivering care to a Patient/Service User

#### Acceptance criterion 1: Care Team Member creates a Shared Care Plan for the Patient/Service User {#SharedCarePlansv1.0.0-Acceptancecriterion1:CareTeamMembercreatesaSharedCarePlanforthePatient/ServiceUser}

Given that the Patient/Service User has been assessed as 'in need of planned care'

And the Care Team Member is permitted to create Shared Care Plans

When the need for a Shared Care Plan is identified for a Patient/Service User

Then the Care Team Member can create a Shared Care Plan for the Patient/Service User

And they can record information relating to the Shared Care Plan

And the Care Plan can be shared with other Care Team Members

---

### EpicSC2 - view Shared Care Plan  {#SharedCarePlansv1.0.0-EpicSC2-viewSharedCarePlan}

As a Care Team Member

I want to be able to view the Shared Care Plan for a Patient/Service User

So that I can understand the Patient/Service User's Plan and use it to deliver the right care

#### Acceptance criterion 1: Care Team Member views a Shared Care Plan for the Patient/Service User {#SharedCarePlansv1.0.0-Acceptancecriterion1:CareTeamMemberviewsaSharedCarePlanforthePatient/ServiceUser}

Given that the Patient/Service User’s Shared Care Plan has been defined

And the Care Team Member is permitted to view Shared Care Plans

When the Care Team Member wants to view the plan for the Patient/Service User

Then the Shared Care Plan for the Patient/Service User is displayed

---

### EpicSC3 - amend Shared Care Plan {#SharedCarePlansv1.0.0-EpicSC3-amendSharedCarePlan}

As a Care Team Member

I want to be able to amend Shared Care Plans

So that progress against the Shared Care Plan can be tracked and the Shared Care Plan can be updated to align to any change in needs of the Patient/Service User

#### Acceptance criterion 1: Shared Care Plan is amended by a Care Team Member or Patient/Service User {#SharedCarePlansv1.0.0-Acceptancecriterion1:SharedCarePlanisamendedbyaCareTeamMemberorPatient/ServiceUser}

Given that the Patient/Service User’s Shared Care Plan has been defined

And the Care Team Member is permitted to amend Shared Care Plans

When a change to the Shared Care Plan is agreed with the Patient/Service User

Then the Shared Care Plan can be amended

---

### EpicSC4 - close Shared Care Plan  {#SharedCarePlansv1.0.0-EpicSC4-closeSharedCarePlan}

As a Care Team Member

I want to be able to close a Shared Care Plan when it is no longer needed

So that I have an accurate view of active and inactive Shared Care Plans

#### Acceptance criterion 1: Care Team Member closes the Shared Care Plan {#SharedCarePlansv1.0.0-Acceptancecriterion1:CareTeamMemberclosestheSharedCarePlan}

Given that the Patient/Service User’s Shared Care Plan has been defined

And the Care Team Member is permitted to close Shared Care Plans

When it is identified that the Shared Care Plan is no longer needed (e.g. desired outcomes have been achieved or the Patient/Service User no longer needs support)

Then the Shared Care Plan can be closed or made inactive

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### EpicSC5 - assign Shared Care Plan actions {#SharedCarePlansv1.0.0-EpicSC5-assignSharedCarePlanactions}

As a Care Team Member

I want to be able to assign actions to a member of the Care Team, the Patient/Service User or their Carer and monitor progress

So that I can track progress against the Shared Care Plan and ensure the outcomes are achieved

#### Acceptance criterion 1:  assign action to Care Team Member, Patient/Service User or Carer {#SharedCarePlansv1.0.0-Acceptancecriterion1:assignactiontoCareTeamMember,Patient/ServiceUserorCarer}

Given that the Patient/Service User’s Shared Care Plan has been defined

When an action needs to be assigned to support delivery of the Shared Care Plan for a Patient/Service User

Then actions can be assigned to a member of the Care Team or the Patient/Service User

And progress on actions can be captured or recorded

And progress can be tracked

---

### EpicSC6 - access Shared Care Plans remotely {#SharedCarePlansv1.0.0-EpicSC6-accessSharedCarePlansremotely}

As a Care Team Member

I want to be able to access and update Shared Care Plans when I am away from my workstation (e.g. during field visits)

So that I can improve productivity by being able to maintain the Shared Care Plan even when I am working remotely

#### Acceptance criterion 1: Care Team Members can view and update the Shared Care Plan during field visits {#SharedCarePlansv1.0.0-Acceptancecriterion1:CareTeamMemberscanviewandupdatetheSharedCarePlanduringfieldvisits}

Given that there is a Shared Care Plan for the Patient/Service User

When the Care Team Members is working remotely (e.g. on field visits)

Then they can view the Shared Care Plan

And any updates to the Shared Care Plan can be made

---

### EpicSC7 - search and view Shared Care Plans {#SharedCarePlansv1.0.0-EpicSC7-searchandviewSharedCarePlans}

As a Care Team Member

I want to be able to search for the Shared Care Plan for Patients/Service Users using search criteria

So that I can access the relevant Shared Care Plan details

#### Acceptance criterion 1: Care Team Member searches for and views Shared Care Plans {#SharedCarePlansv1.0.0-Acceptancecriterion1:CareTeamMembersearchesforandviewsSharedCarePlans}

Given Shared Care Plans have been set up for Patients/Service Users

When criteria (e.g. Patient/Service User name, type of plan) are used to search for Patients/Service Users or their Shared Care Plans

Then a list of records that match the criteria is displayed

And one or more Shared Care Plans can be selected to be viewed

---

### EpicSC8 - real-time access to Shared Care Plans {#SharedCarePlansv1.0.0-EpicSC8-real-timeaccesstoSharedCarePlans}

As a Care Team Member

I want to have continuous access to the current version of a Shared Care Plan within its availability target (e.g. 24x7 and 365 days per year)

So that I can make informed decisions for the Patient/Service User based on the most up-to-date information available in the Shared Care Plan

#### Acceptance criterion 1: Shared Care Plans availability {#SharedCarePlansv1.0.0-Acceptancecriterion1:SharedCarePlansavailability}

Given that there is a Shared Care Plan for the Patient/Service User

When the Shared Care Plan is accessed within its availability target period

Then the Shared Care Plan is available to view and / or update

---

### EpicSC9 - notifications {#SharedCarePlansv1.0.0-EpicSC9-notifications}

As a Care Team Member, Patient/Service User or other person who has access to a Shared Care Plan

I want to be able to send and receive notifications in relation to a Shared Care Plan

So that I can ensure that everyone who is involved in the health or care of the Patient/Service User is kept up to date with any changes to the Shared Care Plan

#### Acceptance criterion 1: send message in relation to Shared Care Plan {#SharedCarePlansv1.0.0-Acceptancecriterion1:sendmessageinrelationtoSharedCarePlan}

Given that the Care Team Member(s), Patient/Service User or other has authorised access to the Shared Care Plan Solution

When they need to communicate with another Care Team Member, the Patient/Service User or their Carer in relation to a Shared Care Plan

Then a message or notification can be sent to one or more recipients

And the message can be read only by the intended recipient(s)

#### Acceptance criterion 2: receive message in relation to Shared Care Plan {#SharedCarePlansv1.0.0-Acceptancecriterion2:receivemessageinrelationtoSharedCarePlan}

Given that the Care Team Member(s), Patient/Service User or other has authorised access to the Shared Care Plan Solution

When a message or notification is received relating to the Shared Care Plan (e.g. action assigned or change to the Plan)

Then they receive a message or notification

And they can view the message or notification

---

### EpicSC10 - reports {#SharedCarePlansv1.0.0-EpicSC10-reports}

As a Care Team Member

I want to have access to custom reports relating to the Shared Care Plans for my Patients/Service Users

So that I can use the information to plan my work better

#### Acceptance criterion 1: Care Team Member views reports {#SharedCarePlansv1.0.0-Acceptancecriterion1:CareTeamMemberviewsreports}

Given that the Care Team Member(s) has access to the Shared Care Plans for one or more Patients/Service Users

And the Care Team Member has access to run reports

When the Care Team Members wants to report on information relating to Shared Care Plans

Then a report can be run to create the relevant output relating to Shared Care Plans

---

### EpicSC11 - manage Shared Care Plan templates {#SharedCarePlansv1.0.0-EpicSC11-manageSharedCarePlantemplates}

As a Care Team Member

I want to be able to maintain Shared Care Plan templates or utilise preloaded Shared Care Plan templates

So that I can improve efficiency by using existing templates to create Shared Care Plans

#### Acceptance criterion 1: Use preloaded Shared Care Plan templates {#SharedCarePlansv1.0.0-Acceptancecriterion1:UsepreloadedSharedCarePlantemplates}

Given that the Care Team Members have authorised access to the Shared Care Plan Solution

When they want to use a Shared Care Plan template to create a Shared Care Plan for a Patient/Service User

Then they can access an existing template

And use the template to create the Shared Care Plan for the Patient/Service User

#### Acceptance criterion 2: maintain Shared Care Plan templates {#SharedCarePlansv1.0.0-Acceptancecriterion2:maintainSharedCarePlantemplates}

Given that a Care Team Member has authorised access to maintain templates in the Shared Care Plan Solution

When a change is required relating to a Shared Care Plan template

Then the Care Team Member can create, update or delete the relevant Shared Care Plan template

---

### EpicSC12 - manage care schedules {#SharedCarePlansv1.0.0-EpicSC12-managecareschedules}

As a Care Team Member

I want to be able to manage my care schedule

So that I can plan my upcoming Patient/Service User visits and actions relating to their Shared Care Plan

#### Acceptance criterion 1: Care Team Member manages care schedules {#SharedCarePlansv1.0.0-Acceptancecriterion1:CareTeamMembermanagescareschedules}

Given that a Care Team Member has authorised access to the Shared Care Plan Solution

When they need a new or updated care schedule

Then they can create or update a care schedule

And information can be recorded about the planned visit(s)

And the schedule can be shared with other Care Team members and Patients/Service Users as appropriate

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