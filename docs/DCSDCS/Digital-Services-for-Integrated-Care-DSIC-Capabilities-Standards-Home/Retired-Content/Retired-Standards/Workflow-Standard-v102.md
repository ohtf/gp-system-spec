---
page_id: "1391134376"
space: "DCSDCS"
title: "Workflow - Standard v1.0.2"
version: 11
updated: "2023-05-22T10:22:38.816Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391134376/Workflow+-+Standard+v1.0.2"
labels: ["capability_specific_retired"]
---

# Workflow - Standard v1.0.2

|  |  |
| --- | --- |
| ID | S20 |
| Version | 1.0.2 |
| Type | Capability Specific Standard |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - GP IT Futures - Tech Innovation |

# Requirements

| Epic Mapping | Requirement ID | Requirement Text | Level |
| --- | --- | --- | --- |
| C20E1 | **GP-WF-01** | **Task configuration - Create, amend, copy and delete task templates**  Ability to create, amend, copy and delete task templates.  Task templates will be able to contain pertinent data items, including:   - Unique identifier - Name - Version - Template Creator - Template Category (e.g. clinical or admin) - Template Status (e.g. draft, published for use across the Solution, active and inactive) - Task Type (e.g. Review Document, Book Appointment, Clinical Approval) - Task Description - Priority - Expected Duration (e.g. time from generation to expected completion (i.e. due date)) - Assignee(s) (default individual User and/or group/team)    - If group/team, define:     - Number of members to complete (i.e. one, some or all) - Supporting Information (e.g. a link to a document, URL to external website etc. defining policy and procedures) | MUST |
| C20E2 | **GP-WF-02** | **Workflow configuration - Create, amend, copy and delete workflow templates**  Ability to create, amend, copy and delete workflow templates.  Workflow templates will be able to contain pertinent data items, including;   - Unique identifier - Name - Version - Template Creator - Template Category - Template Status (whether draft, published for use across the Solution, active and inactive) - Workflow Type - Workflow Description - Workflow Event(s), including:   - Sequential   - Parallel   - Conditional   - Manual   - Automated (time) (e.g. automatic updating of event after certain time period has passed)   - Automated (data driven) (e.g. automatic triggering of event based on data being recorded) - Supporting Information (e.g. a link to a document, URL to external website etc. defining policy and procedures) - Expected Duration (e.g. time from generation to expected completion (i.e due date))   - Manual   - Derived from duration or anticipated timescales of events - Priority | MUST |
| C20E3, C20E4 | **GP-WF-03** | **Workflows and Tasks - Allocation and prioritisation based on rules**  Support for automatic allocation of workflows and tasks based on Type or Assignee. Allowing defaults to be configured, including:   - Default Task Assignee - Default Task deputy assignee - Default Task Assignee(s) can be an individual User and/or group/team   - Define the order of deputation   - If group/team, define the number of members to complete (i.e one, some or all) - Default Priority | MUST |
| C20E5 | **GP-WF-04** | **Task creation - Create ad-hoc task**  Ability for Practice User to create an ad-hoc task, recording:   - Created By - Creation Date and Time - Patient - Assignee(s) - individual User and/or groups(s)/team(s)   - A task can be assigned to multiple recipients   - The person who created the task can choose if the task is to be completed by one or more recipients - Task Type (e.g. Review Document, Book Appointment, Clinical Approval) - Task Description - Task Status - Priority - Supporting Information (e.g. a link to a document, URL to external website etc. defining policy and procedure) - Expected Due Date (e.g. time from generation to expected completion (i.e due date)) | MUST |
| C20E5 | **GP-WF-05** | **Task creation - Create from template**  Create a task from a task template (see GP-WF-01), recording:   - Created By - Creation Date and Time - Task Status (e.g. To Do) - Patient   With the ability to update any of these data items prior to creation:   - Assignee(s) - individual User and/or groups(s)/team(s)   - A task can be assigned to multiple recipients   - The person who created the task can choose if the task is to be completed by one or more recipients - Task type (e.g. Review Document, Book Appointment, Clinical Approval) - Task Description - Priority - Supporting information (e.g. a link to a document, URL to external website etc. defining policy and procedure) - Expected due date and time (derived from Expected Duration) | MUST |
| C20E6 | **GP-WF-06** | **Workflow creation - Manually from template**  Create a workflow manually using a workflow template (see GP-WF-02), recording:   - Created By - Created Date and Time - Workflow Description - Reason for creation - Workflow Status - Patient - Calculated Expected End Date (i.e based on expected due dates of each workflow event)   With the ability to update any of these data items prior to creation:   - Workflow Type - Workflow Event(s) - Supporting information (e.g. a link to a document, URL to external website etc. defining policy and procedures) - Expected Due Date (derived from Expected Duration) - Priority | MUST |
| C20E6 | **GP-WF-07** | **Workflow generation - Automatically from template**  Generate workflow automatically based on automated (data driven or time) workflow events in a workflow template (See GP-WF-02), recording:   - Created By - Created Date and Time - Workflow Description - Reason for creation - Triggering event - Patient - Calculated Expected End Date (i.e based on expected due dates of each workflow event) - Workflow Type - Workflow Event(s) - Supporting information (e.g. a link to a document, URL to external website etc. defining policy and procedures) - Priority | MUST |
| C20E5 | **GP-10.2-04** | **Task management - Manage task**  Manage a task:   - Perform (e.g. update of status to mark as complete) - Cancel - Delete - Reassign to another individual(s) or group/team(s) - Edit (e.g. change the priority or due by date, insert some notes) | MUST |
| C20E5 | **GP-10.2-04A** | **Task management - Enter a reason**  When managing a task as per GP-10.2-04, Practice User to be able to enter a reason for doing so. | MUST |
| C20E6 | **GP-WF-08** | **Workflow management - Manage Workflow**  Ability to manage a workflow, including:   - Update Workflow Status - Update Workflow Event(s) - Delete - Reassign (i.e. individual User and/or group/team) - Edit (e.g. change the priority or due by date, edit supporting information) | MUST |
| C20E2 | **GP-WF-09** | **Workflow management - Automatically update Calculated expected end date**  Automatically update Calculated expected end date (see GP-WF-02). This to be derived from anticipated timescales within Workflow and event statuses and completion dates). To take account for a Practice’s non-working days (as recorded within the Solution - see E00157 in the Resource Management Capability). | MUST |
| C20E7 | **GP-WF-10** | **Task management - Task List**  Display a list of tasks within the Practice including ability to search list by free text, filter by and sort by all characteristics (as defined in GP-WF-04 as a minimum). | MUST |
| C20E7 | **GP-WF-11** | **Task List - Save Configurations**  Ability to save task list configurations (see GP-WF-10). | MUST |
| C20E12 | **GP-WF-12** | **Task List - Share Configurations**  Ability to share saved task list configurations (see GP-WF-10 and GP-WF-11 above) | MAY |
| C20E8 | **GP-WF-13** | **Workflow management - Workflow List**  Display a list of workflows within the Practice including ability to search list by free text, filter by and sort by all characteristics (as defined in GP-WF-06 as a minimum). | MUST |
| C20E8 | **GP-WF-14** | **Workflow List - Save Configurations**  Ability to save workflow list configurations (see GP-WF-13). | MUST |
| C20E13 | **GP-WF-15** | **Workflow List - Share Configurations**  Ability to share saved workflow list configurations (see GP-WF-14) | MAY |
| C20E5 | **GP-WF-16** | **Task management - View Task**  Ability to view all information for an individual task so a Practice User can manage or perform the Task. | MUST |
| C20E6 | **GP-WF-17** | **Workflow management - View Workflow**  Ability to view all information for an individual workflow so a Practice User can manage the Workflow. | MUST |
| C20E5 | **GP-WF-4.2-10** | **Task management - Overdue tasks**  Indicate a task as ‘overdue’ if it is not completed when the Expected Due Date is surpassed. | MUST |
| C20E6 | **GP-WF-18** | **Workflow management - Overdue Workflows**  Indicate a workflow as ‘overdue’ if it is not completed when the Expected Due Date is surpassed. | MUST |
| C20E11 | **GP-WF-6-01** | **Access Patient Record**  Access a Patient Record where a Patient has been successfully identified, linked, listed or otherwise presented to the user. | MUST |

# Capability

**Applicable Capability**

All supplier Solutions will need to meet this Standard if they are delivering the Workflow Capability

# Roadmap

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |