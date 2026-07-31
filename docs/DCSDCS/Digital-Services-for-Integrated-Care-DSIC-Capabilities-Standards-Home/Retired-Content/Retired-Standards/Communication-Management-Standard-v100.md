---
page_id: "1686634760"
space: "DCSDCS"
title: "Communication Management - Standard v1.0.0"
version: 2
updated: "2020-01-15T14:56:35.666Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1686634760/Communication+Management+-+Standard+v1.0.0"
labels: ["capability_specific_retired"]
---

# Communication Management - Standard v1.0.0

|  |  |
| --- | --- |
| ID | S7 |
| Version | 1.0.0 |
| Type | Capability Specific Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

# Requirements

| Epic Mapping | Requirement ID | Requirement Text | Level |
| --- | --- | --- | --- |
| Epic 2 | COM1 | **Communication - Preferences - Patient**  Record and maintain communication preferences for a Patient. It will be possible to specify preferences for all the communication types available. Where there are multiple communication channels available, it will be possible to specify which channels are used for each communication type. | MUST |
| Epic 9 | COM11 | **Communication - Preferences - Proxy**  Record and maintain communication preferences for Proxies. It will be possible for each Proxy to have preferences that are different to the other Proxies. It will be possible to specify preferences for all the communication types available. Where there are multiple communication channels available, it will be possible to specify which channels are used for each communication type. | MAY |
| Epic 1 | COM2 | **Communication - Consent - Patient**  Record and maintain communication consent for a Patient. It will be possible to specify consents for all the communication types available. Where there are multiple communication channels available, it will be possible to consent to multiple communication channels for each communication type. | MUST |
| Epic 8 | COM12 | **Communication - Consent - Proxy**  Record and maintain communication consent for Proxies. It will be possible for each Proxy to:   - Have consents that are different to the other Proxies. - Specify consents for all the communication types available   Where there are multiple communication channels available, it will be possible to consent to multiple communication channels for each communication type. | MAY |
| Epic 3 | GP-08.1-01 | **Communication - Templates**  Create, amend and delete communication templates.  Each template having as a minimum:   - Unique identifier - Name - Template status   - Draft   - Published   - Available for viewing and use across the system   - Archived - Channel e.g. letter, email and SMS - Type e.g. Appointment reminder, cervical cytology screening – this can map to a clinical code if applicable - Body of the communication, including:   - Merge fields of any structured demographic, clinical or administrative data e.g. Patient name and address, Staff Member and referring speciality and clinical terms of problems, allergies and medication, Appointment details.   Where merge fields are to be used to auto-populate data, Practice Users will be able to configure the number of instances and/or time period to be covered e.g. include the latest blood pressure reading, the last three consultations and medication prescribed or recorded over the last six months.  See Data Standards for further information on Clinical Codes and terms | MUST |
| Epic 4 | COM8 | **Communication - Create from template and send - Patient**  Create and send communications for Patients from a communication template.  Support one or more of the following channels of communication:   - Email - SMS - Letter   Recording:   - Created By - Creation Date and Time - Patient - Status (e.g. Sent, Failed) - Status Date & Time | MUST |
| Epic 4 | COM13 | **Communication - Create from template and send - Proxy**  Create and send communications for Proxies from a communication template.  Support one or more of the following channels of communication:   - Email - SMS - Letter   Recording:   - Created By - Creation Date and Time - Patient - Status (e.g. Sent, Failed) - Status Date & Time | MAY |
| Epic 4 | COM7 | **Communication - Create manually and send - Patient**  Ability to manually create and send communications for Patients.  Supporting one or more of the following channels of communication:   - Email - SMS - Letter   Recording:   - Created By - Creation Date and Time - Recipient(s) - Status (e.g. Sent, Failed) - Status Date & Time | MUST |
| Epic 4 | COM14 | **Communication - Create manually and send - Proxy**  Ability to manually create and send communications for Proxies.  Supporting one or more of the following channels of communication:   - Email - SMS - Letter   Recording:   - Created By - Creation Date and Time - Recipient(s) - Status (e.g. Sent, Failed) - Status Date & Time | MAY |
| Epic 4 | COM3 | **Communication - Recipients**  Ability for recipients of communications to be:   - Patients - Staff Members - Groups (Staff Members and Patients) - External organisations | MUST |
| Epic 4 | COM15 | **Communication - Recipients - Proxy**  Ability for recipients of communications to be:   - Proxies - Groups including Proxies | MAY |
| Epic 4 | GP-08.2-03 | **Communication - Edit communication from template**  Edit a communication created from a template before sending, including:   - Amend the body of the communication (text from template) on an ad-hoc basis - Include additional data items from any part of the Patient Record - Remove data items from the populated merge fields within the generated communication | MUST |
| Epic 5 | GP-08.2-04 | **Communication - Automation**  Schedule a communication to be automatically created and sent at a specified date and time or at a specified period prior to an activity.  Examples include:   - Appointment reminder to be generated 24 hours prior to Appointment - Request Appointment to be made for Child immunisation 6 weeks after date of birth. | MUST |
| Epic 4 | GP-08.2-05 | **Communication - Add to Patient Record**  Add any communication for a Patient within the Patient Record. | MUST |
| Epic 4 | COM16 | **Communication - Add to Patient Record - Proxy**  Add any Proxy communication for a Patient within the Patient Record. | MAY |
| Epic 6 | COM9 | **Reporting - Communication usage**  Ability to generate a report on usage of each of the available communication channels which may include:   - Email - SMS - Letter | MUST |
| Epic 6 | GP-08.1-05 | **Reporting - Communication delivery failures**  Provide a mechanism to report delivery failures for the electronic channels that are available e.g. email and SMS. | MUST |
| Epic 7 | COM5 | **Access Patient Record**  Access a Patient Record where a Patient has been successfully identified, linked, listed or otherwise presented to the user. | MUST |

# Capability

**Applicable Capability**

All supplier Solutions will need to meet this Standard if they are delivering the Communication Management Capability

# Roadmap

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |