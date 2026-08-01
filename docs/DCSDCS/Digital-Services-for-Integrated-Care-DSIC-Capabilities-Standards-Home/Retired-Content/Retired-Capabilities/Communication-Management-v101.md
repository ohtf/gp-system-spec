---
page_id: "12417236997"
space: "DCSDCS"
title: "Communication Management v1.0.1"
version: 3
updated: "2023-05-22T10:29:59.947Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12417236997/Communication+Management+v1.0.1"
labels: ["capability_retired"]
---

# Communication Management v1.0.1

|  |  |
| --- | --- |
| ID | C7 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - GP IT Futures - Tech Innovation |

Full Capability status only. For this Capability, Solutions are required to meet all MUST EPICs and associated acceptance criteria.

# Description {#CommunicationManagementv1.0.1-Description}

Supports the delivery and management of communications to Citizens and Practice staff.

# Outcomes {#CommunicationManagementv1.0.1-Outcomes}

|  |  |
| --- | --- |
| For a Patient: | Receiving reliable communications in accordance with their preferences. |
| For General Practice: | Ability to manage communications via a central service, reducing administrative burden and costs, as well as informing recipients via their preferred method. |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C7E1 - manage communication consents for a Patient {#CommunicationManagementv1.0.1-C7E1-managecommunicationconsentsforaPatient}

As a Practice User

I want to manage the communication consents of a Patient

So that communication occurs only via channels the Patient has consented to

#### Acceptance criterion 1: Patient consents to receive communication via a specific channel {#CommunicationManagementv1.0.1-Acceptancecriterion1:Patientconsentstoreceivecommunicationviaaspecificchannel}

Given the Patient has consented to receive communication via a specific channel

When the Practice User adds a record of the consent

Then the consent is recorded

#### Acceptance criterion 2: Patient does not consent to receive communication via a specific channel {#CommunicationManagementv1.0.1-Acceptancecriterion2:Patientdoesnotconsenttoreceivecommunicationviaaspecificchannel}

Given the Patient does not consent to receive communication via a specific channel

When the Practice User adds a record of the dissent

Then the dissent is recorded

---

### C7E2 - manage communication preferences for a Patient {#CommunicationManagementv1.0.1-C7E2-managecommunicationpreferencesforaPatient}

As a Practice User

I want to manage the communication preferences of a Patient

So that communications are delivered to the Patient in the ways that they prefer

#### Acceptance criterion 1: Patient prefers to receive communication via a specific channel {#CommunicationManagementv1.0.1-Acceptancecriterion1:Patientpreferstoreceivecommunicationviaaspecificchannel}

Given the Patient prefers to receive communication via a specific channel

When the Practice User adds a record of the preference

Then the preference is recorded

#### Acceptance criterion 2: Patient prefers not to receive communication via a specific channel {#CommunicationManagementv1.0.1-Acceptancecriterion2:Patientprefersnottoreceivecommunicationviaaspecificchannel}

Given the Patient prefers not to receive communication via a specific channel

When the Practice User adds a record of the preference

Then the preference is recorded

---

### C7E3 - manage communication templates {#CommunicationManagementv1.0.1-C7E3-managecommunicationtemplates}

As a Practice User

I want to manage communication templates

So that communications can be created from templates

#### Acceptance criterion 1: create template {#CommunicationManagementv1.0.1-Acceptancecriterion1:createtemplate}

Given the Practice User is permitted to create templates

When the Practice User creates the template

Then the template is created

#### Acceptance criterion 2: change template status {#CommunicationManagementv1.0.1-Acceptancecriterion2:changetemplatestatus}

Given the Practice User is permitted to change template status

When the Practice User chooses to change the template status

Then the template status is changed

---

### C7E4 - create communications {#CommunicationManagementv1.0.1-C7E4-createcommunications}

As a Practice User

I want to create communications that are in addition to automated communications

So that I can communicate when necessary

#### Acceptance criterion 1: create a communication {#CommunicationManagementv1.0.1-Acceptancecriterion1:createacommunication}

Given the Practice User is permitted to make the communication

When the Practice User chooses to create the communication

Then the communication is created

#### Acceptance criterion 2: create a communication from a template {#CommunicationManagementv1.0.1-Acceptancecriterion2:createacommunicationfromatemplate}

Given the Practice User is permitted to make the communication

When the Practice User chooses to create the communication from a template

Then the communication is created from the template

#### Acceptance criterion 3: include an individual recipient {#CommunicationManagementv1.0.1-Acceptancecriterion3:includeanindividualrecipient}

Given the Practice User is permitted to communicate with the individual

When the Practice User chooses to add the individual to the recipients

Then the individual is included in the recipients

#### Acceptance criterion 4: include a group of Citizens in the recipients {#CommunicationManagementv1.0.1-Acceptancecriterion4:includeagroupofCitizensintherecipients}

Given the Practice User is permitted to communicate with Patients

When the Practice User chooses to add the group of Citizens to the recipients

Then the group of Citizens is included in the recipients

#### Acceptance criterion 5: include a group of Staff in the recipients {#CommunicationManagementv1.0.1-Acceptancecriterion5:includeagroupofStaffintherecipients}

Given the Practice User is permitted to communicate with Staff

When the Practice User chooses to add the group of Staff to the recipients

Then the group of Staff is included in the recipients

#### Acceptance criterion 6: create Communication Records {#CommunicationManagementv1.0.1-Acceptancecriterion6:createCommunicationRecords}

Given the Practice User has created a communication

When the communication is sent by the Practice

Then the Patient Record is updated with the Communication Record

---

### C7E5 - manage automated communications {#CommunicationManagementv1.0.1-C7E5-manageautomatedcommunications}

As a Practice User

I want to manage automated communications

So that communications happen automatically

#### Acceptance criterion 1: create an automated communication {#CommunicationManagementv1.0.1-Acceptancecriterion1:createanautomatedcommunication}

Given the Practice User is permitted to create automated communications

When the Practice User chooses to create the automated communication

Then the automated communication is created

#### Acceptance criterion 2: create an automated communication from a template {#CommunicationManagementv1.0.1-Acceptancecriterion2:createanautomatedcommunicationfromatemplate}

Given the Practice User is permitted to create automated communications

When the Practice User chooses to create the automated communication from a template

Then the automated communication is created from the template

#### Acceptance criterion 3: amend an automated communication {#CommunicationManagementv1.0.1-Acceptancecriterion3:amendanautomatedcommunication}

Given the Practice User is permitted to amend automated communications

When the Practice User chooses to amend the automated communication

Then the automated communication is amended

#### Acceptance criterion 4: disable an automated communication {#CommunicationManagementv1.0.1-Acceptancecriterion4:disableanautomatedcommunication}

Given the Practice User is permitted to disable automated communications

When the Practice User chooses to disable the automated communication

Then the automated communication is disabled

#### Acceptance criterion 5: enable an automated communication {#CommunicationManagementv1.0.1-Acceptancecriterion5:enableanautomatedcommunication}

Given the Practice User is permitted to enable automated communications

When the Practice User chooses to enable the automated communication

Then the automated communication is enabled

---

### C7E6 - view communication reports {#CommunicationManagementv1.0.1-C7E6-viewcommunicationreports}

As a Practice User

I want to view communication reports

So that I can understand what communications activity has occurred

#### Acceptance criterion 1: view communication activity report {#CommunicationManagementv1.0.1-Acceptancecriterion1:viewcommunicationactivityreport}

Given the Practice User is permitted to view communication activity reports

When the Practice User chooses to view the communication activity report

Then the communication activity report is displayed

#### Acceptance criterion 2: view communication failure report {#CommunicationManagementv1.0.1-Acceptancecriterion2:viewcommunicationfailurereport}

Given the Practice User is permitted to view communication failure reports

When the Practice User chooses to view the communication failure report

Then the communication failure report is displayed

---

### C7E7 - access Patient Record {#CommunicationManagementv1.0.1-C7E7-accessPatientRecord}

As a Practice User

I want to access the Patient Record

So that I can access the Patient Record

#### Acceptance criterion 1: accessing Patient Record where identified {#CommunicationManagementv1.0.1-Acceptancecriterion1:accessingPatientRecordwhereidentified}

Given a Patient Record is identified

And the Practice User is permitted to view the Patient Record

When the Practice User chooses to access the Patient Record

Then the Patient Record is accessed

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C7E8 - manage communication consents for a Proxy {#CommunicationManagementv1.0.1-C7E8-managecommunicationconsentsforaProxy}

As a Practice User

I want to manage the communication consents of a Proxy

So that communication occurs only via channels the Proxy has consented to

#### Acceptance criterion 1: Proxy consents to receive communication via a specific channel {#CommunicationManagementv1.0.1-Acceptancecriterion1:Proxyconsentstoreceivecommunicationviaaspecificchannel}

Given the Proxy has consented to receive communication via a specific channel

When the Practice User adds a record of the consent

Then the consent is recorded

#### Acceptance criterion 2: Proxy does not consent to receive communication via a specific channel {#CommunicationManagementv1.0.1-Acceptancecriterion2:Proxydoesnotconsenttoreceivecommunicationviaaspecificchannel}

Given the Proxy does not consent to receive communication via a specific channel

When the Practice User adds a record of the dissent

Then the dissent is recorded

---

### C7E9 - manage communication preferences for a Proxy {#CommunicationManagementv1.0.1-C7E9-managecommunicationpreferencesforaProxy}

As a Practice User

I want to manage the communication preferences of a Proxy

So that communications are delivered to the Proxy in the ways that they prefer

#### Acceptance criterion 1: Proxy prefers to receive communication via a specific channel {#CommunicationManagementv1.0.1-Acceptancecriterion1:Proxypreferstoreceivecommunicationviaaspecificchannel}

Given the Proxy prefers to receive communication via a specific channel

When the Practice User adds a record of the preference

Then the preference is recorded

#### Acceptance criterion 2: Proxy prefers not to receive communication via a specific channel {#CommunicationManagementv1.0.1-Acceptancecriterion2:Proxyprefersnottoreceivecommunicationviaaspecificchannel}

Given the Proxy prefers not to receive communication via a specific channel

When the Practice User adds a record of the preference

Then the preference is recorded

---

### C7E10 - manage incoming communications {#CommunicationManagementv1.0.1-C7E10-manageincomingcommunications}

As a Practice User

I want to manage incoming communications

So that incoming communications can be managed

#### Acceptance criterion 1: manage incoming communications {#CommunicationManagementv1.0.1-Acceptancecriterion1:manageincomingcommunications}

Given incoming communications are permitted by the Practice

When an incoming communication is received

Then the communication is managed

**Capability Specific Standards**

Suppliers will have to attain compliance with this Standard during the compliance stage before they can be live on a framework with this Capability:

- Communication Management - Standard v1.0.1
**Other Applicable Standards**

Suppliers will also have to attain compliance with these additional Standards during the compliance stage before they can be live on a framework with this Capability:

- Interoperability Standard
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

| Roadmap Item |
| --- |
| No content found. |