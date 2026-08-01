---
page_id: "14772371457"
space: "DCSDCS"
title: "Care Plans v1.1.0"
version: 1
updated: "2026-02-17T10:41:06.709Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14772371457/Care+Plans+v1.1.0"
labels: ["capability_retired"]
---

# Care Plans v1.1.0

|  |  |
| --- | --- |
| **ID** | C36 |
| **Version** | 1.1.0 |
| **Type** | Capability |
| **Category** | Patient care management |
| **Status** | Retired |
| **Effective Date** | 25 Oct 2024 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

# Description {#CarePlansv1.1.0-Description}

Enables Health or Care Professionals to manage Care Plans for a Patient/Service User.

# Outcomes {#CarePlansv1.1.0-Outcomes}

|  |  |
| --- | --- |
| For a Patient/Service User: | Collects information relevant to the effective and coordinated care of Patients with long term conditions or needs into a single location. |
| For a Health or Care Professional: | Enables the ability to deliver care to a Patient/Service User according to the agreed plan, by providing easy access to a Patient/Service User’s information. |

|  |
| --- |
| **MUST Epics - Describes the minimum functionality required to deliver a Capability. Solutions MUST be successfully evaluated against each Epic and Acceptance Criteria via Capability Assessment in order to be associated with this Capability** |
| E00485 - manage Care Plans {#CarePlansv1.1.0-E00485-manageCarePlans} As a Health or Care Professional  I want to manage Care Plans for Patients/Service Users  So that Care Plans are managed Acceptance criterion 1: create a Care Plan {#CarePlansv1.1.0-Acceptancecriterion1:createaCarePlan} Given the Health or Care Professional is permitted to manage Care Plans for Patients/Service Users  When the Health or Care Professional selects to create a Care Plan for a Patient/Service User  Then the Care Plan is created for the Patient/Service User Acceptance criterion 2: view a Care Plan {#CarePlansv1.1.0-Acceptancecriterion2:viewaCarePlan} Given the Health or Care Professional is permitted to manage Care Plans for Patients/Service Users  When the Health or Care Professional selects to view a Care Plan  Then the Care Plan for the Patient/Service User is displayed Acceptance criterion 3: amend a Care Plan {#CarePlansv1.1.0-Acceptancecriterion3:amendaCarePlan} Given the Health or Care Professional is permitted to manage Care Plans for Patients/Service Users  When the Health or Care Professional selects to amend a Care Plan for a Patient/Service User  Then the Care Plan is amended for the Patient/Service User Acceptance criterion 4: close a Care Plan {#CarePlansv1.1.0-Acceptancecriterion4:closeaCarePlan} Given the Health or Care Professional is permitted to manage Care Plans for Patients/Service Users  When the Health or Care Professional selects to close a Care Plan for a Patient/Service User  Then the Care Plan is recorded as closed for the Patient/Service User E00485 - Supporting Information {#CarePlansv1.1.0-E00485-SupportingInformation}  - Examples of Care Plans MAY include, but are not limited to:    - End of Life Care Plan - contains a Patient/Service User's preferences and wishes for their end of life care   - Urgent Care Plan - contains a Patient/Service User's preferences and wishes in an urgent care setting   - Transitional Care Plan - contains anticipated changes in a Patient/Service User's health status, helping them to manage key transition periods in their life and their care trajectory   - Advanced Care Plan - contains a Patient/Service User’s preferences and wishes regarding their care, to be enacted if they are unable to express a preference in the future   - Escalation Plan - contains the support the Patient/Service User would receive when managing potential future events relating to their condition(s). It may cover what to do when a Patient/Service User's condition deteriorates and may include instructions for emergency care professionals (e.g. paramedics) |

|  |
| --- |
| **MAY Epics - Describes additional functionality associated with the Capability. Suppliers should consider all MAY Epics as part of their User Research. Suppliers can choose to map their Solutions to these Epics and they will be evaluated via Capability Assessment. Contracting Authorities or purchasing organisations may require these Epics as product qualification or requirements criteria** |
| E00486 - grant access to Care Plans {#CarePlansv1.1.0-E00486-grantaccesstoCarePlans} As a Health or Care Professional  I want to grant access to Care Plans to other Health or Care Professionals  So that other Health or Care Professionals can access Care Plans Acceptance criterion 1: grant access to Care Plans {#CarePlansv1.1.0-Acceptancecriterion1:grantaccesstoCarePlans} Given the Health or Care Professional is permitted to manage Care Plans for Patients/Service Users  When the Health or Care Professional selects to grant access to a Patient/Service User’s Care Plan to another Health or Care Professional  Then access to the Patient/Service User’s Care Plan is granted to the other Health or Care Professional   ---  E00487 - search for Care Plans {#CarePlansv1.1.0-E00487-searchforCarePlans} As a Health or Care Professional  I want to search for Care Plans for Patients/Service Users using defined criteria  So that I can access the relevant Care Plan details Acceptance criterion 1: search for Care Plans {#CarePlansv1.1.0-Acceptancecriterion1:searchforCarePlans} Given the Health or Care Professional is permitted to search for Care Plans  When the Health or Care Professional selects to search for Care Plans using defined criteria  Then the search results are displayed   ---  E00488 - manage Care Plan templates {#CarePlansv1.1.0-E00488-manageCarePlantemplates} As a Health or Care Professional  I want to manage Care Plan templates  So that I can improve efficiency by using locally defined templates to create Care Plans Acceptance criterion 1: create a Care Plan template {#CarePlansv1.1.0-Acceptancecriterion1:createaCarePlantemplate} Given the Health or Care Professional is permitted to manage Care Plan templates  When the Health or Care Professional selects to create a Care Plan template  Then the Care Plan template is created Acceptance criterion 2: view a Care Plan template {#CarePlansv1.1.0-Acceptancecriterion2:viewaCarePlantemplate} Given the Health or Care Professional is permitted to manage Care Plan templates  When the Health or Care Professional selects to view a Care Plan template  Then the Care Plan template is displayed Acceptance criterion 3: amend a Care Plan template {#CarePlansv1.1.0-Acceptancecriterion3:amendaCarePlantemplate} Given the Health or Care Professional is permitted to manage Care Plan templates  When the Health or Care Professional selects to amend a Care Plan template  Then the Care Plan template is amended Acceptance criterion 4: delete a Care Plan template {#CarePlansv1.1.0-Acceptancecriterion4:deleteaCarePlantemplate} Given the Health or Care Professional is permitted to manage Care Plan templates  When the Health or Care Professional selects to delete a Care Plan template  Then the Care Plan template is deleted   ---  E00489 - use Supplier implemented Care Plan templates {#CarePlansv1.1.0-E00489-useSupplierimplementedCarePlantemplates} As a Health or Care Professional  I want to create Care Plans for a Patient/Service User using a Care Plan template created by the Supplier  So that I can improve efficiency by using Supplier defined templates to create Care Plans Acceptance criterion 1: use Supplier implemented Care Plan templates {#CarePlansv1.1.0-Acceptancecriterion1:useSupplierimplementedCarePlantemplates} Given the Health or Care Professional is permitted to manage Care Plans for Patients/Service Users  When the Health or Care Professional selects to create a Care Plan for a Patient/Service User  Then they can select to use a Care Plan template provided by the Supplier  And the Care Plan is created for the Patient/Service User   ---  E00490 - view Care Plan reports {#CarePlansv1.1.0-E00490-viewCarePlanreports} As a Health or Care Professional  I want to view Care Plan reports  So that reports relating to Care Plans for Patients/Service Users can be viewed Acceptance criterion 1: view Care Plan reports {#CarePlansv1.1.0-Acceptancecriterion1:viewCarePlanreports} Given the Health or Care Professional is permitted to view Care Plan reports  When the Health or Care Professional selects to view a Care Plan report  Then the report results are displayed |

## Roadmap {#CarePlansv1.1.0-Roadmap}

Items on the Roadmap which impact or relate to this Capability

| Roadmap Item |
| --- |
| No content found. |