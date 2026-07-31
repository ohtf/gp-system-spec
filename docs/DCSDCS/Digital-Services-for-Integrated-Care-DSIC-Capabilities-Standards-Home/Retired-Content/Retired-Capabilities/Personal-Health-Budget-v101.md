---
page_id: "12879331329"
space: "DCSDCS"
title: "Personal Health Budget v1.0.1"
version: 2
updated: "2024-04-02T14:00:39.281Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12879331329/Personal+Health+Budget+v1.0.1"
labels: ["capability_retired"]
---

# Personal Health Budget v1.0.1

|  |  |
| --- | --- |
| ID | C32 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description

Personal Health Budgets are amounts of money allocated to a Patient/Service User to support their health and well-being needs and to enable them to purchase and manage their own treatments, equipment and personal care. Personal Health Budgets are available to Adults receiving NHS Continuing Healthcare and children receiving continuing care - for example, people with long-term physical or mental health issues. Requests outside this are considered on a case basis by the Patient/Service User's CCG.

A Personal Health Budget Capability will allow a Personal Health Budget to be defined, reviewed and updated. The Capability facilitates the link between the Personal Health Budget and the Patient/Service User's care plan to ensure spend is directed towards meeting the Patient/Service User's health goals. A Personal Health Budget Capability will allow purchases of a range of products and services to deliver the agreed health and well-being outcomes, for example therapies (e.g. counselling), personal care (e.g. a personal assistant), services (e.g. gym membership) and equipment (e.g. a wheelchair). CCGs will be able to assess Personal Health Budgets to ensure they are used appropriately.

A Personal Health Budget Capability may manage multiple budgets and the directory of equipment, treatments and therapies and give further reporting functionality. It may also link to the Patient record and Workflow tasks to further broaden its integration with other functions.

# Outcomes

|  |  |
| --- | --- |
| Patient/Service User | - Able to understand, upfront, the amount of money available to them for healthcare and track spend against this - Able to choose an individual who can manage the Personal Health Budget on their behalf - Able to identify and then purchase the equipment, treatment or services they feel will best deliver the outcomes defined in their care plan - Able to use a Directory of Services to identify potential equipment, treatment or services that might be of benefit and compare costs |
| Care Coordinator or Local NHS Team member or Health Broker | - Facilitates a conversation between the Patient/Service User and their Care Coordinator, local NHS team or Health Broker - Use of eligibility criteria makes it easier to identify Patients/Service Users who are eligible for a Personal Health Budget - Use of eligibility criteria makes it easier to identify products and services that can be purchased using a Personal Health Budget |
| CCG | - Able to audit spend against Budgets and identify inappropriate spend - Able to plan effectively and track spend by monitoring across all Personal Health Budgets within the CCG - Able to utilise different models for the management of Personal Health Budgets - notional, 3rd party and direct payment - Able to pay for equipment, treatment or services direct to the Service Provider or via a 3rd party or the Patient/Service User |
| Service Provider | - Directory of services allows them to share information on their services - Able to understand the take-up of their services by Patients/Service Users |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C32E1 - manage Personal Health Budget

As a Patient/Service User

I want to manage my Personal Health Budget

So that I can use my budget to deliver my desired health outcomes

#### Acceptance criterion 1: create Personal Health Budget

Given the Health or Care Professional has requested a Personal Health Budget

When they choose to create the Personal Health Budget

Then the Personal Health Budget is created for the Patient/Service User

#### Acceptance criterion 2: choose an individual to manage Personal Health Budget

Given the Patient/Service User has been allocated a Personal Health Budget

When the Patient/Service User chooses an individual to manage their Personal Health Budget on their behalf

Then the individual can access the Personal Health Budget

And can make purchases on behalf of the Patient/Service User

#### Acceptance criterion 3: view Personal Health Budget

Given that the Patient/Service User has a Personal Health Budget

And purchases have been entered

When the Patient/Service User chooses to view the Personal Health budget

Then the Personal Health Budget is displayed

#### Acceptance criterion 4: review Personal Health Budget

Given a Personal Health Budget and care plan has been set up for a Patient/Service User

When the Personal Health Budget is reviewed

Then a record of the review can be recorded against the Personal Health Budget

#### Acceptance criterion 5: amend Personal Health Budget

Given a Personal Health Budget and care plan have been set up for a Patient/Service User

When the Personal Health Budget is reviewed

Then the Personal Health Budget can be amended

#### Acceptance criterion 6: close Personal Health Budget

Given a Personal Health Budget and care plan have been set up for a Patient/Service User

When the Personal Health Budget is reviewed

Then a record of the review can be captured against the Personal Health Budget

And the Personal Health Budget can be closed or made inactive

---

### C32E2 - record Personal Health Budget purchases

As a Patient/Service User

I want to be able to record Personal Health Budget purchases

So that I can evidence where my Personal Health Budget has been spent

#### Acceptance criterion 1: record Personal Health Budget purchase

Given that the Patient/Service User can access the Personal Health Budget Solution

When payment is made for products or services (by the NHS team, a Third party or the Patient/Service User)

Then evidence of how and on what the money has been spent (e.g. receipts, invoices, bank statements) can be captured

And this is recorded against the Personal Health Budget for the Patient/Service User

---

### C32E3 - assess Personal Health Budgets

As a representative of the CCG

I want to be able to assess Personal Health Budgets

So that I can ensure that Budgets are only spent on appropriate products and services

#### Acceptance criterion 1: view purchase trail against the budget

Given the user has been permitted access to the Personal Health Budget

And the Personal Health Budget purchase has been recorded

When the user chooses to view the purchase trail against the budget

Then purchase trail against the budget is displayed

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C32E4 - link Personal Health Budget with care plan

As a Patient/Service User

I want to link my care plan and Personal Health Budget

So that I can ensure that my Personal Health Budget is spent in the way most likely to deliver my identified health and well-being outcomes

#### Acceptance criterion 1: link Personal Health Budget with care plan

Given a care plan has been created for a Patient/Service User

When the Personal Health Budget is created

Then the Budget and care plan for the Patient/Service User can be linked

And the care plan can be viewed

#### Acceptance criterion 2: link Purchases to elements on the care plan

Given a Personal Health Budget has been created for a Patient/Service User

And a care plan has been linked

When items of spend are identified for purchase against the Personal Health Budget

Then the purchases can be linked to elements of the care plan

---

### C32E5 - support different models for management of Personal Health Budgets

As a Care Coordinator or Local NHS Team

I want to choose a model to manage a particular Personal Health Budget

So that I can select the model that will be most appropriate and effective for the Patient/Service User and their Care Team

#### Acceptance criterion 1: support different management models

Given a Personal Health Budget has been assigned to a Patient/Service User

When the model to manage Personal Health Budgets is chosen (e.g. via the NHS Care Team, Third Party, direct payment or a combination of these)

Then different elements of the Budget can be assigned to the relevant model

And the agreed equipment, treatments or services can be purchased by the relevant individual or Third Party

---

### C32E6 - apply criteria for the use of Personal Health Budgets

As a representative of the CCG

I want to apply criteria for the use of Personal Health Budgets

So that I can ensure the Budgets are used only by eligible Patients/Service Users

#### Acceptance criterion 1: eligible Patient/Service User

Given the Personal Health Budget eligibility criteria has been defined for Patients/Service Users (e.g. Adults eligible for NHS Continuing Healthcare and children receiving continuing care)

When the Patient/Service User is identified as eligible for a Personal Health Budget

Then the Personal Health Budget can be created for the Patient/Service User

---

### C32E7 - payments under Personal Health Budgets

As a Health or Care Professional

I want to make payments relating to Personal Health Budgets

So that I can enable Patient/Service Users to access appropriate products and services

#### Acceptance criterion 1: pay for products or services

Given a Personal Health Budget is being managed with a model (e.g. via the NHS Care Team, Third Party, direct payment or a combination of these)

When the user chooses to make a payment for a product or service

Then a payment can be made

And the payment can be recorded against the relevant Personal Health Budget

---

### C32E8 - maintain directory of equipment, treatments and services

As a Personal Health Budget Manager or Health or Care Professional

I want to be able to maintain a directory of equipment, treatments or services

So that I can use the directory to find relevant equipment, treatments or services

#### Acceptance criterion 1: create directory of equipment, treatments and services

Given that the user is permitted to create a directory of equipment, treatments and services in the Personal Health Budget Solution

When the user chooses to create the directory of equipment, treatments and services in the Personal Health Budget Solution

Then the directory is created

#### Acceptance criterion 2: view directory of equipment, treatments and services

Given that the user is permitted to view the directory of equipment, treatments and services in the Personal Health Budget Solution

And the directory of equipment, treatments and services has been created in the Personal Health Budget Solution

When the user chooses to view the directory of equipment, treatments and services in the Personal Health Budget Solution

Then the directory is displayed

#### Acceptance criterion 3: amend directory of equipment, treatments and services

Given that a directory of equipment, treatments and services has been created in the Personal Health Budget Solution

When the user chooses to update the directory of equipment, treatments and services in the Personal Health Budget Solution

Then the directory is amended

#### Acceptance criterion 4: remove an item from the directory of equipment, treatments and services

Given that a directory of equipment, treatments and services has been created in the Personal Health Budget Solution

When the user chooses to remove an item from the directory of equipment, treatments and services in the Personal Health Budget Solution

Then then the item in the directory is removed

---

### C32E9 - search a directory of equipment, treatments and services

As a Personal Health Budget Manager or Health or Care Professional

I want to be able to search a directory of equipment, treatments or services

So that I can identify and select the equipment, treatments or services that will support delivery of the Patient/Service User's healthcare outcomes

#### Acceptance criterion 1: search directory of equipment, treatments and services

Given that a directory of equipment, treatments and services has been created in the Personal Health Budget Solution

And search criteria have been defined

When the user chooses to search for equipment, treatment or services

Then the list of equipment, treatments or services that match the search criteria are displayed

---

### C32E10 - manage multiple budgets

As a Personal Health Budget Manager

I want to manage budgets from multiple sources (e.g. those relating to health, care, education or other needs) as a single, joint budget

So that I can more easily manage and co-ordinate across all my needs

#### Acceptance criterion 1: manage multiple health and care budgets

Given a Personal Health Budget has been set up for a Patient/Service User

And the Patient/Service User holds further budgets (e.g. a social care Personal Budget) relating to their needs

When the Patient/Service User identifies they want to manage these as a joint budget

Then the multiple budgets can be managed as a single budget within the Personal Health Budget tool or system

And the Patient/Service User can use the single, joint budget to pay for agreed equipment, treatments or services across their health, care, education or other needs

---

### C32E11 - link to Patient Record

As a Health or Care Professional

I want to be able to access the Patient Record for the Patient

So that I can confirm their medical history and understand their entitlement to a Personal Health Budget

#### Acceptance criterion 1: link to Patient Record

Given the Health or Care Professional has been permitted access to the Patient Record

When the user chooses to view the Patient Record

Then the Patient Record is displayed

---

### C32E12 - link to Workflow

As a Health or Care Professional

I want to be able to create a workflow task from the Personal Health Budget Solution

So that I can send requests for information into the Patient/Service User's Practice (e.g. request for clinical information, request for confirmation of medical history)

#### Acceptance criterion 1: create Workflow task

Given the Health or Care Professional has been permitted to create Workflow Tasks

When the user chooses to create a Workflow task

Then the Workflow task is created

And the task is directed into the workflow for the Practice

---

### C32E13 - provider view

As a Service or Product Provider

I want to be able to view the purchases of my products or services

So that I can analyse and understand take-up of my products and services

#### Acceptance criterion 1: provider can view purchase information

Given a Provider's products or services are included in the Directory

And they are permitted to view information in the Personal Health Budget Solution

When they choose to view purchases of their products and services

Then purchase information relating to their products or services is displayed

---

### C32E14 - Management Information

As a representative of the CCG

I want to analyse and report against data relating to Personal Health Budgets

So that I can use the results to plan and commission healthcare more effectively to meet the needs of Patients/Service Users

#### Acceptance criterion 1: Management Information reporting

Given the user is permitted to run Management Information reports

When the user chooses to run a Management Information report

Then the Management Information report is displayed

---

### C32E15 - identify candidates for Personal Health Budgets

As a representative of the CCG

I want to identify potential candidates eligible for Personal Health Budgets

So that Patients/Service Users can be proactively identified

#### Acceptance criterion 1: identify Patients/Service Users that are candidates for a Personal Health Budget

Given the CCG has defined criteria for prioritising Patient/Service User need

When the CCG representative inputs the criteria to identify Personal Health Budget candidates

Then the results for Patients/Service Users meeting the criteria are displayed

**Capability Specific Standards**

Suppliers will have to attain compliance with these Standards during the compliance stage before they can be live on a framework with this Capability:

None

**Other Applicable Standards**

Suppliers will also have to attain compliance with these additional Standards during the compliance stage before they can be live on a framework with this Capability:

- Interoperability Standard
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |