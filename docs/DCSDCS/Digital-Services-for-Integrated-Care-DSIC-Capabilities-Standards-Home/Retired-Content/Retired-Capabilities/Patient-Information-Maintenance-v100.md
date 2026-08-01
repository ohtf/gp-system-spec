---
page_id: "1686634856"
space: "DCSDCS"
title: "Patient Information Maintenance v1.0.0"
version: 2
updated: "2020-01-15T15:08:23.752Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1686634856/Patient+Information+Maintenance+v1.0.0"
labels: ["capability_retired"]
---

# Patient Information Maintenance v1.0.0

|  |  |
| --- | --- |
| ID {#PatientInformationMaintenancev1.0.0-ID} | C13 |
| Version {#PatientInformationMaintenancev1.0.0-Version} | 1.0.0 |
| Type {#PatientInformationMaintenancev1.0.0-Type} | Capability |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

Full Capability status only. For this Capability, Solutions are required to meet all MUST EPICs and associated acceptance criteria.

# Description {#PatientInformationMaintenancev1.0.0-Description}

Supports the registration of Patients and the maintenance of all Patient personal information. Supports the organisation and presentation of a comprehensive Patient Record. Also supports the management of related persons and configuring access to Citizen Services.

# Outcomes {#PatientInformationMaintenancev1.0.0-Outcomes}

|  |  |
| --- | --- |
| For a Patient: | The accurate recording of a Patient’s personal information (including preferences and related people) which contributes to the identification of the Patient and sharing of correct data across health and care. Increased involvement in their own care through enablement of Citizen Services. Patient safety is increased and facilitates finding patients at risk. |
| For General Practice: | The organisation and presentation of a comprehensive Patient Record ensures up to date and relevant information is available to appropriate staff to support timely Patient care. It supports effective communication with Patients, relevant/nominated parties and other organisations as well as forming the basis for enabling access to Citizen services. |
| For the wider NHS and social care system: | Collecting correct demographic and preference data through a Patient’s primary contact organisation, and making it available across care settings improves efficiency, promotes collaboration and encourages the use of a lifelong integrated care record. By enabling Patients to access Citizen services, Practices improve Audit Trails, have fewer phone calls/face-to-face transactions with Patients, releasing time for staff to be deployed on other tasks. |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### Epic 1 - manage Patients  {#PatientInformationMaintenancev1.0.0-Epic1-managePatients}

As a Practice User

I want to manage Patients

So that there are Registered Patients

#### Acceptance criterion 1: create Patient Registrations {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:createPatientRegistrations}

Given the Practice User is permitted to create Patient Registrations

When they choose to create a Patient Registration

Then the Patient Registration is created

#### Acceptance criterion 2: amend Patient Registration {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:amendPatientRegistration}

Given the Practice User is permitted to amend Patient Registrations

When they choose to amend a Patient Registration

Then the Patient Registration is amended

#### Acceptance criterion 3: end Patient Registration {#PatientInformationMaintenancev1.0.0-Acceptancecriterion3:endPatientRegistration}

Given the Practice User is permitted to end Patient Registrations

When they choose to end a Patient Registration

Then the Patient Registration is ended

#### Acceptance criterion 4: view Patient Registration {#PatientInformationMaintenancev1.0.0-Acceptancecriterion4:viewPatientRegistration}

Given the Practice User is permitted to view Patient Registrations

When they choose to view a Patient Registration

Then the Patient Registration is displayed

#### Acceptance criterion 5: create Patient information {#PatientInformationMaintenancev1.0.0-Acceptancecriterion5:createPatientinformation}

Given the Practice User is permitted to create Patient information

When they choose to create Patient information

Then the Patient information is created

#### Acceptance criterion 6: amend Patient information {#PatientInformationMaintenancev1.0.0-Acceptancecriterion6:amendPatientinformation}

Given the Practice User is permitted to amend Patient information

When they choose to amend Patient information

Then the Patient information is amended

#### Acceptance criterion 7: view Patient information {#PatientInformationMaintenancev1.0.0-Acceptancecriterion7:viewPatientinformation}

Given the Practice User is permitted to view Patient information

When they choose to view Patient information

Then the Patient information is displayed

#### Acceptance criterion 8: create a Patient Record  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion8:createaPatientRecord}

Given the Practice User is permitted to create a Patient Record

And there is not a Patient Record at the Practice

When the Practice User registers the Patient

Then the Patient Record is created

#### Acceptance criterion 9: amend a Patient Record  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion9:amendaPatientRecord}

Given the Practice User is permitted to amend a Patient Record

When the Practice User chooses to amend a Patient Record

Then the Patient Record is amended

#### Acceptance criterion 10: view a Patient Record  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion10:viewaPatientRecord}

Given the Practice User is permitted to view a Patient Record

When the Practice User chooses to view a Patient Record

Then the Patient Record is displayed

---

### Epic 2 - access Patient Record {#PatientInformationMaintenancev1.0.0-Epic2-accessPatientRecord}

As a Practice User

I want to access the Patient Record

So that I can access the Patient Record

#### Acceptance criterion 1: accessing Patient Record where identified {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:accessingPatientRecordwhereidentified}

Given a Patient Record is identified

And the Practice User is permitted to access the Patient Record

When the Practice User chooses to access the Patient Record

Then the Patient Record is accessed

#### Acceptance criterion 2: notification of outstanding actions {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:notificationofoutstandingactions}

Given the Practice User is accessing the Patient Record

When there are outstanding actions relating to the Patient

Then the Practice User is notified

---

### Epic 3 - manage Patient Related Persons {#PatientInformationMaintenancev1.0.0-Epic3-managePatientRelatedPersons}

As a Practice User

I want to manage Patient Related Persons

So that there are Patient Related Persons

#### Acceptance criterion 1: create Patient Related Persons {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:createPatientRelatedPersons}

Given the Practice User is permitted to create a Patient Related Person

When they choose to create a Patient Related Person

Then the Patient Related Person is created

#### Acceptance criterion 2: amend Patient Related Persons {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:amendPatientRelatedPersons}

Given the Practice User is permitted to amend a Patient Related Person

When they choose to amend a Patient Related Person

Then the Patient Related Person is amended

#### Acceptance criterion 3: view Patient Related Persons {#PatientInformationMaintenancev1.0.0-Acceptancecriterion3:viewPatientRelatedPersons}

Given the Practice User is permitted to view a Patient Related Person

When they choose to view a Patient Related Person

Then the Patient Related Person is displayed

#### Acceptance criterion 4: delete Patient Related Persons {#PatientInformationMaintenancev1.0.0-Acceptancecriterion4:deletePatientRelatedPersons}

Given the Practice User is permitted to delete a Patient Related Person

When they choose to delete a Patient Related Person

Then the Patient Related Person is deleted

---

### Epic 4 - manage Patients for Citizen Services {#PatientInformationMaintenancev1.0.0-Epic4-managePatientsforCitizenServices}

As a Practice User

I want to manage Patients for Citizen Services

So that there are Patients for Citizen Services

#### Acceptance criterion 1: create Patient Preferences {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:createPatientPreferences}

Given the Practice User is permitted to create Patient Preferences

When they choose to create a Patient Preference

Then the Patient Preference is created

#### Acceptance criterion 2: amend Patient Preferences {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:amendPatientPreferences}

Given the Practice User is permitted to amend Patient Preferences

When they choose to amend a Patient Preference

Then the Patient Preference is amended

#### Acceptance criterion 3: view Patient Preferences {#PatientInformationMaintenancev1.0.0-Acceptancecriterion3:viewPatientPreferences}

Given the Practice User is permitted to view Patient Preferences

When they choose to view a Patient Preference

Then the Patient Preference is displayed

#### Acceptance criterion 4: enable Patient Service Access {#PatientInformationMaintenancev1.0.0-Acceptancecriterion4:enablePatientServiceAccess}

Given the Practice User is permitted to enable Patient Service Access

When they choose to enable Patient Service Access

Then the Patient Service Access is enabled

#### Acceptance criterion 5: disable Patient Service Access {#PatientInformationMaintenancev1.0.0-Acceptancecriterion5:disablePatientServiceAccess}

Given the Practice User is permitted to disable Patient Service Access

When they choose to disable Patient Service Access

Then the Patient Service Access is disabled

#### Acceptance criterion 6: configure Patient Welcome Message  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion6:configurePatientWelcomeMessage}

Given the Practice User is permitted to configure a Patient Welcome Messages

When they choose to configure a Patient Welcome Message

Then the Patient Welcome Message is configured

#### Acceptance criterion 7: configure Patient Disclaimer {#PatientInformationMaintenancev1.0.0-Acceptancecriterion7:configurePatientDisclaimer}

Given the Practice User is permitted to configure Patient Disclaimers

When they choose to configure a Patient Disclaimer

Then the Patient Disclaimer is configured

#### Acceptance criterion 8: create Verified User Accounts  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion8:createVerifiedUserAccounts}

Given the Practice User is permitted to create a Verified User Accounts

When they choose to create a Verified User Account

Then the Verified User Account is created

#### Acceptance criterion 9: amend Verified User Accounts {#PatientInformationMaintenancev1.0.0-Acceptancecriterion9:amendVerifiedUserAccounts}

Given the Practice User is permitted to amend Verified User Accounts

When they choose to amend a Verified User Account for a Citizen

Then the Verified User Account is amended

#### Acceptance criterion 10: view Verified User Accounts {#PatientInformationMaintenancev1.0.0-Acceptancecriterion10:viewVerifiedUserAccounts}

Given the Practice User is permitted to view Verified User Accounts

When they choose to view a Verified User Account for a Citizen

Then the Verified User Account is displayed

#### Acceptance criterion 11: create Identity Verifications {#PatientInformationMaintenancev1.0.0-Acceptancecriterion11:createIdentityVerifications}

Given the Practice User is permitted to create Identity Verifications

When they choose to create an Identity Verification

Then the Identity Verification is created

#### Acceptance criterion 12: amend Identity Verifications {#PatientInformationMaintenancev1.0.0-Acceptancecriterion12:amendIdentityVerifications}

Given the Practice User is permitted to amend Identity Verifications

When they choose to amend an Identity Verification

Then the Identity Verification is amended

#### Acceptance criterion 13: view Identity Verifications {#PatientInformationMaintenancev1.0.0-Acceptancecriterion13:viewIdentityVerifications}

Given the Practice User is permitted to amend Identity Verifications

When they choose to amend an Identity Verification

Then the Identity Verification is amended

#### Acceptance criterion 14: configure Default Communication Channels {#PatientInformationMaintenancev1.0.0-Acceptancecriterion14:configureDefaultCommunicationChannels}

Given the Practice User is permitted to configure Default Communication Channels

When they choose to configure Default Communication Channels

Then Default Communication Channels are configured

#### Acceptance criterion 15: link Verified User Accounts to Online Service Accounts {#PatientInformationMaintenancev1.0.0-Acceptancecriterion15:linkVerifiedUserAccountstoOnlineServiceAccounts}

Given the Practice User has generated Verified User Account credentials for a Patient

When the Patient enters their Verified User Account credentials

Then the accounts are linked

#### Acceptance criterion 16: configure Patient Access to elements of Patient Record {#PatientInformationMaintenancev1.0.0-Acceptancecriterion16:configurePatientAccesstoelementsofPatientRecord}

Given the Practice User has is permitted to configure Patient Access to the Patient Record

When the Practice User chooses to configure Patient Access to the Patient Record

Then Patient Access to the Patient Record is configured

#### Acceptance criterion 17: view Patient Citizen Service usage {#PatientInformationMaintenancev1.0.0-Acceptancecriterion17:viewPatientCitizenServiceusage}

Given the Practice User is permitted to view Patient Citizen Services usage

When they choose to view Patient Citizen Services usage

Then the Patient Citizen Services usage is displayed

---

### Epic 5 - manage Patient Communications {#PatientInformationMaintenancev1.0.0-Epic5-managePatientCommunications}

As a Practice User

I want to manage Patient communications

So that the Practice can communicate with Patients

#### Acceptance criterion 1: create Communication Records {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:createCommunicationRecords}

Given the Patient has sent a communication

When the communication is received by the Practice

Then the Patient Record is updated with the Communication Record

#### Acceptance criterion 2: respond to Patient communications {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:respondtoPatientcommunications}

Given the Practice User is permitted to communicate with the Patient

When they choose to respond to a Patient communication

Then the communication is created

#### Acceptance criterion 3: configure recipient setting of Patient communications {#PatientInformationMaintenancev1.0.0-Acceptancecriterion3:configurerecipientsettingofPatientcommunications}

Given the Practice User is permitted to configure communication recipients

When they choose to configure a recipient of Patient communications

Then the recipient is configured

---

### Epic 6 - configure Patient notifications {#PatientInformationMaintenancev1.0.0-Epic6-configurePatientnotifications}

As a Practice User

I want to configure Patient notifications

So that Patient notifications are configured

#### Acceptance criterion 1: Patient notification on new association  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:Patientnotificationonnewassociation}

Given the Verified User Account-Patient Association is created

And the Verified User Account-Patient Association has been made with a Patient Record

Then the Patient is notified

#### Acceptance criterion 2: Patient notification on changes in Service Access  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:PatientnotificationonchangesinServiceAccess}

Given the Practice User is permitted to notify the Patient

And the Patient's access to services has changed

When they choose to notify the Patient

Then the Patient is notified

---

### Epic 7 - Manage Practice notifications - Patient {#PatientInformationMaintenancev1.0.0-Epic7-ManagePracticenotifications-Patient}

As a Practice User

I want to manage Practice notifications

So that the Practice notifications are configured

#### Acceptance criterion 1: notification of Patient changes  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:notificationofPatientchanges}

Given the Practice User is permitted to be informed

When the Patient has made changes

Then the Practice User is notified

#### Acceptance criterion 2: notification of unverified Patient Contact Details {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:notificationofunverifiedPatientContactDetails}

Given the Practice User is permitted to be informed

When the Contact Details are unverified

Then the Practice User is notified

---

### Epic 8 - Search for Patient Records {#PatientInformationMaintenancev1.0.0-Epic8-SearchforPatientRecords}

As a Practice User

I want to search for Patient Records

So that I can find Patient Records

#### Acceptance criterion 1: Search for a Patient Record {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:SearchforaPatientRecord}

Given the Practice User is permitted to access Patient Records

When they choose to search for a Patient Records

Then the search results are displayed

---

### Epic 9 - view Patient Reports {#PatientInformationMaintenancev1.0.0-Epic9-viewPatientReports}

As a Practice User

I want to view Patient Reports

So that I can see Patient activity

#### Acceptance criterion 1: view Patient Reports {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:viewPatientReports}

Given the Practice User is permitted to view Patient Reports

When the Practice User chooses to view a Patient Report

Then the report is displayed

---

### Epic 10 - configure Citizen service access for the Practice {#PatientInformationMaintenancev1.0.0-Epic10-configureCitizenserviceaccessforthePractice}

As a Practice User

I want to configure the Citizen service access for the Practice

So that the Citizen service access is configured for the Practice

#### Acceptance criterion 1: enable Citizen services {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:enableCitizenservices}

Given the Practice User is permitted to enable a Citizen service for the Practice

When they choose to enable the Citizen service for the Practice

Then the Citizen service is enabled for the Practice

#### Acceptance criterion 2: disable Citizen services {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:disableCitizenservices}

Given the Practice User is permitted to disable a Citizen service for the Practice

When they choose to disable the Citizen service for the Practice

Then the Citizen service is disabled for the Practice

---

### Epic 11 - identify Patients outside of Catchment Area {#PatientInformationMaintenancev1.0.0-Epic11-identifyPatientsoutsideofCatchmentArea}

As a Practice User

I want Patients that reside outside the Catchment Area to be identified

So that Patients that reside outside the Catchment Area are identified

#### Acceptance criterion 1: identify Patients outside of catchment area {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:identifyPatientsoutsideofcatchmentarea}

Given the Practice User is permitted to view Patient Records

When the Practice User chooses to view a Patient Record

And the Patient resides outside the Catchment area

Then the Patient is identified as residing outside the Catchment Area

### Epic 12 - manage Patient Cohorts from Search Results {#PatientInformationMaintenancev1.0.0-Epic12-managePatientCohortsfromSearchResults}

As a Practice User

I want to manage Patient Cohorts from Search Results

So that Patient Cohorts can be managed

#### Acceptance criterion 1: create Patient Cohorts from Search Results {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:createPatientCohortsfromSearchResults}

Given the Practice User is permitted to manage Patient Cohorts

And there are Search Results

When the Practice User chooses to create a Patient Cohort from Search Results

Then the Patient Cohort is created

#### Acceptance criterion 2: update Patient Cohorts {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:updatePatientCohorts}

Given the Practice User is permitted to manage Patient Cohorts

When the Practice User chooses to update a Patient Cohort

Then the Patient Cohort is updated

#### Acceptance criterion 3: delete Patient Cohorts {#PatientInformationMaintenancev1.0.0-Acceptancecriterion3:deletePatientCohorts}

Given the Practice User is permitted to manage Patient Cohorts

When the Practice User chooses to delete a Patient Cohort

Then the Patient Cohort is deleted

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### Epic 13 - view Subject Access Request reports {#PatientInformationMaintenancev1.0.0-Epic13-viewSubjectAccessRequestreports}

As a Practice User

I want to view Subject Access Request reports

So that I can see Subject Access Request activity

#### Acceptance criterion 1: view Patient reports {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:viewPatientreports}

Given the Practice User is permitted to view Subject Access Request reports

When the Practice User chooses to view a Subject Access Request report

Then the Subject Access Request report is displayed

---

### Epic 14 - manage Acute Prescription Request Service {#PatientInformationMaintenancev1.0.0-Epic14-manageAcutePrescriptionRequestService}

As a Practice User

I want to manage the Acute Prescription Request Service

So that there is an Acute Prescription Request Service

#### Acceptance criterion 1: enable Acute Prescription Request Service {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:enableAcutePrescriptionRequestService}

Given the Practice User is permitted to manage the Acute Prescription Request Service

When the Practice User chooses to enable the Acute Prescription Request Service

Then the Acute Prescription Request Service is enabled

#### Acceptance criterion 2: disable Acute Prescription Request Service {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:disableAcutePrescriptionRequestService}

Given the Practice User is permitted to manage the Acute Prescription Request Service

When the Practice User chooses to disable the Acute Prescription Request Service

Then the Acute Prescription Request Service is disabled

---

### Epic 15 - notify the Patient of changes {#PatientInformationMaintenancev1.0.0-Epic15-notifythePatientofchanges}

As a Practice User

I want to notify the Patient of changes

So that the Patient is notified of changes

#### Acceptance criterion 1: Patient notification of Practice changes  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:PatientnotificationofPracticechanges}

Given the Practice User is permitted to notify the Patient

And they have made changes to Patient information

When they choose to notify the Patient

Then the Patient is notified

#### Acceptance criterion 2: Patient notification via multiple Communication Channels {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:PatientnotificationviamultipleCommunicationChannels}

Given the Practice User is permitted to notify the Patient

When they choose to notify the Patient via multiple Communications Channels

Then the Patient is notified via those Communication Channels

#### Acceptance criterion 3: Patient notification via alternative Communication Channels {#PatientInformationMaintenancev1.0.0-Acceptancecriterion3:PatientnotificationviaalternativeCommunicationChannels}

Given the Practice User is permitted to notify the Patient

And Verified Contact Details have not been created

When they choose to notify the Patient via an alternative Communication Channel

Then the Patient is notified via an alternative channel

---

### Epic 16 - manage Subject Access Request (SAR) requests {#PatientInformationMaintenancev1.0.0-Epic16-manageSubjectAccessRequest(SAR)requests}

As a Practice User

I want to manage SAR requests

So that there are SAR requests

#### Acceptance criterion 1: create SAR requests {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:createSARrequests}

Given the Practice User is permitted to create SAR requests

When they choose to create a SAR request

Then the SAR request is created

#### Acceptance criterion 2: amend SAR requests {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:amendSARrequests}

Given the Practice User is permitted to amend SAR requests

When they choose to amend a SAR request

Then the SAR request is amended

#### Acceptance criterion 3: view SAR requests {#PatientInformationMaintenancev1.0.0-Acceptancecriterion3:viewSARrequests}

Given the Practice User is permitted to view SAR requests

When they choose to view a SAR request

Then the SAR request is displayed

#### Acceptance criterion 4: delete SAR requests {#PatientInformationMaintenancev1.0.0-Acceptancecriterion4:deleteSARrequests}

Given the Practice User is permitted to delete SAR requests

When they choose to delete a SAR request

Then the SAR request is deleted

---

### Epic 17 - notify the Proxy of changes {#PatientInformationMaintenancev1.0.0-Epic17-notifytheProxyofchanges}

As a Practice User

I want to notify the Proxy of changes

So that the Proxy is notified of changes

#### Acceptance criterion 1: Proxy notification of Practice changes  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:ProxynotificationofPracticechanges}

Given the Practice User is permitted to notify the Proxy

And they have made changes to Proxy information

When they choose to notify the Proxy

Then the Proxy is notified

#### Acceptance criterion 2: Proxy notification of Practice changes  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:ProxynotificationofPracticechanges}

Given the Practice User is permitted to notify the Proxy

And they have made changes to Patient information

When they choose to notify the Proxy

Then the Proxy is notified

#### Acceptance criterion 3: Proxy notification via multiple Communication Channels {#PatientInformationMaintenancev1.0.0-Acceptancecriterion3:ProxynotificationviamultipleCommunicationChannels}

Given the Practice User is permitted to notify the Proxy

When they choose to notify the Proxy via multiple Communications Channels

Then the Proxy is notified via those Communication Channels

#### Acceptance criterion 4: Proxy notification via alternative Communication Channels {#PatientInformationMaintenancev1.0.0-Acceptancecriterion4:ProxynotificationviaalternativeCommunicationChannels}

Given the Practice User is permitted to notify the Proxy

And Verified Contact Details have not been created

When they choose to notify the Proxy via an alternative Communication Channel

Then the Proxy is notified via an alternative channel

---

### Epic 18 - Manage Practice notifications - Proxy {#PatientInformationMaintenancev1.0.0-Epic18-ManagePracticenotifications-Proxy}

As a Practice User

I want to manage Practice notifications

So that the Practice notifications are configured

#### Acceptance criterion 1: notification of Proxy changes  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:notificationofProxychanges}

Given the Practice User is permitted to be informed

When a Proxy has made changes

Then the Practice User is notified

#### Acceptance criterion 2: notification of unverified Proxy Contact Details {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:notificationofunverifiedProxyContactDetails}

Given the Practice User is permitted to be informed

When the Contact Details are unverified

Then the Practice User is notified

---

### Epic 19 - configure Proxy notifications {#PatientInformationMaintenancev1.0.0-Epic19-configureProxynotifications}

As a Practice User

I want to configure Proxy notifications

So that Proxy notifications are configured

#### Acceptance criterion 1: Proxy notification on new association  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:Proxynotificationonnewassociation}

Given the Verified User Account-Patient Association is created

And the Verified User Account-Patient Association has been made with a Patient Record

Then the Proxy is notified

#### Acceptance criterion 2: Proxy notification on changes in Service Access  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:ProxynotificationonchangesinServiceAccess}

Given the Practice User is permitted to notify the Proxy

And the Proxy's access to services has changed

When they choose to notify the Proxy

Then the Proxy is notified

---

### Epic 20 - manage Proxy Communications {#PatientInformationMaintenancev1.0.0-Epic20-manageProxyCommunications}

As a Practice User

I want to manage Proxy communications

So that the Practice can communicate with Proxies

#### Acceptance criterion 1: create Communication Records {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:createCommunicationRecords.1}

Given the Proxy has sent a communication

When the communication is received by the Practice

Then the Patient Record is updated with the Communication Record

#### Acceptance criterion 2: respond to Proxy communications {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:respondtoProxycommunications}

Given the Practice User is permitted to communicate with the Proxy

When they choose to respond to a Proxy communication

Then the communication is created

#### Acceptance criterion 3: configure recipient setting of Proxy communications {#PatientInformationMaintenancev1.0.0-Acceptancecriterion3:configurerecipientsettingofProxycommunications}

Given the Practice User is permitted to configure communication recipients

When they choose to configure a recipient of Proxy communications

Then the recipient is configured

---

### Epic 21 - manage Proxys for Citizen Services {#PatientInformationMaintenancev1.0.0-Epic21-manageProxysforCitizenServices}

As a Practice User

I want to manage Proxies for Citizen Services

So that there are Proxies for Citizen Services

#### Acceptance criterion 1: create Proxy Preferences {#PatientInformationMaintenancev1.0.0-Acceptancecriterion1:createProxyPreferences}

Given the Practice User is permitted to create Proxy Preferences

When they choose to create a Proxy Preference

Then the Proxy Preference is created

#### Acceptance criterion 2: amend Proxy Preferences {#PatientInformationMaintenancev1.0.0-Acceptancecriterion2:amendProxyPreferences}

Given the Practice User is permitted to amend Proxy Preferences

When they choose to amend a Proxy Preference

Then the Proxy Preference is amended

#### Acceptance criterion 3: view Proxy Preferences {#PatientInformationMaintenancev1.0.0-Acceptancecriterion3:viewProxyPreferences}

Given the Practice User is permitted to view Proxy Preferences

When they choose to view a Proxy Preference

Then the Proxy Preference is displayed

#### Acceptance criterion 4: enable Proxy Service Access {#PatientInformationMaintenancev1.0.0-Acceptancecriterion4:enableProxyServiceAccess}

Given the Practice User is permitted to enable Proxy Service Access

When they choose to enable Proxy Service Access

Then the Proxy Service Access is enabled

#### Acceptance criterion 5: disable Proxy Service Access {#PatientInformationMaintenancev1.0.0-Acceptancecriterion5:disableProxyServiceAccess}

Given the Practice User is permitted to disable Proxy Service Access

When they choose to disable Proxy Service Access

Then the Proxy Service Access is disabled

#### Acceptance criterion 6: automatically restrict Proxy Service Access {#PatientInformationMaintenancev1.0.0-Acceptancecriterion6:automaticallyrestrictProxyServiceAccess}

Given the Citizen is a proxy for a Patient

When the Patient reaches the age of 11

Then the Proxy's Service Access is restricted

#### Acceptance criterion 7: automatically disable Proxy Citizen Service Access {#PatientInformationMaintenancev1.0.0-Acceptancecriterion7:automaticallydisableProxyCitizenServiceAccess}

Given the Citizen is a proxy for a Patient

When the Patient reaches the age of 16

Then the Proxy's Service Access is disabled

#### Acceptance criterion 8: configure Proxy Welcome Message  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion8:configureProxyWelcomeMessage}

Given the Practice User is permitted to configure Proxy Welcome Messages

When they choose to configure a Proxy Welcome Message

Then the Proxy Welcome Message is configured

#### Acceptance criterion 9: configure Proxy Disclaimer {#PatientInformationMaintenancev1.0.0-Acceptancecriterion9:configureProxyDisclaimer}

Given the Practice User is permitted to configure Proxy Disclaimers

When they choose to configure a Proxy Disclaimer

Then the Proxy Disclaimer is configured

#### Acceptance criterion 10: create Verified User Accounts  {#PatientInformationMaintenancev1.0.0-Acceptancecriterion10:createVerifiedUserAccounts}

Given the Practice User is permitted to create a Verified User Accounts

When they choose to create a Verified User Account

Then the Verified User Account is created

#### Acceptance criterion 11: amend Verified User Accounts {#PatientInformationMaintenancev1.0.0-Acceptancecriterion11:amendVerifiedUserAccounts}

Given the Practice User is permitted to amend Verified User Accounts

When they choose to amend a Verified User Account

Then the Verified User Account is amended

#### Acceptance criterion 12: view Verified User Accounts {#PatientInformationMaintenancev1.0.0-Acceptancecriterion12:viewVerifiedUserAccounts}

Given the Practice User is permitted to view Verified User Accounts

When they choose to view a Verified User Account

Then the Verified User Account is displayed

#### Acceptance criterion 13: create Identity Verifications {#PatientInformationMaintenancev1.0.0-Acceptancecriterion13:createIdentityVerifications}

Given the Practice User is permitted to create Identity Verifications

When they choose to create an Identity Verification

Then the Identity Verification is created

#### Acceptance criterion 14: amend Identity Verifications {#PatientInformationMaintenancev1.0.0-Acceptancecriterion14:amendIdentityVerifications}

Given the Practice User is permitted to amend Identity Verifications

When they choose to amend an Identity Verification

Then the Identity Verification is amended

#### Acceptance criterion 15: view Identity Verifications {#PatientInformationMaintenancev1.0.0-Acceptancecriterion15:viewIdentityVerifications}

Given the Practice User is permitted to amend Identity Verifications

When they choose to amend an Identity Verification

Then the Identity Verification is amended

#### Acceptance criterion 16: configure Default Communication Channels {#PatientInformationMaintenancev1.0.0-Acceptancecriterion16:configureDefaultCommunicationChannels}

Given the Practice User is permitted to configure Default Communication Channels

When they choose to configure Default Communication Channels

Then Default Communication Channels are configured

#### Acceptance criterion 17: link Verified User Accounts to Online Service Accounts {#PatientInformationMaintenancev1.0.0-Acceptancecriterion17:linkVerifiedUserAccountstoOnlineServiceAccounts}

Given the Practice User has generated Verified User Account credentials for a Citizen

When the Proxy enters their Verified User Account credentials

Then the accounts are linked

#### Acceptance criterion 18: configure Proxy Access to elements of Patient Record {#PatientInformationMaintenancev1.0.0-Acceptancecriterion18:configureProxyAccesstoelementsofPatientRecord}

Given the Practice User has is permitted to configure Proxy Access to the Patient Record

When the Practice User chooses to configure Proxy Access to the Patient Record

Then Proxy Access to the Patient Record is configured

#### Acceptance criterion 19: view Proxy Citizen Service usage {#PatientInformationMaintenancev1.0.0-Acceptancecriterion19:viewProxyCitizenServiceusage}

Given the Practice User is permitted to view Proxy Citizen Services usage

When they choose to view Proxy Citizen Services usage

Then the Proxy Citizen Services usage is displayed

**Capability Specific Standards**

Suppliers will have to attain compliance with these Standards during the compliance stage before they can be live on a framework with this Capability:

- Patient Information Maintenance - Standard
- Primary Care Clinical Terminology Usage Report
**Other Applicable Standards**

Suppliers will also have to attain compliance with these additional Standards during the compliance stage before they can be live on a framework with this Capability:

- Interoperability Standard
- Common Reporting
- Management Information (MI) Reporting
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |