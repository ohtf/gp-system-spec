---
page_id: "1693220963"
space: "DCSDCS"
title: "Prescription Ordering - Citizen v1.0.0"
version: 2
updated: "2020-01-15T14:20:48.983Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1693220963/Prescription+Ordering+-+Citizen+v1.0.0"
labels: ["capability_retired"]
---

# Prescription Ordering - Citizen v1.0.0

|  |  |
| --- | --- |
| ID | C3 |
| Version | 1.0.0 |
| Type | Capability |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

Full Capability status only. For this Capability, Solutions are required to meet all MUST EPICs and associated acceptance criteria.

# Description {#PrescriptionOrdering-Citizenv1.0.0-Description}

Enables Citizens to request medication online and manage nominated and preferred Pharmacies for Patients.

# Outcomes {#PrescriptionOrdering-Citizenv1.0.0-Outcomes}

|  |  |
| --- | --- |
| For a Patient: | The timely access to prescribed medicinal products, and easy visibility of existing medications/pharmacy information. |
| For General Practice: | Facilitating access to prescribed medicinal products per the treatment needs of individual Patients. Reducing the risk of transcription errors, fewer phone calls, fewer face-to-face transactions with Patients and releasing time for staff to be deployed on other tasks. Through seamlessly linking with EPS functionality, also promotes an end to end paperless prescription process. |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### Epic 1 - manage Repeat Medications - Patient {#PrescriptionOrdering-Citizenv1.0.0-Epic1-manageRepeatMedications-Patient}

As a Patient

I want to manage Repeat Medications

So that I can receive Repeat Medications

#### Acceptance criterion 1: view Repeat Medications {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion1:viewRepeatMedications}

Given the Patient is logged into Citizen Services

When the Patient chooses to view Repeat Medications

Then the Repeat Medications are displayed

#### Acceptance criterion 2: view most recent Issue of a Repeat Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion2:viewmostrecentIssueofaRepeatMedication}

Given the Patient is logged into Citizen Services

When the Patient chooses to view the most recent Issue of a Repeat Medication

Then the most recent Issue for the Repeat Medication is displayed

#### Acceptance criterion 3: request an Issue of a Repeat Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion3:requestanIssueofaRepeatMedication}

Given the Patient is logged into Citizen Services

When the Patient chooses to request an Issue of a Repeat Medication

Then the Issue is requested

#### Acceptance criterion 4: cancel a request for an Issue of a Repeat Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion4:cancelarequestforanIssueofaRepeatMedication}

Given the Patient is logged into Citizen Services

When the Patient chooses to cancel a request for an Issue a Repeat Medication

Then the Issue request is cancelled

#### Acceptance criterion 5: support a request for an Issue a Repeat Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion5:supportarequestforanIssueaRepeatMedication}

Given the Patient is logged into Citizen Services

When the Patient chooses to support a request for an Issue a Repeat Medication

Then the Issue request can be amended to include the evidence to support the request

#### Acceptance criterion 6: view outstanding requests for Issues of Repeat Medications {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion6:viewoutstandingrequestsforIssuesofRepeatMedications}

Given the Patient is logged into Citizen Services

When the Patient chooses to view outstanding requests for Issues of Repeat Medications

Then the outstanding Issue requests are displayed

---

### Epic 2 - manage my nominated EPS pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Epic2-managemynominatedEPSpharmacy}

As a Patient

I want to manage my nominated EPS pharmacy

So that my nominated pharmacy is correct

#### Acceptance criterion 1: nominate an EPS pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion1:nominateanEPSpharmacy}

Given the Patient is logged into Citizen Services

And the Practice is enabled for the EPS

And the pharmacy chosen by the Patient offers the EPS

When the Patient chooses to nominate the pharmacy

Then the pharmacy is nominated as the EPS pharmacy

#### Acceptance criterion 2: view the nominated EPS pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion2:viewthenominatedEPSpharmacy}

Given the Patient is logged into Citizen Services

And the Patient has nominated a pharmacy for the EPS

When the Patient chooses to view the nominated pharmacy

Then the nominated EPS pharmacy is displayed

#### Acceptance criterion 3: amend the nominated EPS pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion3:amendthenominatedEPSpharmacy}

Given the Patient is logged into Citizen Services

And the Patient has nominated a pharmacy for the EPS

And the alternative pharmacy offers the EPS

When the Patient chooses to amend the nominated pharmacy to the alternative pharmacy

Then the alternative pharmacy is nominated as the EPS pharmacy

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### Epic 3 - manage my Preferred PharmacyAs a Patient {#PrescriptionOrdering-Citizenv1.0.0-Epic3-managemyPreferredPharmacyAsaPatient}

I want to manage my Preferred Pharmacy

So that my Preferred Pharmacy is correct

#### Acceptance criterion 1: Select a Preferred Pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion1:SelectaPreferredPharmacy}

Given the Patient is logged into Citizen Services

When the Patient chooses to select the Preferred Pharmacy

Then the pharmacy is selected as the Preferred Pharmacy

#### Acceptance criterion 2: view the Preferred Pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion2:viewthePreferredPharmacy}

Given the Patient is logged into Citizen Services

When the Patient chooses to view the Preferred Pharmacy

Then the Preferred Pharmacy is displayed

#### Acceptance criterion 3: amend the Preferred Pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion3:amendthePreferredPharmacy}

Given the Patient is logged into Citizen Services

When the Patient chooses to amend the Preferred Pharmacy

Then the Preferred Pharmacy is amended

---

### Epic 4 - manage Acute Medications {#PrescriptionOrdering-Citizenv1.0.0-Epic4-manageAcuteMedications}

As a Patient

I want to manage Acute Medications

So that I can receive Acute Medications

#### Acceptance criterion 1: view Acute Medications {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion1:viewAcuteMedications}

Given the Patient is logged into Citizen Services

When the Patient chooses to view Acute Medications

Then the Acute Medications are displayed

#### Acceptance criterion 2: view Issues of an Acute Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion2:viewIssuesofanAcuteMedication}

Given the Patient is logged into Citizen Services

When the Patient chooses to view Issues of an Acute Medication

Then the Issues for the Acute Medication are displayed

#### Acceptance criterion 3: request an Issue of an Acute Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion3:requestanIssueofanAcuteMedication}

Given the Patient is logged into Citizen Services

When the Patient chooses to request an Issue of an Acute Medication

Then the Issue is requested

#### Acceptance criterion 4: cancel a request for an Issue of an Acute Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion4:cancelarequestforanIssueofanAcuteMedication}

Given the Patient is logged into Citizen Services

When the Patient chooses to cancel a request for an Issue of an Acute Medication

Then the Issue request is cancelled

#### Acceptance criterion 5: support a request for an Issue of an Acute Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion5:supportarequestforanIssueofanAcuteMedication}

Given the Patient is logged into Citizen Services

When the Patient chooses to support a request for an Issue of an Acute Medication

Then the Issue request can be amended to include the evidence to support the request

#### Acceptance criterion 6: view outstanding requests for Issues of Acute Medications {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion6:viewoutstandingrequestsforIssuesofAcuteMedications}

Given the Patient is logged into Citizen Services

When the Patient chooses to view outstanding requests for Issues of Acute Medications

Then the outstanding Issue requests are displayed

---

### Epic 5 - view medication information {#PrescriptionOrdering-Citizenv1.0.0-Epic5-viewmedicationinformation}

As a Patient

I want to view information about medication

So that I can understand how to use it and the implications of doing so

#### Acceptance criterion 1: view medication information {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion1:viewmedicationinformation}

Given the Citizen is logged into Citizen Services

When the Citizen chooses to view medication information

Then information about how to use the medication is displayed

And information about the implications of using the medication

---

### Epic 6 - manage Repeat Medications as a Proxy {#PrescriptionOrdering-Citizenv1.0.0-Epic6-manageRepeatMedicationsasaProxy}

As a Proxy

I want to manage Repeat Medications

So that the Patient can receive Repeat Medications

#### Acceptance criterion 1: view Repeat Medications {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion1:viewRepeatMedications.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to view Repeat Medications

Then the Repeat Medications are displayed

#### Acceptance criterion 2: view most recent Issue of a Repeat Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion2:viewmostrecentIssueofaRepeatMedication.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to view the most recent Issue of a Repeat Medication

Then the most recent Issue for the Repeat Medication is displayed

#### Acceptance criterion 3: request an Issue of a Repeat Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion3:requestanIssueofaRepeatMedication.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to request an Issue of a Repeat Medication

Then the Issue is requested

#### Acceptance criterion 4: cancel a request for an Issue of a Repeat Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion4:cancelarequestforanIssueofaRepeatMedication.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to cancel a request for an Issue a Repeat Medication

Then the Issue request is cancelled

#### Acceptance criterion 5: support a request for an Issue a Repeat Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion5:supportarequestforanIssueaRepeatMedication.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to support a request for an Issue a Repeat Medication

Then the Issue request can be amended to include the evidence to support the request

#### Acceptance criterion 6: view outstanding requests for Issues of Repeat Medications {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion6:viewoutstandingrequestsforIssuesofRepeatMedications.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to view outstanding requests for Issues of Repeat Medications

Then the outstanding Issue requests are displayed

---

### Epic 7 - manage nominated EPS pharmacy as a Proxy {#PrescriptionOrdering-Citizenv1.0.0-Epic7-managenominatedEPSpharmacyasaProxy}

As a Proxy

I want to manage my Patient's nominated EPS pharmacy

So that the Patient's nominated pharmacy is correct

#### Acceptance criterion 1: nominate an EPS pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion1:nominateanEPSpharmacy.1}

Given the Proxy is logged into Citizen Services

And the Practice is enabled for the EPS

And the pharmacy chosen by the Proxy offers the EPS

When the Proxy chooses to nominate the pharmacy

Then the pharmacy is nominated as the EPS pharmacy

#### Acceptance criterion 2: view the nominated EPS pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion2:viewthenominatedEPSpharmacy.1}

Given the Proxy is logged into Citizen Services

And the Proxy has nominated a pharmacy for the EPS

When the Proxy chooses to view the nominated pharmacy

Then the nominated EPS pharmacy is displayed

#### Acceptance criterion 3: amend the nominated EPS pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion3:amendthenominatedEPSpharmacy.1}

Given the Proxy is logged into Citizen Services

And the Proxy has nominated a pharmacy for the EPS

And the alternative pharmacy offers the EPS

When the Proxy chooses to amend the nominated pharmacy to the alternative pharmacy

Then the alternative pharmacy is nominated as the EPS pharmacy

---

### Epic 8 - manage Preferred Pharmacy as a Proxy {#PrescriptionOrdering-Citizenv1.0.0-Epic8-managePreferredPharmacyasaProxy}

As a Proxy

I want to manage the Patient's Preferred Pharmacy

So that the Patient's Preferred Pharmacy is correct

#### Acceptance criterion 1: Select a Preferred Pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion1:SelectaPreferredPharmacy.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to select the Preferred Pharmacy

Then the pharmacy is selected as the Preferred Pharmacy

#### Acceptance criterion 2: view the Preferred Pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion2:viewthePreferredPharmacy.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to view the Preferred Pharmacy

Then the Preferred Pharmacy is displayed

#### Acceptance criterion 3: amend the Preferred Pharmacy {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion3:amendthePreferredPharmacy.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to amend the Preferred Pharmacy

Then the Preferred Pharmacy is amended

---

### Epic 9 - manage Acute Medications as a Proxy {#PrescriptionOrdering-Citizenv1.0.0-Epic9-manageAcuteMedicationsasaProxy}

As a Proxy

I want to manage Acute Medications

So that the Patient can receive Acute Medications

#### Acceptance criterion 1: view Acute Medications {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion1:viewAcuteMedications.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to view Acute Medications

Then the Acute Medications are displayed

#### Acceptance criterion 2: view Issues of an Acute Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion2:viewIssuesofanAcuteMedication.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to view Issues of an Acute Medication

Then the Issues for the Acute Medication are displayed

#### Acceptance criterion 3: request an Issue of an Acute Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion3:requestanIssueofanAcuteMedication.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to request an Issue of an Acute Medication

Then the Issue is requested

#### Acceptance criterion 4: cancel a request for an Issue of an Acute Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion4:cancelarequestforanIssueofanAcuteMedication.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to cancel a request for an Issue of an Acute Medication

Then the Issue request is cancelled

#### Acceptance criterion 5: support a request for an Issue of an Acute Medication {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion5:supportarequestforanIssueofanAcuteMedication.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to support a request for an Issue of an Acute Medication

Then the Issue request can be amended to include the evidence to support the request

#### Acceptance criterion 6: view outstanding requests for Issues of Acute Medications {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion6:viewoutstandingrequestsforIssuesofAcuteMedications.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to view outstanding requests for Issues of Acute Medications

Then the outstanding Issue requests are displayed

---

### Epic 10 - view medication information as a Proxy {#PrescriptionOrdering-Citizenv1.0.0-Epic10-viewmedicationinformationasaProxy}

As a Proxy

I want to view information about medication

So that I can understand how to use it and the implications of doing so

#### Acceptance criterion 1: view medication information {#PrescriptionOrdering-Citizenv1.0.0-Acceptancecriterion1:viewmedicationinformation.1}

Given the Proxy is logged into Citizen Services

When the Proxy chooses to view medication information

Then information about how to use the medication is displayed

And information about the implications of using the medication

**Capability Specific Standards**

Suppliers will have to attain compliance with these Standards during the compliance stage before they can be live on a framework with this Capability:

- Prescription Ordering – Citizen - Standard
**Other Applicable Standards**

Suppliers will also have to attain compliance with these additional Standards during the compliance stage before they can be live on a framework with this Capability:

- Interoperability Standard
- Citizen Access
- Management Information (MI) Reporting
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |