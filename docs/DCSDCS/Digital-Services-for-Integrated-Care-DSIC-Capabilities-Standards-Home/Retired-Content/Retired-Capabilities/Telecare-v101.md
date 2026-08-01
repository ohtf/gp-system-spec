---
page_id: "12818055171"
space: "DCSDCS"
title: "Telecare v1.0.1"
version: 5
updated: "2024-03-07T11:03:58.337Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12818055171/Telecare+v1.0.1"
labels: ["capability_retired"]
---

# Telecare v1.0.1

|  |  |
| --- | --- |
| ID | C38 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description {#Telecarev1.0.1-Description}

NHS England defines Telecare as technologies in the citizen’s home and communities to minimise risk and provide urgent notification of adverse events. Who is alerted will depend on the device being used and circumstances of the Patient/Service User but is typically a friend, neighbour or family member, a call centre or the emergency services. The specific goal of Telecare is to help Patients / Service Users live independently for longer in their own home or a location of their choice by ensuring that, if the Patient/Service User experiences an event that could seriously affect their health or well-being (e.g. a fall, seizure or failing to eat regularly), then the correct responder is notified and action can be taken.

Telecare sits under the umbrella of a wider range of technologies known as Technology Enabled Care Services (TECS). They are intended to help the Patient/Service User better manage and have more control over their healthcare needs, sustain Patient/Service User independence, help information exchange, and assist in the diagnosis and monitoring of health status. TEC services are often sub-divided into: Telehealth; Telecoaching; Teleconsultation (or Telemedicine); and Telecare.

Telecare devices are widely used by individuals, in some cases for health- or care-related purpose but often for a more general sense of safety or well-being. Examples of commonly used Telecare devices include those for:

- Environment monitoring
  - Extreme temperature, smoke, flood or carbon monoxide detectors
  - Sensors monitoring the fridge or cupboards (e.g. has the Patient/Service User opened the fridge/cupboards? Are they eating regularly?)
- Personal monitoring
  - Monitoring of vital signs or for conditions e.g. seizure alarm
  - Personal alarms (including pendants worn on the person or pull cords or alarm buttons in their home)
  - Bed or chair occupancy monitors
  - Intelligent behaviour monitoring e.g. is the Patient/Service User following their usual pattern of movement around the home or their local community?
  - GPS monitoring of the Patient/Service User's location

Telecare devices tend to be quite discrete in function so, often, a Patient/Service User will make use of devices depending on their particular needs. These will complement the Patient/Service User’s use of other TECS and wider health and care services.

Telecare is already well-established in the social care sector. However, more integrated models of care as well as opportunities to use Telecare (and TECS more widely) to help deliver NHS-commissioned services that are more cost-effective and deliver better outcomes for Patients/Service Users mean that Telecare is likely to become a more important part of the health landscape.

# Outcomes {#Telecarev1.0.1-Outcomes}

|  |  |
| --- | --- |
| Patient/Service Users | - Able to mitigate risks associated with their health and environment, enabling them to live independently and / or in a location of their choice for longer - Re-assured that, if an adverse event occurs, appropriate help will be summoned - More timely help or care received in relation to an adverse event leading to better outcomes - Able to address their specific needs by exercising choice in selecting from the wide range of available devices |
| Family member, friend or Carer | - Know that the Patient/Service User is being monitored and that they or another responder will be alerted if anything untoward happens - giving the family member peace of mind - Able to get respite – the family member, friend or Carer doesn't have to be ‘on hand’ 24 hours a day |
| Health and Care Professionals | - Knowledge that adverse events relating to their Patients/Service Users will be identified quickly and routed to the most appropriate responder |
| Local Authorities | - Patients/Service Users able to live independently and in their own home for longer, reducing costs of care - Better able to consider the wider physical, mental and emotional well-being of individuals needing care |
| Integrated or Federated Care Organisations, CCGs, STPs | - Able to choose from a range of devices and related services enabling a wider range of a Patient/Service User’s needs to be met - Able to improve the health and care of Patients through the analysis of Telecare-related MI |
| Hospitals | - Able to discharge Patients earlier as they are able to use Telecare devices to manage the risk |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C38E1 - define response to event {#Telecarev1.0.1-C38E1-defineresponsetoevent}

As a Patient/Service User or someone acting on their behalf

I want to be able to define - within the limits of the Telecare device - the rules governing how particular events will be responded to

So that I can be sure that the correct responder is notified when those events occur

#### Acceptance criterion 1: define response to an event occurring {#Telecarev1.0.1-Acceptancecriterion1:defineresponsetoaneventoccurring}

Given a Telecare device has been identified to meet a Patient/Service User's needs

And the device has been set up or configured to monitor for events occurring (e.g. the Patient/Service User falls, smoke or a flood is detected)

When the Patient/Service User wants to set up the response to the event

Then the device set up (configuration) relating to response to an event can be accessed

And the device can be set up or configured to notify or alert a responder (e.g. a family member, friend or neighbour, 3rd party call centre or the emergency services) when the defined adverse event occurs

#### Acceptance criterion 2: define response to an event not occurring {#Telecarev1.0.1-Acceptancecriterion2:defineresponsetoaneventnotoccurring}

Given a Telecare device has been identified to meet a Patient/Service User's needs

And the device has been set up or configured to monitor for events not occurring (e.g. the Patient/Service User fails to return to bed within a given time-frame or fails to open the fridge or cupboards at regular intervals)

When the Patient/Service User wants to set up the response to the event not occurring

Then the device set up (configuration) relating to response to an event not occurring can be accessed

And device can be set up or configured to notify or alert a responder (e.g. a family member, friend or neighbour, 3rd party call centre or the emergency services) of the event not occurring

---

### C38E2 - monitor and alert {#Telecarev1.0.1-C38E2-monitorandalert}

As a Patient/Service User

I want my Telecare device to continuously monitor for a change in my personal or environmental conditions

So that if an adverse event occurs, the correct responder will be notified

#### Acceptance criterion 1: monitor for an event occurring {#Telecarev1.0.1-Acceptancecriterion1:monitorforaneventoccurring}

Given a Telecare device has been installed

And the device has been set up or configured to monitor for events occurring

When the event occurs (e.g. the Patient/Service User falls, smoke is detected)

Then it is identified as an adverse event by the device

#### Acceptance criterion 2: monitor for an event not occurring {#Telecarev1.0.1-Acceptancecriterion2:monitorforaneventnotoccurring}

Given a Telecare device has been installed

And the device has been set up or configured to monitor for an event not occurring

When an event fails to happen (e.g. the Patient/Service User fails to return to bed or their chair within a given time-frame)

Then this is identified as an adverse event by the device

#### Acceptance criterion 3: alert adverse event {#Telecarev1.0.1-Acceptancecriterion3:alertadverseevent}

Given a Telecare device has been installed

And the device has been set up or configured to monitor for adverse events (event occurs or fails to occur)

When the device identifies an adverse event has occurred

Then an alert or notification is generated

---

### C38E3 - receive alerts {#Telecarev1.0.1-C38E3-receivealerts}

As a Telecare Service Provider or other responder

I want to know that I will receive alerts (e.g. via the careline or call centre system) generated by the Telecare devices of the Patients/Service Users that I support

So that if an adverse event occurs, I will be notified quickly and can take action

#### Acceptance criterion 1: Send alert to the responder {#Telecarev1.0.1-Acceptancecriterion1:Sendalerttotheresponder}

Given a Telecare device has been installed

And the device has been set up or configured to monitor for a change in conditions

And the device has identified that an adverse or non-event has occurred

When the alert or notification is generated

Then the alert is received by the correct responder within the times defined within the service-level agreement for the device

And the responder can identify from the alert which P/SU needs attention

And the responder can identify the device that triggered the alert (e.g. falls bracelet, smoke detector) and hence the type of adverse event (event or non-event)

---

### C38E4 - meet availability targets {#Telecarev1.0.1-C38E4-meetavailabilitytargets}

As a Patient/Service User

I want to know that my Telecare device is monitoring continuously within its availability target (e.g. 24x7 and 365 days per year)

So that I can be confident that any adverse event will be identified regardless of when it occurs

#### Acceptance criterion 1: device is working normally {#Telecarev1.0.1-Acceptancecriterion1:deviceisworkingnormally}

Given a Telecare device has been installed

When the Patient/Service User wants to confirm the device is working correctly

Then the device can indicate (e.g. by a light, display message or noise) that it is operating correctly

#### Acceptance criterion 2: device fails {#Telecarev1.0.1-Acceptancecriterion2:devicefails}

Given a Telecare device has been installed

When the device fails to operate normally (e.g. device has been damaged or has no power)

Then the device can indicate that it is not operating correctly (e.g. by means of a light, warning message, noise or notification to a Telecare Service Provider)

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C38E5 - ease of use {#Telecarev1.0.1-C38E5-easeofuse}

As a Patient/Service User

I want to have access to Telecare devices that are designed to be easy and intuitive to use

So that I can be confident that I can use the device even if I am in pain or in an emergency

#### Acceptance criterion 1: Intuitive products {#Telecarev1.0.1-Acceptancecriterion1:Intuitiveproducts}

Given a Telecare device has been identified to meet a Patient/Service User's needs

When the Telecare device has been installed

Then the design of the interface means that a Patient/Service User can understand how to trigger an alert without requiring any training or reference to a manual or documentation

#### Acceptance criterion 2: ease of triggering an alert {#Telecarev1.0.1-Acceptancecriterion2:easeoftriggeringanalert}

Given a Telecare device has been installed

When the Patient/Service User experiences an event that means they require assistance (e.g. they have a fall)

Then the alert can be triggered by a single action (e.g. pressing a button, pulling a cord) by the Patient/Service User

And the action is simple (i.e. doesn't require manual dexterity)

---

### C38E6 - Patient/Service Users with sensory impairment(s) {#Telecarev1.0.1-C38E6-Patient/ServiceUserswithsensoryimpairment(s)}

As a Patient/Service User

I want to have access to Telecare devices that are designed for use by Patients/Service Users with one or more sensory impairments

So that I can be confident that I will be aware of device warnings or prompts even if I have a visual, hearing and/or other impairment

#### Acceptance criterion 1: prompt Patient/Service User that device isn't working {#Telecarev1.0.1-Acceptancecriterion1:promptPatient/ServiceUserthatdeviceisn'tworking}

Given a Telecare device has been identified to meet a Patient/Service User's needs

When the device fails to operate normally (e.g. device has been damaged or has no power)

Then the device can prompt the Patient/Service User that it is not operating correctly in a way that accommodates their impairment (e.g. by combined audio/visual alert or vibration)

#### Acceptance criterion 2: warn Patient/Service User of an adverse event {#Telecarev1.0.1-Acceptancecriterion2:warnPatient/ServiceUserofanadverseevent}

Given a Telecare device has been identified to meet a Patient/Service User's needs

When an adverse event occurs (e.g. smoke or a flood is detected)

Then the device can warn the Patient/Service User in a way that accommodates their impairment(s) (e.g. by combined audio/visual alert or vibration)

---

### C38E7 - obtain Management Information (MI) on Telecare {#Telecarev1.0.1-C38E7-obtainManagementInformation(MI)onTelecare}

As a Service Manager

I want to have access to management information relating to the full range of Telecare devices used by Patients/Service Users within an area (e.g. Practice, CCG or STP footprint)

So that I can analyse the Telecare data to understand usage (e.g. number and types of device, frequency of adverse events) and how devices can be best used to deliver benefits to Patients/Service Users

#### Acceptance criterion 1: number and type of devices {#Telecarev1.0.1-Acceptancecriterion1:numberandtypeofdevices}

Given information is available relating to Telecare devices in use in an area

And the user has access to a suitable reporting Solution

When report generation is triggered (e.g. regular reporting cycle such as month end, or receipt of new data)

Then a report can be produced on the usage of Telecare devices

#### Acceptance criterion 2: usage of Telecare devices {#Telecarev1.0.1-Acceptancecriterion2:usageofTelecaredevices}

Given information is available relating to Telecare devices in use in an area

And the user has access to a suitable reporting Solution

When report generation is triggered (e.g. regular reporting cycle such as month end, or receipt of new data)

Then a report can be produced of patterns of use in a defined period

#### Acceptance criterion 3: link to other data {#Telecarev1.0.1-Acceptancecriterion3:linktootherdata}

Given information is available relating to Telecare devices in use in an area

And the user has access to a suitable reporting Solution

And the user has access to other datasets (e.g. clinical data)

When report generation is triggered (e.g. regular reporting cycle such as month end, or receipt of new data)

Then a report can be produced linking use of Telecare devices to other data

---

### C38E8 - enable 2-way communication with Patient/Service User {#Telecarev1.0.1-C38E8-enable2-waycommunicationwithPatient/ServiceUser}

As a Telecare Service Provider

I want to be able to communicate with a Patient/Service User via the Telecare device

So that when an alert is raised, I can quickly identify the nature of the emergency and the best response

#### Acceptance criterion 1: communicate with Patient/Service User {#Telecarev1.0.1-Acceptancecriterion1:communicatewithPatient/ServiceUser}

Given a Telecare device has been installed for a Patient/Service User

And the device supports 2-way communication

When an alert of an adverse event has been received

Then the Telecare device can be used to call or contact the Service User

---

### C38E9 - remote testing of Telecare device {#Telecarev1.0.1-C38E9-remotetestingofTelecaredevice}

As a Telecare Service Provider

I want to be able to test my Telecare devices remotely

So that I can quickly identify any devices that have failed or are working incorrectly without needing to send an engineer or other to the Patient/Service User's home

#### Acceptance criterion 1: test Telecare Device {#Telecarev1.0.1-Acceptancecriterion1:testTelecareDevice}

Given a Telecare device has been installed for a Patient/Service User

When a test of the device is required (e.g. as part of a regular testing cycle or in response to Patient/Service User concern)

Then the device can be tested remotely (i.e. without needing an engineer or other on-site)

And the Provider can understand whether the device is operating correctly or not

And diagnostic information about the device can be sent to the Provider

---

### C38E10 - manual testing of Telecare device {#Telecarev1.0.1-C38E10-manualtestingofTelecaredevice}

As a Telecare Service Provider

I want to be able to manually test my Telecare devices (e.g. that the trigger is working correctly)

So that I can test functionality that can't be tested remotely to identify devices that have failed or are working incorrectly

#### Acceptance criterion 1: test Telecare device {#Telecarev1.0.1-Acceptancecriterion1:testTelecaredevice}

Given a Telecare device has been installed for a Patient/Service User

When a test of the device is required (e.g. as part of a regular testing cycle or in response to Patient/Service User concern)

Then the device can be tested manually (e.g. an alert is triggered)

And the outcome of the test (e.g. whether an alert was triggered or not) can be understood by the Service Provider

---

### C38E11 - sustainability of Telecare device {#Telecarev1.0.1-C38E11-sustainabilityofTelecaredevice}

As a Buyer

I want to know that Telecare devices that I am purchasing are digital-ready

So that I can be confident that the devices can continue to be used after the 2025 digital switch-over

#### Acceptance criterion 1: confirm digital-ready {#Telecarev1.0.1-Acceptancecriterion1:confirmdigital-ready}

Given the needs of a Patient/Service User have been assessed

And the use of one or more Telecare devices has been identified as part of the package of care

When a device is selected for possible use by a Patient/Service User

Then the information on the compatibility of the device with digital-only infrastructure is available (e.g. in the form of a product sheet or other)

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