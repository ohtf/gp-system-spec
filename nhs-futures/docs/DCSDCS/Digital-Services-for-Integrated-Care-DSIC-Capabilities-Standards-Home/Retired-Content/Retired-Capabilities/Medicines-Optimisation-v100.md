---
page_id: "1695383700"
space: "DCSDCS"
title: "Medicines Optimisation v1.0.0"
version: 2
updated: "2020-01-15T16:34:51.190Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1695383700/Medicines+Optimisation+v1.0.0"
labels: ["capability_retired"]
---

# Medicines Optimisation v1.0.0

|  |  |
| --- | --- |
| ID | C30 |
| Version | 1.0.0 |
| Type | Capability |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description {#MedicinesOptimisationv1.0.0-Description}

Medicines Optimisation enables Health and Care Professionals to review a Patient's prescribed and other medication to ensure they are taking the most appropriate and relevant combination of medication and prevent unnecessary medicines being prescribed.

It presents a single unified view of a Patient's medication, which could include medication sourced from different care settings and Solutions, and supports Health and Care Professionals in conducting person-centred medicines optimisation reviews. It also supports the creation of medication change requests to ensure the appropriate parties are informed of suggested changes following a medicines review

Medicines Optimisation may also incorporate functionality to establish medicines reviews as part of routine practice, through easy identification of Patients requiring a review and the ability to make changes to the Patient's medication directly. Medicines Optimisation guidance may be provided to Health and Care Professionals through integrated decision support relating to safety, national and locally agreed best practices and cost-savings, as part or outside of the review process.

It may also include the ability to communicate with Health and Care Professionals, Patients and other interested parties when changes to medication are suggested or made.

# Outcomes {#MedicinesOptimisationv1.0.0-Outcomes}

|  |  |
| --- | --- |
| Health and Care Professionals | - Able to take safer and more informed decisions based on a single, unified view of the Patient's medication - Can send change requests to other Health and Care Professionals when they are unable to update the medication record themselves - Can receive requests to change a Patient's medication regimen based on the outcome of a review - May be able to identify all Patients requiring a review - May be able to make changes to medication based on the outcome of a review - May have access to functionality to facilitate easy switching of medications using pre-configured substitutions |
| Patients and Proxies | - Will have more confidence that their medication regimen is both safe and appropriate for their conditions. |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### EpicMO1  - single unified medication view {#MedicinesOptimisationv1.0.0-EpicMO1-singleunifiedmedicationview}

As a Health or Care Professional

I want to be able to access a single, combined view of a Patient's prescribed and other medication (e.g. over the counter medicines and food supplements)

So that I have a complete view of their medication and can make fully informed decisions regarding any changes to medication

#### Acceptance criterion 1: single unified medication view {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:singleunifiedmedicationview}

Given the Patient has prescribed and other medication recorded in one or more Solutions

When a Health or Care Professional chooses to view a single combined view of the Patient's medication

Then the Patient's prescribed and other medication is displayed in a single combined view

---

### EpicMO2 - request medication changes {#MedicinesOptimisationv1.0.0-EpicMO2-requestmedicationchanges}

As a Health or Care Professional

I want to send a request to the appropriate person to make medication changes

So that I can request they make the recommended changes following a medicines review

#### Acceptance criterion 1: request medication changes {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:requestmedicationchanges}

Given a medicines review for a Patient has been completed

And medication changes are required

When the Health or Care Professional chooses to create a request for the required changes

Then the request is created

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### EpicMO3 - identify Patients requiring medicines review {#MedicinesOptimisationv1.0.0-EpicMO3-identifyPatientsrequiringmedicinesreview}

As a Health or Care Professional

I want to search for Patients using a combination of criteria

So that I can identify Patients who require a medicines review

#### Acceptance criterion 1: identify Patients who may require a medicines review {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:identifyPatientswhomayrequireamedicinesreview}

Given there are Patients with prescribed medication

When the Health or Care Professional searches for Patients requiring a medicines review

Then Patients which satisfy the criteria are displayed

---

### EpicMO4 - maintain medicines review {#MedicinesOptimisationv1.0.0-EpicMO4-maintainmedicinesreview}

As a Health or Care Professional

I want to maintain a Patient's medicines review

So that details of any completed reviews and the next review date can be recorded

#### Acceptance criterion 1: record medicines review as complete {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:recordmedicinesreviewascomplete}

Given a medicines review for a Patient has been completed

When the Health or Care Professional chooses to record a medicines review has been completed

Then the review is recorded as complete

#### Acceptance criterion 2: update medicines review date {#MedicinesOptimisationv1.0.0-Acceptancecriterion2:updatemedicinesreviewdate}

Given a medicines review for a Patient has been completed

When the Health or Care Professional chooses to update the medicines review date

Then they can record a future medicines review date

---

### EpicMO5 - notify Patient and Proxies of medication changes {#MedicinesOptimisationv1.0.0-EpicMO5-notifyPatientandProxiesofmedicationchanges}

As a Health or Care Professional

I want to notify the Patient and their Proxies of the changes to the Patient's medication

So that they are informed of the changes

#### Acceptance criterion 1: create Patient notification {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:createPatientnotification}

Given changes have been made to a Patient's medication

When the Health or Care Professional chooses to notify the Patient of the medication changes

Then a notification detailing the changes is created

#### Acceptance criterion 2: create Proxy notification {#MedicinesOptimisationv1.0.0-Acceptancecriterion2:createProxynotification}

Given changes have been made to a Patient's medication

And the Patient has a Proxy

When the Health or Care Professional chooses to notify the Proxy of the medication changes

Then a notification detailing the changes is created

---

### EpicMO6 - notify other interested parties of medication changes {#MedicinesOptimisationv1.0.0-EpicMO6-notifyotherinterestedpartiesofmedicationchanges}

As a Health or Care Professional

I want to notify any other interested parties (e.g. another Prescriber, the patient's GP, the Care Plan Manager) of changes to a Patient's medication

So that they are informed of the changes made

#### Acceptance criterion 1: notify interested parties of a medication change {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:notifyinterestedpartiesofamedicationchange}

Given changes have been made to a Patient's medication

When the Health or Care Professional chooses to notify the other interested parties of the medication changes

Then a notification detailing the changes is created

---

### EpicMO7 - configure medication substitutions {#MedicinesOptimisationv1.0.0-EpicMO7-configuremedicationsubstitutions}

As a Health or Care Professional

I want to configure prescribed medication substitutions

So that I can quickly switch one medication for another when changing medication

#### Acceptance criterion 1: configure medication substitutions {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:configuremedicationsubstitutions}

Given the Health or Care Professional is permitted to configure medication substitutions

When they choose to configure a medication substitution

Then a specific medication can be configured as a substitute for another specific medication

---

### EpicMO8 - use pre-configured medication substitutions {#MedicinesOptimisationv1.0.0-EpicMO8-usepre-configuredmedicationsubstitutions}

As a Health or Care Professional

I want to use pre-configured prescribed medication substitutions

So that I can quickly switch one medication for another when changing medication

#### Acceptance criterion 1: switch medication {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:switchmedication}

Given a Patient has existing prescribed medication

When the Health or Care Professional is changing a Patient's medication

Then they are informed of any pre-configured substitutions

And the medication can be changed to the pre-configured replacement

---

### EpicMO9 - maintain prescribed medication {#MedicinesOptimisationv1.0.0-EpicMO9-maintainprescribedmedication}

As a Health or Care Professional

I want to maintain prescribed medication

So that I can make any changes required following a review

#### Acceptance criterion 1: create medication item {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:createmedicationitem}

Given a Health or Care Professional identifies that a Patient requires new medication

When they choose to create a new medication for a Patient

Then the new medication is created

#### Acceptance criterion 2: amend existing medication item {#MedicinesOptimisationv1.0.0-Acceptancecriterion2:amendexistingmedicationitem}

Given the Patient has a prescribed medication item

When the Health or Care Professional chooses to amend the medication

Then the medication is amended

#### Acceptance criterion 3: stop existing medication item {#MedicinesOptimisationv1.0.0-Acceptancecriterion3:stopexistingmedicationitem}

Given the Patient has a prescribed medication item

When the Health or Care Professional chooses to stop the medication

Then the medication is recorded as stopped

---

### EpicMO10 - access national or local Medicines Optimisation guidance {#MedicinesOptimisationv1.0.0-EpicMO10-accessnationalorlocalMedicinesOptimisationguidance}

As a Health or Care Professional

I want to be able to access any national or local prescribing optimisation guidance

So that I can refer to relevant guidance when reviewing a Patient's medication

#### Acceptance criterion 1: access Medicines Optimisation guidance {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:accessMedicinesOptimisationguidance}

Given Medicines Optimisation guidance exists

When the Health or Care Professional chooses to access the guidance

Then the guidance is displayed

---

### EpicMO11 - prescribing decision support {#MedicinesOptimisationv1.0.0-EpicMO11-prescribingdecisionsupport}

As a Health or Care Professional

I want to have access to prescribing decision support

So that interactions, active ingredient duplication and inappropriate prescribing warnings are displayed when prescribing medication

#### Acceptance criterion 1: display decision support information {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:displaydecisionsupportinformation}

Given a Health or Care Professional is creating medication for a Patient

When there is relevant information to display

Then interactions are displayed

and active ingredient duplication is displayed

and inappropriate prescribing warnings are displayed

---

### EpicMO12 - Medicines Optimisation reporting {#MedicinesOptimisationv1.0.0-EpicMO12-MedicinesOptimisationreporting}

As a Health or Care Professional

I want to generate reports on Medicines Optimisation data using a combination of criteria

So that I can report on the effectiveness of reviews and plan future reviews more effectively

#### Acceptance criterion 1: generate report {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:generatereport}

Given a number of medicines reviews have been completed and changes have been made to Patient medication

When the Manager generates a report using specified criteria

Then the report results are displayed

---

### EpicMO13 - configure notifications for required Medicines Reviews {#MedicinesOptimisationv1.0.0-EpicMO13-configurenotificationsforrequiredMedicinesReviews}

As a Health or Care Professional

I want to configure how and when a notification is presented to a user to indicate that a medicines review is required for a Patient

So that I can ensure the Health or Care Professional is aware of the need for a review

#### Acceptance criterion 1: configure notifications for required medicines reviews {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:configurenotificationsforrequiredmedicinesreviews}

Given a Manager is permitted to Configure notifications for required medicines reviews

When they choose to configure medicines review required notifications

Then how and when the notifications are presented can be configured

---

### EpicMO14 - receive notification for required medicines reviews {#MedicinesOptimisationv1.0.0-EpicMO14-receivenotificationforrequiredmedicinesreviews}

As a Health or Care Professional

I want to receive notifications when a medicines review is required for a Patient

So that I am informed when a review is due

#### Acceptance criterion 1: receive notification for required medicines reviews {#MedicinesOptimisationv1.0.0-Acceptancecriterion1:receivenotificationforrequiredmedicinesreviews}

Given there is a pre-configured notification for required medicines reviews

And the notification is applicable to the Health or Care Professional

When a Patient is due for a medicines review

Then the applicable Health and Care Professionals receive a medicines review due notification

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