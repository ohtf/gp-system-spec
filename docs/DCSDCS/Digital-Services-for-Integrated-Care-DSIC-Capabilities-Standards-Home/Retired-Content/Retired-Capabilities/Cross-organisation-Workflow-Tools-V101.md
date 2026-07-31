---
page_id: "12750028819"
space: "DCSDCS"
title: "Cross-organisation Workflow Tools V1.0.1"
version: 1
updated: "2024-02-05T10:02:05.306Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12750028819/Cross-organisation+Workflow+Tools+V1.0.1"
labels: ["capability_retired"]
---

# Cross-organisation Workflow Tools V1.0.1

|  |  |
| --- | --- |
| ID | C24 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

## Description

A Cross-Organisation workflow can be defined as a series of tasks undertaken across different organisations by Health and Care Professionals in support of a particular clinical or business process. The Cross-organisation Workflow Tools capability supports such workflows and enables organisations to efficiently manage events throughout the various stages of a process through the automation of standard, repeatable processes.

The Cross-Organisation Workflow Tools Capability reduces the communication burden between Organisations and facilitates better coordination of Patient/Service User care across the health and social care system. It allows tasks in the process to be assigned to the correct Health or Care Professional or other Staff Member (the 'participant') and ensures the participant can perform assigned tasks quickly and efficiently by making relevant information about the Patient/Service User and their care available. This could include artefacts such as a shared assessment or care plan.

The Cross-Organisation Workflow Tools Capability provides health and care organisations with the tools that allow them to effectively manage their work across multi-disciplinary and multi-organisational teams. Progress can be tracked, increasing simplicity and allowing issues to be quickly identified and addressed.

Examples of Cross-Organisation workflows include:

- An assessment by one or more people in different organisations which may trigger a subsequent referral of a patient to external services
- The delivery of a Shared Care Plan across a range of service provider teams
- The assessment of arrangements to support the transfer of a patient (e.g. discharge from hospital to home)
- The review of a document (e.g. Care Plan) by all appropriate staff/organisations involved

# Outcomes

|  |  |
| --- | --- |
| Health or Care Professional or other Participant | - Better informed regarding the status of tasks relating to Patient/Service User's care - Able to perform tasks quickly as all the relevant information is accessible (e.g. as supporting information) - Prompted and reminded to complete tasks |
| Manager | - The ability to monitor progress means issues (e.g. late tasks) can be quickly and easily identified: manual overhead associated with tracking problems across multiple organisations is reduced - Use of workflows and templates allows processes to be standardised and made more consistent across the multiple organisations - Availability of information relating to workflows and tasks allows process design issues (e.g. pinch-points, poor hand-offs) to be identified and addressed |
| Integrated and Federated Care Settings | - Integrated care is better supported through automation of cross-organisational clinical and business processes |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C24E1 - use Workflow to run a Cross-organisational Process

As a Manager

I want to be able to initiate, run and monitor cross-organisational workflows

So that I can ensure the workflows are effectively supporting cross-organisational business and clinical processes

#### Acceptance criterion 1: initiate cross-organisational workflow

Given a workflow has been defined to support a cross-organisational process (e.g. workflow to support diagnosis of diabetes)

When the trigger for the process occurs (e.g. a Patient requires a diabetes diagnosis)

Then the cross-organisational workflow can be initiated

And any information regarding workflow can be provided (e.g. information about the Patient/Service User requiring diagnosis)

And any supporting artefacts can be linked to the workflow (e.g. Patient Assessment Form, care plan, referral)

#### Acceptance criterion 2: monitor in-flight cross-organisational workflows

Given workflows are being used to support cross-organisational business and clinical processes

When the cross-organisational workflow management 'view' is accessed

Then information about cross-organisational workflows can be viewed

And the view can be filtered to display only those workflows meeting criteria defined by the user (e.g. overdue workflows or those assigned to a particular user or organisation)

And the order in which the workflows are presented to view can be changed

#### Acceptance criterion 3: participant performs cross-organisational workflow task

Given a cross-organisational workflow has been initiated

And one or more tasks in the workflow have been assigned to participants

When a participant accesses their task or the cross-organisational workflow

Then they can view information on progress of the workflow

And they can view details of their task

And they can access any documents associated with the task or workflow

And they can update their task (e.g. change the status or provide information relating to the process)

---

### C24E2 - maintain cross-organisational workflows

As a Manager

I want to be able to maintain cross-organisational workflows

So that I can use these workflows to correctly deliver the range of clinical and business processes undertaken across the Organisations

#### Acceptance criterion 1: create cross-organisational workflows

Given workflows are used to support the management of cross-organisational processes

When the need for a cross-organisational workflow is identified (e.g. workflow to support diagnosis of diabetes)

Then the workflow can be created

And information about the workflow can be created

And the events of the workflow can be created

And the workflow events can be assigned to participants

#### Acceptance criterion 2: amend cross-organisational workflows

Given workflows are used to support the management of cross-organisational processes

When the need to amend a cross-organisational workflow is identified (e.g. add or remove steps from the diabetes diagnosis workflow)

Then the workflow can be amended

And information about the workflow can be amended

And the events of the workflow can be amended

And the participants assigned to events in the workflow can be amended

#### Acceptance criterion 3: delete cross-organisational workflows

Given workflows are used to support the management of cross-organisational processes

When a cross-organisational workflow is no longer needed

Then the workflow can be deleted

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C24E3 - maintain cross-organisational workflow templates

As a Manager

I want to have access to cross-organisational task and workflow templates

So that I can efficiently and effectively maintain cross-organisation workflows

#### Acceptance criterion 1: create cross-organisational workflow task or template

Given workflows are used to support the management of cross-organisational processes

And some workflows have shared or common elements

When the need for a cross-organisational workflow task or template is identified

Then the relevant cross-organisational workflow task or template can be created

And the new task or template is available, so workflows can be built based on the task or template

#### Acceptance criterion 2: amend cross-organisational workflow task or template

Given workflows are used to support the management of cross-organisational processes

And some workflows have shared or common elements

When the need to update a cross-organisational workflow task or template is identified

Then the relevant cross-organisational workflow task or template can be amended

And the amended task or template is available, so workflows can be built based on the task or template

#### Acceptance criterion 3: delete cross-organisational workflow task or template

Given workflows are used to support the management of cross-organisational processes

When a cross-organisational workflow task or template is no longer needed

Then the workflow task or template can be deleted

---

### C24E4 - share workflow templates

As a Manager

I want to be able to share existing workflow and task templates

So that I can improve efficiency and consistency by using existing templates to create cross-organisation workflows

#### Acceptance criterion 1: share workflow/task templates

Given that one or more templates exist to support the creation of Workflows and Tasks

When a template is shared with another user

Then the template can be used to create a task or workflow

---

### C24E5 - manage automated notifications and reminders

As a Manager

I want to be able to generate notifications and reminders in relation to tasks and cross-organisational workflows

So that I can ensure that cross-organisational workflows are actively managed and progress smoothly

#### Acceptance criterion 1: configure notifications and reminders

Given a cross-organisational workflow has been configured to support a business or clinical process

When the need to generate notifications or reminders in relation to the workflow is identified

Then reminders or notifications can be configured

#### Acceptance criterion 2: generate notification or reminder

Given a cross-organisational workflow has been configured to generate notifications

And the recipient(s) of the notification or reminder have been defined

And recipient contact details have been captured

When the event that triggers the notification or reminder occurs (e.g. a workflow is initiated or is stopped, task is due or overdue)

Then notifications or reminders are sent to the relevant recipients

---

### C24E6 - manage ad-hoc notifications

As a Manager

I want to be able to manually generate ad hoc notifications in relation to cross-organisational workflows

So that I can ensure appropriate people or organisations are kept informed

#### Acceptance criterion 1: generate ad hoc notifications

Given a cross-organisational workflow has been configured to support a business or clinical process

When the need for an ad hoc notification is identified

Then an ad hoc notification can be configured

And the ad hoc notification is sent to the relevant recipients

### C24E7 - Report on Cross-organisational Workflows

As a Manager

I want to be able to generate reports relating to the use of cross-organisational workflows using a variety of parameters (e.g. types of workflow/task, participants, dates, outcomes, length of time to complete, etc.)

So that I can monitor the effectiveness of the workflows in supporting clinical and business processes and use the information to improve workflow design

#### Acceptance criterion 1: report based on a range of selection criteria

Given that information relating to cross-organisation workflows and their associated tasks is available

And this information is available to the reporting tool

When a reporting need is identified

Then a report can be run to create the relevant output relating to cross-organisational workflows

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