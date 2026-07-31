---
page_id: "1391134486"
space: "DCSDCS"
title: "Care Plans"
version: 23
updated: "2026-07-17T10:30:33.111Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391134486/Care+Plans"
labels: ["capability"]
---

# Care Plans

|  |  |
| --- | --- |
| **ID** | C36 |
| **Version** | 1.3.0 |
| **Type** | Capability |
| **Category** | Patient care management |
| **Status** | Effective |
| **Effective Date** | 26 Feb 2026 |
| **Contracting Vehicle(s)** | - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

# Description

Enables Health or Care Professionals to manage Care Plans for a Patient/Service User.

# Outcomes

|  |  |
| --- | --- |
| For a Patient/Service User: | Collects information relevant to the effective and coordinated care of Patients with long term conditions or needs into a single location. |
| For a Health or Care Professional: | Enables the ability to deliver care to a Patient/Service User according to the agreed plan, by providing easy access to a Patient/Service User’s information. |

|  |
| --- |
| **MUST Epics - Describes the minimum functionality required to deliver a Capability. Solutions MUST be successfully evaluated against each Epic and Acceptance Criteria via Capability Assessment in order to be associated with this Capability** |
| E00485 - manage Care Plans As a Health or Care Professional  I want to manage Care Plans for Patients/Service Users  So that Care Plans are managed Acceptance criterion 1: create a Care Plan Given the Health or Care Professional is permitted to manage Care Plans for Patients/Service Users  When the Health or Care Professional selects to create a Care Plan for a Patient/Service User  Then the Care Plan is created for the Patient/Service User Acceptance criterion 2: view a Care Plan Given the Health or Care Professional is permitted to manage Care Plans for Patients/Service Users  When the Health or Care Professional selects to view a Care Plan  Then the Care Plan for the Patient/Service User is displayed Acceptance criterion 3: amend a Care Plan Given the Health or Care Professional is permitted to manage Care Plans for Patients/Service Users  When the Health or Care Professional selects to amend a Care Plan for a Patient/Service User  Then the Care Plan is amended for the Patient/Service User Acceptance criterion 4: close a Care Plan Given the Health or Care Professional is permitted to manage Care Plans for Patients/Service Users  When the Health or Care Professional selects to close a Care Plan for a Patient/Service User  Then the Care Plan is recorded as closed for the Patient/Service User E00485 - Supporting Information  - Examples of Care Plans MAY include, but are not limited to:    - End of Life Care Plan - contains a Patient/Service User's preferences and wishes for their end of life care   - Urgent Care Plan - contains a Patient/Service User's preferences and wishes in an urgent care setting   - Transitional Care Plan - contains anticipated changes in a Patient/Service User's health status, helping them to manage key transition periods in their life and their care trajectory   - Advanced Care Plan - contains a Patient/Service User’s preferences and wishes regarding their care, to be enacted if they are unable to express a preference in the future   - Escalation Plan - contains the support the Patient/Service User would receive when managing potential future events relating to their condition(s). It may cover what to do when a Patient/Service User's condition deteriorates and may include instructions for emergency care professionals (e.g. paramedics) |

|  |
| --- |
| **MAY Epics - Describes additional functionality associated with the Capability. Suppliers should consider all MAY Epics as part of their User Research. Suppliers can choose to map their Solutions to these Epics and they will be evaluated via Capability Assessment. Contracting Authorities or purchasing organisations may require these Epics as product qualification or requirements criteria** |
| E00487 - search for Care Plans As a Health or Care Professional  I want to search for Care Plans for Patients/Service Users using defined criteria  So that I can access the relevant Care Plan details Acceptance criterion 1: search for Care Plans Given the Health or Care Professional is permitted to search for Care Plans  When the Health or Care Professional selects to search for Care Plans using defined criteria  Then the search results are displayed   ---  E00762 - share Care Plans for Patients/Service Users to Health or Care Professionals in other Health Services As a Health or Care Professional  I want to share Care Plans to Health or Care Professionals in other Health Services  So that Care Plans for Patients/Service Users can be shared across multiple Health Services Acceptance criterion 1: share Care Plans for Patients/Service Users to Health or Care Professionals in other Health Services Given the Health or Care Professional is permitted to share Care Plans for Patients/Service Users to Health or Care Professionals in other Health Services  When the Health or Care Professional selects to share a Patient/Service User's Care Plan to a Health or Care Professional in another Health Service  Then the Patient/Service User's Care Plan is shared E00762 - Supporting Information  - Examples of Health Services MAY include, but are not limited to:    - Chiropractic services   - Occupational therapy   - Physiotherapy   - Podiatry   - Speech and language therapy  ---  E00767 - view Patients/Service Users requiring Care Plan reviews As a Health or Care Professional  I want to view Patients/Service Users that require Care Plan reviews  So that I can view Patients/Service Users that require Care Plan reviews Acceptance criterion 1: view Patients/Service Users requiring Care Plan reviews Given the Health or Care Professional is permitted to manage Care Plan reviews for Patients/Service Users  When the Health or Care Professional selects to view Patients/Service Users requiring Care Plan reviews  Then the Patients/Service Users that require a Care Plan review are displayed   ---  E00768 - schedule Care Plan reviews for Patients/Service Users As a Health or Care Professional  I want to schedule Care Plan reviews for Patients/Service Users  So that Care Plan reviews for Patients/Service Users can be conducted Acceptance criterion 1: schedule Care Plan reviews for Patients/Service Users Given the Health or Care Professional is permitted to manage Care Plan reviews for Patients/Service Users  When the Health or Care Professional selects to schedule a Care Plan review for a Patient/Service User  Then the review for the Patient/Service User’s Care Plan is scheduled E00768 - Supporting Information  - Where there are multiple Care Plan reviews that require scheduling, these MAY be scheduled in bulk  ---  E00488 - manage Care Plan templates As a Health or Care Professional  I want to manage Care Plan templates  So that I can improve efficiency by using locally defined templates to create Care Plans Acceptance criterion 1: create a Care Plan template Given the Health or Care Professional is permitted to manage Care Plan templates  When the Health or Care Professional selects to create a Care Plan template  Then the Care Plan template is created Acceptance criterion 2: view a Care Plan template Given the Health or Care Professional is permitted to manage Care Plan templates  When the Health or Care Professional selects to view a Care Plan template  Then the Care Plan template is displayed Acceptance criterion 3: amend a Care Plan template Given the Health or Care Professional is permitted to manage Care Plan templates  When the Health or Care Professional selects to amend a Care Plan template  Then the Care Plan template is amended Acceptance criterion 4: delete a Care Plan template Given the Health or Care Professional is permitted to manage Care Plan templates  When the Health or Care Professional selects to delete a Care Plan template  Then the Care Plan template is deleted   ---  E00489 - use Supplier implemented Care Plan templates As a Health or Care Professional  I want to create Care Plans for a Patient/Service User using a Care Plan template created by the Supplier  So that I can improve efficiency by using Supplier defined templates to create Care Plans Acceptance criterion 1: use Supplier implemented Care Plan templates Given the Health or Care Professional is permitted to manage Care Plans for Patients/Service Users  When the Health or Care Professional selects to create a Care Plan for a Patient/Service User  Then they can select to use a Care Plan template provided by the Supplier  And the Care Plan is created for the Patient/Service User   ---  E00490 - view Care Plan reports As a Health or Care Professional  I want to view Care Plan reports  So that reports relating to Care Plans for Patients/Service Users can be viewed Acceptance criterion 1: view Care Plan reports Given the Health or Care Professional is permitted to view Care Plan reports  When the Health or Care Professional selects to view a Care Plan report  Then the report results are displayed |

## Roadmap

Items on the Roadmap which impact or relate to this Capability

| Roadmap Item |
| --- |
| No content found. |