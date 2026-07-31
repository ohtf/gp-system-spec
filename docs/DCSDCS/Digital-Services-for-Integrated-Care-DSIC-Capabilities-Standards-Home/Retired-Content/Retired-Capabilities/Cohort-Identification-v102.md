---
page_id: "7918551305"
space: "DCSDCS"
title: "Cohort Identification v1.0.2"
version: 12
updated: "2025-11-19T09:59:29.341Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/7918551305/Cohort+Identification+v1.0.2"
labels: ["capability_retired"]
---

# Cohort Identification v1.0.2

|  |  |
| --- | --- |
| **ID** | C45 |
| **Version** | 1.0.2 |
| **Type** | Capability |
| **Category** | Care coordination |
| **Status** | Retired |
| **Effective Date** | 25 Jan 2021 |
| **Framework(s)** | [Vaccinations - Local/PCN Delivery](https://nhse-dsic.atlassian.net/wiki/spaces/CVPDR) |

# Description

The Cohort Identification Capability enables the identification of Patient cohorts by identifying Patients that require a COVID-19 vaccination based on nationally defined criteria.

The Capability may also enable the sending of COVID-19 vaccination invite communications to prompt Patients to book COVID-19 vaccination appointments.

# Outcomes

|  |  |
| --- | --- |
| Patient: | Ability to be identified in the appropriate Patient Cohort so they can receive COVID-19 vaccinations efficiently as part of the PCN led Vaccination programme |
| Healthcare Organisation: | Ability to identify the Patients that meet the nationally defined criteria to ensure Patients can be invited to have a COVID-19 Vaccinations at the most appropriate time |

|  |
| --- |
| **MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding** |
| C45E1 - identify COVID-19 vaccination cohorts As a Health or Care Professional  I want to create Patient cohorts to identify Patients requiring a COVID-19 vaccination that meet the nationally defined criteria  So that I can identify which Patients require a COVID-19 vaccination Acceptance criterion 1: create Patient cohorts for COVID-19 vaccinations Given the Health or Care Professional is permitted to manage Patient cohorts  And criteria for COVID-19 cohorts is pre-defined within the Solution  When the Health or Care Professional selects to create a COVID-19 vaccination Patient cohort using pre-defined criteria  Then the Patient cohort is created Supporting Information  - COVID-19: the green book, chapter 14a - Coronavirus (COVID-19) vaccine - see latest JCVI advice on priority groups for the COVID-19 vaccination - Shielded patients list: guidance for General Practice - NHS Digital - for guidance on identifying Clinically extremely vulnerable individuals  ---  C45E2 - verify Patient information using Personal Demographics Service (PDS) As a Health or Care Professional  I want to verify Patient demographics information using the Personal Demographics Service (PDS)  So that I can ensure Patient information held is as accurate as possible (e.g. if the data held in the Solution has not been previously verified using the Personal Demographics Service (PDS)). Acceptance criterion 1: verify Patient information using Personal Demographics Service (PDS) Given the Health or Care Professional is permitted to manage Patient information  When the Health or Care Professional selects to verify Patient demographic information using the Personal Demographics Service (PDS)  And a match is found on the Personal Demographics Service (PDS)  Then the Patient details can be verified   ---  C45E3 - import or consume COVID-19 vaccination data for Patients As a Health or Care Professional  I want the Solution to be able to import or consume COVID-19 vaccination data for Patients  So that the most up to date vaccination data for Patients is used when identifying which Patients require a COVID-19 Vaccination Acceptance criterion 1: import or consume COVID-19 vaccination data for Patients Given updated COVID-19 vaccination data is made available  When the COVID-19 vaccination data is imported or consumed  Then the data held for Patients is updated  And this data is used when identifying Patients requiring a COVID-19 vaccination |

|  |
| --- |
| **MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. These Epics are not mandatory. Any May Epics that are assessed as met will be available to buyers to support them when comparing Solutions** |
| C45E4 - extract COVID-19 vaccination cohorts data in .CSV file format As a Health or Care Professional  I want to extract COVID-19 vaccination cohorts data in .CSV file format  So that Patient cohorts data can be extracted Acceptance criterion 1: extract COVID-19 vaccination cohorts data in .CSV file format Given the Health or Care Professional is permitted to extract Patient cohorts data  When they select to extract Patient cohort data in .CSV file format  Then the Patient cohort data is extracted in .CSV file format   ---  C45E5 - bulk send SMS messages for COVID-19 vaccination invite communications As a Health or Care Professional  I want to bulk send SMS messages to Patients for COVID-19 vaccination invite communications  So that I can invite Patients to book a COVID-19 vaccination appointment via SMS messages Acceptance criterion 1: bulk create SMS messages for COVID-19 vaccination invite communications Given the Health or Care Professional is permitted to send COVID-19 vaccination communications  When the Health or Care Professional chooses to bulk send SMS messages to Patients for COVID-19 vaccination invite communications  Then the COVID-19 vaccination invite communications are sent as SMS messages   ---  C45E6 - bulk create letters for COVID-19 vaccination invite communications As a Health or Care Professional  I want to bulk create letters to Patients for COVID-19 vaccination invite communications  So that I can invite Patients to book a COVID-19 vaccination appointment via letters Acceptance criterion 1: bulk create letters for COVID-19 vaccination invite communications Given the Health or Care Professional is permitted to create COVID-19 vaccination communications  When the Health or Care Professional chooses to bulk create letters to Patients for COVID-19 vaccination invite communications  Then the COVID-19 vaccination invite communications are created as letters   ---  C45E7 - bulk send email for COVID-19 vaccination invite communications As a Health or Care Professional  I want to bulk send email to Patients for COVID-19 vaccination invite communications  So that I can invite Patients to book a COVID-19 vaccination appointment via email Acceptance criterion 1: bulk send email for COVID-19 vaccination invite communications Given the Health or Care Professional is permitted to send COVID-19 vaccination communications  When the Health or Care Professional chooses to bulk send email to Patients for COVID-19 vaccination invite communications  Then the COVID-19 vaccination invite communications are sent via email   ---  C45E8 - automatically record which Patients have had COVID-19 vaccination invites created As a Health or Care Professional  I want the Solution to automatically record when a Patient has had a COVID-19 vaccination invite communication created  So that I can track which Patients have already been invited to book a COVID-19 vaccination appointment Acceptance criterion 1: automatically record which Patients have had COVID-19 vaccination invites created Given the Health or Care Professional selects to create COVID-19 vaccination invite communications  When the COVID-19 vaccination invite communications are created  Then a record of each communication is created for each Patient  And the date and time the communication was created is recorded  And the method of communication is recorded   ---  C45E9 - view whether Patients have had a COVID-19 vaccination invite communication created As a Health or Care Professional  I want to view whether a Patient has had a COVID-19 vaccination invite communication created or not  So that I can track which Patients have already been invited to book a COVID-19 vaccination appointment Acceptance criterion 1: view which Patients have had COVID-19 vaccination invites created Given COVID-19 vaccination invite communications have been created for Patients  When a Health or Care Professional selects to view which Patients have had a COVID-19 vaccination invite communication created  Then the Patients are displayed  And the date and time the communication was created can be viewed  And the method of communication can be viewed Acceptance criterion 2: view which Patients have not had COVID-19 vaccination invites created Given COVID-19 vaccination invite communications have been created for some Patients  And there are Patients that have not had COVID-19 vaccination invite communications created  When a Health or Care Professional selects to view which Patients have not had a COVID-19 vaccination invite communication created  Then the Patients are displayed |

|  |
| --- |
| **Other Applicable Standards** |
| Suppliers will have to attain compliance with these Standards and technical requirements during the compliance stage before they can be live on a framework with this Capability:   - Overarching Standards |