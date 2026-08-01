---
page_id: "1692893636"
space: "DCSDCS"
title: "Personal Health Record v1.0.0"
version: 2
updated: "2020-01-15T16:36:58.719Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1692893636/Personal+Health+Record+v1.0.0"
labels: ["capability_retired"]
---

# Personal Health Record v1.0.0

|  |  |
| --- | --- |
| ID | C33 |
| Version | 1.0.0 |
| Type | Capability |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description {#PersonalHealthRecordv1.0.0-Description}

The Personal Health Record Capability will allow the Patient/Service User (or their nominee) to maintain Personal Health Record information including conditions (e.g. Crohn's Disease, diabetes or mental health) and health, social care, insurance, lifestyle or any other information relevant to the Personal Health Record.

The Personal Health Record Capability may allow for the data and structure of the Personal Health Record to be organised and for access to the Personal Health Record to be controlled by the user, so that part of or the whole Personal Health Record may be accessed by approved users (e.g. a Proxy for a Patient/Service User).

A Personal Health Record Capability may also allow for other data sources (e.g. Telehealth devices) to contribute data to the Personal Health Record.

# Outcomes {#PersonalHealthRecordv1.0.0-Outcomes}

|  |  |
| --- | --- |
| Patient/Service User or their Proxy | - Ability to share information with Health and Care Professionals who might not otherwise have that information and thus are able to make more appropriate decisions about any treatment - Ability to have access to Health and Care related information from a range of sources - Personalised management of their Personal Health Record |
| Health and Care Professionals | - Access to a wider set of Patient/Service User information to help make more informed decisions |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### EpicPR1 - maintain Personal Health Record content {#PersonalHealthRecordv1.0.0-EpicPR1-maintainPersonalHealthRecordcontent}

As a Patient/Service User (or nominee)

I want to maintain my own content within my Personal Health Record

So that I can easily maintain data which may be of use to those involved in my care

#### Acceptance criterion 1: add information to the Personal Health Record {#PersonalHealthRecordv1.0.0-Acceptancecriterion1:addinformationtothePersonalHealthRecord}

Given the user is permitted to manage their Personal Health Record content

When they choose to add information to their Personal Health Record

Then they can add information to the Personal Health Record

#### Acceptance criterion 2: view information in the Personal Health Record {#PersonalHealthRecordv1.0.0-Acceptancecriterion2:viewinformationinthePersonalHealthRecord}

Given the user is permitted to manage their Personal Health Record content

When they choose to view information in their Personal Health Record

Then information in the Personal Health Record is displayed

#### Acceptance criterion 3: amend information in the Personal Health Record {#PersonalHealthRecordv1.0.0-Acceptancecriterion3:amendinformationinthePersonalHealthRecord}

Given the user is permitted to manage their Personal Health Record content

When they choose to amend information in their Personal Health Record

Then they can amend information in the Personal Health Record

#### Acceptance criterion 4:  comment on information in the Personal Health Record {#PersonalHealthRecordv1.0.0-Acceptancecriterion4:commentoninformationinthePersonalHealthRecord}

Given the user is permitted to manage their Personal Health Record content

When they choose to comment on information in their record

Then they can comment on entries in their record

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### EpicPR2 - organise Personal Health Record  {#PersonalHealthRecordv1.0.0-EpicPR2-organisePersonalHealthRecord}

As a Patient/Service User (or nominee)

I want to organise my Personal Health Record

So that I can keep content organised to my preference

#### Acceptance criterion 1: organise my Personal Health Record data  {#PersonalHealthRecordv1.0.0-Acceptancecriterion1:organisemyPersonalHealthRecorddata}

Given the user is permitted to organise the Personal Health Record data

When the user chooses to organise the Personal Health Record data

Then the Personal Health Record data is organised

#### Acceptance criterion 2: organise my Personal Health Record structure {#PersonalHealthRecordv1.0.0-Acceptancecriterion2:organisemyPersonalHealthRecordstructure}

Given the user is permitted to organise the Personal Health Record structure

When the user chooses to organise the Personal Health Record structure

Then the Personal Health Record structure is organised

---

### EpicPR3 - manage access to Personal Health Record {#PersonalHealthRecordv1.0.0-EpicPR3-manageaccesstoPersonalHealthRecord}

As a Patient/Service User (or nominee)

I want to control who has access to my Personal Health Record

So that my Personal Health Record is shared with Health or Care Professionals in accordance with my preferences

#### Acceptance criterion 1: give Access to a Health or Care Professional to the Personal Health Record {#PersonalHealthRecordv1.0.0-Acceptancecriterion1:giveAccesstoaHealthorCareProfessionaltothePersonalHealthRecord}

Given the user is permitted to give a Health or Care Professional access to their Personal Health Record

And the user has enabled parts of the Personal Health Record to be accessed

When the user chooses to give access to their Personal Health Record

Then the Health or Care Professional has access to the enabled parts of the Personal Health Record

---

### EpicPR4 - manage data coming into Personal Health Record {#PersonalHealthRecordv1.0.0-EpicPR4-managedatacomingintoPersonalHealthRecord}

As a Patient/Service User (or nominee)

I want to control which devices and Solutions can contribute data to my Personal Health Record

So that I can include in my Personal Health Record data that may be of use to those involved in my care

#### Acceptance criterion 1: enable data connection for a device {#PersonalHealthRecordv1.0.0-Acceptancecriterion1:enabledataconnectionforadevice}

Given the user wishes to allow data to be received from a device (e.g. Telehealth or Telecare devices)

When they choose to enable a data connection for a device

Then the device is connected

And can contribute data to the Personal Health Record

#### Acceptance criterion 2: disable data connection for a device {#PersonalHealthRecordv1.0.0-Acceptancecriterion2:disabledataconnectionforadevice}

Given the user wishes to stop a device contributing data to the Personal Health Record

When they choose to disable a data connection for a device

Then the device is disabled to contribute data to the Personal Health Record

#### Acceptance criterion 3: enable data connection for a Solution {#PersonalHealthRecordv1.0.0-Acceptancecriterion3:enabledataconnectionforaSolution}

Given the user wishes to allow data to be received from another Solution (e.g. a clinical system)

When they choose to enable a data connection for a Solution

Then the Solution is connected

And can contribute data to the Personal Health Record

#### Acceptance criterion 4: disable data connection for a Solution {#PersonalHealthRecordv1.0.0-Acceptancecriterion4:disabledataconnectionforaSolution}

Given the user wishes to stop a Solution contributing data to the Personal Health Record

When they choose to disable a data connection for a Solution

Then the Solution is disabled to contribute data to the Personal Health Record

#### Acceptance criterion 5: import data in a variety of formats into the Personal Health Record {#PersonalHealthRecordv1.0.0-Acceptancecriterion5:importdatainavarietyofformatsintothePersonalHealthRecord}

Given a user has some data to import (e.g. HTML, text, a PDF file, a Word document, email)

When the choose to import data into their Personal Health Record

Then they are able to import data into their Personal Health Record

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