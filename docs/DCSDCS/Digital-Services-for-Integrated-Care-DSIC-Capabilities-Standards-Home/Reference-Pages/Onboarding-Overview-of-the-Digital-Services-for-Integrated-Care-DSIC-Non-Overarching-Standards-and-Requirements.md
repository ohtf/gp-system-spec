---
page_id: "11973558273"
space: "DCSDCS"
title: "Onboarding Overview of the Digital Services for Integrated Care (DSIC) Non-Overarching Standards and Requirements"
version: 16
updated: "2026-07-24T16:05:41.016Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11973558273/Onboarding+Overview+of+the+Digital+Services+for+Integrated+Care+DSIC+Non-Overarching+Standards+and+Requirements"
labels: ["reference_page"]
---

# Onboarding Overview of the Digital Services for Integrated Care (DSIC) Non-Overarching Standards and Requirements

|  |  |
| --- | --- |
| ID {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-ID} | R9 |
| Version {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-Version} | 2.6.0 |
| Type {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-Type} | Reference |

# Introduction {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-Introduction}

Suppliers must complete Digital Services for Integrated Care (DSIC) onboarding to get their Solution listed on the NHS Buying Catalogue. The DSIC onboarding process can sometimes be quite long, so it's worth planning well ahead.

The integrations relating to the Non-Overarching Standards each have their own specific onboarding processes.

This page provides an overview of the onboarding for the various Digital Services for Integrated Care (DSIC) Non-Overarching Standards. The guidance assumes that Suppliers are within the DSIC onboarding process and have been allocated a Supplier Manager. If you have not entered the DSIC onboarding process or have not been allocated a Supplier Manager, then please reach out to your key point of contact who should be able to assist.

This page does not describe the complete onboarding journey for DSIC Contracting Vehicles, that will be detailed elsewhere.

![Onboarding TIF via SCAL DOS etc (2) (6) (2)-20260713-095322.png](https://nhse-dsic.atlassian.net/wiki/download/attachments/11973558273/Onboarding%20TIF%20via%20SCAL%20DOS%20etc%20(2)%20(6)%20(2)-20260713-095322.png?api=v2)

# Onboarding / Assurance Processes {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-Onboarding/AssuranceProcesses}

## Supplier Conformance Assessment List (SCAL) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-SupplierConformanceAssessmentList(SCAL)}

Supplier Conformance Assessment List (SCAL) is the checklist and record of both organisational and technical/product compliance. It is used by onboarding teams to capture declarations from connecting parties (CP) on adherence to healthcare system development standards, statements on risk management practices, and evidence of functional and non-functional assurance e.g, test reports. There are currently 2 forms of SCAL in use:

- SCAL - Digital Onboarding Service
- SCAL - Excel Worksheets

The SCAL can be broken down into two main sections:

1. Baseline assurance, a set of assurance questions asked for all integrations, that have been defined as appropriate for all services/APIs. The baseline questions can be broken down further into

   1. Questions that only need to be asked on the first occasion of onboarding (e.g. what is your Organisation Data Service (ODS) code).
   2. Questions that need to be asked on every occasion of onboarding (e.g. has appropriate penetration testing been undertaken for this integration).
2. Service/API specific assurance; assurance set by the specific service/API team SMEs, including questions to support the specific service requirements. These questions may require the partner to provide evidence to support their response and may, where applicable, require witness testing. The SCAL allows additional risk controls to be cross-referenced or indexed e.g. additional clinical testing or Deployment Verification Period (DVP).

## Tailored Assurance {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-TailoredAssurance}

A Tailored Assurance approach will be taken when the SCAL is not considered to be the most effective or efficient method for onboarding a service provider to a service or API. It defines the assurance approach with a focus on the activities to assure technical and clinical risks associated to integrating with that service or API. It is often further underpinned by the assurance executed as part of the Overarching Standards work.

## Interoperability Toolkit (ITK) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-InteroperabilityToolkit(ITK)}

The Interoperability Toolkit (ITK) conformance process is designed to be straightforward, focusing on demonstrating conformance to relevant technical specifications and standards.

Further information on ITK is available at the following URL: <https://digital.nhs.uk/services/interoperability-toolkit>

## External Assurance {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-ExternalAssurance}

Assurance of these Interoperability Requirements are managed and executed outside of NHS England e.g. MHRA Yellow Card Reporting.

## Not Directly Onboarded {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NotDirectlyOnboarded}

These interoperability requirements have no direct onboarding / assurance approach.

# Assurance Approaches / Toolkit {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-AssuranceApproaches/Toolkit}

Each of the Non-Overarching Standards below will have a defined assurance approach or toolkit for achieving compliance with each specification. As these are used beyond Digital Services for Integrated Care (DSIC) then they cannot be held centrally, therefore the Digital Services for Integrated Care (DSIC) Supplier is advised to speak to the nominated point of contact listed for each standard to ensure that they have been sent the latest version of the approach or toolkit.

# Non-Overarching Standards {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-Non-OverarchingStandards}

## [111](../DSIC-Standards/Non-Overarching-Standards/111.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-111}

NHS 111 is a free 24/7/365 call centre service for Patients with urgent medical concerns.  The service is provisioned on a regional basis and run by several different organisations nationally.

111 call handling services use specific software systems that are outside the scope of the Digital Services for Integrated Care (DSIC).

A call to 111 may result in an ambulance call out, or a referral to one of several care settings:

- a local emergency department
- an Out of Hours (OOH) service
- the Patient's registered GP

For GP Solutions, patient encounters with 111 will result in a 111 report message (Post Event Message) being sent to the Patient's GP Practice.  If the patient is referred back to their GP then the referral will additionally trigger a 111 referral message (also known as a Transfer of Care) to the GP Practice.

For Community Pharmacy Solutions, patient encounters with 111 leading to pharmacy referral will result in the trigger of a 111 referral message (also known as a Transfer of Care) to the Community Pharmacy Solution.

111 PEM messaging is assured via tailored assurance incorporating Interoperability Toolkit (ITK3) and end to end clinical assurance. An adapter has been developed and assured by NHS England, using the adaptor means that the Supplier does not need to undertake ITK3 assurance\*

A Digital Services for Integrated Care (DSIC) Service Provider who chooses not to use the adapter must undertake ITK3 accreditation themselves.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on integrating with 111 PEM can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/nhs-111>

\*Further ITK (ITK2) and local assurance may be required where older standards have been defined and are being used at a local level. Suppliers will need to speak to their customers to understand the requirements.

---

## [NHS CIS2 Authentication](../DSIC-Standards/Non-Overarching-Standards/Authentication-and-Access.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NHSCIS2Authentication}

Use this integration to access Care Identity Service (CIS) - the national service for verifying the identity of healthcare workers in England, such as NHS staff, when they access national clinical information systems. You can also get basic profile information about these end users.

You can authenticate the healthcare workers using a range of authenticators, including:

- smartcards
- Windows Hello
- passkeys
- security keys, including YubiKeys
- iPads
- Microsoft Authenticator
- <http://NHS.net> Connect

Digital Services for Integrated Care (DSIC) Providers will be onboarded via the Digital Onboarding Service.

Key programme and assurance contact is via [iamplatforms@nhs.net](mailto:iamplatforms@nhs.net)

Further information on integrating and onboarding can be found at <https://digital.nhs.uk/services/care-identity-service/applications-and-services/cis2-authentication>

---

## [Booking and Referral Standard (BaRS)](../DSIC-Standards/Non-Overarching-Standards/Booking-and-Referral-Standard-BaRS.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-BookingandReferralStandard(BaRS)}

The Booking and Referral Standard (BaRS) is a Non-Overarching Standard that enables digital Patient journeys or operational processes for Patients, healthcare workers and carers. It allows relevant information to be shared quickly, safely and in a format that is useful. It will eventually be available in all care settings.

Digital Services for Integrated Care (DSIC) Providers will be onboarded via the Digital Onboarding Service.

Key programme and assurance contact is via [Bookingandreferralstandard@nhs.net](mailto:Bookingandreferralstandard@nhs.net)

Further information on integrating and onboarding can be found at <https://digital.nhs.uk/developer/api-catalogue/booking-and-referral-fhir/onboarding-support-information>

---

## [Clinical Document Architecture (CDA)](../DSIC-Standards/Non-Overarching-Standards/Clinical-Document-Architecture-CDA.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-ClinicalDocumentArchitecture(CDA)}

CDA is an XML-based HL7 standard for exchange of clinical information.

The only mandated use of CDA in general practice IT is receipt of [111](#) CDA referrals and reports.  However many localities have implemented solutions to ingest external documents in various formats including CDA.  For this reason Suppliers may consider implementing CDA handling functionality for other use cases and payloads.

CDA is assured alongside 111 PEM (including ITK).

Any assurance activities are carried out alongside 111 so engagement for CDA will be made at the same time as engagement for 111.

Further information on integrating with CDA can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/nhs-111>

---

## [Digital Diagnostics and Pathology Messaging](../DSIC-Standards/Non-Overarching-Standards/Digital-Diagnostics-Pathology-Messaging.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-DigitalDiagnosticsandPathologyMessaging}

Digital Diagnostics and Pathology Messaging supports the electronic transmission of results of pathology tests to GP Solutions in response to a test request placed with laboratories

Pathology messages are sent and received via MESH.

NHS England have also developed and assured an adapter to support Pathology messaging.

Digital Services for Integrated Care (DSIC) Suppliers may use the adapter or alternatively develop their own (which will require additional assurance).

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on integrating with the Pathology Edifact API can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/pathology-messaging-edifact>

---

## [Directory of Services (DoS) - Urgent and Emergency Care](../DSIC-Standards/Non-Overarching-Standards/Directory-of-Services-DoS-Urgent-and-Emergency-Care.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-DirectoryofServices(DoS)-UrgentandEmergencyCare}

The urgent and emergency care Directory of Services (DoS) is a database of NHS services in England. It works with NHS Pathways, the decision support system behind 111 and some 999 providers, to provide real-time information for Patients about the right place to go.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on the DoS Urgent and Emergency Care REST API can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/directory-of-services-urgent-and-emergency-care-rest>

---

## [e-Referral Service (eRS) FHIR API - Primary Care Referrer](../DSIC-Standards/Non-Overarching-Standards/e-Referrals-Service-e-RS.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-e-ReferralService(eRS)FHIRAPI-PrimaryCareReferrer}

The e-RS is a digital platform that provides an easy way for referrers and service providers to manage their Patients’ journeys. Users can:

- create referrals for Patients
- book appointments or select services for triage
- change or cancel appointments
- have advice conversations with other users
- add to and select from the Directory of Services (DOS)
- download and create reports and extracts

It's designed to help professionals make more informed choices and manage referrals end-to-end.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a SCAL (Excel).

Assurance key contact for the eRS programme is via the mailbox [ersapi.assurance@nhs.net](mailto:ersapi.assurance@nhs.net)

Further information on integrating and onboarding with the eRS FHIR API can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/e-referral-service-fhir#overview--onboarding>

---

## [Electronic Prescription Service (EPS) - Prescribing](../DSIC-Standards/Non-Overarching-Standards/Electronic-Prescription-Service-EPS-Prescribing.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-ElectronicPrescriptionService(EPS)-Prescribing}

Digital Services for Integrated Care (DSIC) Suppliers can access the Electronic Prescription Service (EPS) - the national service used to allow prescribers (like those using GP Solutions) to send Prescriptions electronically to a dispenser (such as a Pharmacy) of the Patient's choice. Health or Care Professionals can prepare a prescription for signing, create a prescription or cancel a prescription.

EPS Subsequent Cancellation Response messages are received via MESH.

All integrations with the EPS FHIR API will be onboarded via a SCAL (Excel).

Assurance key contact for EPS will be allocated and engaged via the programme onboarding team [epsonboarding@nhs.net](mailto:england.epsonboarding@nhs.net)

More information on integrating with the EPS FHIR API can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/electronic-prescription-service-fhir>

### Digital Signature Service API (DSS) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-DigitalSignatureServiceAPI(DSS)}

EPS utilises the Digital Signature Service API (DSS)

The DSS has been developed to take away the complexity of Suppliers having to develop their own signing solution, it also allows changes to be managed centrally e.g. hashing algorithms. The first use case for the DSS is with the EPS FHIR API.

Assurance key contact for DSS will be allocated and engaged via the EPS programme onboarding team [epsonboarding@nhs.net](mailto:england.epsonboarding@nhs.net)

More information on integrating with the DSS can be found at the following URL:

<https://digital.nhs.uk/developer/api-catalogue/digital-signature-service>

---

## [Electronic Yellow Card Reporting](../DSIC-Standards/Non-Overarching-Standards/Electronic-Yellow-Card-Reporting.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-ElectronicYellowCardReporting}

The Medicines and Healthcare products Regulatory Agency (MHRA) collects reports of suspected adverse drug reactions (ADRs) via the [Yellow Card Scheme](https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fyellowcard.mhra.gov.uk%2Finformation&data=05%7C02%7Crobyn.brooke1%40nhs.net%7C815824d8d9aa4a14873008dca735e972%7C37c354b285b047f5b22207b48d774ee3%7C0%7C0%7C638569097192849398%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=XjiG9YJ81UP5%2FI4tl%2BvwzJmne2Qs21BE94yBBDLbly8%3D&reserved=0). These provide a source of information on potential drug safety issues allowing the agency to take regulatory action to protect public health. Healthcare professionals report ADRs either by completing a paper form or a form on an external website/App.

Electronic Yellow Card Reporting is onboarded via an external organisation (MHRA).

Assurance key contact for Digital Services for Integrated Care (DSIC) is via the MHRA mailbox [pharmacovigilance@mhra.gov.uk](mailto:pharmacovigilance@mhra.gov.uk)

---

## [Email](../DSIC-Standards/Non-Overarching-Standards/Email.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-Email}

There are two ways to meet the secure email standard. Organisations must select one of these methods to comply.

1. Implement an already compliant service such as [NHS.net Connect](https://digital.nhs.uk/services/nhs.net-connect) (formerly NHSmail), Office 365 or Google Workspace for all staff at your organisation.
2. Demonstrate your own service is compliant with the secure email standard by following the secure email accreditation process.

Further information on The Secure email Standard can be found at the following URL: <https://digital.nhs.uk/services/nhs.net-connect/the-secure-email-standard>

---

## [eMED3 (Fit Notes)](../DSIC-Standards/Non-Overarching-Standards/eMED3-Fit-Notes.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-eMED3(FitNotes)}

The Statement of Fitness for Work (known as a Med 3 form or ‘fit note’) is used throughout Great Britain. Fit notes are issued by doctors, usually GPs, for Statutory Sick Pay or Social Security purposes. As a part of a medical consultation, a GP may assess a Patient’s medical condition to determine their fitness for work.  The fit note provides return to work advice for the Patient and their employer and can also be used to support a claim to health-related benefits.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a SCAL (Excel).

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

---

## External Interface Specification {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-ExternalInterfaceSpecification}

Integration utilising the External Interface Specification is now deprecated.

---

## [General Practice Appointments Data Reporting (GPAD)](../DSIC-Standards/Non-Overarching-Standards/General-Practice-Appointments-Data-Reporting.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GeneralPracticeAppointmentsDataReporting(GPAD)}

General Practice Appointments Data Reporting (GPAD) supports the collection and submission by Suppliers to the NHS of Appointment data to support capacity planning and management.

GPAD files are sent to NHS via the Secure Electronic File Transfer (SEFT) service.

GPAD is assured via tailored assurance incorporating a number of deliverables including Traceability Matrix, Risk Log and extract assurance.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

---

## [Generic FHIR Receiver](../DSIC-Standards/Non-Overarching-Standards/Generic-FHIR-Receiver.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GenericFHIRReceiver}

The Generic FHIR Receiver is a component which will receive messages into GP Practice Solutions which are:

- Delivered using MESH
- Structured using FHIR STU3 messages.
- Which meet the ITK3 specification.

The Generic FHIR Receiver will obtain messages from the MESH Client or API depending on the Workflow ID within the MESH message header.

Various types of messages are received into GP Practices via MESH; some other component (referred to in the documentation as a Message Distributor) will usually handle all the incoming messages for the Practice MESH "mailbox", and distribute them to the appropriate handler for processing according to a workflow identifier and/or other metadata in the MESH header. The Generic FHIR Receiver will, therefore, receive its messages from this Message Distributor.

In summary, the responsibilities of the Generic FHIR Receiver are:

- Receive incoming ITK3 FHIR messages.
- Verify the message is a well-formed XML.
- Verify the message is a valid FHIR message conforming to the ITK3 specification.
- Match the message subject to a known Patient.
- Send Infrastructure and Business Acknowledgement messages (which are also FHIR messages which conform to the ITK3 specification) where these have been requested.
- Raise workflow tasks as appropriate using the data in the payload.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

---

## [GP2GP (including GP2GP Sending Adaptor/GP2GP Requesting Adaptor)](../DSIC-Standards/Non-Overarching-Standards/GP2GP.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GP2GP(includingGP2GPSendingAdaptor/GP2GPRequestingAdaptor)}

Digital Services for Integrated Care (DSIC) Suppliers can use GP2GP to transfer Patients' electronic health records between old and new practices when they change GPs.

NHS England have also developed and assured adaptors to support GP2GP.

Digital Services for Integrated Care (DSIC) Suppliers may use the adaptors or alternatively develop their own (which will require additional assurance).

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

---

## [GP Connect (Patient Facing) Access Record](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Access-Record.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GPConnect(PatientFacing)AccessRecord}

Use this API to access structured and coded information from a Patient's GP Practice record to consume in a Patient facing service. The API accesses GP Core Clinical Solution and provides a consistent interface and data model.

You can retrieve Patient record data for the following:

- medications
- allergies
- immunisations
- consultations
- problems
- investigations
- reviewed attachments/documents

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on GP Connect (Patient Facing) Access Record can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/gp-connect-patient-facing-access-record-fhir#overview--onboarding>

---

## [GP Connect (Patient Facing) Prescriptions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Prescriptions.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GPConnect(PatientFacing)Prescriptions}

Use this API to manage a Patient's prescriptions as held by their GP Practice.

You can:

- request a new instance of a repeat prescription
- view all of a Patients medications, whether acute or repeat, past or present
- cancel a repeat prescription request
- check the status of a current prescription request
- request a new instance of a repeat prescription to a one off nomination pharmacy

The end user must be a Patient who is:

- registered with the GP Practice
- registered with NHS login to P9 identity verification level

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on GP Connect (Patient Facing) Access Record can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/gp-connect-patient-facing-prescriptions-fhir>

---

## [GP Connect (Patient Facing) User Permissions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-User-Permissions.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GPConnect(PatientFacing)UserPermissions}

Use this API to list and manage the permissions a Patient has to their medical record and a selection of services provided at their GP Practice.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on GP Connect (Patient Facing) Access Record can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/gp-connect-patient-facing-user-permissions>

---

## [GP Connect Access Record HTML - Provider](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Access-Record-HTML.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GPConnectAccessRecordHTML-Provider}

GP Connect is a national service that's integrated with all major GP Solutions. It routes requests to the appropriate GP Solution, based on the Patient's registered GP.

Use this API to view a Patient's registered GP Practice record, with read-only access.

You can:

- view a Patient’s primary care record by requesting sections or headings
- define a date range to filter larger sections
- incorporate these views directly into Electronic Patient Record systems

For example:

- GP Practices can view all of the Patient’s primary care records even when they are held on a different GP Solution
- care settings such as NHS111, ambulance and emergency care, primary care networks (PCNs), secondary care, pharmacy, care homes, community and dentistry can view the records held by the Patient’s GP Practice to better inform any care decisions they make for a Patient

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on GP Connect Access Record HTML can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/gp-connect-access-record-html-fhir>

---

## [GP Connect Access Record Structured - Provider/Consumer](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Access-Record-Structured.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GPConnectAccessRecordStructured-Provider/Consumer}

GP Connect is a national service that's integrated with all major GP Solutions. It routes requests to the appropriate GP Solution, based on the Patient's registered GP.

Use this API to access structured information from a Patient's registered GP Practice record. Structured information is Patient data in a coded format that a consuming system can import and process.

The API accesses GP Core Clinical Solutions, provides a consistent interface and data model, and is brokered through Spine.

For GP Connect Access Record Structured - **Provider** requirements, Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

For GP Connect Access Record Structured - **Consumer** requirements, Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a SCAL (Excel).

Assurance key contact for the GP Connect programme is via the mailbox [england.gpconnect.operations@nhs.net](mailto:england.gpconnect.operations@nhs.net)

Further information on GP Connect Access Record Stuctured can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/gp-connect-access-record-structured-fhir#onboarding>

---

## [GP Connect Appointment Management - Provider](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Appointment-Management.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GPConnectAppointmentManagement-Provider}

GP Connect is a national service that's integrated with all major GP Solutions. It routes requests to the appropriate GP Solution, based on the Patient's registered GP.

Use this API to enable administrative and clinical end users to book and manage Patient appointments held in any of the principal GP Practice systems.

You can:

- retrieve a Patient’s appointments
- search for free slots
- read an appointment
- book an appointment
- amend an appointment
- cancel an appointment

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on GP Connect Appointment Management can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/gp-connect-appointment-management-fhir>

---

## [GP Connect Emergency Supply of Medications](../Published-Content/GP-Connect-Emergency-Supply-of-Medications-v800.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GPConnectEmergencySupplyofMedications}

GP Connect Emergency Supply of Medications, formerly part of the Digital Medicines (DigiMeds) specification, supports structured emergency medication information to be shared between Healthcare Organisations.

Emergency Supply of Medications messages are sent and received via MESH.

For a Sender Solution (Community Pharmacy) or a Receiver Solution (GP Practice), Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via Tailored Assurance Approaches including Technical (ITK3) and Clinical assurance. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on integrating with Emergency Supply of Medications can be found at the following URL: <https://simplifier.net/guide/gp-connect-digimeds-emergency-supply-of-medications/Home/Design/Design-overview?version=1.3.0-public-beta>

As a Receiver Solution, Suppliers need to provide Self-Certification statements confirming that, through their internal testing and assurance activities, they have ensured that Pharmacy First Urgent Medicine Supply medication information updates recorded for a Patient in their Electronic Patient Record (EPR) are then correctly provisioned to recipient Consumer Solutions via GP Connect Access Record and rendering of the Summary Care Record (SCR) via the National Care Records Service (NCRS).

---

## [GP Connect Send Document - Receiver](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Send-Document.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GPConnectSendDocument-Receiver}

GP Connect is a national service that's integrated with all major GP Solutions. It routes requests to the appropriate GP Solution, based on the Patient's registered GP.

Use this integration to send a PDF consultation summary to a registered GP Practice - using GP Connect Messaging.

For example, use it to send a document containing a Patient's consultation notes to their GP Practice when a Patient is seen:

- at another GP Practice than their own
- by an out of hours service
- by a district nurse at home

Each message sent using this integration uses the GP Connect Messaging components, MESH, and ITK3 to deliver the message.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on GP Connect Send Document can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/gp-connect-send-document-fhir>

---

## [GP Connect Update Record - Sender/Receiver](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Update-Record.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GPConnectUpdateRecord-Sender/Receiver}

GP Connect is a national service that's integrated with all major GP Solutions. It routes requests to the appropriate GP Solution, based on the Patient's registered GP.

Use this integration to update a Patient's GP record from a Community Pharmacy with structured data.

Each message sent using this integration uses the GP Connect Messaging components, MESH, and ITK3 to deliver the message.

For GP Connect Update Record - **Receiver** requirements, Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

For GP Connect Update Record - **Sender** requirements, Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a SCAL (Excel).

Assurance key contact for the GP Connect programme is via the mailbox [england.gpconnect.operations@nhs.net](mailto:england.gpconnect.operations@nhs.net)

Further information on GP Connect Update Record can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/gp-connect-update-record>

---

## GP Data for Planning and Research {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GPDataforPlanningandResearch}

This Non-Overarching Standard has now been retired.

---

## [General Practice Extraction Service (GPES)](../DSIC-Standards/Non-Overarching-Standards/GPES-Data-Extraction.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-GeneralPracticeExtractionService(GPES)}

The General Practice Extraction Service (GPES) collects information for a wide range of purposes, including provision of direct care, GP payments and planning & research purposes. It works with the Calculating Quality Reporting Service (CQRS) and GP clinical Solutions as part of the GP Collections service.

GPES messages are sent and received via MESH and GPDC.

Digital Services for Integrated Care (DSIC) Suppliers will be assured against each extract as described in the Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Assurance key contact for Digital Services for Integrated Care (DSIC) is via the GPES team mailbox [england.gpses@nhs.net](mailto:england.gpses@nhs.net)

**Note**: Although GPDC requirements fall under GPES, there is a separate tailored assurance process. Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

---

## [Interface Mechanism (IM1)](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-InterfaceMechanism(IM1)}

IM1 is a mechanism for accessing data held in GP Systems (Systems providing one or more Foundation Capabilities).

A system or application is required to **provide**IM1 interfaces if it offered IM1 interfaces under GP IT Futures and/or if implementing an IM1 interface is mandated within the Capabilities and Standards.

A system or application may wish to **consume** IM1 interfaces where they have a requirement to access data held in GP Systems and the Provider Solution does not offer a GP Connect interface.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Assurance key contact for Digital Services for Integrated Care (DSIC) is via the IM1 teams mailbox [england.im1.team@nhs.net](mailto:england.im1.team@nhs.net)

---

## [Interoperability Toolkit (ITK)](../DSIC-Standards/Non-Overarching-Standards/Interoperability-Toolkit-ITK.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-InteroperabilityToolkit(ITK).1}

### ITK2 {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-ITK2}

These API standards cover a set of messaging specifications known as the Interoperability Toolkit (ITK). Primarily consisting of ITK Release 2 (ITK2), they also include earlier versions.

They're used, for example, for sending messages about the admission, discharge and transfer (ADT) of a Patient.

They are based on HL7 V2 and HL7 V3 standards. For example, ITK2.2 includes specific messaging domains based on HL7 V2, and also a number of message domains based on HL7 V3 - most notably the CDA messaging specifications which are used by NHS 111 domain messaging.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on ITK2 can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/interoperability-toolkit-messaging-2-standard>

### ITK3 {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-ITK3}

These API standards cover a set of generic FHIR messaging components we developed using FHIR STU3 running over [MESH](https://digital.nhs.uk/developer/guides-and-documentation/api-technologies-at-nhs-digital#mesh) to create a unified approach to NHS message and document flows across England.

Payloads are not specified as these components can carry any payload.

These components, along with the FHIR Message and FHIR Document Specifications, make up the Interoperability Toolkit 3 (ITK3) solution which is accompanied by an ITK3 Test Harness.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on ITK3 can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/interoperability-toolkit-3-messaging-distribution-fhir-standards>

---

## [Message Exchange for Social Care and Health (MESH)](../DSIC-Standards/Non-Overarching-Standards/Messaging-Exchange-for-Social-Care-and-Health-MESH.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-MessageExchangeforSocialCareandHealth(MESH)}

The Message Exchange for Social Care and Health (MESH) is a centralised message transfer service provided by The Authority using the Spine Services Core infrastructure.

The service supports the secure transfer of both clinical and business data flows between NHS Organisations and affiliated organisations.

There are 3 options for Suppliers when implementing MESH, these are:

- MESH UI - Ideal for the transfer of small files. This is pre-assured so there is no further assurance required.
- MESH Client - Ideal for the transfer of large files. This is pre-assured so there is no further assurance required
- MESH API - Ideal for the transfer of large files. This is an option for those service providers who have the technical skills to integrate MESH into their systems, suppliers will be onboarded via the Digital Onboarding Service.

Assurance key contact for MESH API will be allocated and engaged once a Supplier registers for MESH via the Digital Onboarding Service.

Further information on MESH API is available at the following URL: <https://digital.nhs.uk/developer/api-catalogue/message-exchange-for-social-care-and-health-api>

**Note:** This is a key pre-requisite to many other Non-Overarching Standards so should be prioritised.

---

## [Multicast Notification Service (MNS)](../DSIC-Standards/Non-Overarching-Standards/Multicast-Notification-Service-MNS.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-MulticastNotificationService(MNS)}

Use this API to publish or and subscribe to healthcare-related events. This API is currently only live with Patient-related event. However, it is intended as a robust service that could support many types of future event e.g. changes related to healthcare organisations or staff.

The events do not contain clinical information; they simply describe what type of event occurred to whom/what and where. A pointer is provided for retrieval of the data that the event refers to.

This API is for systems that need to share healthcare information with other systems that need to stay up to date with changes to that information.

You can:

- Publish events.
- Subscribe to events based on event type and optional corresponding criteria filter.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service.

Assurance key contact for MNS will be allocated and engaged once a Supplier registers for MNS via the Digital Onboarding Service.

Further information on MNS is available at the following URL: <https://digital.nhs.uk/developer/api-catalogue/multicast-notification-service>

---

## [National Care Record Service (NCRS)](../DSIC-Standards/Non-Overarching-Standards/National-Care-Records-Service-NCRS.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NationalCareRecordService(NCRS)}

The National Care Records Service (NCRS) provides a quick, secure way for health and care workers to access national Patient information to improve clinical decision making and healthcare outcomes.

The service provides a summary of Health and Care information for care settings where the full Patient Record is not required to support direct care for Patients.

Compliance with NCRS will be onboarded via a SCAL (Excel).

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on NCRS is available at the following URL: <https://digital.nhs.uk/developer/api-catalogue/national-care-records-service-integration>

---

## [National Data Opt-Out (NDOP)](../DSIC-Standards/Non-Overarching-Standards/National-Data-Opt-Out.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NationalDataOpt-Out(NDOP)}

Digital Services for Integrated Care (DSIC) Suppliers can use the National Data Opt-Out Service to identify Patients' preferences and control sharing of their data by healthcare organisations for planning and research purposes.

NDOP messages are sent and received via MESH.

Compliance with NDOP will be onboarded via a SCAL (Excel).

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on NDOP via MESH is available at the following URL: <https://digital.nhs.uk/developer/api-catalogue/national-data-opt-out-service-mesh>

---

## [National Event Monitoring Service (NEMS)](../DSIC-Standards/Non-Overarching-Standards/National-Events-Management-Service-NEMS.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NationalEventMonitoringService(NEMS)}

The National Event Monitoring Service works with other interoperability services including the National Record Locator which allows authorised users to find specific Patient records that are held on different health care systems.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service.

Assurance key contact for NEMS will be allocated and engaged once a Supplier registers for NEMS via the Digital Onboarding Service.

More information on integrating with NEMS FHIR API can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/national-events-management-service-fhir>

**Important Note -** It is planned to migrate functionality offered by NEMS to the Multicast Notification Service. Suppliers should seek guidance from their Supplier Manager as to how to proceed with this Non-Overarching Standard.

---

## [NHAIS HA / GP Links (Primary Care Registration Management (PCRM))](../DSIC-Standards/Non-Overarching-Standards/NHAIS-HAGP-Links.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NHAISHA/GPLinks(PrimaryCareRegistrationManagement(PCRM))}

PCRM has now replaced the NHAIS HA / GP Links as a National System although the Supplier requirements for NHAIS are still applicable.

Digital Services for Integrated Care (DSIC) Suppliers can use the PCRM API to manage GP registrations and other Patient data.

PCRM messages are sent and received via MESH.

NHS England have also developed and assured an adapter to support PCRM messaging (may still be referred to as the NHAIS adaptor in diagrams etc.)

Digital Services for Integrated Care (DSIC) Suppliers may use the adapter or alternatively develop their own (which will require additional assurance).

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

---

## [NHS App](../DSIC-Standards/Non-Overarching-Standards/NHS-App.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NHSApp}

The NHS App API allows Solutions to integrate with the NHS App, a simple and secure way for Patients registered with a GP Practice in England to access a range of services on their digital device.

If you want to integrate with the NHS App and you [meet the eligibility criteria](https://digital.nhs.uk/services/nhs-app/how-to-integrate-with-the-nhs-app/nhs-app-web-integration#step-1-tell-us-you-want-to-integrate-with-the-nhs-app), submit an [NHS App expression of interest form](https://digital.nhs.uk/services/nhs-app/how-to-integrate-with-the-nhs-app/nhs-app-integration-expression-of-interest-form).

The NHS App API specification will be provided once the NHS App team have decided your product is a good fit and the NHS England NDA has been signed.

Once your product has been prioritised, an Integration manager will be assigned. They will be your key point of contact throughout your integration process.

The integration process can be viewed in full at [How to integrate with the NHS App](https://digital.nhs.uk/services/nhs-app/how-to-integrate-with-the-nhs-app).

See [here](https://digital.nhs.uk/services/nhs-app/how-to-integrate-with-the-nhs-app/contact-us) for NHS App Team contact details.

---

## [NHS Login Service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NHSLoginService}

Use this API to enable Patients and the public to access multiple digital health and social care services with NHS login, a single re-usable login.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service and assured using the [NHS Login Integration Toolkit](https://digital.nhs.uk/services/nhs-login/nhs-login-for-partners-and-developers/nhs-login-integration-toolkit)

Assurance key contact for Digital Services for Integrated Care (DSIC) will be assigned upon engagement with NHS Login team. To apply for NHS Login integration please go to the following URL:

<https://digital.nhs.uk/services/nhs-login/nhs-login-for-partners-and-developers/nhs-login-integration-toolkit/apply-for-nhs-login#top>

---

## [NHS login Users Endpoint](../Published-Content/NHS-login-Users-Endpoint-v100.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NHSloginUsersEndpoint}

The NHS login Users Endpoint uses the System for Cross-domain Identity Management (SCIM) system to share basic user identity information with other connected services. This allows a Solution to access a NHS login user’s NHS Users attribute details in a standard, compatible way.

NHS login Users Endpoint assurance will be completed via a Supplier Conformance Assessment List (SCAL).

Key programme and assurance contact is via [england.support.nhslogin@nhs.net](mailto:england.support.nhslogin@nhs.net).

Further information on onboarding can be found at<https://nhsconnect.github.io/nhslogin/what-is-users-endpointv2/>

---

## NHS Message Implementation Manual (MIM) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NHSMessageImplementationManual(MIM)}

Integration with the MIM is now deprecated.

---

## [NHSBSA Claims & Reporting](../DSIC-Standards/Non-Overarching-Standards/NHSBSA-Claims-Reporting.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NHSBSAClaims&Reporting}

The NHS Business Services Authority (NHSBSA) enables Health or Care Organisations to submit claims for payment based on services delivered. To onboard, Suppliers must complete two consecutive steps:

- Technical API testing with NHSBSA
- End-to-End system testing with the DSIC Assurance Team.

The NHSBSA Claims and Reporting Standard comprises a suite of APIs designed for reporting and claims functionality. For each API outlined in the DSIC Capabilities and Standards model, NHSBSA will provide Digital Services for Integrated Care (DSIC) Suppliers bespoke test plans. These tests are carried out in partnership with NHSBSA, who oversee the validation of technical API requirements.

NHSBSA Claims and Reporting is assured via tailored assurance, the DSIC Assurance Team provide a risk log to DSIC Suppliers detailing business workflow and data flow risks, including those related to NHSBSA APIs. Suppliers are responsible for presenting evidence of risk mitigation, which involves system-to-system integration testing within the NHS England Integration (INT) test environment. This includes transmitting messages to the NHSBSA APIs for verification.

When Suppliers wish to engage, they should reach out to their Supplier Manager, who will then assign an assurance lead. For questions concerning NHSBSA APIs, please contact [mys-platform@nhsbsa.nhs.uk](mailto:mys-platform@nhsbsa.nhs.uk)

---

## [NHS Notify](../DSIC-Standards/Non-Overarching-Standards/NHS-Notify.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-NHSNotify}

Integration with NHS Notify allows organisations and services to send NHS App messages, emails, texts and letters to Patients, the public and recipients of adult social care.

To implement the NHS Notify requirements, you can either use NHS Notify API or NHS Notify MESH. To determine which method of integration is the most appropriate for your Solution, please refer to the ‘Who can use this API’ section in [NHS Notify API](https://digital.nhs.uk/developer/api-catalogue/nhs-notify) and the ‘Who can use this integration’ section in [NHS Notify MESH](https://digital.nhs.uk/developer/api-catalogue/nhs-notify-mesh).

The onboarding process can be viewed in full at [Onboard with NHS Notify](https://notify.nhs.uk/get-started/onboard-with-nhs-notify).

---

## [Patient Data Manager](../Draft-Content/Patient-Data-Manager-v011.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-PatientDataManager}

The Patient Data Manager enables NHS products to store, retrieve, and manage Patient health and care data in a standardised, interoperable format.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service.

Assurance key contact for Patient Data Manager will be allocated and engaged once a Supplier registers for Patient Data Manager via the Digital Onboarding Service.

Further information on the Patient Data Manager is available at the following URL:<https://digital.nhs.uk/developer/api-catalogue/patient-data-manager>

---

## [Patient Flag Service](../Published-Content/Patient-Flags-Service-v100.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-PatientFlagService}

The Patient Flag Service API is used to access and update Patients Flags and associated supporting resources.

The Patient Flag API can be used to access and update:

- [Reasonable Adjustments (RA) Flag and associated impairments, adjustments and underlying conditions](https://digital.nhs.uk/services/reasonable-adjustment-flag#how-the-reasonable-adjustment-flag-works)
- [Female Genital Mutilation (FGM) Flag](https://digital.nhs.uk/services/patient-flags-service/female-genital-mutilation---information-sharing)

The Patient Flag API can be used to access:

- [Child Protection - Information Sharing (CP-IS) Flag and associated care team (for scheduled care)](https://digital.nhs.uk/services/patient-flags-service/child-protection---information-sharing-cp-is)

The Patient Flag API can be used to:

- get all patient flags
- get the flag and supporting resources for a specific flag
- create a flag and supporting resources
- delete a flag (which deletes all supporting resources)
- create a supporting resource
- delete a supporting resource

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service.

Assurance key contact for Patient Flags will be allocated and engaged once a Supplier registers for Patient Flags Service on the Digital Onboarding Service.

Further information on onboarding can be found at <https://digital.nhs.uk/developer/api-catalogue/patient-flags-service---fhir-api#overview--onboarding>

---

## [Personal Demographics Service (PDS)](../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-PersonalDemographicsService(PDS)}

The Personal Demographics Service is the national electronic database of NHS Patient details such as name, address, date of birth, registered GP, and NHS number.

New Digital Services for Integrated Care (DSIC) Suppliers are expected to integrate with the PDS via the PDS FHIR API. There are 3 modes of access, these are:

- Restricted Access - This access mode is [application-restricted](https://digital.nhs.uk/developer/guides-and-documentation/security-and-authorisation#application-restricted-apis), meaning we authenticate and authorise the calling application but not the end user. This access mode is not designed to be accessed by an end user.
- Healthcare Worker Access - This access mode is [user-restricted](https://digital.nhs.uk/developer/guides-and-documentation/security-and-authorisation#user-restricted-apis), meaning an end user must be present, authenticated and authorised.
- Patient Access - A citizen may access their record and update a restricted list of fields. This access mode is [user-restricted](https://digital.nhs.uk/developer/guides-and-documentation/security-and-authorisation#user-restricted-apis), meaning an end user must be present, authenticated and authorised.

All integrations with PDS FHIR API will be onboarded via the Digital Onboarding Service.

Assurance key contact for PDS will be allocated and engaged once a Supplier registers for PDS on the Digital Onboarding Service. .

Further information on integrating and onboarding with the PDS FHIR API can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/personal-demographics-service-fhir>

**Note:** This is a key pre-requisite to many other Non-Overarching Standards so should be prioritised.

---

## [Primary Care Clinical Terminology Usage Report](../DSIC-Standards/Non-Overarching-Standards/Primary-Care-Clinical-Terminology-Usage-Report.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-PrimaryCareClinicalTerminologyUsageReport}

The purpose of this report is to collect data from each Foundation GP IT Solution Supplier on the frequency of use of clinical coded terms, both terminology (SNOMED CT, Read v2, CTV3) and local codes, recorded through their Solution for fully registered Patients over a 12 month period for all entries which are part of the GP record, aggregated across the selected Practices.

This data on the frequency of usage of clinical terms is to inform which codes are in actual use to:

- support the clinical assurance process with respect to data migration and GP2GP
- support the production, maintenance and clinical assurance of the cross maps for primary care
- facilitate the development of guidance with respect to terminology codes and local codes

Elements of the data submitted will be published and made publicly available once processed to protect any Patient and commercially sensitive data.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

---

## [Register with a GP Surgery Service](../DSIC-Standards/Non-Overarching-Standards/Register-with-a-GP-Surgery-Service.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-RegisterwithaGPSurgeryService}

Use this API to access registration applications using the Register with a GP Surgery service.

This API provides:

- operational parameters
- a set of codeable observations
- questionnaire response relating to a Patients registration request.

You can use this API to:

- retrieve a registration application

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

Further information on integrating and onboarding with the Register with a GP Surgery API can be found at the following URLs:

<https://digital.nhs.uk/developer/api-catalogue/register-with-a-gp-surgery>

<https://digital.nhs.uk/services/register-with-a-gp-surgery-service>

---

## [Screening Messaging](../DSIC-Standards/Non-Overarching-Standards/Screening-Messaging.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-ScreeningMessaging}

Digital Services for Integrated Care (DSIC) Suppliers can use the Bowel Cancer Screening EDIFACT API to receive bowel cancer screening test results in GP Practices from the screening system, specifically faecal occult blood test (FOBT) results.

It's designed for the transmission of structured bowel cancer screening results to GP Solutions from the screening system, using UN/EDIFACT based messages sent over MESH.

NHS England have also developed and assured an adapter to support Pathology messaging.

Digital Services for Integrated Care (DSIC) Suppliers may use the adapter or alternatively develop their own (which will require additional assurance).

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

More information on integrating with the Bowel Cancer Screening EDIFACT API can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/bowel-cancer-screening-edifact>

---

## [Secure Electronic File Transfer (SEFT)](../DSIC-Standards/Non-Overarching-Standards/Secure-Electronic-File-Transfer-SEFT.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-SecureElectronicFileTransfer(SEFT)}

There is no formal onboarding process for this Non-Overarching Standard. Instead Suppliers should seek to be set up with a SEFT account during integration with other Non-Overarching Standards that utilise SEFT such as General Practice Appointments Data Reporting (GPAD).

---

## [Spine Mini Services](../DSIC-Standards/Non-Overarching-Standards/Spine-Mini-Services.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-SpineMiniServices}

There are 3 spine mini services integrations:

- PDS (now deprecated, please use PDS FHIR API)
- SCR <https://digital.nhs.uk/developer/api-catalogue/summary-care-record-smsp-standards>
- CP-IS (marked for deprecation)

Spine Mini Services are onboarded under the ITK standard.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

---

## [Summary Care Record (SCR)](../DSIC-Standards/Non-Overarching-Standards/Summary-Care-Record-SCR.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-SummaryCareRecord(SCR)}

The Summary Care Record (SCR) is an electronic record of important Patient information, created from GP medical records. SCRs can be seen and used by authorised staff in other areas of the health and care system involved in the Patient's direct care.

New Digital Services for Integrated Care (DSIC) Suppliers who need to integrate with the SCR service should do so via the SCR FHIR API.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

More information on integrating with the SCR FHIR API can be found at the following URL: <https://digital.nhs.uk/developer/api-catalogue/summary-care-record-fhir>

---

## [Transfer of Care (TOC) FHIR Payload](../DSIC-Standards/Non-Overarching-Standards/Transfer-of-Care-FHIR-Payload.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-TransferofCare(TOC)FHIRPayload}

Patients move between care settings and responsibility for them is handed over from one Clinician to another. Transfer of Care messaging ensures that the clinical context and information about the Patient is transferred when this occurs.

The scope for Transfer of Care currently covers:

- **InPatient and Day Case Discharge Summary Document** – An ITK3 FHIR Document containing Transfer of Care information supporting inPatient and day case discharges typically between an acute hospital and GP Practice.
- **Emergency Care Discharge Summary Document** – An ITK3 FHIR Document containing Transfer of Care information supporting a discharge typically between an emergency care department and a GP Practice.
- **InPatient and Day Case Discharge Summary (Mental Health) Document** – An ITK3 FHIR Document containing Transfer of Care information supporting a mental health adult discharge summary to a GP Practice.
- **OutPatient Clinic Letter Document** – An ITK3 FHIR Document containing Transfer of Care information between the hospital clinic and the GP and other relevant parties following a consultation in a clinic

TOC messages are sent and received via MESH

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

A Digital Services for Integrated Care (DSIC) Service Provider must undertake ITK3 accreditation in support of TOC.

Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

For end to end assurance Suppliers should contact their Supplier Manager when they want to engage, at this point an assurance lead will be allocated.

---

## [Vaccination Administration (DigiMeds)](../Published-Content/Vaccination-Administration-DigiMeds-v100.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-VaccinationAdministration(DigiMeds)}

Vaccinations Administration (DigiMeds) supports updates to a Patient’s registered GP Practice about vaccinations administered at another Health or Care Organisation.

Vaccination Administration messages are sent and received via MESH.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded for Vaccination Administration (DigiMeds) via the Digital Onboarding Service.

Suppliers should contact their Supplier Manager when they want to engage with the various teams who support integration with this Non-Overarching Standard, at this point assurance lead(s) will be allocated.

---

## [Vaccination Extract](../DSIC-Standards/Non-Overarching-Standards/Vaccination-Extract.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-VaccinationExtract}

The Vaccination Extract Standard specifies the flow of vaccination-related information from healthcare settings to the Authority.

New Digital Services for Integrated Care (DSIC) Suppliers who need to meet this Standard should do so via the Immunisation FHIR API.

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via a Tailored Assurance Approach. The approach will detail the technical and clinical assurance activities to be carried out by NHS England alongside the service provider.

Assurance key contact for Digital Services for Integrated Care (DSIC) is via the Vaccination teams onboarding team mailbox [england.vaccinationsonboardingteam@nhs.net](mailto:england.vaccinationsonboardingteam@nhs.net)

For more information see <https://digital.nhs.uk/developer/api-catalogue/vaccination> and <https://digital.nhs.uk/developer/api-catalogue/immunisation-fhir-api>.

---

## [Validated Relationship Service](../DSIC-Standards/Non-Overarching-Standards/Validated-Relationship-Service.md) {#OnboardingOverviewoftheDigitalServicesforIntegratedCare(DSIC)Non-OverarchingStandardsandRequirements-ValidatedRelationshipService}

The Validated Relationship Service - FHIR API enables a Solution to access the Validated Relationship Service. This is the national electronic database of relationships that have been verified for the purpose of enabling individuals to access healthcare services on behalf of those they care for. The relationships held by this service are strictly for the purpose of enabling access to healthcare services.

The Validated Relationship Service - FHIR API can currently be used to:

- Get Verified Candidate Relationships
- Get Proxy roles
- Create Proxy roles
- Get Proxy role
- Update Proxy roles

Digital Services for Integrated Care (DSIC) Suppliers will be onboarded via the Digital Onboarding Service.

Assurance key contact for the Validated Relationship Service will be allocated and engaged once a Supplier registers for Validated Relationship Service on the Digital Onboarding Service.

Further information on onboarding can be found at <https://digital.nhs.uk/developer/api-catalogue/validated-relationship-service>

## Attachments

- [Screenshot 2022-05-09 at 12.49.35.png](../../../.raw/DCSDCS/attachments/11973558273/att11973558301-Screenshot 2022-05-09 at 12.49.35.png)
- [NME Assurance Approach v2.0.jpg](../../../.raw/DCSDCS/attachments/11973558273/att11973558304-NME Assurance Approach v2.0.jpg)
- [NME Assurance Approach.jpg](../../../.raw/DCSDCS/attachments/11973558273/att11973558307-NME Assurance Approach.jpg)
- [Onboarding TIF via SCAL DOS etc.jpg](../../../.raw/DCSDCS/attachments/11973558273/att14545223780-Onboarding TIF via SCAL DOS etc.jpg)
- [Overview Diagram.jpg](../../../.raw/DCSDCS/attachments/11973558273/att14859763725-Overview Diagram.jpg)
- [image-20260414-152912.png](../../../.raw/DCSDCS/attachments/11973558273/att14957281315-image-20260414-152912.png)
- [Onboarding TIF via SCAL DOS etc (2).drawio.png](../../../.raw/DCSDCS/attachments/11973558273/att14967111683-Onboarding TIF via SCAL DOS etc (2).drawio.png)
- [image-20260512-114452.png](../../../.raw/DCSDCS/attachments/11973558273/att15048179742-image-20260512-114452.png)
- [Onboarding TIF via SCAL DOS etc (2) (6) (2)-20260713-095322.png](../../../.raw/DCSDCS/attachments/11973558273/att15257927692-Onboarding TIF via SCAL DOS etc (2) (6) (2)-20260713-095322.png)
