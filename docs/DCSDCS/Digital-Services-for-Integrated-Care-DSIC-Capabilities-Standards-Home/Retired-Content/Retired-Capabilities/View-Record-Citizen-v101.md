---
page_id: "12212830247"
space: "DCSDCS"
title: "View Record - Citizen v1.0.1"
version: 1
updated: "2022-11-23T11:51:01.902Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12212830247/View+Record+-+Citizen+v1.0.1"
labels: ["capability_retired"]
---

# View Record - Citizen v1.0.1

|  |  |
| --- | --- |
| ID | C4 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

Full Capability status only. For this Capability, Solutions are required to meet all MUST EPICs and associated acceptance criteria.

# Description

Enables Citizens to view their Patient Record online.

# Outcomes

|  |  |
| --- | --- |
| For a Citizen: | Having remote access to their Patient Record, or record(s) of Patients they are proxies for, supporting the accurate recording of personal information, reducing the need to contact the Practice to view information resulting in time saved, and enabling self-care. |
| For General Practice: | Maintenance of an online health record supports the remote care of Patients and maintaining positive relationships. It saves time for staff by reducing the need for Patients to contact the Practice (e.g. no need for Patients to call for test results and Patient more prepared before their Appointment) and supports effective communication with Patients, with relevant/nominated parties and with organisations providing other services. |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C4E1 - view Patient Record - Patient

As a Patient

I want to view my Patient Record

So that I can see the information in my Patient Record

#### Acceptance criterion 1: view Summary Information Record

Given the Patient is logged into Citizen Services

And the Patient is permitted to view the Patient Record

And the Patient is permitted to view the Summary Information Record

And the Patient is configured to view the Summary Information Record

When the Patient chooses to view the Summary Information Record

Then the Summary Information Record is displayed

#### Acceptance criterion 2: view Detailed Coded Records

Given the Patient is logged into Citizen Services

And the Patient is permitted to view the Patient Record

And the Patient is permitted to view Detailed Coded Records

And the Patient is configured to view Detailed Coded Records

When the Patient chooses to view Detailed Coded Records

Then Detailed Coded Records are displayed

#### Acceptance criterion 3: view Documents with Documents permission

Given the Patient is logged into Citizen Services

And the Patient is permitted to view the Patient Record

And the Patient is permitted to view the Detailed Coded Records

And the Patient is permitted to view Documents

And the Patient is configured to view Documents

When the Patient chooses to view Documents

Then Documents are displayed

#### Acceptance criterion 4: view Full Record

Given the Patient is logged into Citizen Services

And the Patient is permitted to view the Patient Record

And the Patient is permitted to view Detailed Coded Records

And the Patient is permitted to view the Full Record

And the Patient is configured to view the Full Record

When the Patient chooses to view the Full Record

Then the Full Record is displayed

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C4E2 - view Patient Record - Proxy

As a Proxy

I want to view a Patient Record

So that I can see the information in the Patient Record

#### Acceptance criterion 1: view Summary Information Record

Given the Proxy is logged into Citizen Services

And the Proxy is permitted to view the Patient Record

And the Proxy is permitted to view the Summary Information Record

And the Proxy is configured to view the Summary Information Record

When the Proxy chooses to view the Summary Information Record

Then the Summary Information Record is displayed

#### Acceptance criterion 2: view Detailed Coded Records

Given the Proxy is logged into Citizen Services

And the Proxy is permitted to view the Patient Record

And the Proxy is permitted to view Detailed Coded Records

And the Proxy is configured to view Detailed Coded Records

When the Proxy chooses to view Detailed Coded Records

Then Detailed Coded Records are displayed

#### Acceptance criterion 3: view Documents with Documents permission

Given the Proxy is logged into Citizen Services

And the Proxy is permitted to view the Patient Record

And the Proxy is permitted to view the Detailed Coded Records

And the Proxy is permitted to view Documents

And the Proxy is configured to view Documents

When the Proxy chooses to view Documents

Then Documents are displayed

#### Acceptance criterion 4: view Full Record

Given the Proxy is logged into Citizen Services

And the Proxy is permitted to view the Patient Record

And the Proxy is permitted to view Detailed Coded Records

And the Proxy is permitted to view the Full Record

And the Proxy is configured to view the Full Record

When the Proxy chooses to view the Full Record

Then the Full Record is displayed

**Capability Specific Standards**

Suppliers will have to attain compliance with this Standard during the compliance stage before they can be live on a framework with this Capability:

- View Record - Citizen - Standard
**Other Applicable Standards**

Suppliers will also have to attain compliance with these additional Standards during the compliance stage before they can be live on a framework with this Capability:

- Interoperability Standard
- Citizen Access v1.0.1
- Management Information (MI) Reporting
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [NHS login interface - Provisioning](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/1391133536/NHS+login+interface+-+Provisioning) | [Interoperability Standard](../../DSIC-Standards/Overarching-Standards/Interoperability-Standard.md), [NHS login Service](../../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md), [Appointments Management - Citizen](../../DSIC-Capabilities/Appointments-Management-Citizen.md), [Communicate With Practice - Citizen](../../Deprecated-Content/Deprecated-Capabilities/Communicate-With-Practice-Citizen.md), [Patient Information Maintenance - GP](../../DSIC-Capabilities/Patient-Information-Maintenance-GP.md), [Prescription Ordering - Citizen](../../DSIC-Capabilities/Prescription-Ordering-Citizen.md), [View Record - Citizen](../../DSIC-Capabilities/View-Record-Citizen.md) | Draft | TBC | The provisioning interface enables GP solutions to provision new Citizen users on the NHS login platform, thus enabling Citizens to use one consistent account for Patient sign-in and ID verification. | Replace | Opportunity Item |