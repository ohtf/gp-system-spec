---
page_id: "14425882674"
space: "DCSDCS"
title: "GP2GP Sending Adaptor v1.0.1"
version: 1
updated: "2025-10-22T09:50:11.185Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/14425882674/GP2GP+Sending+Adaptor+v1.0.1"
labels: ["standard_retired"]
---

# GP2GP Sending Adaptor v1.0.1

|  |  |
| --- | --- |
| ID {#GP2GPSendingAdaptorv1.0.1-ID} | S95 |
| Version {#GP2GPSendingAdaptorv1.0.1-Version} | 1.0.1 |
| Type {#GP2GPSendingAdaptorv1.0.1-Type} | Standard |
| Status {#GP2GPSendingAdaptorv1.0.1-Status} | Retired |
| Effective Date {#GP2GPSendingAdaptorv1.0.1-EffectiveDate} | 22 May 2025 |
| Contracting Vehicle(s) {#GP2GPSendingAdaptorv1.0.1-ContractingVehicle(s)} | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

- [Introduction](#GP2GPSendingAdaptorv1.0.1-Introduction)
- [Requirements](#GP2GPSendingAdaptorv1.0.1-Requirements)
  - [End to End Process](#GP2GPSendingAdaptorv1.0.1-EndtoEndProcess)
    - [Step 1 (GP2GP Adaptor - GP Connect ‘Migrate Record’ request)](#GP2GPSendingAdaptorv1.0.1-Step1(GP2GPAdaptor-GPConnect‘MigrateRecord’request))
    - [Step 2 (GP C Provider - Identity checks)](#GP2GPSendingAdaptorv1.0.1-Step2(GPCProvider-Identitychecks))
    - [Step 3 (GP C Provider - Checks request well formed)](#GP2GPSendingAdaptorv1.0.1-Step3(GPCProvider-Checksrequestwellformed))
    - [Step 4 (GP2GP Adaptor - Retrieves FHIR record bundle)](#GP2GPSendingAdaptorv1.0.1-Step4(GP2GPAdaptor-RetrievesFHIRrecordbundle))
    - [Step 5 (GP2GP Adaptor - Migrate documents)](#GP2GPSendingAdaptorv1.0.1-Step5(GP2GPAdaptor-Migratedocuments))
    - [Step 6 (GP2GP Adaptor - Creates placeholder files)](#GP2GPSendingAdaptorv1.0.1-Step6(GP2GPAdaptor-Createsplaceholderfiles))
    - [Step 7 (GP2GP Adaptor - converts FHIR to HL7)](#GP2GPSendingAdaptorv1.0.1-Step7(GP2GPAdaptor-convertsFHIRtoHL7))
    - [Step 8 (Requesting Site - processes incoming HL7 EHR)](#GP2GPSendingAdaptorv1.0.1-Step8(RequestingSite-processesincomingHL7EHR))
    - [Step 9 (Requesting Site - checks valid request)](#GP2GPSendingAdaptorv1.0.1-Step9(RequestingSite-checksvalidrequest))
    - [Step 10 (Requesting Site - user views and files/rejects record)](#GP2GPSendingAdaptorv1.0.1-Step10(RequestingSite-userviewsandfiles/rejectsrecord))
    - [Step 11 (Requesting Site - Attempts to integrate the record)](#GP2GPSendingAdaptorv1.0.1-Step11(RequestingSite-Attemptstointegratetherecord))
    - [Step 12 (Requesting Site - Integrates & sends positive acknowledgment)](#GP2GPSendingAdaptorv1.0.1-Step12(RequestingSite-Integrates&sendspositiveacknowledgment))
    - [Step 13 (GP2GP Adaptor - Acknowledgement Received)](#GP2GPSendingAdaptorv1.0.1-Step13(GP2GPAdaptor-AcknowledgementReceived))
    - [Step 14 (Sending System - Polls Adaptor for outcome)](#GP2GPSendingAdaptorv1.0.1-Step14(SendingSystem-PollsAdaptorforoutcome))
    - [Step 15a (Sending System - Identifies ‘COMPLETE' Outcome)](#GP2GPSendingAdaptorv1.0.1-Step15a(SendingSystem-Identifies‘COMPLETE'Outcome))
    - [Step 15b (Sending System - Identifies ‘COMPLETE\_WITH\_ISSUES’ Outcome)](#GP2GPSendingAdaptorv1.0.1-Step15b(SendingSystem-Identifies‘COMPLETE_WITH_ISSUES’Outcome))
    - [Step 15c (Sending System - identifies ‘FAILED' outcome’)](#GP2GPSendingAdaptorv1.0.1-Step15c(SendingSystem-identifies‘FAILED'outcome’))
    - [Step 16 (GP2GP Adaptor - Identifies no acknowledgment 8 Days)](#GP2GPSendingAdaptorv1.0.1-Step16(GP2GPAdaptor-Identifiesnoacknowledgment8Days))
  - [Appendix A - Placeholders](#GP2GPSendingAdaptorv1.0.1-AppendixA-Placeholders)
  - [Appendix B - Movement of paper records and PCSE](#GP2GPSendingAdaptorv1.0.1-AppendixB-MovementofpaperrecordsandPCSE)
  - [Appendix C - Incorrect Patient transferred](#GP2GPSendingAdaptorv1.0.1-AppendixC-IncorrectPatienttransferred)
  - [Appendix D - EHR Status Endpoint Data Model](#GP2GPSendingAdaptorv1.0.1-AppendixD-EHRStatusEndpointDataModel)
- [Dependencies](#GP2GPSendingAdaptorv1.0.1-Dependencies)
- [Roadmap](#GP2GPSendingAdaptorv1.0.1-Roadmap)

# Introduction {#GP2GPSendingAdaptorv1.0.1-Introduction}

The GP2GP Sending Adaptor is designed to allow a System Supplier using GP Connect - Access Record Structured API v1.6.0 as a Provider to send a requested Electronic Health Record (EHR) to a System Supplier using GP2GP HL7.

This page documents the details of how a GP System Supplier, using GP Connect as a Provider, will interact with the GP2GP Sending Adaptor when acting as the Sending Site (A Patient previously registered with them has now registered at another site). It also details behaviour of the GP2GP Sending Adaptor, the Requesting and the Sending System interactions.

It assumes the Requesting Site using GP2GP HL7 has made a successful trace to the Personal Demographics Service (PDS) and registered the Patient and sent a HL7 request as per the GP2GP requirements.

This will be received by the GP2GP Sending Adaptor deployed on the Sending System infrastructure. The GP2GP Sending Adaptor will convert this request and then make a GP Connect call to the Sending Systems GP Connect Provider endpoint. It will then retrieve the Electronic Health Record (EHR) and subsequently any associated attachments. It will then convert this to a HL7 payload that is then sent and ingested/filed by the Requesting System using GP2GP and HL7.

![](https://nhse-dsic.atlassian.net/wiki/download/attachments/14425882674/GP2GP%20(2).png?api=v2)

The Sending System will need to monitor the GP2GP Sending Adaptor to ensure it is available on its infrastructure and poll it for any successful or negative acknowledgments that are received by the GP2GP Sending Adaptor from the Requesting Site. This will determine any action the Sending System needs to make to its tasks and workflow and alert the user to any actions.

The GP2GP Sending Adaptor will also provide the necessary HL7 acknowledgments to the Requesting Site to indicate the transfer status.

Please note that all steps for the GP2GP Adaptor and the Requesting Site are listed here to provide the full end to end business process. Any requirements for the Sending System/Site are clearly labelled and will need to be assured by NHS England.

# Requirements {#GP2GPSendingAdaptorv1.0.1-Requirements}

Steps 2 and 3 are requirements from the GP Connect 1.6 specification but listed here for completeness. Full details on this can be found on their developer page GP Connect - Access Record Structured API v1.6.0.

Steps 14 and 15 are Sending System requirements specific to this process that sit outside of GP Connect, the GP2GP Adaptor and the Requesting System and are numbered for reference.

## End to End Process {#GP2GPSendingAdaptorv1.0.1-EndtoEndProcess}

### Step 1 (GP2GP Adaptor - GP Connect ‘Migrate Record’ request) {#GP2GPSendingAdaptorv1.0.1-Step1(GP2GPAdaptor-GPConnect‘MigrateRecord’request)}

The GP2GP Sending Adaptor will receive the HL7 request from the Requesting Site. It will convert this to a FHIR migrate structured record request as documented here:

Migrate a Patient’s structured record | gpconnect

It will now make a call to the Sending Systems GP Connect Provider endpoint to retrieve the FHIR record bundle.

Should the HL7 request not be well formed or fail to convert to a FHIR migrate structured record request, the GP2GP Sending Adaptor will send a negative acknowledgment to the Requesting Site indicating a total failure. The GP2GP Sending Adaptor will send the following error to the Requesting Site.

|  |  |
| --- | --- |
| **HL7 error** | **Notes** |
| Error code: 18 [Request message not well formed or not able to be processed] | This shall be used in circumstances where the contacted Provider cannot read the received EHR request. It is either corrupt, badly formed or using an incompatible message version. |

As the request cannot be processed the GP2GP Sending Adaptor will not provide any outcome for the Sending System to poll as there is no action for the Sending System to take.

### Step 2 (GP C Provider - Identity checks) {#GP2GPSendingAdaptorv1.0.1-Step2(GPCProvider-Identitychecks)}

The Sending Systems GP Connect 1.6 Provider solution will receive the Migrate Structured Record request and as per the GP Connect 1.6 requirements:

*The providing system **MUST** check that the ODS code supplied in the* `requesting_organization` *claim in the JWT matches the Patient’s registered practice on PDS.*

If this check fails (i.e. the Requesting Site is the not the Patients registered practice on PDS), or it can not complete this action, or the Patient is not registered at the Sending Site, the Sending Sites GP Connect Provider 1.6 solution will provide one of the following error responses and the the GP2GP Sending Adaptor will translate this and send a HL7 negative acknowledgment with the relevant error code:

|  |  |  |
| --- | --- | --- |
| **GP C Provider Error** | **HL7 error** | **Notes** |
| NOT\_AUTHORISED | Error code: 19 [Sender check indicates that Requester is not the Patient’s current healthcare provider] | Requesting organisation is not the Patients registered practice |
| INVALID\_NHS\_NUMBER | Error code: 19 [Sender check indicates that Requester is not the Patient’s current healthcare provider] | NHS number is invalid |
| INVALID\_Patient\_DEMOGRAPHICS | Error code: 20 [Spine system responded with an error] | GP Connect Provider is unable to connect to PDS to perform the trace |
| Patient\_NOT\_FOUND | Error code: 6 [Patient not at surgery] | Patient has not been previously registered at the surgery |

As the request cannot be processed the GP2GP Sending Adaptor will not provide any outcome for the Sending System to poll as there is no action for the Sending System to take.

### Step 3 (GP C Provider - Checks request well formed) {#GP2GPSendingAdaptorv1.0.1-Step3(GPCProvider-Checksrequestwellformed)}

If the previous step was successful the Sending Systems GP Connect 1.6 Provider must now determine if the GP Connect request (migratestructuredrecord) sent from the GP2GP Sending Adaptor is well formed and it can respond successfully. If it is not, one of the following error codes will be provided to the GP2GP Sending Adaptor dependent on the issue that the GP2GP Sending Adaptor will translate to the relevant HL7 error.

|  |  |  |
| --- | --- | --- |
| **GP C Provider Error** | **HL7 error** | **Notes** |
| INVALID\_RESOURCE | Error code: 18 [Request message not well formed or not able to be processed] | This is where the FHIR request is invalid |
| INVALID\_PARAMETER | Error code: 18 [Request message not well formed or not able to be processed] | This is where the FHIR request is invalid |
| BAD\_REQUEST | Error code: 18 [Request message not well formed or not able to be processed] | This is where the FHIR request is invalid |

As the request cannot be processed the GP2GP Sending Adaptor will not provide any outcome for the Sending System to poll as there is no action for the Sending System to take.

![](https://nhse-dsic.atlassian.net/wiki/download/attachments/14425882674/GP2GPSteps123.drawio.png?api=v2)

### Step 4 (GP2GP Adaptor - Retrieves FHIR record bundle) {#GP2GPSendingAdaptorv1.0.1-Step4(GP2GPAdaptor-RetrievesFHIRrecordbundle)}

If the above checks are successful the Patient's full FHIR record bundle (EHR) will retrieved via the Sending Systems GP Connect API and sent to the GP2GP Sending Adaptor.

Migrate a Patient’s structured record | gpconnect

This will include the Document Reference resources:

DocumentReference | gpconnect

These represent the Patient’s documents and must include any references where it is known the document can not be returned (there is no corresponding URL as the document was either too large, over 100mb, or not found).

|  |  |  |
| --- | --- | --- |
| **Document** | **Document reference data** | **URL** |
| Doc A | Yes | Yes |
| Doc B | Yes | Yes |
| Doc C | Yes | No (Doc exceeded 100mb) |

For any document where no URL is received the adaptor will create a GP2GP HL7 txt placeholder file as described in Step 6

If there is an error in retrieving the FHIR record bundle by the GP2GP Sending Adaptor, the Sending Systems GP Connect API will provide an error. The GP2GP Sending Adaptor will map this and and send a HL7 negative acknowledgment with the relevant error code as below:

|  |  |  |
| --- | --- | --- |
| **GP C Provider Error** | **HL7 error** | **Notes** |
| INTERNAL\_SERVER\_ERROR | Error code: 99 [Unexpected Condition] | This is a code that should only be used in circumstances where the above codes cannot be used to accurately describe the condition. |

The GP2GP Sending Adaptor will also post a a **Failed** outcome for the Sending System to consume and alert users as in Step 15c.

|  |  |  |
| --- | --- | --- |
| **GP2GP Retrieves FHIR record bundle** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Send-19** | GP Connect migrate structured provides the data model for the sending of an Electronic Health Record (EHR), however, for the avoidance of doubt the following are requirements that are to be followed when providing an EHR for a GP2GP transfer using GP Connect:   1. The sending system will provide all data items in its system for a record that the GP Connect specification allows.  2. Any mapped codes in the Sending System must have any previous code and term text provided (see following example xml for reference).  3. Any unfiled test reports for the Patient are to be provided.  image-20250325-105833.png The original SNOMED code and descriptive text is made available along with the legacy Read v2 code and the original term text. | MUST |

### Step 5 (GP2GP Adaptor - Migrate documents) {#GP2GPSendingAdaptorv1.0.1-Step5(GP2GPAdaptor-Migratedocuments)}

Once the GP2GP Sending Adaptor has received the Patients FHIR record it must identify and find all the Patients documents using the supplied URLs. It will then make a Migrate Document call from the Sending Systems GP Connect 1.6 Provider solution for each identified document.

Migrate a document | gpconnect

For any document it can not retrieve (receives an error - RECORD\_NOT\_FOUND) the adaptor must create a GP2GP HL7 .txt placeholder file as described in Step 6.

### Step 6 (GP2GP Adaptor - Creates placeholder files) {#GP2GPSendingAdaptorv1.0.1-Step6(GP2GPAdaptor-Createsplaceholderfiles)}

For any document that the GP2GP Sending Adaptor was unable to retrieve or that were indicated as placeholders in the FHIR Patient record (Steps 4 and 5), the GP2GP Sending Adaptor must now create GP2GP HL7 txt files. These are specified in the GP2GP documentation which is detailed in Appendix A.

**Please note:** Step 15b details how The Sending Supplier System can query the GP2GP Sending Adaptor to determine any documents that failed and been sent as placeholders from either steps 4 & 5. This is because if in an AA Acknowledgement is received from the Requesting Site (as in Step 15b), the NME Sending Site will need to alert its users to print these documents and send as part of the offline paper process via PCSE.

### Step 7 (GP2GP Adaptor - converts FHIR to HL7) {#GP2GPSendingAdaptorv1.0.1-Step7(GP2GPAdaptor-convertsFHIRtoHL7)}

Once the GP2GP Sending Adaptor has successfully retrieved the Patients FHIR record and any associated attachments, it must now convert these to a HL7 record.

If for any reason this step fails it must send a negative acknowledgment to the Requesting Site.

|  |
| --- |
| **HL7 Error** |
| Error code: 10 [Failed to successfully generate the EHR extract] |

The GP2GP Sending Adaptor will also post a a **Failed** outcome for the Sending System to consume and alert users as in Step 15c.

![](https://nhse-dsic.atlassian.net/wiki/download/attachments/14425882674/GP2GPSteps467.drawio.png?api=v2)

### Step 8 (Requesting Site - processes incoming HL7 EHR) {#GP2GPSendingAdaptorv1.0.1-Step8(RequestingSite-processesincomingHL7EHR)}

The HL7 record is now passed to the Requesting Site who registered the Patient and requested the record. The following is all current GP2GP behaviour. Any failures on the Requesting Site process will result in a negative acknowledgement being sent to the GP2GP Sending Adaptor. The Sending Supplier System is required to poll the GP2GP Sending Adaptor for any EHR transfer status so it can provide the required actions on its workflow and tasks.

### Step 9 (Requesting Site - checks valid request) {#GP2GPSendingAdaptorv1.0.1-Step9(RequestingSite-checksvalidrequest)}

Initially the Requesting Site will check that this is a valid HL7 message it can process. If it is not it will return one of the following HL7 error codes in a negative acknowledgment.

|  |
| --- |
| **HL7 Error** |
| Error code: 9 [EHR Extract received without corresponding request] |
| Error code: 12 [Duplicate EHR Extract received] |
| Error code: 21 [EHR Extract message not well-formed or not able to be processed] |
| Error code: 25 [Large messages rejected due to timeout duration reached of overall transfer] |
| Error code: 29 [Large Message Re-assembly failure] |
| Error code: 30 [Large Message general failure] |
| Error code: 31 [The overall EHR Extract has been rejected because one or more attachments via Large Messages were not received] |

### Step 10 (Requesting Site - user views and files/rejects record) {#GP2GPSendingAdaptorv1.0.1-Step10(RequestingSite-userviewsandfiles/rejectsrecord)}

If the Requesting Site has successfully received the HL7 message and attachments, the user will be alerted to the incoming record and view it. At this stage they may reject the record. This will send a negative acknowledgment to the GP2GP Sending Adaptor. This will be one of the following error codes :

|  |
| --- |
| **HL7 Error** |
| Error code: 17 [A-B-A EHR Extract Received and rejected due to wrong record or wrong Patient] |
| Error code: 28 [Non A-B-A EHR Extract Received and rejected due to wrong record or wrong Patient] |

**Please note:** This step may be removed in the future as a change is expected to the current GP2GP specification that means all incoming records will be auto-integrated and cannot be rejected (GP2GP Auto-Integration - Roadmap Item 175). This will have no impact on the GP2GP Sending Adaptor or Sending System, the only change will be that these error codes will not be received by the GP2GP Sending adaptor.

### Step 11 (Requesting Site - Attempts to integrate the record) {#GP2GPSendingAdaptorv1.0.1-Step11(RequestingSite-Attemptstointegratetherecord)}

If the user accepted the record the Requesting System will attempt to integrate/file the record and any attachments. Should it fail to integrate it will send a negative acknowledgment to the GP2GP Sending Adaptor. One of the following error codes may be returned:

|  |
| --- |
| **HL7 Error** |
| Error code: 11 [Failed to successfully integrate EHR Extract] |
| Error code: 15 [A-B-A EHR Extract Received and Stored As Suppressed Record] |

### Step 12 (Requesting Site - Integrates & sends positive acknowledgment) {#GP2GPSendingAdaptorv1.0.1-Step12(RequestingSite-Integrates&sendspositiveacknowledgment)}

If the record has been successfully integrated/filed, the Requesting Site will now send a Positive Acknowledgment that will be routed to the GP2GP Sending Adaptor. No numeric error code is used, however the typeCode is used as follows:

**<acknowledgement typeCode = “AA”>**

### Step 13 (GP2GP Adaptor - Acknowledgement Received) {#GP2GPSendingAdaptorv1.0.1-Step13(GP2GPAdaptor-AcknowledgementReceived)}

Provided their was no error in Steps 4 or 7 (the GP2GP Adaptor failed to retrieve or convert the FHIR bundle) the GP2GP Sending Adaptor will now have either received either a positive or negative acknowledgment from the Requesting Site. It will now process the HL7 acknowledgment and post the outcome of the EHR transfer to the *(/requests* endpoint). For each conversation ID (transfer request) It will post one of the following outcomes:

- **COMPLETE** (AA Ack received from Requesting Site, EHR and all attachments transferred successfully)
- **FAILED\_INCUMBENT** (Negative acknowledgment received from Requesting Site)
- **COMPLETE\_WITH\_ISSUES** (AA Ack received from the Requesting Site, EHR successful but some failed attachments)
- **IN PROGRESS** (Final outcome not yet determined)

![](https://nhse-dsic.atlassian.net/wiki/download/attachments/14425882674/GP2GPSteps891011.drawio.png?api=v2)

### Step 14 (Sending System - Polls Adaptor for outcome) {#GP2GPSendingAdaptorv1.0.1-Step14(SendingSystem-PollsAdaptorforoutcome)}

It is necessary for the Sending System to poll the adaptor at regular intervals to determine the outcome and status of any EHR request

|  |  |  |
| --- | --- | --- |
| **GP2GP Request outcome** | | |
| **Requirement ID** | Requirement Text {#GP2GPSendingAdaptorv1.0.1-RequirementText} | Level {#GP2GPSendingAdaptorv1.0.1-Level} |
| **GP2GP\_Send-01** | The Sending System is responsible for monitoring and ensuring the GP2GP Adaptor is available at all times so as not to prevent it from processing any inbound messages | MUST |
| **GP2GP\_Send-02** | The Sending System will poll the GP2GP Sending Adaptor *(/requests* endpoint) for the outcome of any transfer of an electronic Patient record as a minimum every 24 hours. | MUST |
| **GP2GP\_Send-03** | If the Sending System identifies an **IN\_PROGRESS** status, then no outcome has been determined (The GP2GP Sending Adaptor has not received any acknowledgment from the Requesting Site at this time) and the Sending System will continue to poll the adaptor until the GP2GP Sending Adaptor posts an outcome | MUST |
| **GP2GP\_Send-04** | The Sending System is responsible for ensuring that the outcome for any transfer **(COMPLETE, FAILED\_NME, FAILED\_INCUMBENT or COMPLETE\_WITH\_ISSUES)** is retrieved from the GP2GP Sending Adaptor and that this triggers the relevant Sending Site workflow and user tasks as described in the subsequent requirements | MUST |

### Step 15a (Sending System - Identifies ‘COMPLETE' Outcome) {#GP2GPSendingAdaptorv1.0.1-Step15a(SendingSystem-Identifies‘COMPLETE'Outcome)}

If the Requesting Site sent an AA acknowledgment and either

- There were no attachments associated with the EHR
- No attachments failed and no placeholders were sent

Then the EHR transfer is considered a success and this will be posted on the GP2GP Sending Adaptor *(/requests* endpoint) for the Sending System to poll

|  |  |  |
| --- | --- | --- |
| **GP2GP Request completed** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Send-05** | On polling the GP2GP Sending Adaptor and identifying a **COMPLETE** outcome the Sending System will update its workflow and mark the EHR transfer as successful | MUST |

### Step 15b (Sending System - Identifies ‘COMPLETE\_WITH\_ISSUES’ Outcome) {#GP2GPSendingAdaptorv1.0.1-Step15b(SendingSystem-Identifies‘COMPLETE\_WITH\_ISSUES’Outcome)}

If the Requesting Site sent an AA acknowledgment, but the GP2GP Adaptor created one or more placeholders for missing attachments it will post a **COMPLETE\_WITH\_ISSUES** outcome on the GP2GP Sending Adaptor *(/requests* endpoint) for the Sending System to poll

|  |  |  |
| --- | --- | --- |
| **GP2GP Request completed with issues** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Send-06** | On polling the GP2GP Sending Adaptor and identifying a **COMPLETE\_WITH\_ISSUES** outcome the Sending System will poll the GP2GP Adaptor */ehrstatus* endpoint. This will allow it to identify all attachments that failed using the GP Connect ‘Description’ string and ‘Identifier’ that is provided by the */ehrstatus* endpoint.  The full data model for the */ehrstatus* endpoint can be found in Appendix E | MUST |
| **GP2GP\_Send-07** | The Sending System will now create a task for the user to print the missing attachments only | MUST |
| **GP2GP\_Send-08** | The Sending System will provide specific links to the missing attachments either in the task or from their GP2GP workflow functionality | MUST |
| **GP2GP\_Send-09\*\*** | It is highly recommended following user research on current GP2GP that the Sending Site enables users to print all missing attachments with one click/workflow, without needing to manually source each missing attachment. | SHOULD |
| **GP2GP\_Send-10** | The Sending System will only mark the EHR transfer as successful once all the missing attachments have been printed by the user. These paper copies will then be included in the PCSE manual off system process. | MUST |

*\*\* The reasons for this are:*

- *If the Sending Site does not allow the user to easily locate the failed documents it creates burden and they may print all the documents. This in turn causes unnecessary burden for the Receiving Site user who receives all the Patients paper documents. They must then determine which are the documents that failed and need to be scanned and added to the Patients electronic record.*
- *The sending site is unable to locate, or prints the wrong document, resulting in the printed document not being received by the receiving site, or the incorrect document, resulting in a loss of clinical data.*

### Step 15c (Sending System - identifies ‘FAILED' outcome’) {#GP2GPSendingAdaptorv1.0.1-Step15c(SendingSystem-identifies‘FAILED'outcome’)}

Failure can occur at two points in the transfer process

1. If the GP2GP Sending Adaptor failed to retrieve or generate the EHR as in Steps 4 & 7 it will post a **FAILED\_NME** outcome to the GP2GP Sending Adaptor *(/requests* endpoint) for the Sending System to retrieve
2. If the GP2GP Sending Adaptor received a negative acknowledgment from the incumbent as in steps 9, 10 and 11 it will post a **FAILED\_INCUMBENT** error to the GP2GP Sending Adaptor *(/requests* endpoint) for the Sending System to retrieve

Regardless of where the failure occurred the following requirements apply

|  |  |  |
| --- | --- | --- |
| **GP2GP Request failed** | | |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP2GP\_Send-11** | On polling the GP2GP Sending Adaptor and identifying a **FAILED** outcome the Sending System will need to update its workflow and mark the EHR transfer as failed | MUST |
| **GP2GP\_Send-12** | The Sending System will create a task for the user to print the full EHR and all attachments  The printing of a summary of the EHR must only be permitted in addition to the printing of the full EHR.  This requirement is to ensure clinical information is not lost by the printing and then the subsequent sending of a printed summary only of the Patients EHR to their new GP Practice. | MUST |
| **GP2GP\_Send-13** | This task will enable the user to easily locate the specific EHR and any attachment(s) for printing | MUST |
| **GP2GP\_Send-14** | This task cannot be archived/removed or deleted until the Sending Site recognises the full EHR and all missing attachments have been printed by the user. These paper copies will then be included in the PCSE manual off system process. | MUST |
| **GP2GP\_Send-15** | The Sending System must provide a function for the user to trigger a re-send of the GP Connect structured record (EHR) for any GP2GP failed transfer. This is because:   - An intermittent network issue may have caused the failure, and this is now resolved. - An underlying system/technical issue is identified for causing the failure and subsequently resolved.   In both cases a re-send should now result in a successful transfer and is preferable to an off-system paper process. | MUST |
| **GP2GP\_Send-16** | The Sending System, when attempting a retry must create the structured GP Connect structured record (EHR) using the latest copy of the record held on their database (so that any additions since the first attempt at sending are included). | MUST |
| **GP2GP\_Send-17** | Prior to re-sending the GP Connect structured record (EHR) the Sending System shall perform the usual PDS checks, as listed in Step 2, to ensure that the Patient is still registered at the requesting practice. | MUST |
| **GP2GP\_Send-18** | If the re-send is successful, and a positive acknowledgment received, the Sending System will update its workflow as per GP2GP\_Send-10. If a negative acknowledgement is received the user can still trigger a re-try but the Sending System may wish to place some restrictions (e.g. only one re-send per failed record every 24 hours). | MUST |

#### Additional Information on outcomes {#GP2GPSendingAdaptorv1.0.1-AdditionalInformationonoutcomes}

The Sending System may access more detailed logs that the GP2GP Adaptor will create with regards each transfer and its status (please note there are no Patient data available only audit logs of each transfer using the conversation ID). These are accessible via the cloud provider (AWS). Further information is available in the GP2GP Sending Adaptor integration specification.

![](https://nhse-dsic.atlassian.net/wiki/download/attachments/14425882674/GP2GPSteps15.drawio.png?api=v2)

### Step 16 (GP2GP Adaptor - Identifies no acknowledgment 8 Days) {#GP2GPSendingAdaptorv1.0.1-Step16(GP2GPAdaptor-Identifiesnoacknowledgment8Days)}

In the GP2GP requirements if no acknowledgment is received within 8 days from the Requesting Practice, the Sending Site must assume that the process has failed. It must then generate a task to print the full electronic health record to be sent via PCSE.

To mimic this behaviour, the GP2GP Sending Adaptor will monitor the status of a transfer and if it has not received an acknowledgment from the Requesting Site within 8 days it will update the status of the transfer to **FAILED\_INCUMBENT**. This will then allow the Sending System when it polls the GP2GP Sending Adaptor to create the task to print and follow the requirements as set out in **Step 15c**. Therefore the GP2GP Sending Adaptor is tracking the status of any acknowledgment received and the Sending System is not required to monitor whether an acknowledgment has been received or not within the 8 days.

## Appendix A - Placeholders {#GP2GPSendingAdaptorv1.0.1-AppendixA-Placeholders}

The following is from the GP2GP specification on Handling Missing Attachments section 2.2.

*This is for information only and applies solely to the GP2GP Sending Adaptor that will need to create these placeholders for Requesting Sites to consume in the case of failure to retrieve.*

[NPFIT-PC-BLD-0099.04 GP2…](../../../../.raw/DCSDCS/attachments/14425882674/att14425882696-NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf)

A placeholder file is a text file with a ‘txt’ suffix and MIME type text/plain. The file must be named as follows:

**AbsentAttachment[GUID].txt**

Where GUID is an HL7-format (upper-case) GUID.

For example: **AbsentAttachmentC49A7603-7CD0-4DE2-B60D-124B42DFD3D2.txt**

The placeholder file must be referenced from the EHR\_Extract as described in the Attachment referencing specification

[NPFIT-PC-BLD-0158 GP2GP …](../../../../.raw/DCSDCS/attachments/14425882674/att14425882693-NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf)

Within the placeholder file the text must be as follows (line numbers given for clarity):

|  |  |
| --- | --- |
| 1  2  3  4 | The following file could not be included with the Electronic Record:  [Original filename and suffix]  [ODS Code of practice generating attachment]:[ConversationID for that transfer]  Reason:[Reason Code]:[Reason Description] |

For example:

|  |
| --- |
| The following file could not be included with the Electronic Record:  Smith\_Edward\_1999\_Oct\_12\_R46TW39.doc  P86001:21EC2020-3AEA-1069-A2DD-08002B30309D  Reason:03:File not found |

## Appendix B - Movement of paper records and PCSE {#GP2GPSendingAdaptorv1.0.1-AppendixB-MovementofpaperrecordsandPCSE}

Regardless of whether a transfer of the EHR and associated attachments are a success, paper records may need to be sent to the Requesting Site from the Sending Site. This is handled via Primary Care Support England. If the electronic transfer was a failure PCSE will collect the paper records and the print out of the full EHR and any electronic attachments. If the electronic transfer of the EHR was a success but some attachments failed then PCSE will collect the printed attachments. Further detail on the movement of these paper records can be found here:

How to move medical records - Primary Care Support England

## Appendix C - Incorrect Patient transferred {#GP2GPSendingAdaptorv1.0.1-AppendixC-IncorrectPatienttransferred}

If a user at either the Sending Site or Requesting Site determine that an incorrect Patient has been registered and therefore the incorrect EHR sent, then they must contact and log this with PCSE. PCSE will then liaise with the Sending Site, Requesting Site and the National Back Office to re-register the Patient at the Sending Site and deduct them from the Requesting Site.

## Appendix D - EHR Status Endpoint Data Model {#GP2GPSendingAdaptorv1.0.1-AppendixD-EHRStatusEndpointDataModel}

**When** endpoint/status/conversation ID is called

**Then** the following data model is returned (EHR Message status)

{  
 "attachmentStatus": [  
 {  
 "identifier": [  
 {  
 "system": String,  
 "value": String  
 }  
 ],  
 "fileStatus": enum (PLACEHOLDER, ORIGINAL\_FILE, ERROR)  
 "fileName": String,  
 "originalDescription": String  
 },  
 "migrationLog": [  
 {  
 "received": String (ISO 8601 timestamp),  
 "conversationClosed": String (ISO 8601 timestamp),  
 "errors": [  
 {  
 "code": String  
 "display": "String"  
 }  
 ],  
 "messageRef": String  
 }  
 ],   
 "migrationStatus": enum (COMPLETE, COMPLETE\_WITH\_ISSUES, FAILED\_NME, FAILED\_INCUMBENT, IN\_PROGRESS),  
 "originalRequestDate": String (ISO 8601 timestamp),  
 "fromAsid": String,  
 "toAsid": String  
}

# Dependencies {#GP2GPSendingAdaptorv1.0.1-Dependencies}

There may be dependencies for implementing this Standard, however, there are no Interoperability Standards within the Capabilities and Standards model that are dependents.

# Roadmap {#GP2GPSendingAdaptorv1.0.1-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf](../../../../.raw/DCSDCS/attachments/14425882674/att14425882693-NPFIT-PC-BLD-0158 GP2GP Supplementary Specification Attachment References.pdf)
- [NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf](../../../../.raw/DCSDCS/attachments/14425882674/att14425882696-NPFIT-PC-BLD-0099.04 GP2GP Handling Missing Attachments.pdf)
- [GP2GPSteps15.drawio.png](../../../../.raw/DCSDCS/attachments/14425882674/att14425882699-GP2GPSteps15.drawio.png)
- [GP2GPSteps891011.drawio.png](../../../../.raw/DCSDCS/attachments/14425882674/att14425882702-GP2GPSteps891011.drawio.png)
- [GP2GPSteps467.drawio.png](../../../../.raw/DCSDCS/attachments/14425882674/att14425882705-GP2GPSteps467.drawio.png)
- [image-20250325-105833.png](../../../../.raw/DCSDCS/attachments/14425882674/att14425882708-image-20250325-105833.png)
- [GP2GPSteps123.drawio.png](../../../../.raw/DCSDCS/attachments/14425882674/att14425882711-GP2GPSteps123.drawio.png)
- [GP2GP (2).png](../../../../.raw/DCSDCS/attachments/14425882674/att14425882714-GP2GP (2).png)
- [GP2GPSteps123.drawio](../../../../.raw/DCSDCS/attachments/14425882674/att14425882717-GP2GPSteps123.drawio)
- [GP2GP Sending Adapter flow diagrams.drawIO.png](../../../../.raw/DCSDCS/attachments/14425882674/att14425882720-GP2GP Sending Adapter flow diagrams.drawIO.png)
- [GP2GP Sending Adapter flow diagrams.drawIO](../../../../.raw/DCSDCS/attachments/14425882674/att14425882723-GP2GP Sending Adapter flow diagrams.drawIO)
- [~GP2GP Sending Adapter flow diagrams.drawIO.tmp](../../../../.raw/DCSDCS/attachments/14425882674/att14425882726-~GP2GP Sending Adapter flow diagrams.drawIO.tmp)
