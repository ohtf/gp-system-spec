---
page_id: "1391135549"
space: "DCSDCS"
title: "Telecare"
version: 29
updated: "2026-07-17T11:14:36.309Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391135549/Telecare"
labels: ["capability"]
---

# Telecare

|  |  |
| --- | --- |
| **ID** | C38 |
| **Version** | 1.0.2 |
| **Type** | Capability |
| **Category** | Community-based care |
| **Status** | Effective |
| **Effective Date** | 05 Mar 2024 |
| **Contracting Vehicle(s)** | - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

# Description {#Telecare-Description}

Enables Health or Care Professionals to configure adverse event notifications so that Telecare devices can automatically send adverse event notifications on behalf of Patient/Service Users.

# Outcomes {#Telecare-Outcomes}

|  |  |
| --- | --- |
| For Health or Care Professionals: | Able to configure adverse event notifications to be sent by Telecare devices as per the needs of Patient/Service Users. |
| For Patient/Service Users: | Telecare devices automatically send notifications when adverse events occur which affect the Patient/Service User. |

|  |
| --- |
| **MUST Epics - Describes the minimum functionality required to deliver a Capability. Solutions MUST be successfully evaluated against each Epic and Acceptance Criteria via Capability Assessment in order to be associated with this Capability** |
| E00670 - configure adverse event notifications {#Telecare-E00670-configureadverseeventnotifications} As a Health or Care Professional  I want to configure adverse event notifications  So that I can configure adverse event notifications Acceptance criterion 1: configure adverse event notifications {#Telecare-Acceptancecriterion1:configureadverseeventnotifications} Given the Health or Care Professional is permitted to manage adverse event notifications  When the Health or Care Professional selects to configure an adverse event notification  Then the adverse event notification is configured E00670 - Supporting Information {#Telecare-E00670-SupportingInformation}  - Examples of adverse events MAY include, but are not limited to:    - Changes in the Patient/Service User’s vital signs (e.g. heart rate, temperature)   - Changes in location (e.g. the Patient/Service User is out of bed for a given length of time, unusual GPS locations)   - Changes in behaviour (e.g. fridge or cupboard doors are not opened at regular intervals, Patient/Service User does not follow normal patterns of behaviour)   - Environmental threats are detected (e.g. extreme temperatures, smoke, carbon monoxide, floods) - Adverse event notifications MAY be manually triggered by Patient/Service Users. - Examples of manually triggering adverse event notifications MAY include, but are not limited to:    - Pressing a button   - Pulling a cord - Examples of configuring of adverse event notifications MAY include, but are not limited to:    - Which adverse events trigger a notification   - Which recipients receive a notification   - When a notification is sent   - What information is included in a notification - Examples of recipients MAY include, but are not limited to:    - Family members   - Friends or neighbours   - 3rd party call centre staff   - Health or Care Professionals   - The Emergency Services - Examples of information included in adverse event notifications MAY include, but are not limited to:    - The Patient/Service User affected by the adverse event   - The type of adverse event which triggered the notification   - The Telecare device which detected the adverse event  ---  E00671 - automatically send adverse event notifications {#Telecare-E00671-automaticallysendadverseeventnotifications} As a Patient/Service User  I want my Telecare device to automatically send adverse event notifications  So that recipients are notified of adverse events Acceptance criterion 1: automatically send adverse event notifications {#Telecare-Acceptancecriterion1:automaticallysendadverseeventnotifications} Given adverse event notifications are configured  When an adverse event notification is triggered for a Patient/Service User  Then an adverse event notification is sent |

|  |
| --- |
| **MAY Epics - Describes additional functionality associated with the Capability. Suppliers should consider all MAY Epics as part of their User Research. Suppliers can choose to map their Solutions to these Epics and they will be evaluated via Capability Assessment. Contracting Authorities or purchasing organisations may require these Epics as product qualification or requirements criteria** |
| E00672 - run remote tests of Telecare devices {#Telecare-E00672-runremotetestsofTelecaredevices} As a Health or Care Professional  I want to be able to run tests of Telecare devices remotely  So that I can identify if Telecare devices that are working correctly without being on-site Acceptance criterion 1: run remote tests of Telecare devices {#Telecare-Acceptancecriterion1:runremotetestsofTelecaredevices} Given the Health or Care Professional is permitted to test Telecare devices remotely  When the Health or Care Professional selects to test a Telecare device  Then the Telecare device is tested E00672 - Supporting information {#Telecare-E00672-Supportinginformation}  - When a test of a Telecare device is complete, the Telecare device MAY send diagnostic information to the Health or Care Professional  ---  E00673 - view Telecare reports {#Telecare-E00673-viewTelecarereports} As a Health or Care Professional  I want to view Telecare reports  So that I can analyse the data and make informed decisions Acceptance criterion 1: view Telecare reports {#Telecare-Acceptancecriterion1:viewTelecarereports} Given a Health or Care Professional is permitted to view Telecare reports  When the Health or Care Professional selects to view a Telecare report  Then the report results are displayed E00673 - Supporting Information {#Telecare-E00673-SupportingInformation}  - Examples of Telecare reports MAY include but are not limited to:    - The number and type of Telecare devices in use   - The number of adverse events occurring |

## Roadmap {#Telecare-Roadmap}

Items on the Roadmap which impact or relate to this Capability

| Roadmap Item |
| --- |
| No content found. |