---
page_id: "11963203826"
space: "DCSDCS"
title: "Prescribing v1.0.1"
version: 1
updated: "2022-04-28T09:47:41.809Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11963203826/Prescribing+v1.0.1"
labels: ["capability_retired"]
---

# Prescribing v1.0.1

|  |  |
| --- | --- |
| ID {#Prescribingv1.0.1-ID} | C14 |
| Version {#Prescribingv1.0.1-Version} | 1.0.1 |
| Type {#Prescribingv1.0.1-Type} | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |

Full Capability status only. For this Capability, Solutions are required to meet all MUST EPICs and associated acceptance criteria.

# Description {#Prescribingv1.0.1-Description}

Supports the effective and safe prescribing of medical products and appliances to Patients. Information to support prescribing will be available.

# Outcomes {#Prescribingv1.0.1-Outcomes}

|  |  |
| --- | --- |
| For a Patient: | Timely access to the right medicinal products, and appliances. |
| For General Practice: | Supporting the prescription of medical products and appliances that are appropriate and safe for the individual Patient and improve Patient safety through access to information on the risk of potential adverse effects of medication. |
| For the wider NHS and social care system: | Efficient and effective use of resources to improve health outcomes for Patients through the appropriate selection and provision of medicinal products, and appliances. |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C14E1 - access prescribable items {#Prescribingv1.0.1-C14E1-accessprescribableitems}

As a Practice User

I want to access prescribable items

So that prescribable items can be accessed

#### Acceptance criterion 1: access prescribable items {#Prescribingv1.0.1-Acceptancecriterion1:accessprescribableitems}

Given the Practice User is permitted to access prescribable items

When the Practice User chooses to access prescribable items

Then the prescribable items are displayed

#### Acceptance criterion 2: access prescribable item information {#Prescribingv1.0.1-Acceptancecriterion2:accessprescribableiteminformation}

Given the Practice User is permitted to access prescribable item information

When the Practice User chooses to access information for a prescribable item

Then the information is displayed

---

### C14E2 - manage Formularies {#Prescribingv1.0.1-C14E2-manageFormularies}

As a Practice User

I want to manage Formularies

So that there are Formularies

#### Acceptance criterion 1: create Formularies {#Prescribingv1.0.1-Acceptancecriterion1:createFormularies}

Given the Practice User is permitted to create Formularies

When the Practice User chooses to create a Formulary

Then the Formulary is created

#### Acceptance criterion 2: amend Formularies {#Prescribingv1.0.1-Acceptancecriterion2:amendFormularies}

Given the Practice User is permitted to amend Formularies

When the Practice User chooses to amend a Formulary

Then the Formulary is amended

#### Acceptance criterion 3: delete Formularies {#Prescribingv1.0.1-Acceptancecriterion3:deleteFormularies}

Given the Practice User is permitted to delete Formularies

When the Practice User chooses to delete a Formulary

Then the Formulary is deleted

---

### C14E3 - manage shared Formularies {#Prescribingv1.0.1-C14E3-managesharedFormularies}

As a Practice User

I want to manage shared Formularies

So that shared Formularies are managed

#### Acceptance criterion 1: share Formularies {#Prescribingv1.0.1-Acceptancecriterion1:shareFormularies}

Given the Practice User is permitted to share Formularies

When the Practice User chooses to share a Formulary to another organisation using this Solution

Then the Formulary is shared

#### Acceptance criterion 2: use shared Formularies {#Prescribingv1.0.1-Acceptancecriterion2:usesharedFormularies}

Given the Practice User is permitted to share Formularies

When the Practice User chooses to use a shared Formulary from another organisation using this Solution

Then the Formulary is used

---

### C14E4 - set default Formulary for Practice Users {#Prescribingv1.0.1-C14E4-setdefaultFormularyforPracticeUsers}

As a Practice User

I want to set a default Formulary for a Practice User

So that a default Formulary can be set for a Practice User

#### Acceptance criterion 1: set default Formularies for Practice Users {#Prescribingv1.0.1-Acceptancecriterion1:setdefaultFormulariesforPracticeUsers}

Given the Practice User is permitted to set default Formularies

When the Practice User chooses to set a default Formulary for a Practice User that is permitted to manage prescribed medication

Then the default Formulary is set

#### Acceptance criterion 2: access prescribable items outside of Formulary {#Prescribingv1.0.1-Acceptancecriterion2:accessprescribableitemsoutsideofFormulary}

Given the Practice User has a default Formulary set

When prescribable items accessed

Then items outside the Practice User's default Formulary are available

---

### C14E5 - manage prescribed medication {#Prescribingv1.0.1-C14E5-manageprescribedmedication}

As a Practice User

I want to manage prescribed medication

So that Patient's medication is managed

#### Acceptance criterion 1: create Acute Medication {#Prescribingv1.0.1-Acceptancecriterion1:createAcuteMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to create an Acute Medication

Then sensitivities are displayed

And interactions are displayed

And active ingredient duplication is displayed

And inappropriate prescribing warnings are displayed

And the medication is created

#### Acceptance criterion 2: amend Acute Medication {#Prescribingv1.0.1-Acceptancecriterion2:amendAcuteMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to amend an Acute Medication

Then the medication is amended

#### Acceptance criterion 3: create issue of Acute Medication {#Prescribingv1.0.1-Acceptancecriterion3:createissueofAcuteMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to create an issue of an Acute Medication

Then the issue is created

#### Acceptance criterion 4: delete Acute Medication {#Prescribingv1.0.1-Acceptancecriterion4:deleteAcuteMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to delete an Acute Medication

Then the medication is deleted

#### Acceptance criterion 5: create Repeat Medication {#Prescribingv1.0.1-Acceptancecriterion5:createRepeatMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to create a Repeat Medication

Then sensitivities are displayed

And interactions are displayed

And active ingredient duplication is displayed

And inappropriate prescribing warnings are displayed

And the medication is created

#### Acceptance criterion 6: amend Repeat Medication {#Prescribingv1.0.1-Acceptancecriterion6:amendRepeatMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to amend a Repeat Medication

Then the medication is amended

#### Acceptance criterion 7: create issue of Repeat Medication {#Prescribingv1.0.1-Acceptancecriterion7:createissueofRepeatMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to create an issue of a Repeat Medication

Then the issue is created

#### Acceptance criterion 8: create Repeatable Batch Issue of Repeat Medication {#Prescribingv1.0.1-Acceptancecriterion8:createRepeatableBatchIssueofRepeatMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to create a Repeatable Batch issue of a Repeat Medication

Then the Repeatable Batch Issue is created

#### Acceptance criterion 9: delete Repeat Medication {#Prescribingv1.0.1-Acceptancecriterion9:deleteRepeatMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to delete a Repeat Medication

Then the medication is deleted

#### Acceptance criterion 10: create Instalment Medication {#Prescribingv1.0.1-Acceptancecriterion10:createInstalmentMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to create an Instalment Medication

Then any appropriate sensitivities, interactions, active ingredient duplication and inappropriate prescribing warnings are displayed

And the medication is created

#### Acceptance criterion 11: amend Instalment Medication {#Prescribingv1.0.1-Acceptancecriterion11:amendInstalmentMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to amend an Instalment Prescription

Then the medication is amended

#### Acceptance criterion 12: create issue of Instalment Medication {#Prescribingv1.0.1-Acceptancecriterion12:createissueofInstalmentMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to create an issue of an Instalment Prescription

Then the issue is created

#### Acceptance criterion 13: delete Instalment Medication {#Prescribingv1.0.1-Acceptancecriterion13:deleteInstalmentMedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to delete an Instalment Prescription

Then the medication is deleted

#### Acceptance criterion 14: record medication not issued by General Practice {#Prescribingv1.0.1-Acceptancecriterion14:recordmedicationnotissuedbyGeneralPractice}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to record medication not issued by General Practice

Then the medication is recorded

#### Acceptance criterion 15: record medication from Schedule 1 of NHS regulations {#Prescribingv1.0.1-Acceptancecriterion15:recordmedicationfromSchedule1ofNHSregulations}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to record medication from Schedule 1 of NHS regulations

Then the medication is recorded

#### Acceptance criterion 16: record medication personally administered or dispensed by General Practice {#Prescribingv1.0.1-Acceptancecriterion16:recordmedicationpersonallyadministeredordispensedbyGeneralPractice}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to record medication personally administered or dispensed by General Practice

Then the medication is recorded

#### Acceptance criterion 17: view prescribed medication {#Prescribingv1.0.1-Acceptancecriterion17:viewprescribedmedication}

Given the Practice User is permitted to manage prescribed medication

When the Practice User chooses to view prescribed medication

Then the prescribed medication is displayed

---

### C14E6 - manage prescriptions {#Prescribingv1.0.1-C14E6-manageprescriptions}

As a Practice User

I want to manage prescriptions

So that Prescriptions for Patients are managed

#### Acceptance criterion 1: create Prescription {#Prescribingv1.0.1-Acceptancecriterion1:createPrescription}

Given the Practice User is permitted to manage prescriptions

When the Practice User chooses to create a Prescription for prescribed medication

Then the Prescription is created

#### Acceptance criterion 2: print Prescription {#Prescribingv1.0.1-Acceptancecriterion2:printPrescription}

Given the Practice User is permitted to manage prescriptions

When the Practice User chooses to print a Prescription

Then the Prescription is printed

#### Acceptance criterion 3: view Prescription {#Prescribingv1.0.1-Acceptancecriterion3:viewPrescription}

Given the Practice User is permitted to manage prescriptions

When the Practice User chooses to view a Prescription

Then the Prescription is displayed

#### Acceptance criterion 4: reprint Prescription {#Prescribingv1.0.1-Acceptancecriterion4:reprintPrescription}

Given the Practice User is permitted to manage prescriptions

When the Practice User chooses to reprint a Prescription

Then the Prescription is printed

#### Acceptance criterion 5: cancel Prescription {#Prescribingv1.0.1-Acceptancecriterion5:cancelPrescription}

Given the Practice User is permitted to manage prescriptions

When the Practice User chooses to cancel a Prescription

Then the Prescription is recorded as cancelled

---

### C14E7 - manage Patient's Preferred Pharmacy {#Prescribingv1.0.1-C14E7-managePatient'sPreferredPharmacy}

As a Practice User

I want to manage a Patient's Preferred Pharmacy

So that their pharmacy preference can be managed

#### Acceptance criterion 1: record Patient's pharmacy preference {#Prescribingv1.0.1-Acceptancecriterion1:recordPatient'spharmacypreference}

Given the Practice User is permitted to manage Patients pharmacies preferences

When the Practice User chooses to record a Patient's pharmacy preference

Then the Patient's Preferred Pharmacy is recorded

#### Acceptance criterion 2: amend Patient's pharmacy preference {#Prescribingv1.0.1-Acceptancecriterion2:amendPatient'spharmacypreference}

Given the Practice User is permitted to manage Patients pharmacy preferences

When the Practice User chooses to amend a Patient's pharmacy preference

Then the Preferred Pharmacy is amended

#### Acceptance criterion 3: delete Patient's pharmacy preference {#Prescribingv1.0.1-Acceptancecriterion3:deletePatient'spharmacypreference}

Given the Practice User is permitted to manage Patients pharmacy preferences

When the Practice User chooses to delete a Patient's pharmacy preference

Then the Preferred Pharmacy is deleted

---

### C14E8 - manage Patient medication reviews {#Prescribingv1.0.1-C14E8-managePatientmedicationreviews}

As a Practice User

I want to manage Patient medication reviews

So that Patient medication reviews are managed

#### Acceptance criterion 1: record medication regimen review date {#Prescribingv1.0.1-Acceptancecriterion1:recordmedicationregimenreviewdate}

Given the Practice User is permitted to manage Patient medication reviews

When the Practice User chooses to record a medication regimen review date for a Patient

Then the review date is recorded

#### Acceptance criterion 2: record medication regimen review performed {#Prescribingv1.0.1-Acceptancecriterion2:recordmedicationregimenreviewperformed}

Given the Practice User is permitted to manage Patient medication reviews

When the Practice User chooses to record a medication regimen review has been performed for a Patient

Then the review is recorded

---

### C14E9 - view prescribed medication reports {#Prescribingv1.0.1-C14E9-viewprescribedmedicationreports}

As a Practice User

I want to view prescribed medication reports

So that reports relating to prescribed medication can be viewed

#### Acceptance criterion 1: view prescribed medication reports {#Prescribingv1.0.1-Acceptancecriterion1:viewprescribedmedicationreports}

Given the Practice User is permitted to view reports for prescribed medication

When the Practice User chooses to view a prescribed medication report

Then the report is displayed

---

### C14E10 - manage Repeat Medication requests {#Prescribingv1.0.1-C14E10-manageRepeatMedicationrequests}

As a Practice User

I want to manage Repeat Medication requests

So that I can manage requests for Repeat Medication

#### Acceptance criterion 1: create Repeat Medication requests {#Prescribingv1.0.1-Acceptancecriterion1:createRepeatMedicationrequests}

Given the Practice User is permitted to create Repeat Medication requests

When the Practice User chooses to create a Repeat Medication request

Then the Repeat Medication request is created

#### Acceptance criterion 2: amend Repeat Medication requests {#Prescribingv1.0.1-Acceptancecriterion2:amendRepeatMedicationrequests}

Given the Practice User is permitted to update Repeat Medication requests

When the Practice User chooses to update a Repeat Medication request

Then the Repeat Medication request is updated

#### Acceptance criterion 3: cancel Repeat Medication requests {#Prescribingv1.0.1-Acceptancecriterion3:cancelRepeatMedicationrequests}

Given the Practice User is permitted to cancel Repeat Medication requests

When the Practice User chooses to cancel a Repeat Medication request

Then the Repeat Medication request is recorded as cancelled

---

### C14E11 - manage Acute Medication requests {#Prescribingv1.0.1-C14E11-manageAcuteMedicationrequests}

As a Practice User

I want to manage Acute Medication requests

So that I can manage requests for Acute Medication

#### Acceptance criterion 1: create Acute Medication requests {#Prescribingv1.0.1-Acceptancecriterion1:createAcuteMedicationrequests}

Given the Practice User is permitted to create Acute Medication requests

When the Practice User chooses to create an Acute Medication request

Then the Acute Medication request is created

#### Acceptance criterion 2: amend Acute Medication requests {#Prescribingv1.0.1-Acceptancecriterion2:amendAcuteMedicationrequests}

Given the Practice User is permitted to update Acute Medication requests

When the Practice User chooses to update an Acute Medication request

Then the Acute Medication request is updated

#### Acceptance criterion 3: cancel Acute Medication requests {#Prescribingv1.0.1-Acceptancecriterion3:cancelAcuteMedicationrequests}

Given the Practice User is permitted to cancel Acute Medication requests

When the Practice User chooses to cancel an Acute Medication request

Then the Acute Medication request is recorded as cancelled

---

### C14E12 - manage Authorising Prescribers {#Prescribingv1.0.1-C14E12-manageAuthorisingPrescribers}

As a Practice User

I want to manage what type of Prescriber my Staff Members are

So that Staff Members prescriber type can be managed

#### Acceptance criterion 1: record Staff Member prescriber type {#Prescribingv1.0.1-Acceptancecriterion1:recordStaffMemberprescribertype}

Given the Practice User is permitted to manage Staff Members prescriber type

When the Practice User chooses to record a Staff Member's prescriber type

Then the Staff Member's prescriber type is recorded

#### Acceptance criterion 2: amend Staff Member prescriber type {#Prescribingv1.0.1-Acceptancecriterion2:amendStaffMemberprescribertype}

Given the Practice User is permitted to manage Staff Members prescriber type

When the Practice User chooses to update a Staff Member's prescriber type

Then the Staff Member's prescriber type is updated

#### Acceptance criterion 3: delete Staff Member prescriber type {#Prescribingv1.0.1-Acceptancecriterion3:deleteStaffMemberprescribertype}

Given the Practice User is permitted to manage Staff Members prescriber type

When the Practice User chooses to delete a Staff Member's prescriber type

Then the Staff Member's prescriber type is deleted

#### Acceptance criterion 4: record Staff Member prescriber sub-type {#Prescribingv1.0.1-Acceptancecriterion4:recordStaffMemberprescribersub-type}

Given the Practice User is permitted to manage Staff Members prescriber sub-type

When the Practice User chooses to record a Staff Member's prescriber sub-type

Then the Staff Member's prescriber sub-type is recorded

#### Acceptance criterion 5: amend Staff Member prescriber sub-type {#Prescribingv1.0.1-Acceptancecriterion5:amendStaffMemberprescribersub-type}

Given the Practice User is permitted to manage Staff Members prescriber sub-type

When the Practice User chooses to update a Staff Member's prescriber sub-type

Then the Staff Member's prescriber sub-type is updated

#### Acceptance criterion 6: delete Staff Member prescriber sub-type {#Prescribingv1.0.1-Acceptancecriterion6:deleteStaffMemberprescribersub-type}

Given the Practice User is permitted to manage Staff Members prescriber sub-type

When the Practice User chooses to delete a Staff Member's prescriber sub-type

Then the Staff Member's prescriber sub-type is deleted

#### Acceptance criterion 7: set Alternate Authorising Prescribers {#Prescribingv1.0.1-Acceptancecriterion7:setAlternateAuthorisingPrescribers}

Given the Practice User is permitted to set Authorising Prescribers

When the Practice User chooses to set an Alternate Authorising Prescriber for a Staff Member

Then the Alternate Authorising Prescriber is set

#### Acceptance criterion 8: amend Alternate Authorising Prescribers {#Prescribingv1.0.1-Acceptancecriterion8:amendAlternateAuthorisingPrescribers}

Given the Practice User is permitted to amend Authorising Prescribers

When the Practice User chooses to amend an Alternate Authorising Prescriber for a Staff Member

Then the Alternate Authorising Prescriber is amended

#### Acceptance criterion 9: delete Alternate Authorising Prescribers {#Prescribingv1.0.1-Acceptancecriterion9:deleteAlternateAuthorisingPrescribers}

Given the Practice User is permitted to delete Authorising Prescribers

When the Practice User chooses to delete an Alternate Authorising Prescriber for a Staff Member

Then the Alternate Authorising Prescriber is deleted

---

### C14E13 - access Patient Record {#Prescribingv1.0.1-C14E13-accessPatientRecord}

As a Practice User

I want to access the Patient Record

So that I can access the Patient Record

#### Acceptance criterion 1: accessing Patient Record where identified {#Prescribingv1.0.1-Acceptancecriterion1:accessingPatientRecordwhereidentified}

Given a Patient Record is identified

And the Practice User is permitted to view the Patient Record

When the Practice User chooses to access the Patient Record

Then the Patient Record is accessed

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C14E14 - view EPS Nominated Pharmacy changes {#Prescribingv1.0.1-C14E14-viewEPSNominatedPharmacychanges}

As a Practice User

I want to view the EPS Nominated Pharmacy changes

So that I can view when a Patient's EPS nominated Pharmacy has been changed or removed.

#### Acceptance criterion 1: view EPS Nominated Pharmacy changes {#Prescribingv1.0.1-Acceptancecriterion1:viewEPSNominatedPharmacychanges}

Given the Practice User is permitted to view EPS Nominated Pharmacies

When the Practice User chooses to view the EPS Nominated Pharmacy changes

Then the changes are displayed

---

### C14E15 - configure warnings for prescribable items {#Prescribingv1.0.1-C14E15-configurewarningsforprescribableitems}

As a Practice User

I want to configure warnings for prescribable items

So that there are warnings for prescribable items

#### Acceptance criterion 1: create configurable warnings for prescribable items {#Prescribingv1.0.1-Acceptancecriterion1:createconfigurablewarningsforprescribableitems}

Given the Practice User is permitted to manage configurable warnings for prescribable items

When the Practice User chooses to create a warning for a prescribable item

Then the warning is created

#### Acceptance criterion 2: amend configurable warnings for prescribable items {#Prescribingv1.0.1-Acceptancecriterion2:amendconfigurablewarningsforprescribableitems}

Given the Practice User is permitted to manage configurable warnings for prescribable items

When the Practice User chooses to amend a warning for a prescribable item

Then the warning is amended

#### Acceptance criterion 3: delete configurable warnings for prescribable items {#Prescribingv1.0.1-Acceptancecriterion3:deleteconfigurablewarningsforprescribableitems}

Given the Practice User is permitted to manage configurable warnings for prescribable items

When the Practice User chooses to delete a warning for a prescribable item

Then the warning is deleted

---

### C14E16 - medications are linked to diagnoses {#Prescribingv1.0.1-C14E16-medicationsarelinkedtodiagnoses}

As a Practice User

I want to link prescribed medication to a diagnosis

So that medications are linked to diagnoses

#### Acceptance criterion 1: link prescribed medication to a diagnosis {#Prescribingv1.0.1-Acceptancecriterion1:linkprescribedmedicationtoadiagnosis}

Given the Practice User is permitted to link prescribed medication to a diagnosis

When the Practice User chooses to link prescribed medication to a diagnosis

Then the prescribed medication is linked to a diagnosis

**Capability Specific Standard**

Suppliers will have to attain compliance with this Standard during the compliance stage before they can be live on a framework with this Capability:

- [Prescribing - Standard v1.1.0](../Retired-Standards/Prescribing-Standard-v110.md)
**Other Applicable Standards**

Suppliers will also have to attain compliance with these additional Standards during the compliance stage before they can be live on a framework with this Capability:

- [Interoperability Standard](../../DSIC-Standards/Overarching-Standards/Interoperability-Standard.md)
- [Common Reporting v2.0.0](../Retired-Standards/Common-Reporting-v200.md)
- [Management Information (MI) Reporting v1.0.1](../Retired-Standards/Management-Information-MI-Reporting-v101.md)
- [Overarching Standards](../../DSIC-Standards/Overarching-Standards/index.md)
**Items on the Roadmap which impact or relate to this Capability**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |