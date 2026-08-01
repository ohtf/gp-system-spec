---
page_id: "11962974263"
space: "DCSDCS"
title: "Citizen Services Implementation Guidance"
version: 3
updated: "2025-09-22T14:56:01.601Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11962974263/Citizen+Services+Implementation+Guidance"
labels: ["reference_page"]
---

# Citizen Services Implementation Guidance

|  |  |
| --- | --- |
| ID {#CitizenServicesImplementationGuidance-ID} | R8 |
| Version {#CitizenServicesImplementationGuidance-Version} | 2.0.0 |
| Type {#CitizenServicesImplementationGuidance-Type} | Reference |

# Introduction {#CitizenServicesImplementationGuidance-Introduction}

Citizen Services allow a Patient (or in some instances a person acting as a Proxy for a Patient) to access Solutions that allow them to perform certain actions online (e.g. via an internet web browser or an App on a Phone). As a minimum, this includes:

- Managing GP Appointments
- Ordering Repeat Prescriptions
- Viewing their Electronic Patient Record (EPR)

The services that are available to a Citizen are configured by their registered GP Practice using their Core Clinical Solution.

## Citizen Capabilities {#CitizenServicesImplementationGuidance-CitizenCapabilities}

To support these Citizen Services, a number of Citizen Capabilities exist which Suppliers can choose to build Solutions to meet:

- [Appointments Management - Citizen](../DSIC-Capabilities/Appointments-Management-Citizen.md)
- [Prescription Ordering - Citizen](../DSIC-Capabilities/Prescription-Ordering-Citizen.md)
- [View Record - Citizen](../DSIC-Capabilities/View-Record-Citizen.md)

Suppliers can choose to build Solutions that meet one or many of these Citizen Capabilities.

Requirements relating to enabling and disabling these Citizen Services at a Patient and Practice level are mandated in the [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Capability.

## Scenarios {#CitizenServicesImplementationGuidance-Scenarios}

There are two main scenarios in terms of Citizen Services implementation:

1. The Core Clinical Solution is the same as the Citizen Service Solution
2. The Core Clinical Foundation Solution is different to the Citizen Services Solution

Where the Citizen Capabilities are being provided by the same Solution as the Core Clinical Solution (Scenario 1), the Supplier is free to determine how access to the appropriate Citizen Services is established for Patients providing they meet all MUST requirements within the Capabilities and Standards. They will still be required to support other Solutions integrating with their Core Clinical Solution as per Scenario 2 above.

Since the Citizen Capabilities can be provided by Solutions that are different to a Core Clinical Solution (Scenario 2), Suppliers of Core Clinical Solutions need to provide the ability for these Citizen Solutions to be integrated with the Core Clinical Solution. There are currently two ways to achieve this integration:

1. GP Connect (Patient Facing APIs) (latest approach)

   1. [GP Connect (Patient Facing) User Permissions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-User-Permissions.md) Standard
   2. [GP Connect (Patient Facing) Prescriptions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Prescriptions.md) Standard
   3. [GP Connect (Patient Facing) Access Record](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Access-Record.md) Standard
2. [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Standard (legacy approach)

The diagram below illustrates the likely relationships between the Capabilities which make up the Citizen Services and the Core Clinical Solution Capabilities where different Solutions are integrated:

As indicated by the diagram, linkage between the Citizen Services Solutions and the Core Clinical Solution is to be achieved through providing and consuming Patient interfaces as per the [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Standard or GP Connect (Patient Facing APIs).

![Citizen access diagram.png](https://nhse-dsic.atlassian.net/wiki/download/attachments/11962974263/Citizen%20access%20diagram.png?api=v2)

# Structure and Lifecycle of Citizen Online Accounts {#CitizenServicesImplementationGuidance-StructureandLifecycleofCitizenOnlineAccounts}

This section is essential reading for Suppliers as it articulates the different types of account a Citizen can have, how they differ and the processes involved in their maintenance. It is primarily focused on the Scenario 2 where two different Solutions need to be integrated to provide access to Citizen Services for a Patient.

This information is intended to be guidance only and does not supersede or replace any mandatory requirements contained within any related Capabilities and Standards.

## Account Types {#CitizenServicesImplementationGuidance-AccountTypes}

Depending on the implementation scenario, as a minimum a Citizen is likely to need up to two accounts as outlined in the table below.

| **Type** | **Description** |
| --- | --- |
| Verified User Account (VUA) | A Verified User Account (VUA) is the Practice based account for a Citizen who can be a registered Patient or a person acting as a Proxy for a Patient. It is created and maintained within the [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Solution (most likely by Practice Staff) which holds the Patient Record, and this VUA will hold details such as the identity verification record and any preferences. |
| Online Service Account (OSA) | An Online Service Account (OSA) is an online account created on any Citizen Services Solution (e.g. a third-party Appointment booking Solution that meets the [Appointments Management - Citizen](../DSIC-Capabilities/Appointments-Management-Citizen.md) Capability), which must integrate with the [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Solution to enable online access to information and services. |

Where the Citizen Capabilities are being provided by the same Solution as the Core Clinical Solution (Scenario 1), it is possible only the VUA account will be required.

## Account Structure and Relationships {#CitizenServicesImplementationGuidance-AccountStructureandRelationships}

The following describes a typical approach to account structure and relationships between accounts.

- A Verified User Account (VUA) consists of a Suppliers' internal ID for the Patient at a specific Practice and Account Linkage Key

  - Where the Citizen Capabilities are being provided by the same Solution as the Core Clinical Solution (Scenario 1), the VUA may be the only account required and may also hold a Username and Password to be used by the Citizen to access Citizen Services
- An Online Service Account (OSA) consists of only a Username and Password, which may be different to the credentials of both the VUA and any other OSA held by the Citizen.

### Account Linkage (IM1 - Interface Mechanism only) {#CitizenServicesImplementationGuidance-AccountLinkage(IM1-InterfaceMechanismonly)}

Where the Core Clinical Solution is different to the Citizen Services Solution (Scenario 2), in order for a Citizen to gain access to Citizen Services a connection will need to be established between an Online Service Account (OSA) and a Verified User Account (VUA) in the [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Solution.

Citizen Services Solutions will allow the Citizen to enter VUA Credentials and Demographics and confirm, in conjunction with the [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Solution, that information provided is a successful match. Where Account Linkage is successful, the Citizen will be informed of the successful linkage.

Once an Online Service Account has been linked to a VUA this then the Citizen can access the relevant Citizen Services as configured by their Practice.

See [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) for more information on Account Linkage and the associated requirements.

#### IM1 - Interface Mechanism {#CitizenServicesImplementationGuidance-IM1-InterfaceMechanism}

![Example - IM1 Interface Mechanism.png](https://nhse-dsic.atlassian.net/wiki/download/attachments/11962974263/Example%20-%20IM1%20Interface%20Mechanism.png?api=v2)

#### GP Connect (Patient Facing APIs) {#CitizenServicesImplementationGuidance-GPConnect(PatientFacingAPIs)}

![Example - GP Connect Patient Facing APIs.png](https://nhse-dsic.atlassian.net/wiki/download/attachments/11962974263/Example%20-%20GP%20Connect%20Patient%20Facing%20APIs.png?api=v2)

## Example Processes {#CitizenServicesImplementationGuidance-ExampleProcesses}

The below diagrams represent example processes for Citizens accessing Citizen Services and may differ to what has been implemented by Suppliers of Citizen Services Solutions

### Scenario 1: Citizen Services Process - Single Solution {#CitizenServicesImplementationGuidance-Scenario1:CitizenServicesProcess-SingleSolution}

![Scenario 1 - Citizen Services Process - Single Solution.png](https://nhse-dsic.atlassian.net/wiki/download/attachments/11962974263/Scenario%201%20-%20Citizen%20Services%20Process%20-%20Single%20Solution.png?api=v2)

### Scenario 2: Citizen Services Process - Integrated Solutions (IM1 - Interface Mechanism) {#CitizenServicesImplementationGuidance-Scenario2:CitizenServicesProcess-IntegratedSolutions(IM1-InterfaceMechanism)}

![Scenario 2 - Citizen Services Process - Integrated Solutions (IM1 - Interface Mechanism).png](https://nhse-dsic.atlassian.net/wiki/download/attachments/11962974263/Scenario%202%20-%20Citizen%20Services%20Process%20-%20Integrated%20Solutions%20(IM1%20-%20Interface%20Mechanism).png?api=v2)

### Scenario 3: Citizen Services Process - Integrated Solutions (GP Connect (Patient Facing APIs)) {#CitizenServicesImplementationGuidance-Scenario3:CitizenServicesProcess-IntegratedSolutions(GPConnect(PatientFacingAPIs))}

![Scenario 3 - Citizen Services Process - Integrated Solutions (GP Connect Patient Facing APIs).png](https://nhse-dsic.atlassian.net/wiki/download/attachments/11962974263/Scenario%203%20-%20Citizen%20Services%20Process%20-%20Integrated%20Solutions%20(GP%20Connect%20Patient%20Facing%20APIs).png?api=v2)

## Online Accounts and Proxy Service Access {#CitizenServicesImplementationGuidance-OnlineAccountsandProxyServiceAccess}

In some circumstances Citizens can be granted access to Citizen Services on behalf of another Citizen (i.e. as their Proxy). For example, as a parent booking Appointments for a Child. Citizen Services account structures that are created to support this can vary depending on the location of the records involved and also the Suppliers' Solution architecture:

| **Scenario** | **Outcome** |
| --- | --- |
| 1. The Citizen is registered at a different Practice than the Patient for whom they are a Proxy, and the Supplier is not able to offer a single VUA covering this Citizen as a Proxy at Practice A, and a Patient at Practice B, accessing Citizen Services | The Proxy must go through Identity Verification with the Practice that holds the target Patient Record (Practice A). They will need to do this even if they have completed Identity Verification at their registered Practice (Practice B). Account Linkage will need to be completed by the Proxy.  This will allow linkage of their VUA at the Patient's Practice (Practice A) with the Patient Record the Proxy needs to view (also at Practice A). |
| Either:   1. The Citizen is registered at the same Practice as the Patient for whom they are a Proxy (Practice A) 2. The Citizen is registered at a different Practice (Practice B) than the Patient for whom they are a Proxy, and the Supplier is able to offer a single VUA covering both Practices | Supplier associates the Proxy's VUA with both their own and the target Patient Record, creating a unique Linkage Key for each association.  In scenario 2, the target Patient's Practice (Practice A) may require the Proxy to verify their identity before allowing the association to be created. For further information on Identity Verification please see [DAPB3051 (previously DCB3051): Identity Verification and Authentication Standard for Digital Health and Care Services - NHS England Digital](https://digital.nhs.uk/data-and-information/information-standards/governance/latest-activity/standards-and-collections/dapb3051-identity-verification-and-authentication-standard-for-digital-health-and-care-services). |

---

# Further Guidance {#CitizenServicesImplementationGuidance-FurtherGuidance}

This section provides supporting information relevant to the different functionality required to support Citizen Services.

## Verified User Account (VUA) Management {#CitizenServicesImplementationGuidance-VerifiedUserAccount(VUA)Management}

As described above, a Verified User Account (VUA) is the Practice based account for a Citizen who can be a registered Patient or a person acting as a Proxy for a Patient. It is created by the [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Solution which holds the Patient Record.

A Patient or Proxy should have a maximum of one VUA per GP Practice, however as covered by the scenarios in the Online Accounts and Proxy Service Access section above, a Supplier may choose to design a Solution where a single VUA is created for an individual for use and management by any Practice that uses their Solution to avoid duplication.

Typically the following data would be recorded in relation to a VUA:

- VUA ID\* - *A unique identifier per Practice (and/or per Solution)*
- VUA Demographics

  - Title
  - Forename(s)
  - Family Name
  - Date of Birth
  - Contact Details - *Postal Address, Telephone Number and Email Address*
- VUA Linkage Key\* - *IM1 - Interface Mechanism only*
- ODS Code\* - *of the GP Practice creating the VUA*
- VUA Status - *Live or Inactive*
- VUA-Patient Association - *association with one or more Patient Records*
- VUA Identity Verification Record

Data items marked with \* will typically be Solution-generated and non-editable.

### **VUA details display** {#CitizenServicesImplementationGuidance-VUAdetailsdisplay}

It’s recommended the following VUA details and historic information are able to be displayed to a User in the [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Solution:

- VUA Demographics
- Preferences
- Service Access (including date and time of changes)
- Identity Verification
- VUA Creation Date & Time
- Patient Association
- Registration for Services (including date and time)
- Current and historic Account Linkages

### VUA Linkage Key (IM1 - Interface Mechanism only) {#CitizenServicesImplementationGuidance-VUALinkageKey(IM1-InterfaceMechanismonly)}

VUA Linkage Key creation and retrieval is required to be implemented as per the [NHS login service](../DSIC-Standards/Non-Overarching-Standards/NHS-login-service.md) Standard to Support linking VUAs to OSAs when integrating via IM1 - Interface Mechanism.

Each VUA Linkage Key will be:

- As per Authority defined requirements within [Information Governance](../DSIC-Standards/Overarching-Standards/Information-Governance.md), including being supportive of complexity management and enforcing suitable strength and character restrictions
- Re-usable i.e. the same VUA Linkage Key for each/all Services accessed

### VUA Status {#CitizenServicesImplementationGuidance-VUAStatus}

VUAs should be able to have the following statuses as a minimum to support the different stages of the VUA lifecycle:

- **Inactive** – default state upon VUA Creation.

  - VUA could revert to Inactive:

    - Automatically if no active VUA-Patient Associations exist e.g. if the Patient leaves the Practice and is not a Proxy for anybody else at that Practice
    - Automatically if Account Linkage is removed/reset e.g. in the instance of unusual activity or compromised Credentials.
    - Manually when changed by a User
- **Active** – to only become Active when the following is completed:

  - Completion of Account Linkage
  - Identity Verification
  - VUA-Patient Association with at least one Patient Record

## VUA-Patient Association {#CitizenServicesImplementationGuidance-VUA-PatientAssociation}

In order for a Citizen to access online services for a Patient, their VUA will need to be associated with at least one Patient Record within a [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Solution.

Typically the following data would be recorded in relation to each VUA-Patient Association:

- Type of Association

  - Self (where the Citizen and the Patient are the same individual - zero or one such Self Association is permitted)
  - Proxy (where the Citizen and the Patient are different individuals - zero, one or many such Proxy Associations are permitted)
- Assurance of the Relationship - i.e. Legal Basis for the association and Online Service access, including:

  - Type of Relationship - e.g. Self, Mother, Father, Son, Daughter, Friend or Carer
  - Explicit consent of the Patient - recording consent has been obtained and method of Consent (i.e. Written or Verbal)
  - Free-text details - for further supporting information
- Services Registered - which Online Services are approved for this association
- Start Date
- End Date

See [DAPB3051 (previously DCB3051): Identity Verification and Authentication Standard for Digital Health and Care Services - NHS England Digital](https://digital.nhs.uk/data-and-information/information-standards/governance/latest-activity/standards-and-collections/dapb3051-identity-verification-and-authentication-standard-for-digital-health-and-care-services)for information on Proxy access.

## Identity Verification {#CitizenServicesImplementationGuidance-IdentityVerification}

Identity Verification functionality is provided by the [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Solution and is intended to support local Practice Policy on recording Identity Verification for Patients in relation to Citizen Services.

The functionality will need to be sufficient to support [DAPB3051 (previously DCB3051): Identity Verification and Authentication Standard for Digital Health and Care Services - NHS England Digital](https://digital.nhs.uk/data-and-information/information-standards/governance/latest-activity/standards-and-collections/dapb3051-identity-verification-and-authentication-standard-for-digital-health-and-care-services) and could be configurable.

Typically the following data would be recorded in relation to Identity Verification:

- Date - of the ID verification
- Health or Care Professional - who verified the identity
- Type of Verification

  - Vouching

    - Personal
    - Information confirmation - e.g. knowledge of details on their medical record
    - Vouched for by - Staff Member responsible for vouching
  - Identity Documentation - will need to be excluded form GP2GP transfers

    - Type of Document, including

      - Passport

        - Birth Certificate
        - Marriage Certificate
        - Other
- Attached evidence - e.g. copy of or link to an image of the identity document

## Online Service Account (OSA) {#CitizenServicesImplementationGuidance-OnlineServiceAccount(OSA)}

As described above, an Online Service Account is an account held by the Citizen Services Solution to enable access to Citizen Services where this is a separate Solution to the Foundation Solution.

Where required, a Citizen Service Solution would typically allow a Citizen to:

- Create a unique Online Service Account
- Create/obtain account Credentials e.g. *utilising NHS Login,* by creating a Username & Password, by integrating a web Single Sign On (SSO) service or by associating a device identifier (such as Mobile Phone Identity IMEI - International Mobile Equipment Identity number)
- Set up security questions for use when account Credentials have been forgotten

All account Credentials to be created/assigned as per [Authentication](../DSIC-Standards/Overarching-Standards/Information-Governance.md) requirements.

## Appointments Management - Citizen {#CitizenServicesImplementationGuidance-AppointmentsManagement-Citizen}

Functionality allowing Citizens to manage Appointments online either for themselves or on behalf of someone else (as a Proxy) will be provided by the [Appointments Management - Citizen](../DSIC-Capabilities/Appointments-Management-Citizen.md) Solution.

This functionality will allow Citizens to book appointments based on availability defined by the [Appointments Management - GP](../DSIC-Capabilities/Appointments-Management-GP.md) Solution (adhering to any additional rules and restrictions defined) through the provision and consumption of Patient interfaces as per the [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Standard.

## View Record - Citizen {#CitizenServicesImplementationGuidance-ViewRecord-Citizen}

Functionality allowing Citizens to access Patient Record information either for themselves or on behalf of someone else (as a Proxy) will be provided by the [View Record - Citizen](../DSIC-Capabilities/View-Record-Citizen.md) Solution.

This functionality will allow Citizens to access different levels of information from the relevant Patient Record as defined by the Service Configuration functionality within the [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Solution and through the provision and consumption of Patient interfaces as per the [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Standard or [GP Connect (Patient Facing) Access Record](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Access-Record.md) Standard.

It is recommended that Citizens have the ability to:

- Be informed upon every access that they might not be accessing the full information held using the following statement “This is a limited view of the Patient Record and may not include any free text. Information that is considered to be sensitive or that existed before the creation of this service may not be available for viewing online.”
- View relevant elements of the Patient’s Record logically grouped as appropriate, including:

  - The clinical term description i.e. not the code
  - Associated free text
  - Date and Time of the event
  - Source/Provenance (Organisation/System, User/Role, Name)
- Sort the Patient’s Record by relevant elements, including:

  - Event Date
  - Type
  - Problem (where available)
  - Source/Provenance (Organisation/System, User/Role, Name)

### View Record - Access Levels {#CitizenServicesImplementationGuidance-ViewRecord-AccessLevels}

The different levels of Patient Record access are:

#### Summary Information Record {#CitizenServicesImplementationGuidance-SummaryInformationRecord}

When enabled for a Patient, the Summary Information dataset (and \*only\* that data) will be made available irrespective of any agreement with the Patient regarding their actual [Summary Care Record](../DSIC-Standards/Non-Overarching-Standards/Summary-Care-Record-SCR.md) (i.e. if certain information for the Patient is excluded from their Summary Care Record, this information will not automatically be excluded from the Summary Information Record and vice versa).

The Summary Information Record dataset is defined [here](https://simplifier.net/guide/GP-Connect-Patient-Facing-Access-Record/Home/Build/Permission-Levels?version=current).

#### Detailed Coded Record {#CitizenServicesImplementationGuidance-DetailedCodedRecord}

Detailed Coded Record Access builds on the data already made available through the Summary Information Record dataset and additionally includes all data held as coded data (See [Data Standards](../DSIC-Standards/Overarching-Standards/Data-Standards.md) for definition of coded data and associated requirements) within the Patient Record, excluding associated free text.

The Detailed Coded Record dataset is defined [here](https://simplifier.net/guide/GP-Connect-Patient-Facing-Access-Record/Home/Build/Permission-Levels?version=current).

Since this builds upon the data provided to the Citizen via the Summary Information Record, the Detailed Coded Record cannot be enabled without the Summary Information Record also being enabled.

#### View Documents {#CitizenServicesImplementationGuidance-ViewDocuments}

View Documents builds on the data already made available through the Summary Information Record and Detailed Coded Record datasets, but also includes the ability for Citizens to be able to view all clinical and administrative documents (inc. Pathology and Radiology test results) made available by the GP Practice.

The Documents dataset is defined [here](https://simplifier.net/guide/GP-Connect-Patient-Facing-Access-Record/Home/Build/Permission-Levels?version=current).

Citizens will not be able to view any clinical or administrative documents until they have been reviewed by the GP Practice. Typically this would mean the documents are marked as ‘Restricted from View Record’ until a review has taken place and the document deemed appropriate to be displayed online to the Citizen.

#### View Full Record {#CitizenServicesImplementationGuidance-ViewFullRecord}

View Full Record builds on the data already made available through the previous levels and the Full Patient Record dataset is defined [here](https://simplifier.net/guide/GP-Connect-Patient-Facing-Access-Record/Home/Build/Permission-Levels?version=current).

### Individual Elements of Patient Record - ‘Restricted from View Record’ {#CitizenServicesImplementationGuidance-IndividualElementsofPatientRecord-‘RestrictedfromViewRecord’}

In addition to the different levels of access to the Patient Record, individual elements of the Patient Record can also be marked as ‘Restricted from View Record’ allowing specific elements of the Patient Record to be hidden from Citizens when viewing the Patient Record information online.

All/any elements of a Patient Record marked as 'Restricted from View Record' will not be displayed by the View Record - Citizen Solution to the Patient irrespective of Record Access Level configuration.

For example, where Service Configuration determines Detailed Coded Record enabled with a Start Date of 1st February 2013 but a Clinician has reviewed a Patient’s Record back to 1st January 2010, any elements of the Patient Record not marked as ‘Restricted from View Record’ as part of the Record review/preparation (between January 2010 and February 2013) to display in addition to those displaying due to the Detailed Coded Record configuration.

## Prescription Ordering - Citizen {#CitizenServicesImplementationGuidance-PrescriptionOrdering-Citizen}

Functionality allowing Citizens to manage requests for Repeat medication and EPS Nominated Pharmacy preferences online either for themselves or on behalf of someone else (as a Proxy) will be provided by the [Prescription Ordering - Citizen](../DSIC-Capabilities/Prescription-Ordering-Citizen.md) Solution. This functionality may also allow Citizens to manage requests for Acute medication, Preferred Pharmacy preferences and view additional medication information (e.g. how to use it and the implications of doing so).

Any submitted medication requests or Pharmacy preference changes will be received and managed by the [Prescribing](../DSIC-Capabilities/Prescribing.md) Solution through the provision and consumption of Patient interfaces as per the [IM1 - Interface Mechanism](../DSIC-Standards/Non-Overarching-Standards/IM1-Interface-Mechanism.md) Standard or [GP Connect (Patient Facing) Prescriptions](../DSIC-Standards/Non-Overarching-Standards/GP-Connect-Patient-Facing-Prescriptions.md) Standard.

## Enabling/Disabling Citizen Services {#CitizenServicesImplementationGuidance-Enabling/DisablingCitizenServices}

The enabling and disabling of the above Citizen Services at both a Patient and Practice level will be configured by the GP Practice using the [Patient Information Maintenance - GP](../DSIC-Capabilities/Patient-Information-Maintenance-GP.md) Solution. It is recommended that the ability for Health or Care Professionals to record a reason when disabling Citizen Services is provided by this Solution.

## Attachments

- [Example Citizen Services Process - Integrated Solutions.png](../../../.raw/DCSDCS/attachments/11962974263/att11962974293-Example Citizen Services Process - Integrated Solutions.png)
- [Example Citizen Services Process - Single Solution.png](../../../.raw/DCSDCS/attachments/11962974263/att11962974296-Example Citizen Services Process - Single Solution.png)
- [Account Structure and Relationships.png](../../../.raw/DCSDCS/attachments/11962974263/att11962974299-Account Structure and Relationships.png)
- [Account Types.png](../../../.raw/DCSDCS/attachments/11962974263/att11962974302-Account Types.png)
- [Example Account Lifecycle.png](../../../.raw/DCSDCS/attachments/11962974263/att11962974305-Example Account Lifecycle.png)
- [Citizen access diagram.png](../../../.raw/DCSDCS/attachments/11962974263/att11962974308-Citizen access diagram.png)
- [Example - IM1 Interface Mechanism.png](../../../.raw/DCSDCS/attachments/11962974263/att14373584953-Example - IM1 Interface Mechanism.png)
- [Example - GP Connect Patient Facing APIs.png](../../../.raw/DCSDCS/attachments/11962974263/att14373847097-Example - GP Connect Patient Facing APIs.png)
- [Scenario 3 - Citizen Services Process - Integrated Solutions (GP Connect Patient Facing APIs).png](../../../.raw/DCSDCS/attachments/11962974263/att14374174813-Scenario 3 - Citizen Services Process - Integrated Solutions (GP Connect Patient Facing APIs).png)
- [Scenario 1 - Citizen Services Process - Single Solution.png](../../../.raw/DCSDCS/attachments/11962974263/att14374666338-Scenario 1 - Citizen Services Process - Single Solution.png)
- [Scenario 2 - Citizen Services Process - Integrated Solutions (IM1 - Interface Mechanism).png](../../../.raw/DCSDCS/attachments/11962974263/att14374699099-Scenario 2 - Citizen Services Process - Integrated Solutions (IM1 - Interface Mechanism).png)
