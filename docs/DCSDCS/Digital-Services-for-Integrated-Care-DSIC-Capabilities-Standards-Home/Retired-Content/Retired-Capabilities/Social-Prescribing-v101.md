---
page_id: "12817825794"
space: "DCSDCS"
title: "Social Prescribing v1.0.1"
version: 4
updated: "2024-03-07T11:03:18.242Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12817825794/Social+Prescribing+v1.0.1"
labels: ["capability_retired"]
---

# Social Prescribing v1.0.1

|  |  |
| --- | --- |
| ID | C37 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description

Social prescribing focuses on a Patient/Service User's needs in a holistic way, and helps to address the social, practical and emotional needs of Patients that can't (wholly) be addressed medically such as social isolation, reduced mobility, mental health issues or some long-term conditions.

Social prescribing provides the ability for Health and Care Professionals to refer a Patient/Service User - or for the Patient/Service User to self-refer - to one or more non-clinical interventions or services. This encompasses a wide variety of services such as activity groups (e.g. walking clubs), peer support groups, volunteer support, or information and guidance services, typically provided by Third Sector Organisations.

Models vary but in many cases, there is a Link Worker (also known as a Support Broker, Community Navigator or Champion) based in the Practice, Healthcare Organisation or in a Connector Scheme who works with Patients/Service Users to assess their needs and identify relevant services.

The Social Prescribing Capability is about the provision of integrated systems or Solutions that allow referral (the aspiration is electronically) of Patients/Service Users to Providers of appropriate and relevant interventions or services.

The Capability allows national and local directories of services to be accessed and allows providers offering such services within a locality to make these available via the Capability. The Patient/Service User or Health or Care Professional then chooses from the directory of locally available services and generates a referral. Subject to appropriate consent, a Patient/Service User's details can be passed to the Organisation delivering the service and data relating to social prescribing referrals can then be maintained as part of the Patient/Service User's clinical record (the aspiration is through integrated systems). 

# Outcomes

|  |  |
| --- | --- |
| Patient/Service User | - Improved well-being through increased levels of social contact and social support - Empowered to take responsibility for what will get them and keep them well - Have easier access, including the ability to self-refer, to a wide range of services and activities to support their care / treatment - Problems are considered from a 'whole person' perspective resulting in the Patient/Service User's wider practical, social or emotional needs being considered |
| Health or Care Professional | - Greater satisfaction from having the ability to treat problems that can't be addressed (wholly) through clinical / medical routes - May see a reduction in demand for:   - GP Appointments   - use of NHS services such as A&E   - prescriptions issued |
| Managers and Commissioners | - Can understand the usage and effectiveness of Social Prescribing through access to relevant management information (MI) |
| Voluntary / Community Sector or other Service providers | - Can publicise services they offer - Able to maintain information about their services via the Solution, including who the service is most relevant to - May experience increased uptake of arts, leisure, education, volunteering, sporting and other activities - Could analyse the value and take up of services to aid decision making on discontinuing/continuing services |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C37E1 - assess wellness or well-being of the Patient or Service User

As a Link Worker or other Health or Care Professional (GP, Nurse or other)

I want to be able to assess the wellness of a Patient/Service User using a methodology appropriate to the Patient/Service User's condition or circumstances

So that I can understand and record their non-clinical healthcare needs

#### Acceptance criterion 1: initial well-being assessment is captured

Given that a Patient/Service User has been referred

And the need for a well-being assessment has been identified

When the Link Worker (or other) undertakes a wellness assessment using a methodology appropriate to the Patient/Service User's condition, circumstances and / or need (e.g. Short Warwick-Edinburgh Mental Well-being Scale (SWEMWBS) or Wellbeing Star)

Then the outcome of the assessment can be recorded on the Patient/Service User's Social Prescribing record

#### Acceptance criterion 2: subsequent well-being assessments are captured

Given a Patient/Service User has been assigned a series of sessions or engagements with the service provider(s)

And the Patient/Service User and Link Worker (or other) have agreed to meet at regular intervals

When the wellness assessment is repeated

Then the outcome of second and subsequent assessments can be recorded on the Patient/Service User's Social Prescribing record

---

### C37E2 - search the directory

As a Link Worker, Health or Care Professional or other member of the Practice/Healthcare Organisation team

I want to be able to search the Directory of non-clinical services and interventions (e.g. support groups, sporting activities, information or guidance services, etc.)

So that I can identify the services that are most relevant to a Patient/Service User's needs

#### Acceptance criterion 1: directory search returns services that match criteria

Given that a directory of services has been created in the Social Prescribing Solution

And criteria have been defined for each service (e.g. age or gender restrictions of use or relevance to conditions)

And the search criteria (e.g. specifying the age / gender of the Patient/Service User, their condition, geographic location or mobility status) have been defined

When a search is run against the directory

Then the list of services that match the search criteria are displayed

---

### C37E3 - refer Patient/Service User to service(s)

As a Link Worker, Health or Care Professional or other member of the Practice/Healthcare Organisation team

I want to be able to refer a Patient/Service User to one or more non-clinical services

So that they can receive the most appropriate support for their non-clinical needs

#### Acceptance criterion 1: Patient/Service User is referred to a service

Given the Patient/Service User's needs have been understood

When one or more possible services have been identified matching their needs

Then the relevant service(s) can be selected

And a referral for each service for the relevant service provider can be created

---

### C37E4 - maintain referral record

As a Link Worker or Health or Care Professional

I want to be able to maintain a record of assessments and referrals, including information about each referral (e.g. attendance, outcomes), for a Patient/Service User

So that G.P.s, Nurses and other Health and Care Professionals can understand the Patient/Service User's wider healthcare issues and needs

#### Acceptance criterion 1: Patient/Service User's attendance is captured

Given a Patient/Service User has been referred to a service

When information is received relating to the Patient/Service User's attendance (electronically or via a manual route such as telephoning the service provider)

Then the Patient/Service User's record can be updated

And their attendance or non-attendance can be recorded

And this information is available to those other Health and Care Professionals (e.g. GPs, Nurses) with appropriate access to the record

#### Acceptance criterion 2: Patient/Service User's outcomes are captured

Given a Patient/Service User has been referred to a service

And has attended some or all the referred sessions

When information relating to the Patient/Service User's outcomes is received in relation to using the service, electronically or via manual route (such as telephoning the service provider)

Then the Patient/Service User's record can be updated

And their outcomes recorded

And this information is available to those other Health and Care Professionals (e.g. GPs, Nurses) with appropriate access to the record

---

### C37E5 - link to national or local directory of services

As a Link Worker or Administrator

I want the Social Prescribing Solution to be able to link to or make use of national or local directories of services

So that the directory includes a broader range of available and relevant services with the minimum maintenance overhead for my Practice/Healthcare Organisation

#### Acceptance criterion 1: link to national directory of services

Given that national directories of services (e.g. e-Referral Service or 111) are available

When one or more national directories of relevance are identified

Then the national directory (or directories) can be linked to or accessed via the Social Prescribing Solution

And the national directory can be searched

#### Acceptance criterion 2: link to local directory of services

Given that local directories of services (e.g. the Leeds Directory) are available

When one or more local directories of relevance are identified

Then the local directory (or directories) can be linked to or accessed via the Social Prescribing Solution

And the local directory can be searched

---

### C37E6 - maintain directory of services

As a Link Worker or Service Administrator

I want to be able to manually maintain (add, update or delete) the directory of services

So that the directory is always up to date and reflects the full range of services available

#### Acceptance criterion 1: new service is added to the directory

Given that a directory of services has been created in the Social Prescribing Solution

When a new service is identified that does not appear in any linked local or national directories

Then details of this new service can be manually added to the directory

#### Acceptance criterion 2: existing service is updated in the directory

Given that one or more services have been created manually in the Social Prescribing Solution

When the details relating to a service change

Then the details of the service can be updated in the directory

#### Acceptance criterion 3: existing service is withdrawn or no longer available

Given that a directory of services has been created in the Social Prescribing Solution

And details of the service exist in the directory

When a service is withdrawn (closes or is no longer available for referrals)

Then the details of the service can be updated such that it doesn't appear in searches

And Patients / Service Users can no longer be referred to the service

---

### C37E7 - maintain service criteria

As a Link Worker or Service Administrator

I want to maintain (add, update or remove) information about services (such as any restrictions on usage or fit with Patients' conditions or circumstances)

So that the directory is always up to date and reflects the services available

#### Acceptance criterion 1: Restrictions on usage are applied to a service

Given that a directory of services has been created in the Social Prescribing Solution

When restrictions on or criteria for usage of a service are identified (e.g. minimum or maximum age of Patient/Service User or their gender)

Then information about the service can be updated

And the service will only be returned in searches that specify matching service restrictions (including no service restrictions specified)

#### Acceptance criterion 2: Relevance of service to Patient/Service User's circumstances or conditions is captured

Given that a directory of services has been created in the Social Prescribing Solution

When a service is identified as being relevant for Patient/Service Users with circumstances (e.g. they are a carer) or with conditions (e.g. dementia, depression)

Then information about the service can be updated

And the service will only be returned in searches specifying matching conditions or circumstances (including no conditions / circumstances specified)

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of unsafe-On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C37E8 - refer Patient/Service User to Link Worker

As a Health or Care Professional

I want to refer a Patient, who has highlighted a healthcare issue to a Social Prescribing Link Worker (may also be known as a Support Broker, Community Navigator, Champion, Well-being Co-ordinator or other term), based in the Healthcare Organisation (e.g. the Practice) or a Connector Scheme

So that the Link Worker can contact and assess the Patient/Service User

#### Acceptance criterion 1: New referral to Link Worker is created

Given the Healthcare Organisation offers a Social Prescribing Capability

And has a Link Worker based either in the Practice, Healthcare Organisation or in a Connector Scheme

When a healthcare issue is highlighted by a Patient/Service User

Then a referral for the Patient/Service User to the Link Worker can be generated

#### Acceptance criterion 2: Link Worker is notified of new referral

Given that a healthcare need has been identified for a Patient/Service User

And there is a Link Worker based either in the Practice, Healthcare Organisation or in a Connector Scheme

When a referral to the Link Worker is generated

Then the Link Worker is notified (by email, a task in a workflow or other means) that a new referral has been made

And the Link Worker can identify the relevant Patient/Service User in order to initiate contact

---

### C37E9 - capture Patient/Service User consent

As a Link Worker, Health or Care Professional or other member of the Practice/Healthcare Organisation

I want to be able to capture Patient/Service User consent

So that I have a record of their wishes with respect to receiving non-clinical treatment and the sharing of their data

#### Acceptance criterion 1: Patient consent is captured

Given an appropriate service referral has been identified

When the Patient/Service User consents to being referred to the service provider

Then consent to non-clinical treatment can be captured or recorded on the Patient/Service User's record

And consent to share their data can be captured or recorded on the Patient/Service User's record

#### Acceptance criterion 2: Patient consent to non-clinical treatment is not obtained

Given an appropriate service referral has been identified

When the Patient/Service User refuses consent to non-clinical treatment by the service provider

Then lack of consent to non-clinical treatment can be captured or recorded on the Patient/Service User's record

#### Acceptance criterion 3: Patient consent is not obtained for information sharing

Given an appropriate service referral has been identified

When the Patient/Service User does not agree to the sharing of their data with the service provider

Then lack of consent to share data can be captured or recorded on the Patient/Service User's record

### C37E10 - Patient self-referral

As a Patient/Service User

I want to be able to self-refer to services

So that I can quickly access support services relevant to my needs or condition

#### Acceptance criterion 1: Patient/Service User searches the directory of services

Given that a Patient/Service User has identified a healthcare need that can wholly or partially be met by a non-clinical treatment

And a directory of services has been created in the Social Prescribing Solution

And the directory is available to Patients/Service Users

And the Patient/Service User has the correct access enabling self-referral

When the Patient/Service User searches the directory for services (using an open search or specifying their condition or circumstances)

Then a list of services is displayed

And the Patient/Service User can select one or more services to which they want to self-refer

And a referral form for each service for the relevant service provider can be created

And the Patient/Service User can be referred to the service provider(s) automatically (for integrated systems) or manually (via letter, phone, email, web form, etc.)

---

### C37E11 - integrate Social Prescribing Referral Record with Clinical Record

As a GP, Nurse or other Health or Care Professional

I want to be able to view a Patient/Service User's assessments and referrals as part of their clinical record

So that I can understand a Patient/Service User's healthcare issues and interactions with services in a more holistic way

#### Acceptance criterion 1: View social prescribing activities as part of clinical record

Given that the Social Prescribing Solution has been linked or integrated with the Clinical System

And a consultation or other interaction has been held between the Patient/Service User and their Link Worker or other Health or Care Professional

When updates are made to the Patient/Service User's Social Prescribing record (e.g. consultation notes, wellness assessment undertaken, referral to service, outcome of referral)

Then the updates are incorporated into the clinical record of the Patient/Service User

And can be viewed on the timeline for the Patient/Service User as part of the consultation history

---

### C37E12 - receive notification of an Appointment

As a Link Worker

I want notifications relating to Appointments to be generated automatically and sent to defined recipients (e.g. the Patient/Service User and their Practice) by their preferred method (e.g. letter, email, Short Message Service (SMS))

So that they are aware of Appointments and any changes and can act on this information (e.g. make arrangements to attend, update records)

#### Acceptance criterion 1: Patient/Service User receives notification

Given that a Patient/Service User has been referred to a service

And their preferred method of communication (e.g. letter, email, SMS) has been captured

And the relevant contact details are recorded

When an Appointment is booked, amended or cancelled

Then the Patient/Service User receives a notification via their preferred method with the details of the booking, amendment or cancellation

#### Acceptance criterion 2: Patient/Service User's Practice receives notification

Given that a Patient/Service User has been referred to a service

And the preferred method of communication (e.g. letter, email, SMS) has been captured

And the relevant contact details are recorded

When an Appointment is booked, amended or cancelled

Then the Patient/Service User's Organisation receives a notification via the preferred method with the details of the booking, amendment or cancellation

---

### C37E13 - remind Patients/Service Users of Appointments

As a Link Worker

I want to be able to issue reminders about Appointments to a Patient/Service User by their preferred method (e.g. letter, email, SMS)

So that the likelihood of them attending is increased

#### Acceptance criterion 1: Patient/Service User receives reminder

Given that a Patient/Service User has an Appointment with a Social Prescribing service

And their preferred method of communication (e.g. letter, email, SMS) has been captured

And the relevant contact details are recorded

And rules relating to reminders have been defined (e.g. how far in advance of the Appointment reminders are sent)

When the trigger point for an Appointment is reached

Then the Patient/Service User receives a reminder of the Appointment via their preferred method of communication

---

### C37E14 - provide service feedback

As a Patient/Service User

I want to be to provide feedback on non-clinical services

So that I can share my experiences (e.g. experience of booking, effectiveness of the service) with other Patients/Service Users, Link Workers and other Health and Care Professionals

#### Acceptance criterion 1: Patient/Service User creates feedback

Given that a Patient/Service User has been referred to a service

And the Patient/Service User has access to the Social Prescribing Solution

When the Patient/Service User has engaged (or attempted to engage) with the service provider

Then the Patient/Service User can create feedback on the service

And the feedback is associated with the service

And the feedback can be viewed by other users of the Social Prescribing Solution

#### Acceptance criterion 2: Link Worker, Administrator or other creates feedback on behalf of the Patient/Service User

Given that a Patient/Service User has been referred to a service

When the Patient/Service User provides feedback on the service to the Link Worker or other team member

Then the Link Worker or other team member can create feedback on the service on their behalf

And the feedback is associated with the service

And the feedback can be viewed by other users of the Social Prescribing Solution

#### Acceptance criterion 3: Patient/Service User provides feedback anonymously

Given that a Patient/Service User has been referred to a service

When the Patient/Service User decides to provide anonymous feedback

Then the Patient/Service User can create feedback on the service using a guest or other anonymous account

And the feedback is associated with the service

And the feedback can be viewed by other users of the Social Prescribing Solution

#### Acceptance criterion 4: feedback is moderated

Given that an individual has been identified as a moderator for service-related feedback

And feedback has been created for a service

When feedback is identified as being unfair or inappropriate

Then the moderator can moderate (remove or hide) the feedback

And the feedback can no longer be viewed by other users of the Social Prescribing Solution

---

### C37E15 - view service feedback

As a Patient/Service User or Link Worker

I want to be able to see feedback on non-clinical services used by Patients/Service Users

So that I can select services that have been most effective for Patients/Service Users with similar circumstances or conditions

#### Acceptance criterion 1: Patient/Service User views feedback

Given that a Patient/Service User has identified a service that might meet their health or well-being needs

And the Patient/Service User has access to the Social Prescribing Solution

And feedback has been captured in relation to the service

When the Patient/Service User views the details of the service

Then the Patient/Service User can also view any feedback recorded against the service

---

### C37E16 - Obtain Management Information (MI) on Social Prescribing

As a Manager or Commissioner

I want to have access to management information relating to Social Prescribing

So that I can analyse the Social Prescribing data to understand usage (e.g. volume of referrals, number of Patients completing an intervention) and outcomes

#### Acceptance criterion 1: understand usage of Social Prescribing

Given that information relating to Social Prescribing has been created within the relevant Solution

And the user has access to the data

And the user has access to a reporting Solution

When a new reporting need is identified

Then a report can be designed to create output relating to the use of Social Prescribing

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