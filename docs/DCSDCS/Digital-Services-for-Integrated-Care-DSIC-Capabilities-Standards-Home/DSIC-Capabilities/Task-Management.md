---
page_id: "12417368065"
space: "DCSDCS"
title: "Task Management"
version: 8
updated: "2026-07-17T11:14:13.162Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12417368065/Task+Management"
labels: ["capability"]
---

# Task Management

|  |  |
| --- | --- |
| **ID** | C50 |
| **Version** | 1.1.0 |
| **Type** | Capability |
| **Category** | Health or care organisation management |
| **Status** | Effective |
| **Effective Date** | 26 Feb 2026 |
| **Contracting Vehicle(s)** | - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

# Description

Supports the management of Tasks relating to activities within a Health or Care Organisation.

# Outcomes

|  |  |
| --- | --- |
| For a Patient/Service User: | Receive accurate and efficient care provision from effective management of Tasks. |
| For Health or Care Organisations: | Supporting and facilitating the coordination of Patient/Service User care within the Health or Care Organisation. |

|  |
| --- |
| **MUST Epics - Describes the minimum functionality required to deliver a Capability. Solutions MUST be successfully evaluated against each Epic and Acceptance Criteria via Capability Assessment in order to be associated with this Capability.** |
| E00267 - manage Tasks As a Health or Care Professional  I want to manage Tasks  So thatI can manage activities within Health or Care Organisations Acceptance criterion 1: create a Task Given a Health or Care Professional is permitted to manage Tasks  When the creation of a Task is triggered  Then the Task is created Acceptance criterion 2: view a Task Given a Health or Care Professional is permitted to manage Tasks  When the Health or Care Professional selects to view a Task  Then the Task is displayed Acceptance criterion 3: amend a Task Given the Health or Care Professional is permitted to manage Tasks  When the Health or Care Professional selects to amend a Task  Then the Task is amended Acceptance criterion 4: delete a Task Given the Health or Care Professional is permitted to manage Tasks  When the Health or Care Professional selects to delete a Task  Then the Task is deleted E00267 - Supporting Information  - Examples of data items for Task creation MAY include, but are not limited to;    - Task Type   - Task Description   - Creator   - Creation Date and Time   - Task Status   - Expected Due Date   - Priority   - Supporting Information (e.g. a link to a document, URL to external website etc.) |

|  |
| --- |
| **MAY Epics - Describes additional functionality associated with the Capability. Suppliers should consider all MAY Epics as part of their User Research. Suppliers can choose to map their Solutions to these Epics and they will be evaluated via Capability Assessment. Contracting Authorities or purchasing organisations may require these Epics as product qualification or requirements criteria.** |
| E00268 - manually create ad-hoc Tasks As a Health or Care Professional  I want to manually create ad-hoc Tasks  So that Tasks can be manually created when required Acceptance criterion 1: create ad-hoc Tasks Given a Health or Care Professional is permitted to manage Tasks  When the Health or Care Professional selects to manually create a Task  Then the Task is created   ---  E00269 - assign Tasks to Health or Care Professionals As a Health or Care Professional  I want to manage Task assignments  So that I can assign Tasks to Health or Care Professionals Acceptance criterion 1: assign a Task Given a Health or Care Professional is permitted to manage Tasks  When the Health or Care Professional selects to assign a Task to a Health or Care Professional  Then the Task is assigned to the Health or Care Professional Acceptance criterion 2: reassign a Task Given a Health or Care Professional is permitted to manage Tasks  When the Health or Care Professional selects to reassign a Task to another Health or Care Professional  Then the Task is reassigned to another Health or Care Professional E00269 - Supporting Information  - A Task MAY be assigned or reassigned to an individual Health or Care Professional or multiple Health or Care Professionals - The person who created the Task MAY select if the Task is to be completed by one or more Health or Care Professionals  ---  E00270 - flag overdue Tasks As a Health or Care Professional  I want overdue Tasks to be automatically flagged  So that I can see which Tasks are overdue Acceptance criterion 1: flag overdue Tasks Given there are overdue Tasks  When a Health or Care Professional is viewing Tasks  Then overdue Tasks are flagged E00270 - Supporting Information  - For example, Indicate a Task as ‘overdue’ if it is not completed when the Expected Due Date is surpassed  ---  E00271 - manage Task templates As a Health or Care Professional  I want to manage Task templates  So that ad-hoc Tasks can be created based on a template Acceptance criterion 1: create a Task template Given a Health or Care Professional is permitted to manage Task templates  When the Health or Care Professional selects to create a Task template  Then the Task template is created Acceptance criterion 2: create a Task from a Task template Given a Health or Care Professional is permitted to manage Task templates  When the Health or Care Professional selects to create a Task from a Task template  Then the Task is created Acceptance criterion 3: view a Task template Given a Health or Care Professional is permitted to manage Task templates  When the Health or Care Professional selects to view a Task template  Then the Task template is displayed Acceptance criterion 4: amend a Task template Given a Health or Care Professional is permitted to manage Task templates  When the Health or Care Professional selects to amend a Task template  Then the Task template is amended Acceptance criterion 5: delete a Task template Given a Health or Care Professional is permitted to manage Task templates  When the Health or Care Professional selects to delete a Task template  Then the Task template is deleted E00271 - Supporting Information  - Task templates MAY include, but are not limited to;    - Template Name   - Task Type   - Task Description   - Creator   - Creation Date and Time   - Task Status   - Assignee   - Expected Due Date   - Priority   - Supporting Information (e.g. a link to a document, URL to external website etc.)  ---  E00769 - share Task templates As a Health or Care Professional  I want to share existing task templates  So that I can improve consistency by using existing templates to create tasks Acceptance criterion 1: share task templates Given the Health or Care Professional is permitted to share task templates  When the Health or Care Professional selects to share a task template with another Health or Care Professional  Then the task template is shared   ---  E00272 - manage a personalised display for Tasks As a Health or Care Professional  I want to manage a personalised display for Tasks  So that I have a personalised display of Tasks that can be saved and applied to Tasks Acceptance criterion 1: create a personalised display of Tasks Given the Health or Care Professional is permitted to manage Tasks  When the Health or Care Professional select to create a personalised display for Tasks  Then a personalised display is created Acceptance criterion 2: view Tasks using personalised display Given the Health or Care Professional is permitted to manage Tasks  When the Health or Care Professional select to view Tasks  And they have created a personalised display for their Tasks  Then the Tasks are displayed with the personalised display applied Acceptance criterion 3: delete a personalised display of Tasks Given the Health or Care Professional has created a personalised display for Tasks  When the Health or Care Professional select to delete the personalised display for Tasks  Then the personalised display is deleted  And Tasks are displayed with the default display applied E00272 - Supporting Information  - Examples of Task personalisation MAY include, but are not limited to:    - Reordering the Task content, for example chronologically or based on certain characteristics   - Filtering Tasks in or out based on certain characteristics  ---  E00273 - configure Task rules As a Health or Care Professional  I want to configure rules for Tasks  So that rules for Tasks can be applied Acceptance criterion 1: create a Task rule Given the Health or Care Professional is permitted to manage Task rules  When the Health or Care Professional selects to define a rule  Then the Task rule is created Acceptance criterion 2: applying a Task rule Given Task rules have been created  When a Health or Care Professional creates a Task  And the criteria for a Task rule is met  Then the Task rule is applied E00273 - Supporting Information  - Examples of rules MAY include, but not limited to;    - Default Task Assignee   - Default Priority  ---  E00274 - view Task reports As a Health or Care Professional  I want to view Task reports  So that I can see Task activity Acceptance criterion 1: view Task reports Given the Health or Care Professional is permitted to view Task reports  When the Health or Care Professional selects to view a Task report  Then the Task report is displayed E00274 - Supporting Information Examples of reports MAY include, but not limited to:   - An aggregated dashboard view of the status of Tasks assigned to Health or Care Professionals |

## Roadmap

Items on the Roadmap which impact or relate to this Capability

| Title |
| --- |
| No content found. |