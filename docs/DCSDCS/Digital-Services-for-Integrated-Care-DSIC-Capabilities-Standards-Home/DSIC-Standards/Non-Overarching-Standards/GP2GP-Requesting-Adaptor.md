---
page_id: "12512034968"
space: "DCSDCS"
title: "GP2GP Requesting Adaptor"
version: 13
updated: "2026-07-22T08:02:04.149Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12512034968/GP2GP+Requesting+Adaptor"
labels: ["standard"]
---

# GP2GP Requesting Adaptor

|  |  |
| --- | --- |
| **ID** | S94 |
| **Version** | 1.0.2 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 22 Oct 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#GP2GPRequestingAdaptor-Introduction)
- [Requirements](#GP2GPRequestingAdaptor-Requirements)
  - [Registration Process & EHR Request](#GP2GPRequestingAdaptor-RegistrationProcess&EHRRequest)
    - [Step 1 - Patient Registration](#GP2GPRequestingAdaptor-Step1-PatientRegistration)
    - [Step 2 - User performs PDS Trace](#GP2GPRequestingAdaptor-Step2-UserperformsPDSTrace)
    - [Step 3 - Requesting System - Lookup previous ODS code on PDS](#GP2GPRequestingAdaptor-Step3-RequestingSystem-LookuppreviousODScodeonPDS)
    - [Step 4 - Requesting System Query ODS for previous GP Practice details](#GP2GPRequestingAdaptor-Step4-RequestingSystemQueryODSforpreviousGPPracticedetails)
    - [Step 5 - Requesting System updates PDS](#GP2GPRequestingAdaptor-Step5-RequestingSystemupdatesPDS)
    - [Step 6 - Query SDS API for Provider ASID](#GP2GPRequestingAdaptor-Step6-QuerySDSAPIforProviderASID)
    - [Step 7 - Build request to migrate structured record](#GP2GPRequestingAdaptor-Step7-Buildrequesttomigratestructuredrecord)
  - [GP2GP Requesting Adaptor converts and sends HL7 request](#GP2GPRequestingAdaptor-GP2GPRequestingAdaptorconvertsandsendsHL7request)
    - [Step 8 - Requesting Adaptor validates request](#GP2GPRequestingAdaptor-Step8-RequestingAdaptorvalidatesrequest)
    - [Step 9 - Requesting Adaptor validates request](#GP2GPRequestingAdaptor-Step9-RequestingAdaptorvalidatesrequest)
  - [Providing the EHR Process](#GP2GPRequestingAdaptor-ProvidingtheEHRProcess)
    - [Step 10 - Sending Site validates the HL7 request](#GP2GPRequestingAdaptor-Step10-SendingSitevalidatestheHL7request)
    - [Step 11 - Sending Site generates the HL7 EHR](#GP2GPRequestingAdaptor-Step11-SendingSitegeneratestheHL7EHR)
    - [Step 12 - Sending Site sends the HL7 EHR](#GP2GPRequestingAdaptor-Step12-SendingSitesendstheHL7EHR)
  - [Conversion and retrieval of the EHR Process](#GP2GPRequestingAdaptor-ConversionandretrievaloftheEHRProcess)
    - [Step 13 - GP2GP Requesting Adaptor converts HL7 EHR to GP C Payload](#GP2GPRequestingAdaptor-Step13-GP2GPRequestingAdaptorconvertsHL7EHRtoGPCPayload)
    - [Step 14 - Requesting System polls the adaptor](#GP2GPRequestingAdaptor-Step14-RequestingSystempollstheadaptor)
  - [Prepare to integrate the record](#GP2GPRequestingAdaptor-Preparetointegratetherecord)
    - [Step 15 - Validate incoming FHIR record](#GP2GPRequestingAdaptor-Step15-ValidateincomingFHIRrecord)
    - [Step 16 - Identifying and retrieving attachments](#GP2GPRequestingAdaptor-Step16-Identifyingandretrievingattachments)
  - [Integrate the record](#GP2GPRequestingAdaptor-Integratetherecord)
    - [Step 17 - Automatic Integration of the Record Bundle](#GP2GPRequestingAdaptor-Step17-AutomaticIntegrationoftheRecordBundle)
    - [Step 18 - Post integration actions](#GP2GPRequestingAdaptor-Step18-Postintegrationactions)
    - [Step 19 - Returning Patients/A-B-A Transfers](#GP2GPRequestingAdaptor-Step19-ReturningPatients/A-B-ATransfers)
    - [Step 20 - Handling Degrades](#GP2GPRequestingAdaptor-Step20-HandlingDegrades)
    - [Step 21 - Audit Requirements](#GP2GPRequestingAdaptor-Step21-AuditRequirements)
  - [Internal Transfers](#GP2GPRequestingAdaptor-InternalTransfers)
  - [User Experience](#GP2GPRequestingAdaptor-UserExperience)
    - [User stories](#GP2GPRequestingAdaptor-Userstories)
  - [Appendix A - Negative Acknowledgments](#GP2GPRequestingAdaptor-AppendixA-NegativeAcknowledgments)
    - [Sending System Negative Acknowledgements](#GP2GPRequestingAdaptor-SendingSystemNegativeAcknowledgements)
    - [GP2GP Requesting Adaptor Negative Acknowledgments](#GP2GPRequestingAdaptor-GP2GPRequestingAdaptorNegativeAcknowledgments)
  - [Appendix B - Primary Care Support England (PCSE)](#GP2GPRequestingAdaptor-AppendixB-PrimaryCareSupportEngland(PCSE))
  - [Appendix C - Suspended and Orphaned Records](#GP2GPRequestingAdaptor-AppendixC-SuspendedandOrphanedRecords)
    - [Suspended Patients](#GP2GPRequestingAdaptor-SuspendedPatients)
    - [Orphaned Records](#GP2GPRequestingAdaptor-OrphanedRecords)
  - [Appendix D - Further information on Attachments](#GP2GPRequestingAdaptor-AppendixD-FurtherinformationonAttachments)
    - [Important Information on the failure to retrieve](#GP2GPRequestingAdaptor-ImportantInformationonthefailuretoretrieve)
    - [GP Connect Attachment Placeholder](#GP2GPRequestingAdaptor-GPConnectAttachmentPlaceholder)
    - [Sending Site failure [Existing GP2GP placeholder behaviour]](#GP2GPRequestingAdaptor-SendingSitefailure[ExistingGP2GPplaceholderbehaviour])
    - [File Size](#GP2GPRequestingAdaptor-FileSize)
- [Dependencies](#GP2GPRequestingAdaptor-Dependencies)
- [Roadmap](#GP2GPRequestingAdaptor-Roadmap)

# Introduction

The GP2GP Requesting Adaptor is designed to allow a System Supplier who does not have GP2GP HL7 and instead uses [GP Connect Access Record Structured](GP-Connect-Access-Record-Structured.md) to request an Electronic Health Record (EHR) from a System Supplier using GP2GP HL7. Specifically, this uses ‘Migrate a Patient’s structured record' and ‘Migrate a document’.

This page documents the details of how the Requesting System will interact with the GP2GP Requesting Adaptor. It also details the requirements of the Requesting Site (the GP Practice the Patient is registering with) around the initial registration process and then ingesting/filing the received EHR from the Sending Site.

# Requirements

## Registration Process & EHR Request

The following section details the initial registration steps that are required before the request for the registering Patients Electronic Health Record from their previous practice can begin via GP2GP and the Requesting Adaptor.

### Step 1 - Patient Registration

The first step is for the Patient to provide their demographic details e.g. name, NHS number, address to the GP Practice staff, who will then in turn access PDS.

|  |  |  |
| --- | --- | --- |
| **Patient Registration** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_01** | Only Patients registering for GMS1 Permanent registrations qualify for the electronic transfer of Patient records (GP2GP). Any other Patient registration type (e.g. temporary/private) does not qualify for GP2GP. | MUST |
| **GP2GP\_Req\_02** | If the Patient was registered at the Requesting site under any other registration status (e.g. private or temporary) and then applies to become a GMS1 Permanent Patient, it is necessary for the Requesting system to still initiate the request for the EHR from the Sending site. | MUST |
| **GP2GP\_Req\_03** | The Requesting System will limit access to perform permanent Patient registrations, PDS Advanced Trace and PDS General Update interactions to only users who have the appropriate RBAC permissions as defined in the PDS requirements. | MUST |
| **GP2GP\_Req\_04** | If there is no response from PDS (it is unavailable and error has been received) then the user would benefit from being prompted to contact the National Help Desk or their Clinical System Supplier Help Desk to resolve the issue.  The GP2GP process will end until such time is PDS available and a user with appropriate permissions logs in again to perform a PDS trace to find and register the Patient. | SHOULD |
| **GP2GP\_Req\_05** | In the exceptional scenario where PDS is unavailable, and there is a critical need to record information about the Patient, functionality is accessible to allow a user to electronically record information about the Patient until such time as PDS is available so as to provide continuity of care. | MUST |

### Step 2 - User performs PDS Trace

The GP Practice staff member will now attempt to trace (find) the Patient on PDS

|  |  |  |
| --- | --- | --- |
| **PDS Trace** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_06** | The user will now need to search for the Patient on PDS in line with their guidance:  [Personal Demographics Service - FHIR API](https://digital.nhs.uk/developer/api-catalogue/personal-demographics-service-fhir#api-Default-search-patient) | MUST |
| **GP2GP\_Req\_07** | The Requesting system will not automatically select a Patient from the search results, irrespective of the number of results.  i.e. if only one Patient is returned they should not be auto-selected. | MUST |
| **GP2GP\_Req\_08** | The user needs to select a Patient from the PDS trace results if they wish to continue the registration.  If the PDS search fails to identify the Patient then then there is no previous registration available and no transfer of an EHR is possible. | MUST |
| **GP2GP\_Req\_09** | If the PDS record is flagged as ‘sensitive’ then it cannot be updated and the electronic transfer of the EHR cannot proceed. There is a separate manual process via National Back Office and PCSE to deal with the transfer of Patients records who are flagged as sensitive. | MUST |

Now that the GP Practice Staff member has selected a Patient to register, the Requesting System must follow the steps below to complete the request for the EHR to send to the GP2GP Requesting Adaptor.

![](https://nhse-dsic.atlassian.net/wiki/download/attachments/12512034968/ReqAdptSteps1234.jpg?api=v2)

### Step 3 - Requesting System - Lookup previous ODS code on PDS

The Requesting System will now lookup the Patients current registered ODS code on PDS (the one the Patient is currently registered at and the Requesting System will be requesting the EHR from). This needs to be performed before the Requesting Site updates PDS as in Step 5, otherwise its ODS code will be that of the Patients on PDS.

|  |  |  |
| --- | --- | --- |
| **Lookup previous ODS code** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_10** | If the user identifies and selects a Patient from the PDS trace that is unique and not ‘sensitive’ then the Requesting System will need to store and persist the data item `generalPractitioner` field on PDS. This is the ODS code of the Patients current registered GP Practice and this will be used to identify and make the electronic request for the transfer from that site. | MUST |
| **GP2GP\_Req\_11** | If the `generalPractitioner`ODS Code is the same as the Requesting Site then the electronic transfer of the EHR process ends**.** This is because the Patient is already registered at the practice. | MUST |
| **GP2GP\_Req\_12** | If the `generalPractitioner` ODS Code of the Sending Site is identified as a GP Practice on the same GP Clinical System as the Requesting Site, then the Requesting System will follow the requirements as described in the ‘Internal Transfers’ requirements found on this page. | MUST |
| **GP2GP\_Req\_13** | Should the `generalPractitioner` data item be null, then the Requesting System queries the PDS `managingOrganisation` field. If this is populated with an ODS code, it will then store this value. This will be the ODS code of either the Patients last previous registered GP Practice or the NHS England repository (Please see Appendix C for more details). | MUST |

### Step 4 - Requesting System Query ODS for previous GP Practice details

The Requesting System will now query ODS for the details of the Patients current registered GP Practice.

The information retrieved from the ODS API about the current GP Practice is purely so the the user (GP Practice Staff) has access to contact details for the Sending Site should there be any queries about the transfer of the EHR. It will not prevent the processing of the GP2GP request.

|  |  |  |
| --- | --- | --- |
| **Lookup previous ODS code** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_14** | The Requesting System will now retrieve the following details of the previous GP Practice using the ODS API:   - Practice Name - Practice Address - Practice Telephone number   This is purely so the user has access to information that may help them in contacting the Sending System in case of any issues with the EHR transfer. | MUST |
| **GP2GP\_Req\_15** | The Requesting System will display the previous practice details obtained to the user registering the Patient. | MUST |
| **GP2GP\_Req\_16** | This information needs to be cached and the most up to date details made available. This is to allow any necessary follow up should the user need to contact the previous GP Practice. | MUST |
| **GP2GP\_Req\_17** | The failure to obtain the previous GP Practice details from ODS does not prevent the Requesting System from initiating the electronic transfer of the EHR from the Sending Site. | MUST |

### Step 5 - Requesting System updates PDS

Now the Requesting System has obtained the Patients current GP Practice details it will now update PDS to indicate they are now the registered GP Practice.

|  |  |  |
| --- | --- | --- |
| **Update PDS** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_18** | Once the user has selected a Patient to be registered the Requesting System will update PDS (after obtaining the Sending Practice ODS code from PDS as in Step 3). This will set the Patients GP Practice code to that of the Requesting System (the GP Practice the Patient is registering at) on PDS and the registration date. | MUST |
| **GP2GP\_Req\_19** | The PDS update interaction is an synchronous transaction and the Requesting System waits for a PDS Successful Update Response. | MUST |
| **GP2GP\_Req\_20** | If an error is received indicating a failure to update PDS, then the GP2GP process ends as the Patient has not been registered. | MUST |
| **GP2GP\_Req\_21** | If an error is encountered updating PDS the user is to be prompted to contact the National Help Desk or their Clinical System Supplier Help Desk to resolve the issue.  Note: PDS system retries are not possible, but if the user is present and logged in with the appropriate RBAC permissions they may attempt to re-register the Patient. | SHOULD |
| **GP2GP\_Req\_22** | On receiving a PDS Successful Update Response the following steps are now triggered by the Requesting System to transfer the EHR using the GP2GP Requesting Adaptor | MUST |

### Step 6 - Query SDS API for Provider ASID

The Requesting System will now need to retrieve the Accredited System Identifier of the Sending Site (now the Patients previous GP Practice). These are required so they can be passed to the GP2GP Requesting Adaptor so it can route the request via Spine Message Handling Service (MHS).

|  |  |  |
| --- | --- | --- |
| **Retrieve ASID details** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_23** | The Requesting System performs the GP2GP process only with the previously registered GP Practice ODS details retrieved in Step 3 obtained from PDS. | MUST |
| **GP2GP\_Req\_24** | The Requesting System queries SDS for the Patients previous GP Practice ASID (Accredited System Identifier) which is needed to create the request to the GP2GP Requesting Adaptor GPC API Facade endpoint.  To query SDS for the Provider ASID it will need   - The previous GP Practice ODS code obtained from PDS in Step 3 - The GP2GP Service Identifier: `urn:nhs:names:services:gp2gp:RCMR_IN010000UK05`   Further detail on the SDS API can be found here [Spine Directory Service - FHIR API](https://digital.nhs.uk/developer/api-catalogue/spine-directory-service-fhir) | MUST **T** |
| **GP2GP\_Req\_25** | If the lookup to SDS fails or no ASID exists for any reason (e.g. the previous practice was a Defence Medical Services that does not support GP2GP) then the GP2GP process cannot proceed as the Sending Site end point has not been identified. The GP2GP status for this transfer in the workflow will be marked as ‘failed’ and will indicate that the user must contact the Sending Site as no GP2GP request was made. | MUST |
| **GP2GP\_Req\_26** | The Requesting System is permitted to perform a retry of the lookup to SDS if the error returned is a timeout. | MAY |
| **GP2GP\_Req\_27** | If the error persists the user is to be prompted that an error has occurred and the GP2GP process will not proceed until the system issue has been resolved. | SHOULD |
| **GP2GP\_Req\_28** | The failure to perform the lookup on SDS results in the automatic generation of a ticket to the Requesting System Service Desk | SHOULD |
| **GP2GP\_Req\_29** | If the SDS lookup is successful then the Requesting System will need to build the request for the GP2GP Requesting Adaptor | MUST |

### Step 7 - Build request to migrate structured record

The GP2GP Requesting Adaptor provides a GP Connect like API facade. The Requesting System will now need to build the request for the EHR and post this to the facade to initiate the EHR transfer..

|  |  |  |
| --- | --- | --- |
| **Retrieve ASID details** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_30** | The Requesting System now constructs and posts the bespoke migratestructuredrecord request to the Requesting Adaptor GPC API Facade endpoint URL (`POST /Patient/$gpc.migratestructuredrecord`)  The following is required to call this endpoint   - TO\_ASID: The ASID identifier of the Requesting Site - FROM\_ASID: The ASID identifier of the Sending Site - TO\_ODS: The ODS identifier of the Requesting Site - FROM\_ODS: the ODS identifier of the Sending Site - ConversationId : A unique GUID for each request; if a ConversationId is not provided, the Requesting Aadaptor will create one and return it in the response headers. | MUST |
| **GP2GP\_Req\_31** | The Requesting System uses only the Sending System (Providers) ASID as obtained from the SDS Query in Step 6 and the Sending System (Providers) ODS code obtained from Step 3. | MUST |
| **GP2GP\_Req\_32** | The ConversationId is retained by the Requesting System and used for all further calls for the Patient’s NHS number (this EHR transfer) | MUST |
| **GP2GP\_Req\_33** | The endpoint also requires a JSON body that includes the Patient NHS number. The format of the body is as follows:  {  "resourceType": "Parameters",  "parameter": [  {  "name": "PatientNHSNumber",  "valueIdentifier": {  "system": "[https://fhir.nhs.uk/Id/nhs-number",](https://fhir.nhs.uk/Id/nhs-number%22,)  "value": "{{nhs-number-test-group-8}}"  }  },  {  "name": "includeFullRecord",  "part": [  {  "name": "includeSensitiveInfomation",  "valueBoolean": true  }  ]  }  ]  } | MUST |
| **GP2GP\_Req\_34** | As soon as the Requesting System has posted the GP C migratestructuredrecord request to the Requesting Adaptor GPC API Facade endpoint URL it should receive a 202-accepted response. This means the adaptor has received the request and is validating and making the relevant requests. The Requesting System now begins to poll the endpoint for a response. Polling details are set out in Step 14. | MUST |

![](https://nhse-dsic.atlassian.net/wiki/download/attachments/12512034968/ReqAdpSteps567.jpg?api=v2)

## GP2GP Requesting Adaptor converts and sends HL7 request

### Step 8 - Requesting Adaptor validates request

The GP2GP Requesting Adaptor has now received the Requesting Site GP Connect migratestructuredrecord request.

It will now take the following actions

- Check the message is well formed (it can retrieve the NHS number of the Patient in the request)
- Checks the url of the recipient GP2GP endpoint to ensure it is compliant using the MHS Adaptor

 If the body is malformed in a way that the NHS number cannot be extracted the Migrate Structured endpoint will respond with `422 Unprocessable Entity` and an Operation Outcome of `INVALID_RESOURCE`:

The `Content-Type` header must equal `application/fhir+json` otherwise the response will be `415 Unsupported Media Type`.

If any of the following headers are missing, then the Migrate Structured endpoint will respond with `400 Bad Request`.

- `to-asid`
- `from-asid`
- `to-ods`
- `from-ods`

Any errors will be posted to the GPC API Facade endpoint URL and the request for the EHR will not be processed and this is is picked up by the Requesting System in Step 14.

### Step 9 - Requesting Adaptor validates request

The Requesting Adaptor will now attempt to convert the migratestructuredrecord request to a HL7 request. Should the conversion fail or cannot be sent for any reason it will generate a `500 Internal Server Error` and post to the GP C Facade endpoint URL. The the request for the EHR will not be processed and this is is picked up by the Requesting System when polling the Adaptor in step 14.

Provided the above steps are successful then the Requesting Adaptor will now send the HL7 request to the Sending System via Spine.

## Providing the EHR Process

There are no changes to the process for existing System Suppliers using GP2GP HL7. So as to provide context this is a high level overview of the steps taken in GP2GP for the Sending Site once it has received the HL7 request.

Please note in the case of failure, all HL7 negative acknowledgements have been mapped to appropriate GP Connect error codes (Please see Appendix A). These will be provided to the Requesting System via the GP2GP Requesting Adaptor as in Step 14 so it can take the appropriate action.

### Step 10 - Sending Site validates the HL7 request

As per the GP2GP 2.2b v7.2 HL7 Requirements

*The Sending system shall automatically check the local Patient index for the NHS Number supplied on the EHR Request, populating the Application Acknowledgement with response code 06 if the Patient is not registered at the practice.*

*The Sending system must query PDS to ensure the registered GP Practice details are consistent with the EHR Request before the EHR Response is sent. If the current GP Practice on PDS does not match the Requesting practice the Sending system must return a negative acknowledgement with Response code 19 (Requesting practice is not the Patient’s current primary healthcare provider)*

*A negative application acknowledgement message shall also be returned if an EHR Request that cannot be fulfilled for other reasons, including GP2GP messaging not enabled (End Point setup but GP2GP configuration switched OFF) (Response code 07)*

### Step 11 - Sending Site generates the HL7 EHR

The Sending Site will now generate the EHR. If any attachments fail to be retrieved placeholders will be created. This will generate tasks for users to print these attachments that will then be sent manually off system via PCSE (Please see Appendix B for further information on PCSE)

If the Sending Site fails to generate the EHR extract it will send a negative acknowledgement (Response code 10)

### Step 12 - Sending Site sends the HL7 EHR

The Sending Site will now commence thesending of any Common Point to Point messages that form part of the EHR extract.

The Sending system will commence thesending of any Common Point to Point messages that form part of an EHR Extract immediately after a “continue” response is received from the GP2GP Requesting Adaptor.

The GP2GP Requesting Adaptor will not attempt to convert the HL7 message to FHIR until all Common Point to Point messages have been received.

## Conversion and retrieval of the EHR Process

### Step 13 - GP2GP Requesting Adaptor converts HL7 EHR to GP C Payload

The GP2GP Requesting Adaptor will now convert the HL7 record to GP Connect FHIR.

It will also parse all the documents (including any .txt placeholders) from the HL7 file and write them individually to the file storage of the GP2GP Requesting Adaptor so they can be individually retrieved by the Requesting System directly from the S3 file storage.

At this point it will provide a `200 response` and the GP Connect payload to GP Connect API Facade endpoint URL.

Should the conversion have failed it will provide a `500 Internal Server Error` error. This will be posted to the GP Connect API Facade endpoint URL. It will also post a HL7 ack to the incumbent sending site `Error 11 Failed to successfully integrate EHR Extract` so the incumbent system is aware to alert its users to print the EHR and send via PCSE.

### Step 14 - Requesting System polls the adaptor

The Requesting System will need to continually poll the adaptor to retrieve the outcome of any GP2GP transfer.

If the request has been successfully fulfilled by the Sending Site and converted by the adaptor it can validate the FHIR payload, retrieve the documents and integrate the record.

Should it determine there has been a failure in processing the request it will need to determine the failure point and alert its users appropriately.

|  |  |  |
| --- | --- | --- |
| **Retrieve ASID details** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_35** | It is the responsibility of the Requesting System to ensure that the GP2GP Requesting Adaptor is monitored and available at all times so as to process any GP2GP EHR requests and responses. | MUST |
| **GP2GP\_Req\_36** | As described in Step 7, once the request has been made the Requesting System polls the GP C Façade endpoint of the GP2GP Requesting Adaptor. This is done initially at a a maximum timeframe of 120 seconds | MUST |
| **GP2GP\_Req\_37** | If a HTTP code 204 response is returned the request is in progress and the Requesting Site polls again at regular intervals.  *The following are suggested intervals but these can be agreed at the time of assurance:*   - *5 minutes* - *10 minutes* - *20 minutes* - *40 minutes* - *60 minutes* - *120 minutes* - *240 minutes*   *Then continually every 480 minutes.* | MUST |
| **GP2GP\_Req\_38** | If a 200 OK/completed GP C HTTP response has been returned and the EHR payload has been successfully delivered then the Requesting System now follows the requirements in Step 15 | MUST |
| **GP2GP\_Req\_39** | If the Requesting System identifies any Operational Outcome (error) then it must mark the transfer as failed and the GP2GP process ends. Please see Appendix A (Negative Acknowledgments) for further information. | MUST |
| **GP2GP\_Req\_40** | The Requesting System must make the user aware that the process has failed for this GP2GP transfer and whether they should expect the printed EHR from the Sending Site via PCSE. Please see Appendix A (Negative Acknowledgments) for further information. | MUST |
| **GP2GP\_Req\_101** | Where a GP2GP transfer has failed, the Sending Site may attempt a re-send of the EHR. The Requesting System will need to allow receipt of a re-sent EHR that has the same Conversation ID of the EHR that previously failed. The Requesting System will also update its GP2GP workflow associated with the outcome of the resend (if it fails again or is successful). | MUST |

## Prepare to integrate the record

This initial step ensures that the record bundle the NME Requesting Site retrieves is of a format that is valid and can be integrated, before it identifies and retrieves its associated documents.

### Step 15 - Validate incoming FHIR record

|  |  |  |
| --- | --- | --- |
| **Validation** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_41** | When the Requesting System polls the GP C Facade endpoint of the GP2GP Requesting Adaptor and received a 200 completed HTTP Operational Outcome it will then retrieve the FHIR structured record from the GP2GP Requesting Adaptor. | MUST |
| **GP2GP\_Req\_42** | The Requesting System validates the incoming EHR and retrieves all documents before committing the EHR to its database | MUST |
| **GP2GP\_Req\_43** | The Requesting System ensures the structured record bundle is well formed and contains all the necessary resources/profiles | MUST |
| **GP2GP\_Req\_44** | For the avoidance of doubt the validation does not involve any user involvement, it is strictly a system based validation. | MUST |
| **GP2GP\_Req\_45** | The Requesting System ensures that any validation on the incoming record bundles Patient profile does not prevent it from accepting the record without the Patient name\* | MUST |
| **GP2GP\_Req\_46** | If the initial validation is successful the Requesting System now identifies and retrieve all associated documents. | MUST |
| **GP2GP\_Req\_47** | If the Requesting System identifies any issues with the GP C structured record bundle provided it will provide the following error to the GP2GP Requesting Adaptor  Endpoint facadelocation/$gpc.ack  With the following:  header fields: confirmationResponse : “failed\_to\_integrate“, conversationID: “string“  The GP2GP Requesting Adaptor will then convert this to the appropriate HL7 negative acknowledgment:  `Error code: 11 [Failed to successfully integrate EHR Extract]` | MUST |
| **GP2GP\_Req\_48** | In the case of failure the Requesting System updates the GP2GP transfer status as failed | MUST |
| **GP2GP\_Req\_49** | In the case of failure the Requesting System makes the user aware that validation has failed and no EHR will be available and a printed EHR and attachments will be provided by the Sending Site via PCSE. | MUST |

#### Re GP2GP\_Req\_45:

GP Connect mandates a sending system to provide the Patient name and the NHS number in the Patient profile when providing a record. In GP2GP HL7 the EHR is not provided with the Patient name only the NHS number. As the GP2GP Requesting adaptor is converting the HL7 record this requirement has been relaxed for the adaptor only as it is a GP Connect Façade API. The GP2GP Requesting adaptor will convert the HL7 to GP Connect and will not provide the Patient name (as it has not received this information in the GP2GP HL7 EHR). This mimics current GP2GP HL7 behaviour. The Requesting System (the NME in this case) will already have the Patient name on their system from the PDS trace and Patient registration process.

### Step 16 - Identifying and retrieving attachments

Document references returned are identified within the Patient’s structured record identified via `"resourceType": "DocumentReference"`. The key pieces of information are in the `"attachment"` section which provides the mime-type of the file (MSWord, PDF, etc.), and the URL to retrieve the file and its size on disk in bytes.

|  |  |  |
| --- | --- | --- |
| **Identify attachments** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_50** | Having checked that this is a well formed structured record the Requesting System then parses the file and identifies if there are any document references. | MUST |
| **GP2GP\_Req\_51** | The Requesting System now establishes the number of documents within the structured record bundle and creates a cached status against each document. | MUST |
| **GP2GP\_Req\_52** | The Requesting System now attempts to retrieve each document using the URL supplied in the `"DocumentReference"`. This URL will point to the the GP2GP Requesting Adaptor File Storage. | MUST |
| **GP2GP\_Req\_53** | The Requesting System attempts to retrieve all attachments regardless of the size of the attachment (no upper limits are to be set). Please see the section on file size below in [Appendix D](GP2GP-Requesting-Adaptor.md). | MUST |
| **GP2GP\_Req\_54** | The Requesting System keeps track of each documents status. A document transfer can have a status of   - Completed (successfully retrieved) - Failed (error) - In Progress (no outcome has been received or the migrate document request is in progress) | MUST |
| **GP2GP\_Req\_55** | If the Requesting System identifies that either:   - all documents where successfully retrieved - there are no documents contained in the structured record `"DocumentReference"`   Then it proceeds to Step 17 (Prepare to integrate) | MUST |
| **GP2GP\_Req\_56** | If the Requesting System encounters an error when trying to retrieve an attachment(s) from the GP2GP Requesting Adaptor storage then it creates an automatic Service Desk alert/ticket for the Requesting System support team. | SHOULD |
| **GP2GP\_Req\_57** | If the issue cannot be resolved within 1 hour, then the Requesting System creates a placeholder. This is so as not to delay the integration of the EHR because of a failed document(s) | MUST |
| **GP2GP\_Req\_58** | The placeholder is a file that is text with a ‘txt’ suffix and MIME type text/plain. | MUST |
| **GP2GP\_Req\_59** | The file is named as follows:  **AbsentAttachment\_[description]\_[Owning Organisation ODS Code]\_[Date created].txt**  Where [id] is the GP Connect ‘Document Reference Id’ and [description] is the Document Reference ‘Description’.  For example: **AbsentAttachment\_discharge summary\_A12345\_18012022.txt**  The title is labelled with these data items to make it clear what the document is, when it was created and who was the original owner. This is to help users identifying attachments, especially with the pain point where a record moves from A-B-C, where B has missing attachments from A and then C has missing attachments from both A and B and needs to be able to clearly identify where the missing attachments came from originally. | MUST |
| **GP2GP\_Req\_60** | Within the placeholder file the text is as set out in Appendix D - GP C placeholder.  An example is provided here  [AbsentAttachment\_example](GP2GP-Requesting-Adaptor.md) | MUST |
| **GP2GP\_Req\_61** | Once all placeholders have been created the Requesting System proceeds to Step 17 | MUST |
| **GP2GP\_Req\_62** | The Requesting System alerts its users to any placeholders it has created (i.e. document could not be retrieved) and that the user will need to contact the Sending Site should they want a copy. Further information can be found in Appendix D. | MUST |
| **GP2GP\_Req\_63** | If after the record has been integrated (the completion of Step 17) either   - the Requesting System reaches a resolution on the service incident raised in requirement **GP2GP\_Req\_56** and is able to successfully retrieve the attachment - The user is able to obtain an electronic copy of an attachment from the Sending Site   The Requesting System has the functionality to allow the user todelete the .txt placeholder and insert the retrieved document it related to.  This is because it is preferable to have a placeholder replaced with the actual document so as not to ensure the attachment is available and to prevent the propagation of placeholders in onward transfers | SHOULD |

## Integrate the record

Once the the electronic Patient record has been validated and all documents retrieved (or placeholders created) the Requesting System will now look to integrate/file all elements into its database, this is all done without any user interaction.

### Step 17 - Automatic Integration of the Record Bundle

The following must have occurred before integration of the record can take place.

- The NME Requesting System has polled the GP C Façade endpoint of the GP2GP Requesting Adaptor and received a 200 completed HTTP Operational Outcome that includes the Patient record bundle (EHR).
- All attachments identified in the Patient record bundle (EHR) have either

  - been successfully retrieved from the Requesting Adaptor local file storage
  - failed and the Requesting System has generated a placeholder

The following set of requirements follow the same principal for auto-integration, but the wording has changed as they only apply to suppliers who are using the GP2GP Requesting Adaptor and there are slight changes in behaviour.

|  |  |  |
| --- | --- | --- |
| **Integrate the EHR** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_64** | EHRs are automatically integrated by the Requesting system immediately, without delay after they have been received. (As a performance measure, EHRs are to be integrated within 20 minutes of receipt). | MUST |
| **GP2GP\_Req\_65** | Automatic integration is a System based activity, thereis no user involvement in triggering the integration task. | MUST |
| **GP2GP\_Req\_66** | Requesting System Users are not prevented from accessing and using the Requesting System whilst the integration system task is being processed.  For example: A User mustbe able to use the Requesting System to book an appointment, open a EHR or add a consultation whilst the Requesting System is performing integration processes. | MUST |
| **GP2GP\_Req\_67** | The Requesting System handles the following scenarios in such a way as to prevent loss of data during automatic integration:   - The local EHR for a Patient is being accessed or updated by a Requesting System User when a GP2GP EHR is received for the same Patient. - A Requesting System User attempts to access a local EHR whilst the automatic integration is in progress. | MUST |
| **GP2GP\_Req\_68** | The Requesting System only performs a full integration, there is no concept of a partial integration of the Patients EHR. (e.g. integrating Observations, Medications and not integrating Allergies is not allowed) | MUST |
| **GP2GP\_Req\_69** | If the integration of the record is successful then the Requesting System provides the following success message to the GP2GP Requesting Adaptor:  Endpoint facadelocation/`$gpc.ack/`  With the following:  header fields: confirmationResponse : “accepted“, conversationID: “string”  The GP2GP Requesting Adaptor will then convert this to the appropriate HL7 Positive acknowledgment  `<acknowledgement typeCode = “AA”>` | MUST |
| **GP2GP\_Req\_70** | If the automatic integration system task cannot be started, completed or fails to integrate, the Requesting System creates an automatic Service Desk alert/ticket for the Requesting System support team. | SHOULD |
| **GP2GP\_Req\_71** | The Requesting System creates an alert for the user to let them know that the integration has failed and is being investigated along with the ticket ID. | SHOULD |
| **GP2GP\_Req\_72** | The failure to integrate means losing the EHR and fall back to the off system process. To avoid this the Requesting System assigns the issue as a priority and looks to re-integrate the EHR within 72 hours. | SHOULD |
| **GP2GP\_Req\_73** | If no resolution can be found to the issue within 72 hours then the Requesting System will automatically provide the following error to the GP2GP Requesting Adaptor  Endpoint facadelocation/$gpc.ack  With the following:  header fields: confirmationResponse : “failed\_to\_integrate“, conversationID: “string“  The GP2GP Requesting Adaptor will then convert this to the appropriate HL7 negative acknowledgment  `Error code: 11 [Failed to successfully integrate EHR Extract]`  This will trigger the Sending Site to print the EHR and all attachments for sending off system via PCSE. | MUST |
| **GP2GP\_Req\_74** | If the 72 hours has eclipsed the Requesting System updates the GP2GP transfer status as failed and makes the user aware that no EHR will be available as integration failed and a printed EHR and attachments will be provided by the Sending Site via PCSE. | MUST |
| **GP2GP\_Req\_102** | When the Requesting System is integrating a re-send of an EHR, it must not overwrite any data that has been entered since the Patient has been registered. | MUST |

### Step 18 - Post integration actions

Once an EHR has been integrated along with all the attachments and any placeholders, there a number of system checks that need to be performed and potential tasks created for the user(s).

|  |  |  |
| --- | --- | --- |
| **Post integration checks** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_75** | All problem links, where possible, are to be retained. Further information can be found in the GP Connect ‘Linkages’ page. | MUST |
| **GP2GP\_Req\_76** | All incoming clinical codes from that of the Sending system to that of the Receiving system are converted (using approved mapping tables or use of translations as instructed by the Authority’s interoperability team.) | MUST |
| **GP2GP\_Req\_77** | The Requesting System degrades appropriately, codes for which a mapping does not exist (please refer to the ‘Handling Degrades section of this document for further information) | MUST |
| **GP2GP\_Req\_78** | The Requesting System de-activates all active repeat medications on import into the active record and flags them for manual processing. Such flags are readily visible to, and/or brought to the attention of, clinicians processing the medication records so that they take responsibility for any re-authorisations and if necessary be validated with the Patient. | MUST |
| **GP2GP\_Req\_79** | The Requesting Systemflags any current medications that have been degraded on import into the active record so that clinicians can re-code any that are clinically appropriate.  Further information can be found in the GP Connect ‘Medication Guidance’ page. | MUST |
| **GP2GP\_Req\_80** | Where any Drug Allergies have been degraded on import into the active record, the Requesting System flags these and prevents the prescribing of any medication for the Patient until the degraded items have been either re-coded or removed from the record.  Further information can be found in the GP Connect ‘Allergies Guidance’ page. | MUST |
| **GP2GP\_Req\_81** | Following a successful automatic integration, the Requesting Systemadds an administrative entry to the current EHR, advising Users who view the EHR that a GP2GP EHR has been automatically integrated. The timestamp for the administrative entry will match the time and date at which the automatic integration was completed. This entry will be carried forward to new transfers. It will drop down the journal view over time and become less prominent.  The following SNOMED CT code should be used for this administrative entry  `SCTID: 715411000000103; Record transfer administration (record artifact)` | MUST |
| **GP2GP\_Req\_82** | The Requesting System could implement other optional post integration actions/workflow beyond those listed in these requirements, for example:   - Alerts to all, or other degraded items such as observations, referrals etc. - Alerts to failed documents - Alerts to any chronic conditions   These could be configurable for the user(s) at the Requesting Site (i.e. turned on or off at GP Practice level) | MAY |
| **GP2GP\_Req\_103** | The Requesting System must preserve any legacy codes it receives from the Sending System (i.e. Read v2/CTv3 or local codes that have been mapped to SNOMED CT). This is to ensure they are available for audit purposes and these codes are made available again for any future GP2GP transfer back to the original system.  Example below, the SNOMED CT code will be used by the Requesting System to populate the record, but the original ctv3 code must also be stored, but does not need to be made available to the user. image-20250321-134838.png | MUST |

### Step 19 - Returning Patients/A-B-A Transfers

A Returning Patient is where

- a Patient has been a permanently registered (GMS1) at Practice A
- Has left and been deregistered at practice A and registered as a permanent Patient at Practice B
- Has now registered again as a permanent Patient at Practice A

In this scenario Practice A, now the Requesting System will already hold a pre-existing EHR for the Patient. These requirements detail how the incoming record from the Sending Site (Practice B ) should be handled and merged with the existing EHR at the Requesting System.

For the avoidance of doubt, all the requirements set in Steps 16 and 17 apply to A-B-A scenarios. These are additional requirements that must be applied when receiving an EHR for a returning Patient.

|  |  |  |
| --- | --- | --- |
| **Returning Patients** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_83** | The Requesting system identifies a returning Patient (known as an A-B-A scenario) by using the local index(es), not PDS. A Returning Patient is defined as:  A Patient who has an existing permanent Patient record within the system prior to this registration. | MUST |
| **GP2GP\_Req\_84** | For returning Patients, when an EHR is received from the Sending System, then any new information that has been added to the EHR since the Patient last left the practice is to be copied into the record that already exists in the Requesting System | MUST |
| **GP2GP\_Req\_85** | The Requesting system, when copying content added to a returning Patient’s record since the Patient’s record last left the practice, copy additions to the Patient’s record based on comparing date of the addition with date of the record leaving the practice. | MUST |
| **GP2GP\_Req\_86** | For returning Patients, in addition to the administrative entry requirement in Step 17 `SCTID: 715411000000103; Record transfer administration (record artifact)`, the Requesting Systemadvises Users who view the record that:  ●       The GP2GP record has been automatically integrated for a returning Patient.  ●       A summary of what information will have been copied into the local EHR and what would not.  ●       The user should check the received GP2GP EHR for information that has not been imported into the core record with a prompt on how to access the information.  Note: The administrative entry content will be the same static text for all returning GP2GP EHRs and is not expected to be detailed information that is unique to each Patient record. | MUST |
| **GP2GP\_Req\_87** | The Requesting system provides the user with the ability to view both the received EHR Extract and the Patient’s previous record in a suitably rendered form (i.e. not raw XML) for the user to review. | MUST |
| **GP2GP\_Req\_88** | The Requesting system provides the user with the ability to compare the received EHR Extract and the Patient’s previous record in a suitably rendered form (i.e. not raw XML) for the user to review. | SHOULD |

### Step 20 - Handling Degrades

The Requesting System is only responsible for preserving and handling degrades for the FHIR payload it receives via the adaptor. i.e. any loss of data that happened as part of the HL7 to FHIR conversion are out of scope for the Requesting System. The conversion of data from HL7 to FHIR has been clinically risk assured by NHS England.

There is no change in the way the Requesting System Supplier should handle degrades from the current GP2GP version 2.2b using the requirements from the document “*NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling”* as linked below.

|  |  |  |
| --- | --- | --- |
| **Handling Degrades** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_89** | The Requesting system handles degrades as set out in the GP2GP “*NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling”*.  [NPFIT-PC-BLD-0132.03 GP2…](GP2GP-Requesting-Adaptor.md) | MUST |

### Step 21 - Audit Requirements

Please note the following requirements only apply to the payload that the Requesting System has retrieved from the GP2GP Requesting Adaptor.

|  |  |  |
| --- | --- | --- |
| **Audit** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_90** | Following an automatic integration, the Requesting System adds an entry to the Audit trail as a system action to record that the GP2GP record has been automatically integrated. | MUST |
| **GP2GP\_Req\_91** | The Requesting System retains the EHR received from the GP2GP Requesting Adaptor in its entirety for audit purposes (the below is from the existing GP2GP requirements, 5.6 Processing and Acknowledging a Received EHR Extract, from GP2GP Requirements Specification 2.2)  *This is defined more specifically as:*  ·       *3 years on-line*  ·       *A further 4 years off-line recoverable within 1 working day (yrs 4 – 10)*  ·       *A further 20 years off-line recoverable within 1 working week (years 11 – 30)*  *The system supplier shall ensure that the Audit Trail is retained for the entire retention period of the records audited, to enable investigations to be carried out when necessary and provide evidence where required by the Authority.* | MUST |

## Internal Transfers

In GP2GP one of the largest failure rates can be seen when a Patient registers at a GP Practice that is on the same clinical system as they were previously registered at. This means the GP2GP process is triggered and the clinical system outputs a record from its system into a HL7 payload as the Sending Site and sends via Spine. The same clinical system then ingests the HL7 payload as the Requesting System mapping the HL7 back to its own internal database structure. This inevitably results in a loss of data as not all of the record can be mapped to HL7 and failures may occur in transmitting the record and documents over Spine. This same issue is present in any GP Connect transfer as well.

Any loss of clinical information in a GP2GP transfer is undesirable. Therefore when a Patient transfers from one practice to another on the same clinical system it should perform this operation in a way that means the Patient record is not transformed using GP Connect or the Adaptors. Instead the record should be retained as is and then transferred to the new registered GP Practice using an agreed method via the clinical systems architecture. This should significantly mitigate the risk of failure, document failures or clinical record data being degraded in the transfer.

Any internal transfer need to meet the following requirements regardless of its internal method of transfer. NHS England and their Solutions Assurance and Clinical team will work with any supplier to determine if all requirements apply and what the assurance approach would be based on the proposed method.

|  |  |  |
| --- | --- | --- |
| **Internal Transfers** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_92** | Where a clinical system is installed at more than one GP Practice it has a method agreed with NHS England that allows an internal transfer of a Patients record that results in a lossless native transfer. | MUST |
| **GP2GP\_Req\_93** | All the requirements in Steps 1, 2, and 5 apply to any internal transfer (Registration, PDS Trace and PDS Update respectively) | MUST |
| **GP2GP\_Req\_94** | The requirements in Step 4 apply but may be sourced from the clinical system rather than the ODS API | MUST |
| **GP2GP\_Req\_95** | It is assumed that the requirements in Step 18 (post integration actions) regards degrades should be irrelevant if this is a native lossless transfer, but the de-activation of all active repeat medications and the creation of tasks is still mandatory so as not to introduce any clinical risk. | MUST |

## User Experience

Throughout the GP2GP process there are a number of tasks generated for the user. This section provides more information on these.

|  |  |  |
| --- | --- | --- |
| **User Experience** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Req\_96** | It is not possible to either delete or archive the mandatory tasks generated via the GP2GP process detailed in these requirements for the user .  This is because all tasks detailed in these requirements relate to clinical safety of continuity of care for the Patient and the safe movement of their record. | MUST |
| **GP2GP\_Req\_97** | Where a clinical system supplier provides a dashboard/report of all registrations and deductions it would be beneficial to include the GP2GP status alongside any NHAIS registration status | SHOULD |
| The following requirements and user stories are taken from the GP2GP Automatic Integration Specification and support the user stories below this table which are also taken from the requirements. | | |
| **GP2GP\_Req\_98** | The Requesting Systemprovides a facility that allows a User, should they need to, to easily identify records that are new to their practice and have not been reviewed by a user.  See existing requirement IDs S75, S76, S77 [HSCIC-PC-BLD-0068 26 GP2GP R2 2 Requirements Specification v7.2](https://gpitbjss.atlassian.net/wiki/download/attachments/1391134336/HSCIC-PC-BLD-0068%2026%20GP2GP%20R2%202%20Requirements%20Specification%20v7.2.pdf?version=2&modificationDate=1583165398789&cacheVersion=1&api=v2) | MUST |
| **GP2GP\_Req\_99** | The Requesting System provides a facility that allows a User to mark that a record has been reviewed post automatic integration. | MUST |
| **GP2GP\_Req\_100** | The Requesting System provides, within the record, an indicator on whether or not a record has been reviewed post automatic integration. This is be visible to all users accessing the record. The indicator doesn't obstruct the user from viewing/using the record i.e. must not be a popup that requires the user to dismiss. The indicator is not be included in future GP2GP transfers. | MUST |

### User stories

●      ***As an Administrator*** who is responsible for processing new Patient registrations, ***I want*** to know the status of any requested records (e.g. In progress, failed or successful) , ***so that*** I can understand where they are in the process and keep clinicians and the Patient informed.

●      ***As an Administrator*** who is responsible for processing new Patient registrations, ***I want*** to know which EHRs are new to my practice and have not been reviewed, ***so that*** I can prioritise my effort to review and amend as per our local processes.

●      ***As a Clinician*** who is using a EHR that is new to my practice,***I want*** to know if the EHR has not been reviewed and amended as per our local processes, ***so that*** I have confidence in the structure and content of the EHR information.

## Appendix A - Negative Acknowledgments

### Sending System Negative Acknowledgements

The following are negative acknowledgments that have been received by the GP2GP Adaptor from the Sending System in HL7 and converted to an Operation Outcome that will be posted to the /$gpc.ack endpoint

#### Neg Acks no printed EHR expected

The following are negative acknowledgements that indicate a total failure by the incumbent to process the request and the process has failed. A printed copy of the EHR is not expected in these circumstances as the Sending System is unable to process the request.

GP2GP NACK case "06" -> *EHR\_EXTRACT\_REQUEST\_NEGATIVE\_ACK\_GP2GP\_Patient\_NOT\_REGISTERED*;

operationErrorCode = "Patient\_NOT\_FOUND";  
 operationErrorMessage = "GP2GP - Patient is not registered at the practice";

GP2GP NACK case "07" -> *EHR\_EXTRACT\_REQUEST\_NEGATIVE\_ACK\_GP2GP\_SENDER\_NOT\_CONFIGURED*;

operationErrorCode = "NOT\_IMPLEMENTED";  
 operationErrorMessage = "GP2GP - End Point setup but GP2GP configuration switched OFF";

GP2GP NACK case "18" -> *EHR\_EXTRACT\_REQUEST\_NEGATIVE\_ACK\_GP2GP\_MISFORMED\_REQUEST*;

operationErrorCode = "BAD\_REQUEST";  
 operationErrorMessage = "GP2GP - Request message not well-formed or not able to be processed";

GP2GP NACK case "19" -> *EHR\_EXTRACT\_REQUEST\_NEGATIVE\_ACK\_GP2GP\_NOT\_PRIMARY\_HEALTHCARE\_PROVIDER*;

operationErrorCode = "Patient\_NOT\_FOUND";  
 operationErrorMessage = "GP2GP - PDS indicates Requesting practice is not the Patient’s current primary healthcare provider";

GP2GP NACK case "24" -> *EHR\_EXTRACT\_REQUEST\_NEGATIVE\_ACK\_GP2GP\_MULTI\_OR\_NO\_RESPONSES*;

operationErrorCode = "INTERNAL\_SERVER\_ERROR";  
 operationErrorMessage = "GP2GP - SDS lookup provided zero or more than one result to the query for each interaction.";

GP2GP NACK case "99" -> *EHR\_EXTRACT\_REQUEST\_NEGATIVE\_ACK\_UNKNOWN*;

operationErrorCode = "INTERNAL\_SERVER\_ERROR";  
 operationErrorMessage = "GP2GP - This is a code that should only be used in circumstances where no other codes can"

#### Neg Acks printed EHR expected

GP2GP NACK case "10" -> *EHR\_EXTRACT\_REQUEST\_NEGATIVE\_ACK\_GP2GP\_EHR\_GENERATION\_ERROR*;

operationErrorCode = "INTERNAL\_SERVER\_ERROR";  
 operationErrorMessage = "GP2GP - Failed to successfully generate the EHR";

### GP2GP Requesting Adaptor Negative Acknowledgments

The following are specific errors that occur as part of the GP2GP Requesting Adaptor process. No printed EHR will be expected in these circumstances as the error has occurred in the adaptor that the incumbent Sending System will be unaware of.

case *ERROR\_LRG\_MSG\_REASSEMBLY\_FAILURE*:  
   operationErrorCode = "INTERNAL\_SERVER\_ERROR";  
   operationErrorMessage = "Patient Switching - The Adaptor was unable to recombine the parts of a received attachment";

case *ERROR\_LRG\_MSG\_ATTACHMENTS\_NOT\_RECEIVED*:  
   operationErrorCode = "INTERNAL\_SERVER\_ERROR";  
   operationErrorMessage = " Patient Switching - At least one attachment has not be received";

case *ERROR\_LRG\_MSG\_GENERAL\_FAILURE*:  
   operationErrorCode = "INTERNAL\_SERVER\_ERROR";  
   operationErrorMessage = " Patient Switching - A general processing error has occurred";

case *ERROR\_LRG\_MSG\_TIMEOUT*:  
   operationErrorCode = "INTERNAL\_SERVER\_ERROR";  
   operationErrorMessage = " Patient Switching - An attachment was not received before a timeout condition occurred";

case ERROR\_NHS\_NUMBER\_ALREADY\_IN\_PROGRESS:  
 operationErrorCode = "INTERNAL\_SERVER\_ERROR";  
 operationErrorMessage = " Patient Switching - The Given NHS number is already being processed against Conversation ID: {conversationId}, you cannot start a new request until the current request has completed or failed ";

case ERROR\_EHR\_REQUEST\_TIMEOUT:  
 operationErrorCode = "INTERNAL\_SERVER\_ERROR";  
 operationErrorMessage = "Patient Switching - The EHR record was not received within the given timeout timeframe"

default:  
   operationErrorCode = "INTERNAL\_SERVER\_ERROR";  
   operationErrorMessage = "Patient Switching - A general error has occurred";

## Appendix B - Primary Care Support England (PCSE)

Regardless of whether a transfer of the EHR and associated attachments are a success, paper records may need to be sent to the Requesting Site from the Sending Site. This is handled via Primary Care Support England. If the electronic transfer was a failure the Sending Site will be informed via acknowledgments. The Sending Site will then create a task for the user to print the relevant EHR and/or attachments(S). PCSE will then collect the paper records and the print out of the full EHR and any electronic attachments. If the electronic transfer of the EHR was a success but some attachments failed then PCSE will collect the printed attachments. Further detail on the movement of these paper records can be found here:

[How to move medical records - Primary Care Support England](https://pcse.england.nhs.uk/services/medical-records/moving-medical-records)

## Appendix C - Suspended and Orphaned Records

### Suspended Patients

A suspended Patient is one that is deducted from a GP Practice but does not register elsewhere. A recent update to PDS means that these Patients will now have their last GP Practice ODS code set on PDS as the `Managingorganisation`. This means that these suspended Patient records that are still held electronically at the GP Practice the Patient was previously registered at can be retrieved using the GP2GP process.

### Orphaned Records

Any Patient that was last registered at a closed GP Practice and has not registered with another GP Practice will have their record transferred to a central NHS repository. Work is ongoing to ensure the electronic health record for these Patients is available via GP2GP when the Patient registers at a new GP Practice. It is expected that this will be be done through querying the PDS `Managingorganisation` that will point to an ODS code assigned to the NHS repository.

## Appendix D - Further information on Attachments

The following is important for context on of the entire business process and does not describe any requirements for the NME Requesting System

### Important Information on the failure to retrieve

It is important to note that when the Requesting System fails to retrieve an attachment from the GP2GP Requesting Adaptor that the Sending Site will be unaware it has failed. Therefore it will not be aware of the need to prompt the user to print the attachment and send via PCSE. This differs from GP2GP behaviour (as described below) where the Sending Site creates the placeholder and is always aware of the need to print any document it fails to send.

Therefore the Requesting System when creating its own placeholders will need to make the user aware of the need to contact the Sending Site to request a paper copy.

It is anticipated that this issue should be very low frequency as the NME Requesting System is retrieving documents from the GP2GP Requesting Adaptor file storage that sits within its own infrastructure, and as a result is seen as low risk.

However, should this occur the format for GP C placeholders is documented below:

### GP Connect Attachment Placeholder

Within the placeholder file the text ***must*** be as follows on each row.

The header is a generic text string for all placeholders.

The referenced Name, Element and Resource ***must*** be taken from the GP Connect Document Reference where available.

|  |  |  |  |
| --- | --- | --- | --- |
| Row 1 | **Header** | The following attachment could not be retrieved via GP2GP when the Patient registered | |
| N/A | **Name** | **Element** | **Resource** |
| Row 2 | Internal Supplier ID: | id | Record Bundle Document Reference |
| Row 3 | GPC Document Identifier: | identifier | Record Bundle Document Reference |
| Row 4 | Document Description: | description | Record Bundle Document Reference |
| Row 5 | Patient NHS no. | nhs-number | Patient Resource Reference |
| Row 6 | Date created: | created | Record Bundle Document Reference |
| Row 7 | Author: | author (name of) | Organisation and Practitioner Reference |
| Row 8 | Owning organisation: | custodian (ODS code and name of GP Practice) | Organisation and Practitioner Reference |
| Row 9 | Size | content.attachment.size | Record Bundle Document Reference |
| Row 10 | Content | content.format | Record Bundle Document Reference |

### Sending Site failure [Existing GP2GP placeholder behaviour]

When a GP2GP HL7 Sending Site fails to retrieve any attachment from its systems, or encounters an error a placeholder is created before it is sent to the GP2GP Requesting Adaptor.

The GP2GP Requesting Adaptor will treat this like any other attachment and make it available in the GP2GP Requesting Adaptor file storage for the NME Requesting System to retrieve.

The Requesting Site will then retrieve this placeholder from the GP2GP Requesting Adaptor file storage GP2GP Requesting Adaptor file storage as described in requirement 2\_08 . It will then insert the placeholder created by the GP2GP Sending Site into the Patient record if the electronic file is successfully integrated.

GP2GP HL7 placeholder files are text files with a ‘txt’ suffix and MIME type text/plain.

They differ from those placeholders created by the NME Requesting Site when it cannot retrieve a file, as they are generated by the incumbent according to the GP2GP HL7 requirements.

The file will be named and have the format as follows as per the GP2GP requirements:

**AbsentAttachment[GUID].txt**

Where GUID is an HL7-format (upper-case) GUID.

For example: **AbsentAttachmentC49A7603-7CD0-4DE2-B60D-124B42DFD3D2.txt**

Within the placeholder file the text will be as follows (line numbers given for clarity):

|  |  |
| --- | --- |
| 1  2  3  4 | The following file could not be included with the Electronic Record:  [Original filename and suffix]  [ODS Code of practice generating attachment]:[ConversationID for that transfer]  Reason:[Reason Code]:[Reason Description] |

 For example:

|  |
| --- |
| The following file could not be included with the Electronic Record:  Smith\_Edward\_1999\_Oct\_12\_R46TW39.doc  P86001:21EC2020-3AEA-1069-A2DD-08002B30309D   Reason:03:File not found |

The creation of a placeholder by the Sending Site automatically triggers a task in GP2GP systems. This task will inform the user at the Sending Site that these documents need to be printed and sent via Primary Care Support England.

No action is required of the Requesting System in this scenario.

### File Size

As the existing GP2GP service has no specific file size limits, it is envisaged that all attachments regardless of size will be passed to the GP2GP Requesting Adaptor.

GP Connect does have a requirement for an upper file size limit of 100mb from the Sending Site (i.e. it will not pass through attachments greater than 100mb).

However, as the Requesting System will be retrieving the attachments from the GP2GP Requesting Adaptor file storage, that sits on its own infrastructure, there should be no file size limits and all attachments should be provided.

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [GP Connect Access Record Structured](GP-Connect-Access-Record-Structured.md) - Refer to ‘Migrate a Patient’s structured record' and ‘Migrate a document’ for more information

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [AbsentAttachment_example](../../../../.raw/DCSDCS/attachments/12512034968/att12512034985-AbsentAttachment_example)
- [NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf](../../../../.raw/DCSDCS/attachments/12512034968/att12512034988-NPFIT-PC-BLD-0132.03 GP2GP Supplementary Specification on Structured Degrade Handling.pdf)
- [ReqAdptSteps1234.jpg](../../../../.raw/DCSDCS/attachments/12512034968/att12512034991-ReqAdptSteps1234.jpg)
- [ReqAdpSteps567.jpg](../../../../.raw/DCSDCS/attachments/12512034968/att12512034994-ReqAdpSteps567.jpg)
- [image-20250321-134838.png](../../../../.raw/DCSDCS/attachments/12512034968/att14151352513-image-20250321-134838.png)
