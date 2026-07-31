---
page_id: "12212830209"
space: "DCSDCS"
title: "Appointments Management - Citizen v1.0.1"
version: 1
updated: "2022-11-23T09:48:08.471Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12212830209/Appointments+Management+-+Citizen+v1.0.1"
labels: ["capability_retired"]
---

# Appointments Management - Citizen v1.0.1

|  |  |
| --- | --- |
| ID | C1 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

Full Capability status only. For this Capability, Solutions are required to meet all MUST EPICs and associated acceptance criteria.

# Description

Enables Citizens to manage their Appointments online. Supports the use of Appointment Slots that have been configured in Appointments Management - GP.

# Outcomes

|  |  |
| --- | --- |
| For a Patient: | The ability to view, book and cancel Appointments online efficiently and in a manner that suits their needs and with easy visibility of future booked Appointments and available Appointment Slots. |
| For General Practice: | The effective management of time, personnel, and resources to ensure Patients have timely access to appropriate medical services. As a result, there will be fewer phone calls/face-to-face transactions with Patients, releasing time for staff to be deployed on other tasks. |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C1E1 - manage Appointments

As a Patient

I want to manage Appointments

So that I can manage my Appointments without contacting the Practice

#### Acceptance criterion 1: book Appointments

Given the Patient is logged into Citizen Services

When they choose to book an Appointment

Then the Appointment is booked with the Practice

#### Acceptance criterion 2: view Appointments

Given the Patient is logged into Citizen Services

When they choose to view the Appointments

Then the Appointments are displayed

#### Acceptance criterion 3: cancel Appointments

Given the Patient is logged into Citizen Services

When they choose to cancel an Appointment

Then the Appointment is cancelled with the Practice

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C1E2 - manage Appointments by Proxy

As a Proxy

I want to manage Appointments for a Patient

So that I can manage Appointments for a Patient without contacting the Practice

#### Acceptance criterion 1: book Appointments

Given the Proxy is logged into Citizen Services

When they choose to book an Appointment

Then the Appointment is booked with the Practice

#### Acceptance criterion 2: view Appointments

Given the Proxy is logged into Citizen Services

When they choose to view the Appointments

Then the Appointments are displayed

#### Acceptance criterion 3: cancel Appointments

Given the Proxy is logged into Citizen Services

When they choose to cancel an Appointment

Then the Appointment is cancelled with the Practice

**Capability Specific Standards**

Suppliers will have to attain compliance with these Standards during the compliance stage before they can be live on a framework with this Capability:

- Appointments Management - Citizen - Standard
**Other Applicable Standards**

Suppliers will also have to attain compliance with these additional Standards during the compliance stage before they can be live on a framework with this Capability:

- Interoperability Standard
- Citizen Access
- Management Information (MI) Reporting
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [NHS login interface - Provisioning](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/1391133536/NHS+login+interface+-+Provisioning) | [Interoperability Standard](../../DSIC-Standards/Overarching-Standards/Interoperability-Standard.md), [NHS login Service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md), [Appointments Management - Citizen](../../DSIC-Capabilities/Appointments-Management-Citizen.md), [Communicate With Practice - Citizen](../../Deprecated-Content/Deprecated-Capabilities/Communicate-With-Practice-Citizen.md), [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Prescription Ordering - Citizen](../../DSIC-Capabilities/Prescription-Ordering-Citizen.md), [View Record - Citizen](../../DSIC-Capabilities/View-Record-Citizen.md) | Draft | TBC | The provisioning interface enables GP solutions to provision new Citizen users on the NHS login platform, thus enabling Citizens to use one consistent account for Patient sign-in and ID verification. | Replace | Opportunity Item |