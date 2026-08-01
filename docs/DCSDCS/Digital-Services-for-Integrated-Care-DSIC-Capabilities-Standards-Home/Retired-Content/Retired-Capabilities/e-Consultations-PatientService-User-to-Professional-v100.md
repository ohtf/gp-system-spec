---
page_id: "1695383694"
space: "DCSDCS"
title: "e-Consultations (Patient/Service User to Professional) v1.0.0"
version: 2
updated: "2020-01-15T16:32:21.513Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1695383694/e-Consultations+Patient+Service+User+to+Professional+v1.0.0"
labels: ["capability_retired"]
---

# e-Consultations (Patient/Service User to Professional) v1.0.0

|  |  |
| --- | --- |
| ID | C28 |
| Version | 1.0.0 |
| Type | Capability |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Description}

The e-Consultations (Patient/Service User to Professional) Capability allows Patients/Service Users to request and receive support relating to their healthcare concerns. They can make requests to the relevant Healthcare Organisation, at a time convenient to them, for support in relation to their healthcare conditions.

Provision of information by the Patient/Service User allows the Health or Care Professional dealing with the request to triage requests effectively and make informed decisions about how best to respond - the response could be information or advice, an offer of a consultation, provision of a repeat prescription, test results, or a referral to other services. This may be enhanced by the ability to link the request, and the response, to the Patient/Service User's record

The Capability may provide the Patient/Service User with instant self-help advice or sign-post them to relevant services, including emergency services. It may also offer Health and Care Professionals facilities to conduct online or video consultations with individuals or groups of Patients/Service Users, reducing the need to travel and the demand on surgery or clinic settings. It also supports the remote delivery of a range of clinical scenarios, including:

- Clinical consultation
- Medication review
- Direct care advice (from a Health or Care Professional)

# Outcomes {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Outcomes}

|  |  |
| --- | --- |
| Patient/Service User | - Able to make healthcare-related requests, at a time convenient to them - Able to provide relevant information, increasing the likelihood of obtaining their desired outcome - Able to self-serve advice and guidance for non-urgent symptoms without the need for a surgery Appointment, including direction to other sources of appropriate care - Able to use video to improve the convenience of consultations with Health and Care Professionals |
| Health or Care Professional | - Able to triage and prioritise requests ensuring the most urgent are responded to quickly and are directed to the most appropriate person or service - Able to make more informed decisions relating to Patient/Service User's requests through access to the Patient/Service User's record and information provided by them |
| Healthcare Organisation | - Able to reduce the manual overhead of receiving, dealing with and responding to requests from Patients/Service Users - Increase Patient/Service User access to advice or consultation by providing access to advice on their health conditions, enabling a greater degree of self-care - Able to use Management Information (MI) about e-Consultations to improve services and access to information |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### EpicEC1 - Patient/Service User requests support {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-EpicEC1-Patient/ServiceUserrequestssupport}

As a Patient/Service User

I want to be able to make a request for support in relation to a healthcare concern

So that I can receive the most appropriate support (e.g. advice or a consultation) from a Healthcare Organisation

#### Acceptance criterion 1: Patient/Service User requests advice or consultation {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion1:Patient/ServiceUserrequestsadviceorconsultation}

Given that Patients/Service Users can request support in respect to a healthcare concern

When a Patient/Service User decides to request support from a Healthcare Organisation

Then a request for support is created

And the Patient/Service can provide information about their request (e.g. their condition, contact information or what they would like to achieve)

And the request can be sent to the Healthcare Organisation

---

### EpicEC2 -  respond to request for support from Patient/Service User {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-EpicEC2-respondtorequestforsupportfromPatient/ServiceUser}

As a Health or Care Professional

I want to be able to review and respond to a request submitted by a Patient/Service User

So that I can respond to their request in the most appropriate way (e.g. refer them to other services, offer advice or a consultation or clinical tests)

#### Acceptance criterion 1: view request for support from Patient/Service User {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion1:viewrequestforsupportfromPatient/ServiceUser}

Given that a request for support in respect to a healthcare concern has been received

When the Health or Care Professional decides to review the request

Then they can view the request for support

And any additional information provided in the request can be viewed (e.g. their condition, contact information or what they would like to achieve)

#### Acceptance criterion 2: respond to Patient/Service User's request for support {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion2:respondtoPatient/ServiceUser'srequestforsupport}

Given that a request for support has been viewed by a Health or Care Professional

When the Health or Care Professional decides to respond to the request

Then a response can be created

And the Health or Care Professional can provide advice or information (e.g. offer a consultation or refer the Patient/Service User to a service) in the response

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### EpicEC3 - Patient/Service User makes administrative request {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-EpicEC3-Patient/ServiceUsermakesadministrativerequest}

As a Healthcare Service Provider

I want Patients/Service Users to be able to make administrative requests (e.g. request repeat prescription, fit note or test results) relating to their health or care needs

So that the overhead of processing these requests is reduced

#### Acceptance criterion 1: Patient makes administrative request {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion1:Patientmakesadministrativerequest}

Given that Patients/Service Users can make administrative requests in relation to their health and care needs

When the Patient/Service User identifies the need for an administrative request

Then an administrative request can be made

And the Patient/Service can provide information about the nature of their request (e.g. request repeat prescription or specific test result)

And the administrative request can be sent to the Healthcare Organisation

#### Acceptance criterion 2: receive administrative request {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion2:receiveadministrativerequest}

Given that Patients/Service Users can make administrative requests in relation to their health and care needs

When a Patient/Service User makes an administrative request

Then the request can be received by the Healthcare Organisation

And a response can be sent to the Patient/Service User

---

### EpicEC4 -  link requests and responses to Patient/Service User Record {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-EpicEC4-linkrequestsandresponsestoPatient/ServiceUserRecord}

As a Health or Care Professional

I want to be able to link requests and responses to the Patient/Service User's record

So that I have a complete record of interactions with the Patient/Service User

#### Acceptance criterion 1: Patient/Service User’s request is linked to their details {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion1:Patient/ServiceUser’srequestislinkedtotheirdetails}

Given that Patients/Service Users can request support in respect to a healthcare concern

When a Patient/Service User decides to request support from a Healthcare Organisation

Then the request can be linked to information about the Patient/Service User that is held by the Healthcare Organisation

And the request can be viewed as part of the information about the Patient/Service User held by the Healthcare Organisation

#### Acceptance criterion 2: Health or Care Professional’s response is linked to Patient/Service User’s details {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion2:HealthorCareProfessional’sresponseislinkedtoPatient/ServiceUser’sdetails}

Given that a Patient/Service User has requested support in relation to a healthcare concern

When the Health or Care Professional provides a response

Then the response can be linked to the original request from the Patient/Service User

And the response can be viewed as part of the information about the Patient/Service User held by the Healthcare Organisation

---

### EpicEC5 - self-help and signposting {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-EpicEC5-self-helpandsignposting}

As a Health or Care Professional

I want to enable Patients/Service Users to access information relating to their healthcare condition(s)

So that they can self-care through provision of relevant information or sign-posting to relevant services

#### Acceptance criterion 1: Patient/Service User views information relating to their healthcare condition {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion1:Patient/ServiceUserviewsinformationrelatingtotheirhealthcarecondition}

Given that the Patient has concerns in respect to a healthcare condition

When they request information relating to their healthcare condition

Then they can view information relating to their condition (e.g. videos, self-help guides)

#### Acceptance criterion 2: Patient/Service User is sign-posted to services {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion2:Patient/ServiceUserissign-postedtoservices}

Given that the Patient has concerns in respect to a healthcare condition

When they request information on services that are relevant to their healthcare condition

Then they can view information on relevant services (e.g. NHS111, NHS Choices)

---

### EpicEC6 - Live Consultation: Patient/Service User and Health and Care Professionals {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-EpicEC6-LiveConsultation:Patient/ServiceUserandHealthandCareProfessionals}

As a Health or Care Professional

I want to be able to conduct a live consultation with a Patient/Service User who is in another location

So that I can provide healthcare support to the Patient/Service User when face to face consultation is not feasible

#### Acceptance criterion 1: Patient/Service User has a consultation with a Health or Care Professional {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion1:Patient/ServiceUserhasaconsultationwithaHealthorCareProfessional}

Given that a facility to support live consultations is available

When a Health or Care Professional requests a live consultation with a Patient/Service User

Then a live consultation can be conducted between the Patient/Service User and the Health or Care Professional

And the consultation can be recorded

And the recording can be linked to information about the Patient/Service User that is held by the Healthcare Organisation

---

### EpicEC7 - group e-Consultations {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-EpicEC7-groupe-Consultations}

As a Health and Care Professional

I want to be able to conduct group e-Consultations

So that I can provide support to a group of Patients/Service Users in the most convenient and cost effective way

#### Acceptance criterion 1: Health and Care Professional conducts group e-Consultation {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion1:HealthandCareProfessionalconductsgroupe-Consultation}

Given that there are Patients/Service Users who participate in group Consultations

When the need for a group consultation is identified (e.g. related to a condition or an educational session)

Then a group e-Consultation session can be set up

And the relevant Patients/Service Users can participate in the group e-Consultation

---

### EpicEC8 - reports {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-EpicEC8-reports}

As a Manager

I want to have access to custom reports relating to e-Consultations

So that I can make informed decisions

#### Acceptance criterion 1: report on use of e-Consultations {#e-Consultations(Patient/ServiceUsertoProfessional)v1.0.0-Acceptancecriterion1:reportonuseofe-Consultations}

Given that Patients/Service Users can make healthcare-related requests via the e-Consultations solution

And information on the use of e-Consultations is available

When the Manager wants to report on use of e-Consultations

Then a report can be run to create output relating to the use of e-Consultations

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