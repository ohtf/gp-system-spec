---
page_id: "12417400866"
space: "DCSDCS"
title: "Cross-organisation Appointment Booking v1.0.1"
version: 1
updated: "2023-05-22T11:22:56.152Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12417400866/Cross-organisation+Appointment+Booking+v1.0.1"
labels: ["capability_retired"]
---

# Cross-organisation Appointment Booking v1.0.1

|  |  |
| --- | --- |
| ID | C23 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - GP IT Futures - Tech Innovation |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description

Cross-Organisation Appointment Booking supports Health and Care Professionals and others to make Appointments for Patients/Service Users across traditional Organisation boundaries. For example, Service Providers working across Integrated and Federated Care, Super Partnerships and Health and Care Professionals within multi-disciplinary teams. This collaborative approach to offering Appointments creates efficiencies in resourcing, and by giving Patients/Service Users a greater variety of Appointments, creates a better experience for the Patient/Service User.

The Capability allows the user to book Appointments across Organisations from a single system rather than logging into multiple systems, improving efficiency and reducing the need for multiple log-ons. The Capability will be able to support diaries across multiple Organisations, which may follow different naming/formatting conventions.

Examples of the use of Cross-Organisation Appointment Booking include:

- A group of Practices providing extended hours Appointments by making Appointments available to Patients/Service Users from other practices within the group
- Shared Appointment management across a group of organisations to allow Patients/Service Users to be triaged to the most appropriate service to meet the Patient/Service User's need
- Making specified Appointment slots available to external organisations such as an NHS 111 service so the service can book an Appointment on behalf of the Patient /Service User with their GP Practice

# Outcomes

|  |  |
| --- | --- |
| Patient/Service User | - Able to access the most appropriate Appointment slot based on criteria such as location, time and type of Appointment - Able to access Appointments across traditional Organisation boundaries increasing the likelihood of finding a convenient Appointment |
| Health and Care Professionals | - Able to book Appointments for Patients/Service Users without needing manual intervention, saving time and effort - Able to identify the most appropriate Appointment for the Patient/Service User prior to Booking, improving Patient/Service User experience and making the most efficient use of available Appointments |
| Organisation/Service Provider | - Able to make Appointments available to external organisations to book in a controlled and managed way, supporting new ways of working and across organisational boundaries |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C23E1 - make Appointments available to external organisations

As a Service Provider

I want to be able to manage my Appointment slots

So that I can make certain slots available to be booked by other Service Providers and manage how they are used

#### Acceptance criterion 1: create Appointment slots that can be booked by other organisations

Given there are Appointment slots that are to be made available to be booked by external Service Providers

When the Cross-Organisation Appointment Booking Service is accessed

Then Appointment slots can be created that can be booked externally

And rules can be defined relating to Booking or usage of the Appointment Slots (e.g. which organisations can book)

#### Acceptance criterion 2: amend Appointment slots that can be booked by other organisations

Given that Appointment slots have been created

When a change to the Appointment slots that are available to external organisations for Booking has been identified

Then the Appointment slots that can be booked externally can be amended

And rules relating to Booking or usage of the Appointment Slots (e.g. which organisations can book) can be updated

---

### C23E2 - search externally bookable Appointment slots

As a Health or Care Professional

I want to be able to search the Appointment slots made available by another Organisation

So that I can find the Appointment slot most appropriate to meet the needs of the Patient/Service User

#### Acceptance criterion 1: search Appointment slots

Given that Appointment slots have been made available to external Organisations to book

And can be booked by the requesting Organisation

When an Appointment is required at another Organisation for a Patient/Service User

Then one or more adjacent Slots can be selected to book

---

### C23E3 - book externally bookable Appointment slots

As a Health or Care Professional

I want to book Patients/Service Users into Appointment slots made available by another Organisation

So that I can meet the Appointment needs of my Patients/Service Users

#### Acceptance criterion 1: organisation user books available Appointment slot

Given that Appointment slots have been made available to external Organisations to book

And can be booked by the requesting Organisation

When an available Appointment slot is identified that fits with the needs of the Patient/Service User

Then an Appointment slot can be booked for the Patient/Service User

And the booking is confirmed

---

### C23E4 - maintain Appointments

As a Service Provider

I want to be able to maintain the Appointments made for Patients/Service Users

So that I can ensure booked Appointments continue to align to the Patient/Service User's needs

#### Acceptance criterion 1: view Appointments

Given that Appointment slots have been booked for Patients/Service Users

When the Cross-Organisation Appointment Booking Service is accessed

Then all Appointments booked with external Organisations can be viewed

And the details of the Appointment(s) can be viewed

#### Acceptance criterion 2: amend Appointment

Given that Appointment slots have been booked for Patients/Service Users

When the need to amend an Appointment slot is identified

Then the Appointment details for the Patient/Service User is amended

#### Acceptance criterion 3: cancel Appointment

Given that Appointment slots have been booked for Patients/Service Users

When it is identified that an Appointment is no longer required by a Patient/Service User

Then the Appointment for the Patient/Service User is cancelled

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C23E5 - notifications

As a Health or Care Professional

I want to receive notifications in relation to Bookings I have made into slots made available by another Organisation

So that I am aware of Bookings and any changes and can act on these

#### Acceptance criterion 1: receive notification about Appointments

Given that an Appointment has been booked for the Patient/Service User with an external Organisation

And recipient contact details have been captured

When an Appointment is booked with an external Organisation

Then the recipients receive a notification that the Appointment has been booked

And the notification contains information about the Appointment

#### Acceptance criterion 2: receive notification about change to Appointment

Given that an Appointment has been booked for the Patient/Service User with an external organisation

And recipient contact details have been captured

When the Appointment is amended (updated or cancelled)

Then the recipients receive a notification that the Appointment has been amended

And the notification contains information about the changes to the Appointment

---

### C23E6 - manage Appointment Requests

As a Health or Care Professional

I want to request a specific Appointment for a Patient/Service User with an external Organisation

So that I can obtain the Appointment that best fits the needs of the Patient/Service User

#### Acceptance criterion 1: make a request for an Appointment slot

Given that an Appointment is required for a Patient/Service User with an external Organisation

When it is identified that a suitable Appointment (e.g. the correct time or location, with the relevant Clinician) is not currently available

Then a request for an Appointment can be created

And information relating to the requested Appointment can be provided

And the request can be sent to the relevant external Organisation

#### Acceptance criterion 2: amend request for an Appointment slot

Given a request for an Appointment slot has been sent to an external Organisation

When a need to change (update or delete) the request is identified

Then the Appointment request can be amended

And the revised Appointment request can be sent to the relevant external Organisation

#### Acceptance criterion 3: respond to Appointment request

Given that an Organisation makes Appointment slots available to external Organisations to book

When a request for an Appointment slot is received by the Organisation

Then the request for an Appointment slot can be viewed

And the request can be responded to (accepted or rejected)

---

### C23E7 - booking approval

As a Service Provider

I want to be able to create Appointment slots that require approval by my Organisation before the Appointment is confirmed

So that I can better manage the Booking of Appointment slots by external Organisations

#### Acceptance criterion 1: create Appointment slots that need approval

Given that an Organisation makes Appointments available to external Organisations to book

When the Organisation identifies Appointment slots that require approval before Booking is confirmed for an external Organisation

Then the Appointment slots can be identified as requiring approval

#### Acceptance criterion 2: book Appointment slot that requires approval

Given that an Organisation has made Appointment slots available to external Organisations to book

And some or all of the Appointment slots have been identified as requiring approval

When an external Organisation requests an Appointment slot that requires approval

Then the request for the Appointment slot is sent to the Provider of the Appointment slot

And the requestor can identify that the Appointment slot requires approval before being confirmed

#### Acceptance criterion 3: respond to request for Appointment slot

Given that an Organisation has made Appointment slots available to external Organisations to book

And some or all of the Appointment slots have been identified as requiring approval

When a request to book an Appointment slot that requires approval is received from an external Organisation

Then the request for an Appointment slot can be responded to (approved or rejected)

And the requestor is notified of the outcome

---

### C23E8 - report on usage of Cross-Organisation Appointments

As a Manager

I want to have access to custom reports relating to externally bookable Appointment slots

So that I can make informed decisions relating to these Appointments

#### Acceptance criterion 1: report on use of Appointments by external organisations

Given that an organisation has made Appointments available to external organisations to book

And information on these Appointment slots is available

When the Manager wants to report on use of their Organisation’s Appointments by external organisations

Then a report can be run to create output relating to the use of externally bookable Appointment slots

#### Acceptance criterion 2: report on use of other organisation’s Appointments

Given that an organisation has booked Appointments for their Patients/Service Users with external organisations

And information on these Appointments is available

When the Manager wants to report on Appointments made for their Patients/Service Users with other Organisations

Then a report can be run to create output relating to the use of externally bookable Appointment slots

---

### C23E9 - manage Cross-Organisation Appointment Booking templates

As a Service Provider

I want to be able to maintain templates for Appointment slots

So that I can improve efficiency by using existing templates to create externally bookable Appointment slots

#### Acceptance criterion 1: maintain Appointment slot template

Given that there is a need to create Appointment slots that can be made available to external Service Providers to book

When a change is required relating to an Appointment slot template

Then the relevant template for externally bookable Appointment slots can be created, updated or deleted

#### Acceptance criterion 2: Use booking slot template

Given that one or more templates exist to support the creation of Appointment slots

When the Service Provider decides to create one or more externally bookable Appointment slots based on a template

Then the existing templates can be viewed

And the relevant template can be selected

And one or more externally bookable Appointment slots can be created based on the template

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