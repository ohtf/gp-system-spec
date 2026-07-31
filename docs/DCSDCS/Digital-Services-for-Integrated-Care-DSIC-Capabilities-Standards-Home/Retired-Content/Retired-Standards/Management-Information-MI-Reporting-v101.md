---
page_id: "1391134317"
space: "DCSDCS"
title: "Management Information (MI) Reporting v1.0.1"
version: 18
updated: "2025-12-15T16:14:18.246Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391134317/Management+Information+MI+Reporting+v1.0.1"
labels: ["standard_retired"]
---

# Management Information (MI) Reporting v1.0.1

|  |  |
| --- | --- |
| **ID** | S49 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Retired |
| **Effective Date** | 01 Apr 2019 |
| **Framework(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) |

/\*<![CDATA[\*/
div.rbtoc1785498422486 {padding: 0px;}
div.rbtoc1785498422486 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785498422486 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#ManagementInformation(MI)Reportingv1.0.1-Introduction)
- [Requirements](#ManagementInformation(MI)Reportingv1.0.1-Requirements)
- [Data Fields Definition](#ManagementInformation(MI)Reportingv1.0.1-DataFieldsDefinition)
  - [All Submissions](#ManagementInformation(MI)Reportingv1.0.1-AllSubmissions)
  - [All Citizen Capabilities](#ManagementInformation(MI)Reportingv1.0.1-AllCitizenCapabilities)
  - [Patient Information Maintenance - GP](#ManagementInformation(MI)Reportingv1.0.1-PatientInformationMaintenance-GP)
  - [Communicate With Practice - Citizen](#ManagementInformation(MI)Reportingv1.0.1-CommunicateWithPractice-Citizen)
  - [Appointments Management - Citizen](#ManagementInformation(MI)Reportingv1.0.1-AppointmentsManagement-Citizen)
  - [Prescription Ordering – Citizen](#ManagementInformation(MI)Reportingv1.0.1-PrescriptionOrdering–Citizen)
  - [View Record - Citizen](#ManagementInformation(MI)Reportingv1.0.1-ViewRecord-Citizen)
  - [Appointments Management - GP](#ManagementInformation(MI)Reportingv1.0.1-AppointmentsManagement-GP)
  - [Document Management](#ManagementInformation(MI)Reportingv1.0.1-DocumentManagement)
  - [Prescribing](#ManagementInformation(MI)Reportingv1.0.1-Prescribing)
  - [Ethnicity Mappings](#ManagementInformation(MI)Reportingv1.0.1-EthnicityMappings)
  - [Healthcare Professional Types](#ManagementInformation(MI)Reportingv1.0.1-HealthcareProfessionalTypes)
  - [Third Next Available Appointment (TNA) Calculation Methodology](#ManagementInformation(MI)Reportingv1.0.1-ThirdNextAvailableAppointment(TNA)CalculationMethodology)
- [Applicable Capabilities](#ManagementInformation(MI)Reportingv1.0.1-ApplicableCapabilities)
- [Dependencies](#ManagementInformation(MI)Reportingv1.0.1-Dependencies)
- [Roadmap](#ManagementInformation(MI)Reportingv1.0.1-Roadmap)

# Introduction

There is a subset of this collection known as Patient Online Management Information (POMI), which is used by NHS England to monitor uptake and usage of online Services and is published regularly. There are also fields included as part of this collection which form part of the GP Workload Tool, a project commissioned by NHS England to aid in improving Patient access to General Practice as part of the goals set out in the Five Year Forward View.

All the necessary governance procedures have been completed for this collection:

- There is a signed Direction to The Authority from NHS England
- The collection has been approved by the Data Coordination Board (formerly SCCI) under reference DCB2236

Although the Direction issued from NHS England mandates that Practices provide the data, they must approve the collection via the Calculating Quality Reporting System (CQRS). Therefore, each month a list of participating Practices will be made available which Suppliers must apply to the data return. Information should not be returned for any Practices who have not consented to this collection via CQRS.

Suppliers will need to adhere to requests made by The Authority within 5 working days including:

- Suppliers to respond to any questions The Authority may have regarding the data submitted
- Where errors are discovered on a report, Suppliers will provide a corrected version

# Requirements

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Requirement Text** | **Level** |
| **GP-MI.1-01** | Each data submission will cover one calendar month  *Between midnight (00:00) on the first day of the calendar month being reported and 23:59 on the last day of the calendar month being reported inclusive. For example, if the report is being produced in November 2015 then the reporting period will be between midnight (00:00) on the 01/10/2015 and 23:59 on the 31/10/2015 inclusive* | MUST |
| **GP-MI.1-02** | Data to be submitted to The Authority on a monthly basis in the month following the reporting period  *If the reporting period is October, then the data will be submitted in November i.e. a retrospective collection* | MUST |
| **GP-MI.1-03** | Data to be submitted to The Authority within 10 working days of the end of each reporting period  *If the reporting period is October, the data will be submitted within 10 working days after 31st October* | MUST |
| **GP-MI.1-04** | Data to be submitted through the nominated The Authority Data Collection Service  *This is the Secure Electronic File Transfer (SEFT) portal and details on using this are embedded below:*   - Secure Electronic File Transfer (SEFT) - Creating Automated SFTP Transfers - Guidance | MUST |
| **GP-MI.1-05** | Data to be submitted in the format prescribed by The Authority  *This is as a csv file and Suppliers have a choice between two templates, as below. Blank templates will be made available on the last working day of each month via the relevant SEFT folder.*   1. [Long and skinny csv template.csv](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134317/Long%20and%20skinny%20csv%20template.csv?version=1&modificationDate=1548932040215&cacheVersion=1&api=v2) 2. [Tabular csv template.csv](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134317/Tabular%20csv%20template.csv?version=1&modificationDate=1549537325950&cacheVersion=1&api=v2)   *Suppliers will inform The Authority which template they will be using* | MUST |
| **GP-MI.1-06** | CSV data submissions will contain all fields in the same order as defined in the CSV file structure table and all applicable data as defined in the Data Fields Definition section. Click here to view CSV file structure table  | Field ID | Data Item | | --- | --- | | H1 | report\_period\_start | | H2 | report\_period\_end | | H3 | supplier | | H4 | supplier\_system | | H5 | supplier\_ system\_version | | H6 | gp\_practice\_code | | 408 | online\_service\_enabled\_status **(retired - return blank)** | | 513 | new\_online\_patient\_count | | 511 | new\_vua\_count | | 512 | online\_patient\_count | | 510 | vua\_count | | 409 | online\_appointment\_enabled\_status | | 514 | online\_patient\_appointment\_count | | 515 | rosu\_appointment\_count **(retired - return blank)** | | 208 | appointment\_available\_count | | 209 | appointment\_available\_online\_count | | 210 | appointment\_scheduled\_count | | 108 | appointment\_scheduled\_trans\_count | | 110 | appointment\_scheduled\_ooh\_online\_trans\_count | | 610 | appointment\_scheduled\_online\_trans\_count | | 109 | appointment\_cancelled\_trans\_count | | 111 | appointment\_cancelled\_ooh\_online\_trans\_count | | 611 | appointment\_cancelled\_online\_trans\_count | | 212 | appointment\_dna\_appt\_count | | 213 | appointment\_dna\_online\_appt\_count | | 620 | appointment\_view\_online\_count **(retired - return blank)** | | 410 | online\_prescription\_enabled\_status | | 516 | online\_patient\_prescription\_count | | 517 | rosu\_prescription\_count **(retired - return blank)** | | 612 | prescription\_online\_trans\_count | | 308 | prescriptions\_ordered\_trans\_count | | 310 | prescription\_online\_ooh\_trans\_count | | 311 | prescription\_online\_eps\_count | | 309 | items\_ordered\_total\_count | | 621 | prescription\_view\_online\_count **(retired - return blank)** | | 411 | online\_communication\_enabled\_status | | 518 | online\_patient\_communication\_count | | 519 | rosu\_communication\_count **(retired - return blank)** | | 613 | comms\_online\_patient\_count | | 614 | comms\_online\_clinician\_count | | 420 | online\_document\_view\_enabled\_status | | 524 | online\_patient\_document\_view\_count | | 525 | rosu\_letter\_view\_count **(retired - return blank)** | | 617 | online\_record\_document\_view\_count | | 413 | online\_record\_view\_enabled\_status | | 522 | online\_patient\_record\_view\_count | | 523 | rosu\_record\_view\_count **(retired - return blank)** | | 615 | online\_record\_view\_count | | 412 | online\_summary\_record\_view\_enabled\_status | | 520 | online\_patient\_summary\_record\_view\_count | | 521 | rosu\_summary\_record\_view\_count **(retired - return blank)** | | 616 | online\_summary\_record\_view\_count | | 421 | online\_test\_result\_view\_enabled\_status **(retired - return blank)** | | 526 | online\_patient\_test\_result\_view\_count **(retired - return blank)** | | 527 | rosu\_test\_result\_view\_count **(retired - return blank)** | | 618 | online\_record\_test\_result\_view\_count **(retired - return blank)** | | 619a | update\_demographics\_online\_trans\_count | | 619b | other\_online\_trans\_count **(retired - return blank)** | | 608 | total\_online\_transactions\_count | | 609 | unique\_online\_patient\_record\_trans\_count **(retired - return blank)** | | 622 | coded\_record\_view\_enabled\_status | | 623 | coded\_online\_patient\_record\_view\_count | | 624 | coded\_record\_view\_online\_count | | 1010 | total\_login\_count\_p | | 1011 | total\_login\_count\_p1 | | 1108 | total\_documents\_count | | 1109 | total\_documents\_scanned\_count | | 1110 | total\_documents\_electronic\_count | | 1201 | appointment\_available\_core\_hours\_count | | 1202 | appointment\_available\_extended\_hours\_count | | 1203 | appointment\_available\_duration\_less\_10\_count | | 1204 | appointment\_available\_duration\_over\_10\_count | | 1207 | appointment\_available\_mode\_face\_to\_face\_count | | 1208 | appointment\_available\_mode\_phone\_count | | 1209 | appointment\_available\_mode\_video\_count | | 1210 | appointment\_available\_mode\_home\_visit\_count | | 1211 | appointment\_available\_mode\_online\_count | | 1213 | appointment\_available\_mode\_other\_count | | 1214 | appointment\_available\_hcptype\_gp\_count | | 1216 | appointment\_available\_hcptype\_nurse\_count | | 1217 | appointment\_available\_hcptype\_other\_clinical\_count | | 1218 | appointment\_available\_hcptype\_other\_count | | 1219 | appointment\_scheduled\_online\_count | | 1220 | appointment\_cancelled\_count | | 1221 | appointment\_cancelled\_online\_count | | 1222 | appointment\_scheduled\_core\_hours\_count | | 1223 | appointment\_scheduled\_extended\_hours\_count | | 1224 | appointment\_attended\_count | | 1227 | appointment\_scheduled\_mode\_face\_to\_face\_count | | 1228 | appointment\_scheduled\_mode\_phone\_count | | 1229 | appointment\_scheduled\_mode\_video\_count | | 1230 | appointment\_scheduled\_mode\_home\_visit\_count | | 1231 | appointment\_scheduled\_mode\_online\_count | | 1232 | appointment\_scheduled\_mode\_other\_count | | 1233 | appointment\_scheduled\_hcptype\_gp\_count | | 1235 | appointment\_scheduled\_hcptype\_nurse\_count | | 1236 | appointment\_scheduled\_hcptype\_other\_clinical\_count | | 1237 | appointment\_scheduled\_hcptype\_other\_count | | 1238 | third\_next\_appointment\_time\_GP\_total | | 1239 | third\_next\_appointment\_time\_nurse\_total | | 1240 | third\_next\_appointment\_time\_other\_clinical\_total | | 1241 | third\_next\_appointment\_time\_GP\_trans\_count | | 1242 | third\_next\_appointment\_time\_nurse\_trans\_count | | 1243 | third\_next\_appointment\_time\_other\_clinical\_trans\_count | | 1244 | appointment\_patient\_sex\_male\_count | | 1245 | appointment\_patient\_sex\_female\_count | | 1246 | appointment\_patient\_sex\_unknown\_count | | 1247 | appointment\_patient\_ethnicity\_white\_count | | 1248 | appointment\_patient\_ethnicity\_mixed\_count | | 1249 | appointment\_patient\_ethnicity\_asian\_count | | 1250 | appointment\_patient\_ethnicity\_black\_count | | 1251 | appointment\_patient\_ethnicity\_other\_count | | 1252 | appointment\_patient\_ethnicity\_unknown\_count | | 1253 | appointment\_patient\_age\_0-1\_count | | 1254 | appointment\_patient\_age\_1-5\_count | | 1255 | appointment\_patient\_age\_6-15\_count | | 1256 | appointment\_patient\_age\_16-45\_count | | 1257 | appointment\_patient\_age\_46-64\_count | | 1258 | appointment\_patient\_age\_65-80\_count | | 1259 | appointment\_patient\_age\_over\_81\_count | | 1260 | patient\_attended\_multiple\_appointments\_count | | MUST |
| **GP-MI.1-06a** | Where a Supplier is not required to provide or cannot provide certain fields, these fields will be included within the data submitted, but left blank, rather than giving a value of '0'.  Suppliers will inform The Authority where there are fields that they are required to return but are unable to do so and explain the reasons for this. | MUST |
| **GP-MI.1-07** | Data will only be returned for Practices which have approved the collection using CQRS  *A list of the ODS codes of all Practices which have approved the collection will be made available to Suppliers as a csv file on the last working day of each month via the relevant SEFT folder.*  *Upon receipt of the data, The Authority will validate that the latest version of this list has been applied* | MUST |
| **GP-MI.1-08** | Suppliers to have a process for checking data quality in reports before they are submitted | MUST |
| **GP-MI.1-09** | Suppliers to ensure that the processes used to produce reports preserve the meaning of data items from one reporting period to the next, so that the content of a report can be compared between periods  *In cases where the Supplier does need to change the process for producing reports in a manner that means reports cannot be compared between reporting periods, they will alert the The Authority Primary Care Data team* | MUST |

# Data Fields Definition

The list of data fields which form this specification are listed below, along with their associated definition, format, and if they are part of Patient Online Management Information (POMI). Some data fields are required to be submitted for all submissions and some are required to be submitted by Suppliers delivering certain Capabilities.

Where a Supplier is offering multiple Solutions which support these Capabilities, a return may be submitted for each Solution individually or as a single submission covering all Solutions so long as it is made clear which Solution the data relates to.

## All Submissions

These data items are to be provided for all submissions regardless of which other data items a Supplier is required to provide based on the Capabilities offered:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field ID** | **Data Item** | **Definition** | **Format** | **Level** |
| **H1** | report\_period\_start | First day of reporting period which the report covers *(the 1st of the month prior to the month in which the data is being submitted i.e. if data is being submitted in July 2018, this field will be 01/06/2018).* | Date (dd/mm/yyyy) | MUST |
| **H2** | report\_period\_end | Last day of reporting period which the report covers *(the final day of the month prior to the month in which the data is being submitted i.e. if data is being submitted in July 2018, this field will be 30/06/2018).* | Date (dd/mm/yyyy) | MUST |
| **H3** | Supplier | Name of Supplier returning the data. | String (63) | MUST |
| **H4** | Supplier\_system | Name of Solution for which data is being returned. | String (63) | MAY |
| **H5** | Supplier\_ system\_version | Version number of the Supplier Solution used at the practice. | String (63) | MAY |
| **H6** | gp\_practice\_code | The GP Practice Code for the GP Practice for which the data is being returned. | String (6) | MUST |

## All Citizen Capabilities

These data items are to be provided by Suppliers delivering any Citizen Capability:

Data items are only to be returned once per Solution (i.e. where a single Solution delivers multiple Citizen Capabilities).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field ID** | **Data Item** | **Definition** | **Format** | **Level** |
| **619a** | update\_demographics\_online\_trans\_count | Total number of demographics update transactions: *(this is the number of transactions involving an update of Patient demographic details, NOT a count of the fields updated; where a transaction includes the update of multiple demographic information fields, this should only be counted as a single transaction)*   - via any Citizen Service - for Patients who are associated with at least one LOSA who is registered to use any Citizen Capability on their behalf whether as 'self' or 'proxy' - at any time within the reporting period | Numeric (integer) | MAY |
| **608** | total\_online\_transactions\_count | Total number of transactions recorded by the Solution:   - transaction took place at any time within the reporting period - Solution logins *(each individual login should be counted separately; this DOES include re-logins after a system time-out)* - via View Record - Citizen Solution *(each view/access of: any part of the Full Care Record, elements of the Detailed Coded Record, Summary Information Record, letters; if any element is viewed/accessed multiple times within the reporting period each view/access should be counted separately)* - via Appointments Management - Citizen Solution *(Appointment scheduling transactions, Appointment cancellation transactions)* - via Prescription Ordering – Citizen Solution *(Prescription ordering transactions; where multiple items are included within a single transaction, this should only be counted once)* - via Communicate With Practice - Citizen Solution *(messages sent from Patient to practice, messages sent from practice to Patient)* - all transactions from update\_demographics\_online\_trans\_count (field 619a)  Validation  - Must be greater or equal to the sum of :    - 610-appointment\_scheduled\_online\_trans\_count   - 611-appointment\_cancelled\_online\_trans\_count   - 612-prescription\_online\_trans\_count   - 613-comms\_online\_Patient\_count   - 614-comms\_online\_clinician\_count   - 615-online\_record\_view\_count   - 616-online\_summary\_record\_view\_count   - 617-online\_record\_document\_view\_count   - 619a-update\_demographics\_online\_trans\_count   - 619b-other\_online\_trans\_count | Numeric (integer) | MAY |
| **1010** | total\_login\_count\_p | Total number of logins to a Citizen Service:   - at any time within the reporting period - by LOSAs - where the Citizen Service being logged into is provided by the same Supplier as provides the Patient Information Maintenance - GP Solution for the Practice | Numeric (integer) | MAY |
| **1011** | total\_login\_count\_p1 | Total number of logins to a Citizen Service:   - at any time within the reporting period - by LOSAs - where the Citizen Service being logged into is provided by a different Supplier than provides the Patient Information Maintenance - GP Solution for the Practice | Numeric (integer) | MAY |

## Patient Information Maintenance - GP

These data items are to be provided by any Supplier delivering the Patient Information Maintenance - GP Capability:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field ID** | **Data Item** | **Definition** | **Format** | **Level** |
| **513** | new\_online\_Patient\_count | Total number of Patients registered for at least one Citizen Service as at report\_period\_end who:   - were registered for any Citizen Service for the first time during the reporting period *(this does NOT include Patients who were previously registered, but for whom service access was changed during the reporting period.)* - are active at the Practice *(this DOES include Patients who moved from 'inactive' to 'active' during the reporting period)* - had a VUA created and associated with their record, which enables the use of any Citizen Service on their behalf whether as 'self' or 'proxy' *(this is a count of Patients associated with VUAs, NOT of the VUAs. Patients with both a 'self and 'proxy' association should only be counted once)* | Numeric (integer) | MAY |
| **511** | new\_vua\_count | Total number of VUAs enabled for the use of at least one Citizen Service as at report\_period\_end where:   - VUA was created by the Practice during the reporting period *(this does NOT include VUAs that were previously created, but where service access configuration was changed during the reporting period. It DOES include VUAs where the status changed from 'inactive' to 'active' during the reporting period)* - VUA account is active and associated with at least one Active Patient whether as 'self' or 'proxy' *(VUAs that enable both 'self' and 'proxy' association should only be counted once)* | Numeric (integer) | MAY |
| **512** | online\_Patient\_count | Total number of Patients registered for at least one Citizen Service as at report\_period\_end who:   - were registered for any Citizen Service as at report\_period\_end *(this DOES include registrations completed within or at any point before the reporting period)* - are active at the Practice - have a VUA associated with their record, which enables the use of any Citizen Service on their behalf whether as 'self' or 'proxy' *(this is a count of Patients associated with VUAs, NOT of the VUAs. Patients with both a 'self and 'proxy' association should only be counted once)* | Numeric (integer) | MAY |
| **510** | vua\_count | Total number of VUAs enabled for the use of at least one Citizen Service as at report\_period\_end where:   - VUA was created by the Practice and exists at report\_period\_end *(this DOES include VUAs created within or at any point before the reporting period)* - VUA account is active and associated with at least one Active Patient whether as 'self' or 'proxy' *(VUAs with both a 'self' and 'proxy' association should only be counted once)* | Numeric (integer) | MAY |
| **409** | online\_appointment\_enabled\_status | Functionality status in the Patient Information Maintenance - GP Solution at the Practice for enabling the use of Appointments Management - Citizen Capability for booking and/or cancelling Appointments as at reporting\_end\_date. | Flag (0, 1, 2, 9) | MUST |
| **514** | online\_Patient\_appointment\_count | Total number of Patients registered to use Appointments Management - Citizen Capability as at report\_period\_end who:   - were registered to use Appointments Management - Citizen Capability as at report\_period\_end *(this DOES include registrations completed within or at any point before the reporting period)* - are active at the Practice - have a VUA associated with their record, which enables the use of the Appointments Management - Citizen Capability on their behalf whether as 'self' or 'proxy' *(this is a count of Patients associated with VUAs, NOT of the VUAs. Patients with both a 'self and 'proxy' association should only be counted once)* | Numeric (integer) | MUST |
| **410** | online\_prescription\_enabled\_status | Functionality status in the Patient Information Maintenance - GP Solution at the Practice for enabling the use of Prescription Ordering – Citizen Capability as at report\_period\_end. | Flag (0, 1, 2, 9) | MUST |
| **516** | online\_Patient\_prescription\_count | Total number of Patients registered to use Prescription Ordering – Citizen Capability as at report\_period\_end who:   - were registered to use Prescription Ordering – Citizen Capability as at report\_period\_end *(this DOES include registrations completed within or at any point before the reporting period)* - are active at the Practice - have a VUA associated with their record, which enables the use of the Prescription Ordering – Citizen Capability on their behalf whether as 'self' or 'proxy' *(this is a count of Patients associated with VUAs, NOT of the VUAs. Patients with both a 'self and 'proxy' association should only be counted once)* | Numeric (integer) | MUST |
| **411** | online\_communication\_enabled\_status | Functionality status in the Patient Information Maintenance - GP Solution at the Practice for enabling the use of Communicate With Practice - Citizen Capability as at report\_period\_end. | Flag (0, 1, 2, 9) | MAY |
| **518** | online\_Patient\_communication\_count | Total number of Patients registered to use Communicate With Practice - Citizen Capability as at report\_period\_end who:   - were registered to use Communicate With Practice - Citizen Capability as report\_period\_end *(this DOES include registrations completed within or at any point before the reporting period)* - are active at the Practice - have a VUA associated with their record, which enables the use of the Communicate With Practice - Citizen Capability on their behalf whether as 'self' or 'proxy' *(this is a count of Patients associated with VUAs, NOT of the VUAs. Patients with both a 'self and 'proxy' association should only be counted once)* | Numeric (integer) | MAY |
| **420** | online\_document\_view\_enabled\_status | Functionality status in the Patient Information Maintenance - GP Solution at the Practice for enabling the use of the Document Access Level Record Access Service as at report\_period\_end. | Flag (0, 1, 2, 9) | MUST |
| **524** | online\_Patient\_document\_view\_count | Total number of Patients registered to use the Document Access Level Record Access Service at report\_period\_end who:   - were registered to use the Document Access Level Record Access Service to view documents as at report\_period\_end *(this DOES include registrations completed within or at any point before the reporting period)* - are active at the Practice - have a VUA associated with their record, which enables the use of the Document Access Level Record Access Service to view documents on their behalf whether as 'self' or 'proxy' *(this is a count of Patients associated with VUAs, NOT of the VUAs. Patients with both a 'self and 'proxy' association should only be counted once)* | Numeric (integer) | MUST |
| **413** | online\_record\_view\_enabled\_status | Functionality status in the Patient Information Maintenance - GP Solution for enabling the use of the Full Record Record Access Service as at report\_period\_end. | Flag (0, 1, 2, 9) | MUST |
| **522** | online\_Patient\_record\_view\_count | Total number of Patients registered to use the Full Record Record Access Service to view their Full Record as at report\_period\_end who:   - were registered to use the Full Record Record Access Service to view their Full Record as at report\_period\_end *(this DOES include registrations completed within or at any point before the reporting period)* - are active at the Practice - have a VUA associated with their record, which enables the use of the Full Record Record Access Service to view documents on their behalf whether as 'self' or 'proxy' *(this is a count of Patients associated with VUAs, NOT of the VUAs. Patients with both a 'self and 'proxy' association should only be counted once)* | Numeric (integer) | MUST |
| **412** | online\_summary\_record\_view\_enabled\_status | Functionality status in the Patient Information Maintenance - GP Solution for enabling the use of the Summary Information Record Record Access Service as at report\_period\_end. | Flag (0, 1, 2, 9) | MUST |
| **520** | online\_Patient\_summary\_record\_view\_count | Total number of Patients registered to use the Summary Information Record Record Access Service to view their Summary Information Record as at report\_period\_end who:   - were registered to use the Summary Information Record Record Access Service to view their Summary Information Record as at report\_period\_end *(this DOES include registrations completed within or at any point before the reporting period)* - are active at the Practice - have a VUA associated with their record, which enables the use of the Summary Information Record Record Access Service to view documents on their behalf whether as 'self' or 'proxy' *(this is a count of Patients associated with VUAs, NOT of the VUAs. Patients with both a 'self and 'proxy' association should only be counted once)* | Numeric (integer) | MUST |
| **622** | coded\_record\_view\_enabled\_status | Functionality status in the Patient Information Maintenance - GP Solution for enabling the use of the Detailed Coded Record Record Access Service as at report\_period\_end. | Flag (0, 1, 2, 9) | MUST |
| **623** | coded\_online\_Patient\_record\_view\_count | Total number of Patients registered to use the Detailed Coded Record Record Access Service to view their Detailed Coded Record as at report\_period\_end who:   - were registered to use Detailed Coded Record Record Access Service to view their Detailed Coded Record as at report\_period\_end *(this DOES include registrations completed within or at any point before the reporting period)* - are active at the Practice - have a VUA associated with their record, which enables the use of the Detailed Coded Record Record Access Service to view documents on their behalf whether as 'self' or 'proxy' *(this is a count of Patients associated with VUAs, NOT of the VUAs. Patients with both a 'self and 'proxy' association should only be counted once)* | Numeric (integer) | MUST |
| **1108** | total\_documents\_count | Total number of unique documents received into and stored by the Solution that were: *(this does NOT include instances of duplicate documents being received and recorded against a Patient record)*   - recorded against a Patient record - recorded against a Patient record at any time within the reporting period *(if the document is received by the system outside of the reporting period, but saved against a Patient record within the reporting period, then this WILL be included; if the document is received into the system within the reporting period, but not saved against a Patient record until outside the reporting period this will NOT be included)* - received via any mechanism *(i.e. electronic, scanned, manual etc. are all included)*   If same data is stored by multiple Solutions, it will only be submitted once by one Supplier (see 1108 in Document Management) | Numeric (integer) | MAY |
| **1109** | total\_documents\_scanned\_count | Total number of unique documents received into the system that were: *(this does NOT include instances of duplicate documents being received and recorded against a Patient record)*   - recorded against a Patient record - recorded against a Patient record at any time within the reporting period *(if the document is received by the system outside of the reporting period, but saved against a Patient record within the reporting period, then this WILL be included; if the document is received into the system within the reporting period, but not saved against a Patient record until outside the reporting period this will NOT be included)* - received via scanning *(i.e. documents received on paper and scanned as opposed to being received via an electronic format)*   If same data is stored by multiple Solutions, it will only be submitted once by one Supplier (see 1109 in Document Management) | Numeric (integer) | MAY |
| **1110** | total\_documents\_electronic\_count | Total number of unique documents received into the system that were: *(this does NOT include instances of duplicate documents being received and recorded against a Patient record)*   - recorded against a Patient record - recorded against a Patient record at any time within the reporting period *(if the document is received by the system outside of the reporting period, but saved against a Patient record within the reporting period, then this WILL be included; if the document is received into the system within the reporting period, but not saved against a Patient record until outside the reporting period this will NOT be included)* - received electronically *(i.e. documents received electronically as opposed to being received in paper format and scanned)*   If same data is stored by multiple Solutions, it will only be submitted once by one Supplier (see 1110 in Document Management) | Numeric (integer) | MAY |

## Communicate With Practice - Citizen

These data items to be provided by any Supplier delivering the Communicate with Practice - Citizen Capability:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field ID** | **Data Item** | **Definition** | **Format** | **Level** |
| **613** | comms\_online\_Patient\_count | Total number of communications sent:   - using the Communicate With Practice - Citizen Solution - from Patient to practice - at any time within the reporting period | Numeric (integer) | MAY |
| **614** | comms\_online\_clinician\_count | Total number of communications sent:   - using the Communicate With Practice - Citizen Solution - from practice to Patient - at any time within the reporting period | Numeric (integer) | MAY |

## Appointments Management - Citizen

These data items to be provided by any Supplier delivering the Appointments Management - Citizen Capability:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field ID** | **Data Item** | **Definition** | **Format** | **Level** |
| **610** | appointment\_scheduled\_online\_trans\_count | All transactions from appointment\_scheduled\_trans\_count (field 108) where:   - the scheduling transaction took place via Appointments Management - Citizen Solution | Numeric (integer) | MAY |
| **110** | appointment\_scheduled\_ooh\_online\_trans\_count | All transactions from appointment\_scheduled\_online\_trans\_count (field 610) where:   - the scheduling transaction took place via Appointments Management - Citizen Solution - the scheduling transaction took place within the reporting period, but outside of regular working hours *(outside of regular working hours is defined as between 1830 and 0759 inclusive on weekdays; weekends i.e. 1830 Friday to 0759 Monday; all day bank holidays i.e. 0000 to 2359)*  Validation  - Must be less or equal to 108 appointment\_scheduled\_trans\_count | Numeric (integer) | MAY |
| **611** | appointment\_cancelled\_online\_trans\_count | All transactions from appointment\_cancelled\_trans\_count (field 109) where:   - the cancellation transaction took place via Appointments Management - Citizen Solution | Numeric (integer) | MUST |
| **111** | appointment\_cancelled\_ooh\_online\_trans\_count | All transactions from appointment\_cancelled\_online\_trans\_count (field 611) where:   - the cancellation transaction took place via Appointments Management - Citizen Solution - the cancellation transaction took place within the reporting period, but outside of regular working hours *(outside of regular working hours is defined as between 1830 and 0759 inclusive on weekdays; weekends i.e. 1830 Friday to 0759 Monday; all day bank holidays i.e. 0000 to 2359)*  Validation  - Must be less or equal to 109 appointment\_cancelled\_trans\_count | Numeric (integer) | MAY |
| **1219** | appointment\_scheduled\_online\_count | All Appointments from appointment\_scheduled\_count (field 210) which were:   - scheduled using the Appointments Management - Citizen Solution *(A count as at the end of the reporting period of the number of Appointments booked via an online method based on the final status and booking method of each Slot made available for Patients to book in the period based on start time. NOT the number of transactions which took place for booking Appointments online i.e. an Appointment Slot which was booked online then cancelled will NOT be included in this count; an Appointment Slot which was booked over the phone, cancelled and then booked again via a Citizen Service WILL be included in this count)*  Validation  - Must be less than or equal to 209-appointment\_available\_online\_count - Must be less than or equal to 210-appointment\_scheduled\_count - Must be less than or equal to 610-appointment\_scheduled\_online\_trans\_count | Numeric (integer) | MAY |
| **1221** | appointment\_cancelled\_online\_count | All Appointments from appointment\_cancelled\_count (field 1220) which were:   - cancelled using the Appointments Management - Citizen Solution *(A count as at the end of the reporting period of the number of Appointments cancelled via an online method based on the final status and cancellation method of each Slot made available for Patients to book in the period based on start time. NOT the number of transactions which took place for cancelling Appointments online i.e. an Appointment Slot which is booked over the phone, then cancelled online WILL be included in this count; an Appointment which is booked, then cancelled online, then booked again will NOT be included in this count.)*  Validation  - Must be less than or equal to 1220-appointment\_cancelled\_count - Must be less than or equal to 611-appointment\_cancelled\_online\_trans\_count | Numeric (integer) | MAY |

## Prescription Ordering – Citizen

These data items to be provided by any Supplier delivering the Prescription Ordering - Citizen Capability:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field ID** | **Data Item** | **Definition** | **Format** | **Level** |
| **612** | prescription\_online\_trans\_count | All transactions from prescriptions\_ordered\_trans\_count (field 308) where:   - the ordering transaction took place via the Prescription Ordering - Citizen Solution | Numeric (integer) | MUST |
| **310** | prescription\_online\_ooh\_trans\_count | All transactions from prescription\_online\_trans\_count (field 612) where:   - the ordering transaction took place via the Prescription Ordering - Citizen Solution - the ordering transaction took place within the reporting period, but outside of regular working hours *(outside of regular working hours is defined as between 1830 and 0759 inclusive on weekdays; weekends i.e. 1830 Friday to 0759 Monday; all day bank holidays i.e. 0000 to 2359)* | Numeric (integer) | MAY |
| **311** | prescription\_online\_eps\_count | All transactions from prescription\_online\_trans\_count (field 612) where:   - the order was for a repeat Prescription - the transaction is linked to Electronic Prescription Service (EPS) - Prescribing | Numeric (integer) | MAY |

## View Record - Citizen

These data items to be provided by any Supplier delivering the View Record - Citizen Capability:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field ID** | **Data Item** | **Definition** | **Format** | **Level** |
| **615** | online\_record\_view\_count | Total number of accesses/views of any part of the Full Record:   - using View Record - Citizen Solution - by Patients enabled for the Full Record Record Access Service - at any time within the reporting period *(if any element of the Full Record is viewed/accessed multiple times within the reporting period, each view/access should be counted separately)* | Numeric (integer) | MUST |
| **616** | online\_summary\_record\_view\_count | Total number of accesses/views of the Summary Information Record:   - using View Record - Citizen Solution - by Patients enabled for the Summary Information Record Record Access Service - at any time within the reporting period *(if the Summary Information Record is viewed/accessed multiple times within the reporting period, each view/access should be counted separately)* | Numeric (integer) | MUST |
| **624** | coded\_record\_view\_online\_count | Total number of accesses/views of the Detailed Coded Record:   - using View Record - Citizen Solution - by Patients enabled for the Detailed Coded Record Record Access Service - at any time within the reporting period *(if the Detailed Coded Record is viewed/accessed multiple times within the reporting period, each view/access should be counted separately)* | Numeric (integer) | MUST |
| **617** | online\_record\_document\_view\_count | Total number of document accesses/views:   - using View Record - Citizen Solution - by Patients using the Document Access Level Record Access Service - at any time within the reporting period *(if a letter is viewed/accessed multiple times within the reporting period, each view/access should be counted separately)* | Numeric (integer) | MUST |

## Appointments Management - GP

These data items to be provided by any Supplier delivering the Appointments Management - GP Capability:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field ID** | **Data Item** | **Definition** | **Format** | **Level** |
| **208** | appointment\_available\_count | Total number of Slots that were available for Patients to book as Appointments: *(Slots made available NOT Appointments which were booked/scheduled OR actually took place)*   - with a start date and time within the reporting period *(based on start time of Appointment)* - bookable via any booking method - with any healthcare professional type - of any Slot Type *(type of Appointment is defined as routine, emergency, or specialist clinics etc. terminology may differ between Supplier systems; where Appointment Slot was available for a Patient to book i.e. exclude any Slots marked as 'blocked' or 'non-bookable')* - of any duration | Numeric (integer) | MAY |
| **209** | appointment\_available\_online\_count | All Slots from appointment\_available\_count (field 208) which were:   - bookable via Appointments Management - Citizen Solution | Numeric (integer) | MAY |
| **210** | appointment\_scheduled\_count | Total number of Appointments as at report\_period\_end that were booked: *(with status of 'booked' as at the end of the reporting period; terminology for 'booked' may differ between Supplier systems; status at the end of the reporting period may also be 'attended' or 'DNA')*   - with a start date and time within the reporting period *(based on start time of Appointment)* - via any booking method - with any healthcare professional type - of any Slot Type *(type of Appointment is defined as routine, emergency, or specialist clinics etc. terminology may differ between Supplier Solutions)* - of any duration - of any attendance status | Numeric (integer) | MAY |
| **108** | appointment\_scheduled\_trans\_count | Total number of Appointment scheduling transactions where: *(this is a count of transactions resulting in an Appointment booking, NOT the number of Appointment Slots with a status of 'booked')*   - the scheduling transaction took place at any time within the reporting period - the start date and time of the Appointment being booked may be within or outside of the reporting period - the scheduling transaction took place via any booking method - Appointment is with any healthcare professional type - Appointment is of any Slot Type - Appointment is of any duration - Appointment has any attendance status *e.g. An Appointment scheduling transaction takes place on 23/01/2018 to schedule an Appointment for 02/02/2018. The report for January 2018 would include an Appointment scheduled transaction (field 108) but NOT an available Appointment (field 208) or a scheduled Appointment (field 210)*  Validation  - Must be greater or equal to 110 appointment\_scheduled\_ooh\_trans\_count | Numeric (integer) | MUST |
| **109** | appointment\_cancelled\_trans\_count | Total number of Appointment cancellation transactions where: *(this is a count of transactions resulting in an Appointment cancellation, NOT the number of Appointment Slots with a status of 'cancelled')*   - the cancellation transaction took place at any time within the reporting period - the start date and time of the Appointment being cancelled may be within or outside of the reporting period - the cancellation transaction took place via any cancellation method - Appointment is with any healthcare professional type - Appointment is of any Slot Type - Appointment is of any duration - Appointment has any attendance status *e.g. An Appointment cancellation transaction takes place on 23/01/2018 to cancel an Appointment for 02/02/2018. The report for January 2018 would include an Appointment cancelled transaction (field 109) but NOT an available Appointment (field 208), a scheduled Appointment (field 210) or a cancelled Appointment* *(field 1220)*  Validation  - Must be greater or equal to 111 appointment\_cancelled\_ooh\_trans\_count | Numeric (integer) | MAY |
| **212** | appointment\_dna\_appt\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - Appointment status is 'Did Not Attend' as at report\_period\_end\_date *(terminology for 'Did Not Attend' may differ between Supplier systems)* | Numeric (integer) | MAY |
| **213** | appointment\_dna\_online\_appt\_count | All Appointments from appointment\_dna\_appt\_count (field 212) which were:   - scheduled via  Appointments Management - Citizen Solution | Numeric (integer) | MAY |
| **1201** | appointment\_available\_core\_hours\_count | All Slots from appointment\_available\_count (field 208):   - with a start date and time within core hours (defined as 8am to 6.30pm on weekdays) *(core hours defined as 8am-6.30pm on weekdays except Good Friday, Christmas Day or bank holidays, as set out in the GMS contract. Based on Appointment start time i.e. a 10 minute Appointment scheduled to start at 6.25pm will be counted as a core hours Appointment; an Appointment scheduled to start at 8am will be counted as a core hours Appointment; an Appointment scheduled to start at 6.30pm will be counted as an extended hours Appointment)*  Validation  - Must be Sum of 1201-appointment\_available\_core\_hours\_count AND 1202-appointment\_available\_extended\_hours\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1202** | appointment\_available\_extended\_hours\_count | All Slots from appointment\_available\_count (field 208):   - with a start date and time NOT in core hours *(core hours defined as 8am-6.30pm on weekdays except Good Friday, Christmas Day or bank holidays, as set out in the GMS contract. Based on Appointment start time i.e. a 10 minute Appointment scheduled to start at 6.25pm will be counted as a core hours Appointment; an Appointment scheduled to start at 8am will be counted as a core hours Appointment; an Appointment scheduled to start at 6.30pm will be counted as an extended hours Appointment; this is a count of Appointments which do NOT fall within core hours)*  Validation  - Must be Sum of 1201-appointment\_available\_core\_hours\_count AND 1202-appointment\_available\_extended\_hours\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1203** | appointment\_available\_duration\_less\_10\_count | All Slots from appointment\_available\_count (field 208):   - with duration of 10 minutes or less *(an Appointment of exactly 10 minutes duration will be included in this count)*  Validation  - Must be Sum of 1203-appointment\_available\_duration\_less\_10\_count AND 1204-appointment\_available\_duration\_over\_10\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1204** | appointment\_available\_duration\_over\_10\_count | All Slots from appointment\_available\_count (field 208):   - with duration of more than 10 minutes *(an Appointment of exactly 10 minutes duration will NOT be included in this count)*  Validation  - Must be Sum of 1203-appointment\_available\_duration\_less\_10\_count AND 1204-appointment\_available\_duration\_over\_10\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1207** | appointment\_available\_mode\_face\_to\_face\_count | All Slots from appointment\_available\_count (field 208):   - of mode of Appointment: Face to face *(a count as at the end of the reporting period of the number of Slots made available for Patients to book as a face to face Appointment i.e. if an Appointment Slot is initially made available as a face to face Appointment and then reassigned as a telephone Appointment, this will NOT be included in this count; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)*  Validation  - Must be Sum of 1207-appointment\_available\_mode\_face\_to\_face\_count AND 1208-appointment\_available\_mode\_phone\_count AND 1209-appointment\_available\_mode\_video\_count AND 1210-appointment\_available\_mode\_home\_visit\_count AND 1211-appointment\_available\_mode\_online\_count AND 1213-appointment\_available\_mode\_other\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1208** | appointment\_available\_mode\_phone\_count | All Slots from appointment\_available\_count (field 208):   - of mode of Appointment: Telephone *(a count as at the end of the reporting period of the number of Slots made available for Patients to book as a telephone Appointment i.e. if an Appointment Slot is initially made available as a face to face Appointment and then reassigned as a telephone Appointment, this WILL be included in this count; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)*  Validation  - Must be Sum of 1207-appointment\_available\_mode\_face\_to\_face\_count AND 1208-appointment\_available\_mode\_phone\_count AND 1209-appointment\_available\_mode\_video\_count AND 1210-appointment\_available\_mode\_home\_visit\_count AND 1211-appointment\_available\_mode\_online\_count AND 1213-appointment\_available\_mode\_other\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1209** | appointment\_available\_mode\_video\_count | All Slots from appointment\_available\_count (field 208):   - of mode of Appointment: Video (i.e. Skype) *(a count as at the end of the reporting period of the number of Slots made available for Patients to book as a video Appointment i.e. if an Appointment Slot is initially made available as a video Appointment and then reassigned as a telephone Appointment, this will NOT be included in this count; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)*  Validation  - Must be Sum of 1207-appointment\_available\_mode\_face\_to\_face\_count AND 1208-appointment\_available\_mode\_phone\_count AND 1209-appointment\_available\_mode\_video\_count AND 1210-appointment\_available\_mode\_home\_visit\_count AND 1211-appointment\_available\_mode\_online\_count AND 1213-appointment\_available\_mode\_other\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1210** | appointment\_available\_mode\_home\_visit\_count | All Slots from appointment\_available\_count (field 208):   - of mode of Appointment: Home Visit *(a count as at the end of the reporting period of the number of Slots made available for Patients to book as a home visit i.e. if an Appointment Slot is initially made available as a face to face Appointment and then reassigned as a home visit, this WILL be included in this count; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)*  Validation  - Must be Sum of 1207-appointment\_available\_mode\_face\_to\_face\_count AND 1208-appointment\_available\_mode\_phone\_count AND 1209-appointment\_available\_mode\_video\_count AND 1210-appointment\_available\_mode\_home\_visit\_count AND 1211-appointment\_available\_mode\_online\_count AND 1213-appointment\_available\_mode\_other\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1211** | appointment\_available\_mode\_online\_count | All Slots from appointment\_available\_count (field 208):   - of mode of Appointment: Online *(a count as at the end of the reporting period of the number of Slots made available for Patients to book as an online Appointment i.e. if an Appointment Slot is initially made available as an online Appointment and then reassigned as a telephone Appointment, this will NOT be included in this count; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)*  Validation  - Must be Sum of 1207-appointment\_available\_mode\_face\_to\_face\_count AND 1208-appointment\_available\_mode\_phone\_count AND 1209-appointment\_available\_mode\_video\_count AND 1210-appointment\_available\_mode\_home\_visit\_count AND 1211-appointment\_available\_mode\_online\_count AND 1213-appointment\_available\_mode\_other\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1213** | appointment\_available\_mode\_other\_count | All Slots from appointment\_available\_count (field 208):   - of mode of Appointment: Other *(a count as at the end of the reporting period of the number of Slots made available for Patients to book as any other mode of Appointment not given above; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this; this count WILL include any unknowns)*  Validation  - Must be Sum of 1207-appointment\_available\_mode\_face\_to\_face\_count AND 1208-appointment\_available\_mode\_phone\_count AND 1209-appointment\_available\_mode\_video\_count AND 1210-appointment\_available\_mode\_home\_visit\_count AND 1211-appointment\_available\_mode\_online\_count AND 1213-appointment\_available\_mode\_other\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1214** | appointment\_available\_hcptype\_gp\_count | All Slots from appointment\_available\_count (field 208):   - with healthcare professional type: General-Practitioner-(GP) *(a count as at the end of the reporting period of the number of Slots made available for Patients to book with healthcare professional type of GP or similar i.e. if an Appointment Slot is initially made available with a GP and then reassigned to nurse, this will NOT be included in this count; healthcare professional groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this; see embedded document for a list of types to be included in this count)*  Validation  - Must be Sum of 1214-appointment\_available\_hcptype\_gp\_count AND 1216-appointment\_available\_hcptype\_nurse\_count AND 1217-appointment\_available\_hcptype\_other\_clinical\_count AND 1218-appointment\_available\_hcptype\_other\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1216** | appointment\_available\_hcptype\_nurse\_count | All Slots from appointment\_available\_count (field 208):   - with healthcare professional type: Nurse *(a count as at the end of the reporting period of the number of Slots made available for Patients to book with healthcare professional type of Nurse or similar i.e. if an Appointment Slot is initially made available with a Nurse and then reassigned to GP, this will NOT be included in this count; healthcare professional groupings may differ between Supplier systems and The Authority will consult with Suppliers on this; see embedded document for a list of types to be included in this count)*  Validation  - Must be Sum of 1214-appointment\_available\_hcptype\_gp\_count AND 1216-appointment\_available\_hcptype\_nurse\_count AND 1217-appointment\_available\_hcptype\_other\_clinical\_count AND 1218-appointment\_available\_hcptype\_other\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1217** | appointment\_available\_hcptype\_other\_clinical\_count | All Slots from appointment\_available\_count (field 208):   - with healthcare professional type: Other – Clinical *(a count as at the end of the reporting period of the number of Slots made available for Patients to book with healthcare professional type of Other – Clinical i.e. if an Appointment Slot is initially made available with a Nurse and then reassigned to another clinical user other than Nurse or GP, this WILL be included in this count; healthcare professional groupings may differ between Supplier systems and The Authority will consult with Suppliers on this; see embedded document for a list of types to be included in this count)*  Validation  - Must be Sum of 1214-appointment\_available\_hcptype\_gp\_count AND 1216-appointment\_available\_hcptype\_nurse\_count AND 1217-appointment\_available\_hcptype\_other\_clinical\_count AND 1218-appointment\_available\_hcptype\_other\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1218** | appointment\_available\_hcptype\_other\_count | All Slots from appointment\_available\_count (field 208):   - with healthcare professional type: Other *(a count as at the end of the reporting period of the number of Slots made available for Patients to book with any other healthcare professional type, including clerical user types i.e. if an Appointment Slot is initially made available with a Nurse and then reassigned to another health care professional type which is not GP, Nurse or other clinical, this WILL be included in this count; see embedded document for a list of all the types which will NOT be included in this count; this count WILL include any unknowns)*  Validation  - Must be Sum of 1214-appointment\_available\_hcptype\_gp\_count AND 1216-appointment\_available\_hcptype\_nurse\_count AND 1217-appointment\_available\_hcptype\_other\_clinical\_count AND 1218-appointment\_available\_hcptype\_other\_count - Must be less than or equal to 208-appointment\_available\_count | Numeric (integer) | MAY |
| **1220** | appointment\_cancelled\_count | Total number of Appointments as at report\_period\_end that were cancelled: *(with status of 'cancelled' as at the end of the reporting period; terminology for 'cancelled' may differ between Supplier systems)*   - with a start date and time within the reporting period *(based on start time of Appointment)* - using any method *(A count as at the end of the reporting period of the number of Appointments cancelled based on the final status of each Slot made available for Patients to book in the period based on start time. NOT the number of transactions which took place for cancelling Appointments i.e. an Appointment Slot which is booked, then cancelled, then booked again will NOT be included in this count)* - with any healthcare professional type - of any Slot Type *(type of Appointment is defined as routine, emergency, or specialist clinics etc. terminology may differ between Supplier systems)* - of any duration  Validation  - Must be less than or equal to 208-appointment\_available\_count - Must be less than or equal to 109-appointment\_cancelled\_trans\_count | Numeric (integer) | MAY |
| **1222** | appointment\_scheduled\_core\_hours\_count | All Appointments from appointment\_scheduled\_count (field 210) which were:   - with a start date and time within core hours (defined as 8am to 6.30pm on weekdays) *(core hours defined as 8am-6.30pm on weekdays except Good Friday, Christmas Day or bank holidays, as set out in the GMS contract. Based on Appointment start time i.e. a 10 minute Appointment scheduled to start at 6.25pm will be counted as a core hours Appointment; an Appointment scheduled to start at 8am will be counted as a core hours Appointment; an Appointment scheduled to start at 6.30pm will be counted as an extended hours Appointment)*  Validation  - Must be less than or equal to 1201-appointment\_available\_core\_hours\_count - Must be Sum of 1222-appointment\_scheduled\_core\_hours\_count AND 1223-appointment\_scheduled\_extended\_hours\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1223** | appointment\_scheduled\_extended\_hours\_count | All Appointments from appointment\_scheduled\_count (field 210) which were:   - with a start date and time NOT in core hours *(core hours defined as 8am-6.30pm on weekdays except Good Friday, Christmas Day or bank holidays, as set out in the GMS contract. Based on Appointment start time i.e. a 10 minute Appointment scheduled to start at 6.25pm will be counted as a core hours Appointment; an Appointment scheduled to start at 8am will be counted as a core hours Appointment; an Appointment scheduled to start at 6.30pm will be counted as an extended hours Appointment; this is a count of Appointments which do NOT fall within core hours)*  Validation  - Must be less than or equal to 1202-appointment\_available\_extended\_hours\_count - Must be Sum of 1222-appointment\_scheduled\_core\_hours\_count AND 1223-appointment\_scheduled\_extended\_hours\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1224** | appointment\_attended\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - Appointment status is 'Attended' as at report\_period\_end\_date *(terminology for 'Attend' may differ between Supplier systems)*  Validation  - Must be less than or equal to 210-appointment\_scheduled\_count - Must be Sum of 1224-appointment\_attended\_count AND 212-appointment\_dna\_appt\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1227** | appointment\_scheduled\_mode\_face\_to\_face\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - of mode of Appointment: Face to face *(a count as at the end of the reporting period of the number of Slots scheduled as a face to face Appointment i.e. if an Appointment Slot is initially scheduled as a face to face Appointment and then reassigned as a telephone Appointment, this will NOT be included in this count; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)*  Validation  - Must be less than or equal to 1207-appointment\_available\_mode\_face\_to\_face\_count - Must be Sum of 1227-appointment\_scheduled\_mode\_face\_to\_face\_count AND 1228-appointment\_scheduled\_mode\_phone\_count AND 1229-appointment\_scheduled\_mode\_video\_count AND 1230-appointment\_scheduled\_mode\_home\_visit\_count AND 1231-appointment\_scheduled\_mode\_online\_count AND 1232-appointment\_scheduled\_mode\_other\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1228** | appointment\_scheduled\_mode\_phone\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - of mode of Appointment: Telephone *(a count as at the end of the reporting period of the number of Slots scheduled as a telephone Appointment i.e. if an Appointment Slot is initially scheduled as a face to face Appointment and then reassigned as a telephone Appointment, this WILL be included in this count; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)*  Validation  - Must be less than or equal to 1208-appointment\_available\_mode\_phone\_count - Must be Sum of 1227-appointment\_scheduled\_mode\_face\_to\_face\_count AND 1228-appointment\_scheduled\_mode\_phone\_count AND 1229-appointment\_scheduled\_mode\_video\_count AND 1230-appointment\_scheduled\_mode\_home\_visit\_count AND 1231-appointment\_scheduled\_mode\_online\_count AND 1232-appointment\_scheduled\_mode\_other\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1229** | appointment\_scheduled\_mode\_video\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - of mode of Appointment: Video (i.e. Skype) *(a count as at the end of the reporting period of the number of Slots scheduled as a video Appointment i.e. if an Appointment Slot is initially scheduled as a video Appointment and then reassigned as a telephone Appointment, this will NOT be included in this count; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)*  Validation  - Must be less than or equal to 1209-appointment\_available\_mode\_video\_count - Must be Sum of 1227-appointment\_scheduled\_mode\_face\_to\_face\_count AND 1228-appointment\_scheduled\_mode\_phone\_count AND 1229-appointment\_scheduled\_mode\_video\_count AND 1230-appointment\_scheduled\_mode\_home\_visit\_count AND 1231-appointment\_scheduled\_mode\_online\_count AND 1232-appointment\_scheduled\_mode\_other\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1230** | appointment\_scheduled\_mode\_home\_visit\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - of mode of Appointment: Home Visit *(a count as at the end of the reporting period of the number of Slots scheduled as home visits i.e. if an Appointment Slot is initially scheduled as a face to face Appointment and then reassigned as a home visit, this WILL be included in this count; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)*  Validation  - Must be less than or equal to 1210-appointment\_available\_mode\_home\_visit\_count - Must be Sum of 1227-appointment\_scheduled\_mode\_face\_to\_face\_count AND 1228-appointment\_scheduled\_mode\_phone\_count AND 1229-appointment\_scheduled\_mode\_video\_count AND 1230-appointment\_scheduled\_mode\_home\_visit\_count AND 1231-appointment\_scheduled\_mode\_online\_count AND 1232-appointment\_scheduled\_mode\_other\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1231** | appointment\_scheduled\_mode\_online\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - of mode of Appointment: Online *(a count as at the end of the reporting period of the number of Slots scheduled as an online Appointment i.e. if an Appointment Slot is initially scheduled as an online Appointment and then reassigned as a telephone Appointment, this will NOT be included in this count; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)*  Validation  - Must be less than or equal to 1211-appointment\_available\_mode\_online\_count - Must be Sum of 1227-appointment\_scheduled\_mode\_face\_to\_face\_count AND 1228-appointment\_scheduled\_mode\_phone\_count AND 1229-appointment\_scheduled\_mode\_video\_count AND 1230-appointment\_scheduled\_mode\_home\_visit\_count AND 1231-appointment\_scheduled\_mode\_online\_count AND 1232-appointment\_scheduled\_mode\_other\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1232** | appointment\_scheduled\_mode\_other\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - of mode of Appointment: Other *(a count as at the end of the reporting period of the number of Slots scheduled as any other mode of Appointment not given above; Appointment mode groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this; this count WILL include any unknowns)*  Validation  - Must be less than or equal to 1213-appointment\_available\_mode\_other\_count - Must be Sum of 1227-appointment\_scheduled\_mode\_face\_to\_face\_count AND 1228-appointment\_scheduled\_mode\_phone\_count AND 1229-appointment\_scheduled\_mode\_video\_count AND 1230-appointment\_scheduled\_mode\_home\_visit\_count AND 1231-appointment\_scheduled\_mode\_online\_count AND 1232-appointment\_scheduled\_mode\_other\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1233** | appointment\_scheduled\_hcptype\_gp\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - with healthcare professional type: General-Practitioner-(GP)  *(a count as at the end of the reporting period of the number of Slots scheduled with healthcare professional type of GP or similar i.e. if an Appointment Slot is initially scheduled with a GP and then reassigned to nurse, this will NOT be included in this count; healthcare professional groupings and terminology may differ between Supplier systems and The Authority will consult with Suppliers on this; see embedded document for a list of types to be included in this count)*  Validation  - Must be less than or equal to 1214-appointment\_available\_hcptype\_gp\_count - Must be Sum of 1233-appointment\_scheduled\_hcptype\_gp\_count AND 1235-appointment\_scheduled\_hcptype\_nurse\_count AND 1236-appointment\_scheduled\_hcptype\_other\_clinical\_count AND 1237-appointment\_scheduled\_hcptype\_other\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1235** | appointment\_scheduled\_hcptype\_nurse\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - with healthcare professional type: Nurse *(a count as at the end of the reporting period of the number of Slots scheduled with healthcare professional type of Nurse or similar i.e. if an Appointment Slot is initially scheduled with a Nurse and then reassigned to GP, this will NOT be included in this count; healthcare professional groupings may differ between Supplier systems and The Authority will consult with Suppliers on this; see embedded document for a list of types to be included in this count)*  Validation  - Must be less than or equal to 1216-appointment\_available\_hcptype\_nurse\_count - Must be Sum of 1233-appointment\_scheduled\_hcptype\_gp\_count AND 1235-appointment\_scheduled\_hcptype\_nurse\_count AND 1236-appointment\_scheduled\_hcptype\_other\_clinical\_count AND 1237-appointment\_scheduled\_hcptype\_other\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1236** | appointment\_scheduled\_hcptype\_other\_clinical\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - with healthcare professional type: Other – Clinical *(a count as at the end of the reporting period of the number of Slots scheduled with healthcare professional type of Other – Clinical i.e. if an Appointment Slot is initially scheduled with a Nurse and then reassigned to another clinical user other than Nurse or GP, this WILL be included in this count; healthcare professional groupings may differ between Supplier systems and The Authority will consult with Suppliers on this; see embedded document for a list of types to be included in this count)*  Validation  - Must be less than or equal to 1217-appointment\_available\_hcptype\_other\_clinical\_count - Must be Sum of 1233-appointment\_scheduled\_hcptype\_gp\_count AND 1235-appointment\_scheduled\_hcptype\_nurse\_count AND 1236-appointment\_scheduled\_hcptype\_other\_clinical\_count AND 1237-appointment\_scheduled\_hcptype\_other\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1237** | appointment\_scheduled\_hcptype\_other\_count | All Appointments from appointment\_scheduled\_count (field 210) where:   - with healthcare professional type: Other *(a count as at the end of the reporting period of the number of Slots scheduled with any other healthcare professional type, including clerical user types i.e. if an Appointment Slot is initially scheduled with a Nurse and then reassigned to another health care professional type which is not GP, Nurse or other clinical, this WILL be included in this count; see embedded document* *for a list of all the types which will NOT be included in this count; this count WILL include any unknowns)*  Validation  - Must be less than or equal to 1218-appointment\_available\_hcptype\_other\_count - Must be Sum of 1233-appointment\_scheduled\_hcptype\_gp\_count AND 1235-appointment\_scheduled\_hcptype\_nurse\_count AND 1236-appointment\_scheduled\_hcptype\_other\_clinical\_count AND 1237-appointment\_scheduled\_hcptype\_other\_count - Must be less than or equal to 210-appointment\_scheduled\_count | Numeric (integer) | MAY |
| **1238** | third\_next\_appointment\_time\_GP\_total | Sum of the time to third next available Appointment figures calculated for each scheduling transaction associated with Appointments:   - with a start date and time within the reporting period *(based on start time of Appointment)* - of any Slot Type *(where Appointment Slot was available for a Patient to book i.e. exclude any 'blocked' or 'embargoed' Slots; terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)* - with healthcare professional type: General-Practitioner-(GP) *(healthcare professional groupings may differ between Supplier systems and The Authority will consult with Suppliers on this; see embedded document for a list of types to be included in this count)* - as per the methodology | Numeric (integer) | MAY |
| **1239** | third\_next\_appointment\_time\_nurse\_total | Sum of the time to third next available Appointment figures calculated for each scheduling transaction associated with Appointments:   - with a start date and time within the reporting period *(based on start time of Appointment)* - of any Slot Type *(where Appointment Slot was available for a Patient to book i.e. exclude any 'blocked' or 'embargoed' Slots terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)* - with healthcare professional type: Nurse *(healthcare professional groupings may differ between Supplier systems and The Authority will consult with Suppliers on this; see embedded document* *for a list of types to be included in this count)* - as per the methodology | Numeric (integer) | MAY |
| **1240** | third\_next\_appointment\_time\_other\_clinical\_total | Sum of the time to third next available Appointment figures calculated for each scheduling transaction associated with Appointments:   - with a start date and time within the reporting period *(based on start time of Appointment)* - of any Slot Type *(where Appointment Slot was available for a Patient to book i.e. exclude any 'blocked' or 'embargoed' Slots terminology may differ between Supplier systems and The Authority will consult with Suppliers on this)* - with healthcare professional type: Other – Clinical *(healthcare professional groupings may differ between Supplier systems and The Authority will consult with Suppliers on this; see embedded document for a list of types to be included in this count)* - as per the methodology | Numeric (integer) | MAY |
| **1241** | third\_next\_appointment\_time\_GP\_trans\_count | Total number of time to third next available Appointment figures which were summed together to give field 1238 Validation  - Must be Sum of 1241-third\_next\_appointment\_time\_GP\_trans\_count AND 1242-third\_next\_appointment\_time\_nurse\_trans\_count AND 1243-third\_next\_appointment\_time\_other\_clinical\_trans\_count - Must be less than or equal to 108-appointment\_scheduled\_trans\_count | Numeric (integer) | MAY |
| **1242** | third\_next\_appointment\_time\_nurse\_trans\_count | Total number of time to third next available Appointment figures which were summed together to give field 1239 Validation  - Must be Sum of 1241-third\_next\_appointment\_time\_GP\_trans\_count AND 1242-third\_next\_appointment\_time\_nurse\_trans\_count AND 1243-third\_next\_appointment\_time\_other\_clinical\_trans\_count - Must be less than or equal to 108-appointment\_scheduled\_trans\_count | Numeric (integer) | MAY |
| **1243** | third\_next\_appointment\_time\_other\_clinical\_trans\_count | Total number of time to third next available Appointment figures which were summed together to give field 1240 Validation  - Must be Sum of 1241-third\_next\_appointment\_time\_GP\_trans\_count AND 1242-third\_next\_appointment\_time\_nurse\_trans\_count AND 1243-third\_next\_appointment\_time\_other\_clinical\_trans\_count - Must be less than or equal to 108-appointment\_scheduled\_trans\_count | Numeric (integer) | MAY |
| **1244** | appointment\_Patient\_sex\_male\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was of sex: Male *(based on the sex of the Patient attending the Appointment NOT who booked it)*  Validation  - Must be Sum of 1244-appointment\_Patient\_sex\_male\_count AND 1245-appointment\_Patient\_sex\_female\_count AND 1246-appointment\_Patient\_sex\_unknown\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1245** | appointment\_Patient\_sex\_female\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was of sex: Female *(based on the sex of the Patient attending the Appointment NOT who booked it)*  Validation  - Must be Sum of 1244-appointment\_Patient\_sex\_male\_count AND 1245-appointment\_Patient\_sex\_female\_count AND 1246-appointment\_Patient\_sex\_unknown\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1246** | appointment\_Patient\_sex\_unknown\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was of sex: Unknown *(based on the sex of the Patient attending the Appointment NOT who booked it; this field WILL include Patients with sex recorded as 'indeterminate')*  Validation  - Must be Sum of 1244-appointment\_Patient\_sex\_male\_count AND 1245-appointment\_Patient\_sex\_female\_count AND 1246-appointment\_Patient\_sex\_unknown\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1247** | appointment\_Patient\_ethnicity\_white\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was of ethnicity group: White *(based on the ethnicity group of the Patient attending the Appointment NOT who booked it; see Read/CTV3/SNOMED mapping embedded below)*  Validation  - Must be Sum of 1247-appointment\_Patient\_ethnicity\_white\_count AND 1248-appointment\_Patient\_ethnicity\_mixed\_count AND 1249-appointment\_Patient\_ethnicity\_asian\_count AND 1250-appointment\_Patient\_ethnicity\_black\_count AND 1251-appointment\_Patient\_ethnicity\_other\_count AND 1252-appointment\_Patient\_ethnicity\_unknown\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1248** | appointment\_Patient\_ethnicity\_mixed\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was of ethnicity group: Mixed *(based on the ethnicity group of the Patient attending the Appointment NOT who booked it; see Read/CTV3/SNOMED* *mapping embedded below)*  Validation  - Must be Sum of 1247-appointment\_Patient\_ethnicity\_white\_count AND 1248-appointment\_Patient\_ethnicity\_mixed\_count AND 1249-appointment\_Patient\_ethnicity\_asian\_count AND 1250-appointment\_Patient\_ethnicity\_black\_count AND 1251-appointment\_Patient\_ethnicity\_other\_count AND 1252-appointment\_Patient\_ethnicity\_unknown\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1249** | appointment\_Patient\_ethnicity\_asian\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was of ethnicity group: Asian or British Asian *(based on the ethnicity group of the Patient attending the Appointment NOT who booked it)*  Validation  - Must be Sum of 1247-appointment\_Patient\_ethnicity\_white\_count AND 1248-appointment\_Patient\_ethnicity\_mixed\_count AND 1249-appointment\_Patient\_ethnicity\_asian\_count AND 1250-appointment\_Patient\_ethnicity\_black\_count AND 1251-appointment\_Patient\_ethnicity\_other\_count AND 1252-appointment\_Patient\_ethnicity\_unknown\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1250** | appointment\_Patient\_ethnicity\_black\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was of ethnicity group: Black or Black British *(based on the ethnicity group of the Patient attending the Appointment NOT who booked it)*  Validation  - Must be Sum of 1247-appointment\_Patient\_ethnicity\_white\_count AND 1248-appointment\_Patient\_ethnicity\_mixed\_count AND 1249-appointment\_Patient\_ethnicity\_asian\_count AND 1250-appointment\_Patient\_ethnicity\_black\_count AND 1251-appointment\_Patient\_ethnicity\_other\_count AND 1252-appointment\_Patient\_ethnicity\_unknown\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1251** | appointment\_Patient\_ethnicity\_other\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was of ethnicity group: Other*(based on the ethnicity group of the Patient attending the Appointment NOT who booked it)*  Validation  - Must be Sum of 1247-appointment\_Patient\_ethnicity\_white\_count AND 1248-appointment\_Patient\_ethnicity\_mixed\_count AND 1249-appointment\_Patient\_ethnicity\_asian\_count AND 1250-appointment\_Patient\_ethnicity\_black\_count AND 1251-appointment\_Patient\_ethnicity\_other\_count AND 1252-appointment\_Patient\_ethnicity\_unknown\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1252** | appointment\_Patient\_ethnicity\_unknown\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was of ethnicity group: Unknown*(based on the ethnicity group of the Patient attending the Appointment NOT who booked it)*  Validation  - Must be Sum of 1247-appointment\_Patient\_ethnicity\_white\_count AND 1248-appointment\_Patient\_ethnicity\_mixed\_count AND 1249-appointment\_Patient\_ethnicity\_asian\_count AND 1250-appointment\_Patient\_ethnicity\_black\_count AND 1251-appointment\_Patient\_ethnicity\_other\_count AND 1252-appointment\_Patient\_ethnicity\_unknown\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1253** | appointment\_Patient\_age\_0-1\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was in age band: 0-1 year *(based on the age of the Patient attending the Appointment NOT who booked it; Patients who are less than 1 year old)*  Validation  - Must be Sum of 1253-appointment\_Patient\_age\_0-1\_count AND 1254-appointment\_Patient\_age\_1-5\_count AND 1255-appointment\_Patient\_age\_6-15\_count AND 1256-appointment\_Patient\_age\_16-45\_count AND 1257-appointment\_Patient\_age\_46-64\_count AND 1258-appointment\_Patient\_age\_65-80\_count AND 1259-appointment\_Patient\_age\_over\_81\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1254** | appointment\_Patient\_age\_1-5\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was in age band: 1-5 years *(based on the age of the Patient attending the Appointment NOT who booked it; age banding is inclusive i.e. a Patient aged 1 year and a Patient aged 5 years WILL both be included in this count)*  Validation  - Must be Sum of 1253-appointment\_Patient\_age\_0-1\_count AND 1254-appointment\_Patient\_age\_1-5\_count AND 1255-appointment\_Patient\_age\_6-15\_count AND 1256-appointment\_Patient\_age\_16-45\_count AND 1257-appointment\_Patient\_age\_46-64\_count AND 1258-appointment\_Patient\_age\_65-80\_count AND 1259-appointment\_Patient\_age\_over\_81\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1255** | appointment\_Patient\_age\_6-15\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was in age band: 6-15 years *(based on the age of the Patient attending the Appointment NOT who booked it; age banding is inclusive i.e. a Patient aged 6 years and a Patient aged 15 years WILL both be included in this count)*  Validation  - Must be Sum of 1253-appointment\_Patient\_age\_0-1\_count AND 1254-appointment\_Patient\_age\_1-5\_count AND 1255-appointment\_Patient\_age\_6-15\_count AND 1256-appointment\_Patient\_age\_16-45\_count AND 1257-appointment\_Patient\_age\_46-64\_count AND 1258-appointment\_Patient\_age\_65-80\_count AND 1259-appointment\_Patient\_age\_over\_81\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1256** | appointment\_Patient\_age\_16-45\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was in age band: 16-45 years *(based on the age of the Patient attending the Appointment NOT who booked it; age banding is inclusive i.e. a Patient aged 16 years and a Patient aged 45 years WILL both be included in this count)*  Validation  - Must be Sum of 1253-appointment\_Patient\_age\_0-1\_count AND 1254-appointment\_Patient\_age\_1-5\_count AND 1255-appointment\_Patient\_age\_6-15\_count AND 1256-appointment\_Patient\_age\_16-45\_count AND 1257-appointment\_Patient\_age\_46-64\_count AND 1258-appointment\_Patient\_age\_65-80\_count AND 1259-appointment\_Patient\_age\_over\_81\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1257** | appointment\_Patient\_age\_46-64\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was in age band: 46-64 years *(based on the age of the Patient attending the Appointment NOT who booked it; age banding is inclusive i.e. a Patient aged 46 years and a Patient aged 64 years WILL both be included in this count)*  Validation  - Must be Sum of 1253-appointment\_Patient\_age\_0-1\_count AND 1254-appointment\_Patient\_age\_1-5\_count AND 1255-appointment\_Patient\_age\_6-15\_count AND 1256-appointment\_Patient\_age\_16-45\_count AND 1257-appointment\_Patient\_age\_46-64\_count AND 1258-appointment\_Patient\_age\_65-80\_count AND 1259-appointment\_Patient\_age\_over\_81\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1258** | appointment\_Patient\_age\_65-80\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was in age band: 65-80 years *(based on the age of the Patient attending the Appointment NOT who booked it; age banding is inclusive i.e. a Patient aged 65 years and a Patient aged 80 years WILL both be included in this count)*  Validation  - Must be Sum of 1253-appointment\_Patient\_age\_0-1\_count AND 1254-appointment\_Patient\_age\_1-5\_count AND 1255-appointment\_Patient\_age\_6-15\_count AND 1256-appointment\_Patient\_age\_16-45\_count AND 1257-appointment\_Patient\_age\_46-64\_count AND 1258-appointment\_Patient\_age\_65-80\_count AND 1259-appointment\_Patient\_age\_over\_81\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1259** | appointment\_Patient\_age\_over\_81\_count | All Appointments from appointment\_attended\_count (field 1224):   - where Patient attending Appointment was in age band: 81 years and over *(based on the age of the Patient attending the Appointment NOT who booked it; Patients who are aged 81 years or older i.e. a Patient aged 81 WILL be included in this count)*  Validation  - Must be Sum of 1253-appointment\_Patient\_age\_0-1\_count AND 1254-appointment\_Patient\_age\_1-5\_count AND 1255-appointment\_Patient\_age\_6-15\_count AND 1256-appointment\_Patient\_age\_16-45\_count AND 1257-appointment\_Patient\_age\_46-64\_count AND 1258-appointment\_Patient\_age\_65-80\_count AND 1259-appointment\_Patient\_age\_over\_81\_count - Must be less than or equal to 1224-appointment\_attended\_count | Numeric (integer) | MAY |
| **1260** | Patient\_attended\_multiple\_appointments\_count | Total number of Patients who attended three or more Appointments in the period *(a count as at the end of the reporting period of the number of Patients who attended three or more Appointments)*   - with a start date and time within the reporting period *(based on start time of Appointment)* - with attendance status of 'attended' *(scheduled Appointments where Patients attended their Appointment; terminology for 'attended' may differ between Supplier systems)* - booked using any method - with any healthcare professional type - of any Slot Type *(type of Appointment is defined as routine, emergency, or specialist clinics etc. terminology may differ between Supplier systems)* - of any duration | Numeric (integer) | MAY |

## Document Management

These data items to be provided by any Supplier delivering the Document Management Capability:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field ID** | **Data Item** | **Definition** | **Format** | **Level** |
| **1108** | total\_documents\_count | Total number of unique documents received into and stored by the Solution that were: *(this does NOT include instances of duplicate documents being received and recorded against a Patient record)*   - recorded against a Patient record - recorded against a Patient record at any time within the reporting period *(if the document is received by the system outside of the reporting period, but saved against a Patient record within the reporting period, then this WILL be included; if the document is received into the system within the reporting period, but not saved against a Patient record until outside the reporting period this will NOT be included)* - received via any mechanism *(i.e. electronic, scanned, manual etc. are all included)*   If same data is stored by multiple Solutions, it will only be submitted once by one Supplier (see 1108 in Patient Information Maintenance - GP) | Numeric (integer) | MAY |
| **1109** | total\_documents\_scanned\_count | Total number of unique documents received into and stored by the Solution that were: *(this does NOT include instances of duplicate documents being received and recorded against a Patient record)*   - recorded against a Patient record - recorded against a Patient record at any time within the reporting period *(if the document is received by the system outside of the reporting period, but saved against a Patient record within the reporting period, then this WILL be included; if the document is received into the system within the reporting period, but not saved against a Patient record until outside the reporting period this will NOT be included)* - received via scanning *(i.e. documents received on paper and scanned as opposed to being received via an electronic format)*   If same data is stored by multiple Solutions, it will only be submitted once by one Supplier (see 1109 in Patient Information Maintenance - GP) | Numeric (integer) | MAY |
| **1110** | total\_documents\_electronic\_count | Total number of unique documents received into and stored by the Solution that were: *(this does NOT include instances of duplicate documents being received and recorded against a Patient record)*   - recorded against a Patient record - recorded against a Patient record at any time within the reporting period *(if the document is received by the system outside of the reporting period, but saved against a Patient record within the reporting period, then this WILL be included; if the document is received into the system within the reporting period, but not saved against a Patient record until outside the reporting period this will NOT be included)* - received electronically *(i.e. documents received electronically as opposed to being received in paper format and scanned)*   If same data is stored by multiple Solutions, it will only be submitted once by one Supplier (see 1110 in Patient Information Maintenance - GP) | Numeric (integer) | MAY |

## Prescribing

These data items to be provided by any Supplier delivering the Prescribing Capability:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field ID** | **Data Item** | **Definition** | **Format** | **Level** |
| **308** | prescriptions\_ordered\_trans\_count | Total number of Prescription ordering transactions: *(this is a count of transactions resulting in a Prescription/s being ordered, NOT the number of items ordered; ordering several items in one transaction should only be counted as a single transaction)*   - via any Prescription ordering method - the ordering transaction took place within the reporting period | Numeric (integer) | MAY |
| **309** | items\_ordered\_total\_count | Total number of Prescription items ordered: *(this is a count of the items ordered, NOT the number of transactions; if ordering several items in one transaction each item should be counted individually)*   - via any Prescription ordering method - the ordering transaction took place within the reporting period | Numeric (integer) | MAY |

## Ethnicity Mappings

The Ethnicity codes to use for each category within the Management Information (MI) reports are defined in the Patient Ethnicity tables.

![](https://nhse-dsic.atlassian.net/wiki/images/icons/grey_arrow_down.png)Click here to view Patient Ethnicity tables

- White
- Mixed
- Asian
- Black
- Other
- Unknown

### Patient Ethnicity - White

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Cluster\_ID** | **Cluster\_Desc** | **Read\_Code** | **Code\_Description** | **SNOMED Concept ID** | **SNOMED Desc ID** |
| ETH2016WB\_COD | White: English or Welsh or Scottish or Northern Irish or British ethnicity group codes (The Authority 2016 grouping) | 9i00. | White British - ethnic category 2001 census | 494131000000105 | 1063981000000117 |
| ETH2016WB\_COD | White: English or Welsh or Scottish or Northern Irish or British ethnicity group codes (The Authority 2016 grouping) | 9t00. | White: English or Welsh or Scottish or Northern Irish or British - England and Wales ethnic category 2011 census | 976631000000101 | 2484631000000115 |
| ETH2016WGT\_COD | White: Gypsy or Irish Traveller ethnicity group codes (The Authority 2016 grouping) | 9i2C. | Irish Traveller - ethnic category 2001 census | 88911000000101 | 138171000000114 |
| ETH2016WGT\_COD | White: Gypsy or Irish Traveller ethnicity group codes (The Authority 2016 grouping) | 9i2D. | Traveller - ethnic category 2001 census | 88921000000107 | 138181000000111 |
| ETH2016WGT\_COD | White: Gypsy or Irish Traveller ethnicity group codes (The Authority 2016 grouping) | 9i2E. | Gypsy/Romany - ethnic category 2001 census | 88931000000109 | 138191000000113 |
| ETH2016WGT\_COD | White: Gypsy or Irish Traveller ethnicity group codes (The Authority 2016 grouping) | 9t02. | White: Gypsy or Irish Traveller - England and Wales ethnic category 2011 census | 976671000000104 | 2484711000000117 |
| ETH2016WI\_COD | White: Irish ethnicity group codes (The Authority 2016 grouping) | 9i10. | White Irish - ethnic category 2001 census | 494161000000100 | 1064041000000111 |
| ETH2016WI\_COD | White: Irish ethnicity group codes (The Authority 2016 grouping) | 9t01. | White: Irish - England and Wales ethnic category 2011 census | 976651000000108 | 2484671000000118 |
| ETH2016WO\_COD | White: Any other White background ethnicity group codes (The Authority 2016 grouping) | 9t03. | White: any other White background - England and Wales ethnic category 2011 census | 976691000000100 | 2484751000000118 |

### Patient Ethnicity - Mixed

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Cluster\_ID** | **Cluster\_Desc** | **Read\_Code** | **Code\_Description** | **SNOMED Concept ID** | **SNOMED Desc ID** |
| ETH2016MO\_COD | Mixed or multiple ethnic groups: Any other Mixed or multiple ethnic background ethnicity group codes (The Authority 2016 grouping) | 9t07. | Mixed multiple ethnic groups: any other Mixed or multiple ethnic background - England and Wales ethnic category 2011 census |  |  |
| ETH2016MWA\_COD | Mixed or multiple ethnic groups: White and Asian ethnicity group codes (The Authority 2016 grouping) | 9i5.. | White and Asian - ethnic category 2001 census | 976771000000108 | 2484911000000115 |
| ETH2016MWA\_COD | Mixed or multiple ethnic groups: White and Asian ethnicity group codes (The Authority 2016 grouping) | 9t06. | Mixed multiple ethnic groups: White and Asian - England and Wales ethnic category 2011 census | 976751000000104 | 2484871000000117 |
| ETH2016MWBA\_COD | Mixed or multiple ethnic groups: White and Black African ethnicity group codes (The Authority 2016 grouping) | 9t05. | Mixed multiple ethnic groups: White and Black African - England and Wales ethnic category 2011 census | 976731000000106 | 2484831000000119 |
| ETH2016MWBC\_COD | Mixed or multiple ethnic groups: White and Black Caribbean ethnicity group codes (The Authority 2016 grouping) | 9i3.. | White and Black Caribbean - ethnic category 2001 census | 92421000000102 | 141321000000118 |
| ETH2016MWBC\_COD | Mixed or multiple ethnic groups: White and Black Caribbean ethnicity group codes (The Authority 2016 grouping) | 9t04. | Mixed multiple ethnic groups: White and Black Caribbean - England and Wales ethnic category 2011 census | 976711000000103 | 2484791000000114 |

### Patient Ethnicity - Asian

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Cluster\_ID** | **Cluster\_Desc** | **Read\_Code** | **Code\_Description** | **SNOMED Concept ID** | **SNOMED Desc ID** |
| ETH2016AB\_COD | Asian or Asian British: Bangladeshi ethnicity group codes (The Authority 2016 grouping) | 9i9.. | Bangladeshi or British Bangladeshi - ethnic category 2001 census | 92471000000103 | 141371000000119 |
| ETH2016AB\_COD | Asian or Asian British: Bangladeshi ethnicity group codes (The Authority 2016 grouping) | 9t0A. | Asian or Asian British: Bangladeshi - England and Wales ethnic category 2011 census | 976831000000100 | 2485031000000111 |
| ETH2016AC\_COD | Asian or Asian British: Chinese ethnicity group codes (The Authority 2016 grouping) | 9i64. | Asian and Chinese - ethnic category 2001 census | 92611000000106 | 158361000000116 |
| ETH2016AC\_COD | Asian or Asian British: Chinese ethnicity group codes (The Authority 2016 grouping) | 9iE.. | Chinese - ethnic category 2001 census | 92511000000107 | 141401000000117 |
| ETH2016AC\_COD | Asian or Asian British: Chinese ethnicity group codes (The Authority 2016 grouping) | 9t0B. | Asian or Asian British: Chinese - England and Wales ethnic category 2011 census | 976851000000107 | 2485071000000113 |
| ETH2016AI\_COD | Asian or Asian British: Indian ethnicity group codes (The Authority 2016 grouping) | 9i7.. | Indian or British Indian - ethnic category 2001 census | 110751000000108 | 157271000000119 |
| ETH2016AI\_COD | Asian or Asian British: Indian ethnicity group codes (The Authority 2016 grouping) | 9t08. | Asian or Asian British: Indian - England and Wales ethnic category 2011 census | 976791000000107 | 2484951000000116 |
| ETH2016AO\_COD | Asian or Asian British: Any other Asian background ethnicity group codes (The Authority 2016 grouping) | 9t0C. | Asian or Asian British: any other Asian background - England and Wales ethnic category 2011 census | 976871000000103 | 2485111000000119 |
| ETH2016AP\_COD | Asian or Asian British: Pakistani ethnicity group codes (The Authority 2016 grouping) | 9i8.. | Pakistani or British Pakistani - ethnic category 2001 census | 92461000000105 | 141361000000114 |
| ETH2016AP\_COD | Asian or Asian British: Pakistani ethnicity group codes (The Authority 2016 grouping) | 9t09. | Asian or Asian British: Pakistani - England and Wales ethnic category 2011 census | 976811000000108 | 2484991000000112 |

### Patient Ethnicity - Black

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Cluster\_ID** | **Cluster\_Desc** | **Read\_Code** | **Code\_Description** | **SNOMED Concept ID** | **SNOMED Desc ID** |
| ETH2016BA\_COD | Black or African or Caribbean or Black British: African ethnicity group codes (The Authority 2016 grouping) | 9t0D. | Black or African or Caribbean or Black British: African - England and Wales ethnic category 2011 census | 976891000000104 | 2485151000000115 |
| ETH2016BC\_COD | Black or African or Caribbean or Black British: Caribbean ethnicity group codes (The Authority 2016 grouping) | 9t0E. | Black or African or Caribbean or Black British: Caribbean - England and Wales ethnic category 2011 census | 976911000000101 | 2485191000000111 |
| ETH2016BO\_COD | Black or African or Caribbean or Black British: Any other Black or African or Caribbean background ethnicity group codes (The Authority 2016 grouping) | 9t0F. | Black or African or Caribbean or Black British: other Black or African or Caribbean background - England and Wales ethnic category 2011 census | 976931000000109 | 2485231000000119 |

### Patient Ethnicity - Other

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Cluster\_ID** | **Cluster\_Desc** | **Read\_Code** | **Code\_Description** | **SNOMED Concept ID** | **SNOMED Desc ID** |
| ETH2016OA\_COD | Other ethnic group: Arab ethnicity group codes (The Authority 2016 grouping) | 9iF9. | Arab - ethnic category 2001 census | 89001000000105 | 138251000000111 |
| ETH2016OA\_COD | Other ethnic group: Arab ethnicity group codes (The Authority 2016 grouping) | 9t0G. | Other ethnic group: Arab - England and Wales ethnic category 2011 census | 976951000000102 | 2485271000000117 |
| ETH2016OO\_COD | Other ethnic group: Any other ethnic group ethnicity group codes (The Authority 2016 grouping) | 9iF.. | Other - ethnic category 2001 census | 92521000000101 | 141411000000115 |
| ETH2016OO\_COD | Other ethnic group: Any other ethnic group ethnicity group codes (The Authority 2016 grouping) | 9iFK. | Any other group - ethnic category 2001 census | 94151000000105 | 142901000000119 |
| ETH2016OO\_COD | Other ethnic group: Any other ethnic group ethnicity group codes (The Authority 2016 grouping) | 9t0H. | Other ethnic group: any other ethnic group - England and Wales ethnic category 2011 census | 976971000000106 | 2485311000000117 |

### Patient Ethnicity - Unknown

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Cluster\_ID** | **Cluster\_Desc** | **Read\_Code** | **Code\_Description** | **SNOMED Concept ID** | **SNOMED Desc ID** |
| ETH2016NSTAT\_COD | Not stated ethnicity group codes (The Authority 2016 grouping) | 9iG.. | Ethnic category not stated - 2001 census | 92531000000104 | 141421000000114 |

## Healthcare Professional Types

The following tables define the Healthcare Professional (HCP) types referenced in the reporting data items.

![](https://nhse-dsic.atlassian.net/wiki/images/icons/grey_arrow_down.png)Click here to view Healthcare Professional Types tables

- General Practitioner (GP)
- Nurse
- Other - Clinical

### General Practitioner (GP)

|  |
| --- |
| Associate Specialist |
| Asst. Clinical Medical Officer |
| Doctor |
| General Medical Practitioner |
| GP Assistant |
| GP Associate / Associate / Associate Practitioner / Associate Practitioner - General Practitioner |
| GP CMO / Clinical Medical Officer |
| GP Locum / Locum |
| GP Partner / Partner |
| GP Registrar |
| GP Retainer |
| GP Sole Practitioner / Sole Practitioner |
| GP Surgery |
| GP Trainee |
| GP/HV |
| Registrar (Closed) |
| Salaried General Practitioner |
| Salaried Partner |
| Senior Partner |
| Senior Registrar (Closed) |
| Sessional GP |
| Specialist Registrar |

### Nurse

|  |  |
| --- | --- |
| Associate Practitioner - Nurse | Nurse Consultant |
| Associate Specialist | Nurse Manager |
| Clinical Practitioner Access Role | Nurse Manager Access Role |
| Community Learning Disabilities Nurse | Nurse Practitioner |
| Community Mental Health Nurse | Nurse Practitioner - Substance Misuse |
| Community Nurse | Nurse Prescriber |
| Community Practitioner | Nursery Nurse |
| Community Psychiatric Nurse | Nursing Cadet |
| Contact Tracing Nurse | Other Nursing & Midwifery |
| District Nurse | Practice Nurse |
| District Nurse (G Grade) | School Nurse / CMO |
| Enrolled Nurse | Specialist Health Visitor Substance Misuse |
| Health Professional Access Role | Specialist Health Visitor Support Worker |
| Health Visitor | Specialist Nurse Practitioner |
| Health Visitor at Home | Specialist Practitioner |
| Healthcare Cadet | Staff Nurse |
| Healthcare Officer Nurse | Student Community Learning Disabilities Nurse |
| Healthcare Student Access Role | Student Community Mental Health Nurse |
| Macmillan Nurse | Student Community Paediatric Nurse |
| Macmillan Palliative Care Specialist Nurse | Student Community Practitioner |
| Mental Handicap Nurse | Student District Nurse |
| Mental Health Nurse | Student Health Visitor |
| Midwife | Student Midwife |
| Midwife - Consultant | Student Nurse - Adult Branch |
| Midwife - Manager | Student Nurse - Child Branch |
| Midwife - Sister/Charge Nurse | Student Nurse - Learning Disabilities Branch |
| Midwife - Specialist Practitioner | Student Nurse - Mental Health Branch |
| Midwife Access Role | Student Occupational Health Nurse |
| Midwife Manager Access Role | Student Practice Nurse |
| Modern Matron | Student School Nurse |
| Nurse Access Role |  |

### Other - Clinical

|  |  |  |  |
| --- | --- | --- | --- |
| Approved Social Worker | Medical Technical Officer - Pharmacy | Paramedic Consultant | Social services care manager (adults) |
| Art Therapist | Multi Therapist | Paramedic Manager | Social services care manager (children) |
| Assistant Psychologist | Multi Therapist Consultant | Paramedic Specialist Practitioner | Social services care manager (mental health) |
| Assistant Psychotherapist | Multi Therapist Manager | Pharmacist | Social work  team manager (children) |
| Chiropodist | Multi Therapist Specialist Practitioner | Pharmacy Technician | Social work assistant (adults) |
| Chiropodist/Podiatrist | Nurse Consultant | Phlebotomist | Social work assistant (children) |
| Chiropodist/Podiatrist Consultant | Occupational Therapist | Physiotherapist | Social work assistant (mental health) |
| Chiropodist/Podiatrist Manager | Occupational Therapist Consultant | Physiotherapist Consultant | Social work team manager (adults) |
| Chiropodist/Podiatrist Specialist Practitioner | Occupational Therapist Manager | Physiotherapist Manager | Social work team manager (mental health) |
| Clinical Pharmacy Specialist | Occupational Therapy Specialist Practitioner | Physiotherapist Specialist Practitioner | Social Worker |
| Clinical Psychologist | Occupational Therapy Team Manager | Podiatrist | Social Worker Access Role |
| Community Practitioner | Orthoptist Specialist Practitioner | Pre-reg Pharmacist | Speech & Language Therapist |
| Community Team Manager | Orthotist | Prosthetist | Speech & Language Therapist Consultant |
| Community Worker (children) | Orthotist Consultant | Prosthetist Consultant | Speech & Language Therapist Manager |
| Counsellor | Orthotist Manager | Prosthetist Manager | Speech & Language Therapist Specialist Practitioner |
| Dietician | Orthotist Specialist Practitioner | Prosthetist Specialist Practitioner | Speech Therapist |
| Dietitian | Osteopath | Psychologist | Stomatherapist |
| Dietitian Consultant | OT assistant | Psychotherapist | Student Chiropodist |
| Dietitian Manager | Other Additional Clinical Services | Senior social worker (adults) | Student Community Practitioner |
| Dietitian Specialist Practitioner | Other Allied Health Professionals | Senior social worker (children) | Student Dietitian |
| Dispenser | Other Community Health Service - Social Care Worker | Senior social worker (mental health) | Student Occupational Therapist |
| Health Care Support Worker | Other' Community Health Service - Social Care Worker | Sexual Health Outreach Worker | Student Physiotherapist |
| Health Promotions Specialist | Other Health Care Professional | Social Care SAP Manager | Student Psychotherapist |
| Healthcare Assistant | Other Health Care Professionals | Social Care SAP User | Student Speech & Language Therapist |
| Homeopath | Paramedic | Social Care Support Worker | Therapist |

## Third Next Available Appointment (TNA) Calculation Methodology

This page sets out the methodology by which TNA will be calculated by Suppliers and provided via the Management Information (MI) Reporting Specification. This will calculate a TNA figure based on each Appointment booking transaction associated with each Appointment in the reporting period (month). The figures for the number of days to the TNA identified by the methodology set out below based on each booking transaction will then be summed and returned as part of the Management Information (MI) Reporting Specification.

There are six fields within the specification that need to be returned by Suppliers:

- 1238 - third\_next\_appointment\_time\_GP\_total
- 1239 - third\_next\_appointment\_time\_nurse\_total
- 1240 - third\_next\_appointment\_time\_other\_clinical\_total
- 1241 - third\_next\_appointment\_time\_GP\_trans\_count
- 1242 - third\_next\_appointment\_time\_nurse\_trans\_count
- 1243 - third\_next\_appointment\_time\_other\_clinical\_trans\_count

There is a defined methodology which Suppliers are to follow to calculate these fields, however there are three options for how this could be applied to the system which should calculate the same output as set out below.

![](https://nhse-dsic.atlassian.net/wiki/images/icons/grey_arrow_down.png)Click here to view the available options

### OPTION 1 – Extract data

At the end of each reporting period (month) Suppliers will need to extract the following data items from each Practice into a central location.

Please note the following:

- Four instances of booked and cancelled date/time have been listed, however Suppliers should extract ALL booking and cancellation dates/times associated with EVERY Appointment as necessary.
- Data extracted must be for Appointments with a start date and time within the reporting period (month) ONLY and nothing beyond this i.e. up to 23:59pm on the final day of the reporting period (month).

*NB. Appointments with a booked date/time and/or cancelled date/time prior to the reporting period (month) must be included in the extraction*

- Suppliers will also require the data from previous reporting periods (months) in order to complete the calculation methodology i.e. if the reporting period is February, then the data for all Appointments with a start date and time in February, plus January and several months previous will be required.

*NB. This should go back as far as the month of the earliest booked date/time associated with any Appointment in the reporting period i.e. for the February reporting period, if an Appointment has a booked date/time in November then all Appointments with a start date/time in November, December, January and February will be required.*

*If it is not possible to achieve this, then at least the month prior to the reporting period (month) should be considered. Any booked date/time(s) in a month which is two or more before the reporting period should then be discarded.*

|  |  |
| --- | --- |
| appointment\_start\_date | The date on which the Appointment is due to take place (within the reporting period)  *Format: dd/mm/yyyy* |
| appointment\_start\_time | The time at which the Appointment is due to start (within the reporting period)  *Format:  hh:mm* *(must use 24 hour clock or have an indication of ‘am’ or ‘pm’)* |
| appointment\_slot\_type | The Slot Type assigned to the Appointment (i.e. routine/standard or urgent/on the day)    *As the need to differentiate between ‘routine’ and ‘urgent’ Appointments has now been removed, it may no longer be necessary to extract the ‘appointment\_slot\_type’ field.  However, it is necessary to exclude ‘embargoed’ and/or ‘blocked’ Slots i.e. Appointment Slots showing as available but which were never actually available for a Patient to book. Slots such as these should either not be extracted from the system at all or an indicator of this status should be extracted.  This may be the ‘slot type’ field, a different field or a flag etc. dependent on system functionality. The Authority will engage with Suppliers on this.* |
| appointment\_hcp\_type | The healthcare professional type assigned to the Appointment (GP, Nurse, Other – clinical) |
| appointment\_booked\_date\_1 | The date on which the Appointment was booked for the first time (whether in or before the reporting period)  *Format:  dd/mm/yyyy* |
| appointment\_booked\_time\_1 | The time at which the Appointment was booked for the first time (whether in or before the reporting period)  *Format:  hh:mm:ss (must use 24 hour clock or have an indication of ‘am’ or ‘pm’)* |
| appointment\_booked\_date\_2 | The date on which the Appointment was booked for the second time (whether in or before the reporting period)  *Format: dd/mm/yyyy* |
| appointment\_booked\_time\_2 | The time at which the Appointment was booked for the second time (whether in or before the reporting period)  *Format:  hh:mm:ss (must use 24 hour clock or have an indication of ‘am’ or ‘pm’)* |
| appointment\_booked\_date\_3 | The date on which the Appointment was booked for the third time (whether in or before the reporting period)  *Format: dd/mm/yyyy* |
| appointment\_booked\_time\_3 | The time at which the Appointment was booked for the third time (whether in or before the reporting period)  *Format:  hh:mm:ss (must use 24 hour clock or have an indication of ‘am’ or ‘pm’)* |
| appointment\_booked\_date\_4 | The date on which the Appointment was booked for the fourth time (whether in or before the reporting period)  *Format: dd/mm/yyyy* |
| appointment\_booked\_time\_4 | The time at which the Appointment was booked for the fourth time (whether in or before the reporting period)  *Format:  hh:mm:ss (must use 24 hour clock or have an indication of ‘am’ or ‘pm’)* |
| appointment\_cancelled\_date\_1 | The date on which the Appointment was cancelled for the first time (whether in or before the reporting period)  *Format: dd/mm/yyyy* |
| appointment\_cancelled\_time\_1 | The time at which the Appointment was cancelled for the first time (whether in or before the reporting period)  *Format:  hh:mm:ss (must use 24 hour clock or have an indication of ‘am’ or ‘pm’)* |
| appointment\_cancelled\_date\_2 | The date on which the Appointment was cancelled for the second time (whether in or before the reporting period)  *Format: dd/mm/yyyy* |
| appointment\_cancelled\_time\_2 | The time at which the Appointment was cancelled for the second time (whether in or before the reporting period)  *Format:  hh:mm:ss (must use 24 hour clock or have an indication of ‘am’ or ‘pm’)* |
| appointment\_cancelled\_date\_3 | The date on which the Appointment was cancelled for the third time (whether in or before the reporting period)  *Format: dd/mm/yyyy* |
| appointment\_cancelled\_time\_3 | The time at which the Appointment was cancelled for the third time (whether in or before the reporting period)  *Format:  hh:mm:ss (must use 24 hour clock or have an indication of ‘am’ or ‘pm’)* |
| appointment\_cancelled\_date\_4 | The date on which the Appointment was cancelled for the fourth time (whether in or before the reporting period)  *Format: dd/mm/yyyy* |
| appointment\_cancelled\_time\_4 | The time at which the Appointment was cancelled for the fourth time (whether in or before the reporting period)  *Format:  hh:mm:ss (must use 24 hour clock or have an indication of ‘am’ or ‘pm’)* |

Following the extraction of the raw data items, there are some initial steps to be undertaken to group the data which are unique to each of the first three new fields (1238, 1239, 1240).  These are set out below:

#### 1238:  third\_next\_appointment\_time\_GP\_total

1. List all Appointments for the reporting period (month) and the previous reporting periods as far back as the month of the earliest booked date/time associated with an Appointment *e. for February reporting period, if an Appointment has a booked date/time in December, all Appointments with a start date/time in February, January and December should be included.*
2. Order by Appointment start date and time
3. Remove any blocked/embargoed Appointment Slots if extracted *(any Appointments which were not actually available for Patients to book)*
4. Create sub-group of those Appointments with HCP type of General Practitioner (GP)*(as defined in Healthcare Professional Types)*

#### 1239:  third\_next\_appointment\_time\_nurse\_total

1. List all Appointments for the reporting period (month) and the previous reporting periods as far back as the month of the earliest booked date/time associated with an Appointment *e. for February reporting period, if an Appointment has a booked date/time in December, all Appointments with a start date/time in February, January and December should be included.*
2. Order by Appointment start date and time
3. Remove any blocked/embargoed Appointment Slots if extracted *(any Appointments which were not actually available for Patients to book)*
4. Create sub-group of those Appointments with HCP type of Nurse *(as defined in Healthcare Professional Types)*

#### 1240:  third\_next\_appointment\_time\_other\_clinical\_total

1. List all Appointments for the reporting period (month) and the previous reporting periods as far back as the month of the earliest booked date/time associated with an Appointment *e. for February reporting period, if an Appointment has a booked date/time in December, all Appointments with a start date/time in February, January and December should be included.*
2. Order by Appointment start date and time
3. Remove any blocked/embargoed Appointment Slots if extracted *(any Appointments which were not actually available for Patients to book)*
4. Create sub-group of those Appointments with HCP type of Other – Clinical *(as defined in Healthcare Professional Types)*

Having created these three subgroups of Appointments, the following query set should be run to generate the figures to be entered into the Management Information Reports Specification spreadsheet.

It is likely that there will be some instances of booked date/time(s) towards the end of the reporting period (month) where the actual TNA cannot be identified as it falls in a subsequent month.  These MUST be omitted to ensure that false values are not included.  As such, Suppliers will also need to return a figure for the total number of TNA figures summed together (fields 1241, 1242, 1243) in order that The Authority can calculate an average.

![](https://nhse-dsic.atlassian.net/wiki/download/attachments/1391134317/Diagram.jpg?api=v2)

### OPTION 2 – Apply methodology directly to the system

Rather than extracting data at the end of each reporting period as per Option 1, the methodology as set out above could be applied directly to the information held in the system at each Practice at the end of each reporting period (month).

The fields to be populated and the query set to be applied remain exactly the same.

- There is no requirement to differentiate between ‘routine’ and ‘urgent’ Appointments. All Slots should be included.
- Ensure that ‘blocked’ and/or ‘embargoed’ Appointment Slots i.e. Appointment Slots which may show as available but which were not actually available for a Patient to book, are NOT included.

Please note the following exclusion:

Taking this approach allows for the identification of a TNA which falls in a month subsequent to the reporting period (month) as all information is available.

**Therefore, for consistency, any instance where the TNA identified falls in a month subsequent to the reporting period (month) MUST be excluded and ignored** ***i.e. for the February reporting period, in any case where the actual TNA identified is in March or later, this instance MUST be ignored and excluded from the sum returned.***

### OPTION 3 – Calculate at time of booking and store

The third option for returning the TNA sum as part of the Business Information Reporting Specification does not rely on the methodology for a retrospective calculation as set out for Options 1 and 2 above.

Instead the third next available Appointment would be identified and the time in days between the booking time and the start time of the TNA calculated as any Appointment is booked i.e. any time an Appointment booking is saved into the Appointments system the TNA is identified and the number of days between the booking time and the start date/time of the TNA is stored to be returned in Management Information for the appropriate month.

Please note the following conditions:

- The split by HCP type will be determined by the characteristics of the Appointment booked even if this is not the third next available Appointment. *e. if the Appointment booking is for an Appointment with a nurse, then the third next available Appointment with a nurse should be identified at the point of this booking and included within the figure returned for field 1239.*
- The figure calculated should be included in the Management Information return for the reporting period in which the Appointment booked is due to take place based on the start date/time of that Appointment.

*i.e. if a booking is made in January for an Appointment in February, the TNA figure calculated at the time of that booking should be returned as part of the February Management Information return.*

- Ensure that ‘blocked’ and/or ‘embargoed’ Appointment Slots i.e. Appointment Slots which may show as available but which were not actually available for a Patient to book, are NOT included
- Instances where the TNA identified falls in a month subsequent to the Appointment being booked MUST be ignored and excluded from the figures to be returned in order to be consistent with Options 1 and 2.

*i.e. if a booking is made for an Appointment in February, but the TNA identified at the time of this booking is in March (or later), this MUST be excluded from any data returned.*

- It is recognised that selecting option 3 is unlikely to allow for the return of historical TNA data

### Worked Examples

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Appt no.** | **Appt start date/time** | **Booked date/time 1** | **Cancelled date/time 1** | **Booked date/time 2** |
| 1 | Jan 28th 10am | Jan 16th 10am | Jan 18th 11am | Jan 19th 9am |
| 2 | Jan 29th 3pm | Jan 20th 2pm |  |  |
| 3 | Jan 30th 10am | x |  |  |
| 4 | Jan 30th 3pm | Jan 23rd 4pm | Jan 26th 2pm |  |
| 5 | Jan 31st 10am | x |  |  |
| 6 | Feb 1st 10am | Jan 25th 4pm | Jan 26th 9am | Jan 26th 10am |
| 7 | Feb 1st 3pm | x |  |  |
| 8 | Feb 2nd 10am | Jan 12th 11am |  |  |
| 9 | Feb 2nd 3pm | Jan 31st 9am |  |  |
| 10 | Feb 3rd 10am | Jan 28th 3pm | Jan 30th 1pm |  |
| 11 | Feb 3rd 3pm | x |  |  |
| 12 | Feb 4th 10am | Feb 1st 9am |  |  |
| 13 | Feb 4th 3pm | x |  |  |
| 14 | Feb 5th 10am | Feb 2nd 9am |  |  |
| 15 | Feb 5th 3pm | Feb 2nd 11am |  |  |
| 16 | Feb 15th 2pm | Feb 1st 10am | Feb 4th 3pm | Feb 5th 9am |
| 17 | Feb 26th 10am | Feb 12th 3pm | Feb 14th 2pm | Feb 15th 9am |
| 18 | Feb 26th 3pm | Feb 14th 5pm |  |  |
| 19 | Feb 27th 10am | Feb 20th 10am | Feb 24th 2pm |  |
| 20 | Feb 28th 10am | x |  |  |
| 21 | Feb 28th 3pm | Feb 23rd 10am |  |  |
| 22 | Mar 1st 10am | Feb 20th 3pm | Feb 27th 2pm |  |
| 23 | Mar 1st 3pm | x |  |  |

#### Option 1

After end of February, Supplier extracts all Appointments with a start date/time in February.  **Appt Nos. 6-21 ONLY**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Appt no.** | **Appt start date/time** | **Booked date/time 1** | **Cancelled date/time 1** | **Booked date/time 2** | **Action** | **Reason** | **TNA** |
| 1 | Jan 28th 10am | Jan 16th 10am | Jan 18th 11am | Jan 19th 9am | Ignore | Start date/time is before BT\_1 |  |
| 2 | Jan 29th 3pm | Jan 20th 2pm |  |  | Ignore | Booked date/time 1 is before BT\_1 |  |
| 3 | Jan 30th 10am | x |  |  | Ignore | Start time after BT\_1 and not booked | 1 |
| 4 | Jan 30th 3pm | Jan 23rd 4pm | Jan 26th 2pm |  | Ignore | Cancelled date/time 1 is before BT\_1 and no Booked date/time 2 | 2 |
| 5 | Jan 31st 10am | x |  |  | Include | Start time after BT\_1 and not booked | 3 |
| 6 | Feb 1st 10am | Jan 25th 4pm | Jan 26th 9am | Jan 26th 10am |  |  |  |
| 7 | Feb 1st 3pm | x |  |  |  |  |  |
| 8 | Feb 2nd 10am | Jan 12th 11am |  |  |  |  |  |
| 9 | Feb 2nd 3pm | Jan 31st 9am |  |  |  |  |  |
| 10 | Feb 3rd 10am | Jan 28th 3pm  ***(BT\_1)*** | Jan 30th 1pm |  |  |  |  |
| 11 | Feb 3rd 3pm | x |  |  |  |  |  |
| 12 | Feb 4th 10am | Feb 1st 9am |  |  |  |  |  |
| 13 | Feb 4th 3pm | x |  |  |  |  |  |
| 14 | Feb 5th 10am | Feb 2nd 9am |  |  |  |  |  |
| 15 | Feb 5th 3pm | Feb 2nd 11am |  |  |  |  |  |
| 16 | Feb 15th 2pm | Feb 1st 10am | Feb 4th 3pm | Feb 5th 9am |  |  |  |
| 17 | Feb 26th 10am | Feb 12th 3pm | Feb 14th 2pm | Feb 15th 9am |  |  |  |
| 18 | Feb 26th 3pm | Feb 14th 5pm |  |  |  |  |  |
| 19 | Feb 27th 10am | Feb 20th 10am | Feb 24th 2pm |  |  |  |  |
| 20 | Feb 28th 10am | x |  |  |  |  |  |
| 21 | Feb 28th 3pm | Feb 23rd 10am |  |  |  |  |  |
| 22 | Mar 1st 10am | Feb 20th 3pm | Feb 27th 2pm |  |  |  |  |
| 23 | Mar 1st 3pm | x |  |  |  |  |  |

1. Take Appt 10 *(as an example only – usually would start with Appt 6)*
2. Does it have a booked date/time? **YES, Jan 28th 3pm**
3. Call this BT\_1
4. Compare BT\_1 against all Appointments in list including those with a start date/time in the previous month. **Start with Appt 1**
5. Is BT\_1 associated with Appt 1? **NO**
6. Is BT\_1 before the start date/time of Appt 1? **NO – IGNORE**
7. Now compare against Appt 2
8. Is BT\_1 associated with Appt 2? **NO**
9. Is BT\_1 before the start date/time of Appt 2? **YES**
10. Does Appt 2 have a booked date/time 1? **YES**
11. Is BT\_1 before booked date/time 1 of Appt 2? **NO**
12. Does Appt 2 have a cancelled date/time 1? **NO – IGNORE Appt was already booked**
13. Now compare against Appt 3
14. Is BT\_1 associated with Appt 3? **NO**
15. Is BT\_1 before start date/time of Appt 3? **YES**
16. Does Appt 3 have a booked date/time 1? **NO – IGNORE this is the 1st next available Appointment**
17. Now compare against Appt 4
18. Is BT\_1 associated with Appt 4? **NO**
19. Is BT\_1 before start date/time of Appt 4? **YES**
20. Does Appt 4 have a booked date/time 1? **YES**
21. Is BT\_1 before booked date/time 1 of Appt 4? **NO**
22. Does BT\_1 have a cancelled date/time 1? **YES**
23. Is BT\_1 before cancelled date/time 1 of Appt 4? **NO**
24. Does Appt 4 have a booked date/time 2? **NO – IGNORE this is the 2nd next available Appointment**
25. Now compare against Appt 5
26. Is BT\_1 associated with Appt 5? **NO**
27. Is BT\_1 before start date/time of Appt 5? **YES**
28. Does Appt 5 have a booked date/time? **NO – INCLUDE this is the 3rd next available Appointment**
29. Now calculate start date/time of Appt 5 (Jan 31st 10am) MINUS BT\_1 (Jan 28th 3pm) to get figure to be included in return

The process should be followed for every Booked date/time associated with every Appointment with a start date/time in February.

Looking towards the end of the month, take Appt 21.  The TNA identified would be Appt 23. However, because the Supplier only extracts the data for the reporting month (February), Appt 22 and Appt 23 which are in March do not appear in the data. Hence it would not be possible to identify the TNA. Therefore, this MUST be excluded from the data returned.

#### Option 2

- Apply the methodology to calculate TNA directly to the system without an extraction of data.
- Any TNA identified which falls in March (or any month after February) should be ignored and excluded from the data returned. Although it would be possible to identify that the TNA for the booked date/time associated with Appt 21 is Appt 23, this figure should be ignored for consistency as it would not be possible to obtain it using Option 1 methodology.

#### Option 3

- The TNA is identified and calculated at the time at which the Appointment is booked i.e. for Appt 10, the TNA would be identified as Appt 5 at the point at which Appt 10 was booked (28th Jan at 3pm), the amount of time between the booking time and the start time would be calculated and stored ready to be returned as part of the February Management Information return.
- The figure calculated must be included in the Management Information for the reporting period in which the Appointment booked is due to take place based on the start date/time of that Appointment i.e. for Appt 10, although the booked date/time is in January, the start date/time of the Appointment booked is in February, therefore this should be returned as part of the February return.
- Any TNA identified which falls in March (or any month after February) should be ignored and excluded from the data returned. Although it would be possible to identify that the TNA for the booked date/time associated with Appt 21 is Appt 23, this figure should be ignored for consistency as it would not be possible to obtain it using Option 1 methodology.

#### Summary

Looking at all the Appointments, the table below shows the TNA which should be identified for each booking time associated with each Appointment for the February return

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Appt No.** | **Start date/time** | **Booked date/time(s)** | **Which appt is TNA?** | **Time until TNA? (days)** |
| 6 | Feb 1st 10am | Jan 25th 4pm | Appt 6 (Feb 1st 10am) | 7 |
| 6 | Feb 1st 10am | Jan 26th 10am | Appt 6 (Feb 1st 10am) | 6 |
| 7 | Feb 1st 3pm | X | n/a | - |
| 8 | Feb 2nd 10am | Jan 12th 11am | Appt 3 (Jan 30th 10am) | 18 |
| 9 | Feb 2nd 3pm | Jan 31st 9am | Appt 9 (Feb 2nd 3pm) | 2 |
| 10 | Feb 3rd 10am | Jan 28th 3pm | Appt 5 (Jan 31st 10am) | 3 |
| 11 | Feb 3rd 3pm | X | n/a | - |
| 12 | Feb 4th 10am | Feb 1st 9am | Appt 11 (Feb 3rd 3pm) | 2 |
| 13 | Feb 4th 3pm | X | n/a | - |
| 14 | Feb 5th 10am | Feb 2nd 9am | Appt 13 (Feb 4th 3pm) | 2 |
| 15 | Feb 5th 3pm | Feb 2nd 11am | Appt 13 (Feb 4th 3pm) | 2 |
| 16 | Feb 15th 2pm | Feb 1st 10am | Appt 11 (Feb 3rd 3pm) | 2 |
| 16 | Feb 15th 2pm | Feb 5th 9am | Appt 18 (Feb 26th 3pm) | 21 |
| 17 | Feb 26th 10am | Feb 12th 3pm | Appt 19 (Feb 27th 10am) | 15 |
| 17 | Feb 26th 10am | Feb 15th 9am | Appt 20 (Feb 28th 10am) | 13 |
| 18 | Feb 26th 3pm | Feb 14th 5pm | Appt 19 (Feb 27th 10am) | 13 |
| 19 | Feb 27th 10am | Feb 20th 10am | Appt 21 (Feb 28th 3pm) | 8 |
| 20 | Feb 28th 10am | X | n/a | - |
| 21 | Feb 28th 3pm | Feb 23rd 10am | Appt 23 (in next period) | - |
| **Sum of time until 3rd next available Appointment (to be returned (field 1238, 1239, 1240)** | **114** |  |  |  |
| **Total number of figures added together to get the sum (field 1241, 1242, 1243)** | **14** |  |  |  |

# Applicable Capabilities

All Supplier Solutions will need to meet this Standard if they are delivering the Capability.

- Page:[GP Extracts Verification](../../DSIC-Capabilities/GP-Extracts-Verification.md)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Secure Electronic File Transfer (SEFT)](../../DSIC-Standards/Non-Overarching-Standards/Secure-Electronic-File-Transfer-SEFT.md)

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Title |
| --- |
| No content found. |

## Attachments

- [Long and skinny csv template.csv](../../../../.raw/DCSDCS/attachments/1391134317/att1391150062-Long and skinny csv template.csv)
- [Tabular csv template.csv](../../../../.raw/DCSDCS/attachments/1391134317/att1391150199-Tabular csv template.csv)
- [Diagram.jpg](../../../../.raw/DCSDCS/attachments/1391134317/att1391160862-Diagram.jpg)
- [Creating Automated SFTP Transfers - Guidance.docx](../../../../.raw/DCSDCS/attachments/1391134317/att13172736004-Creating Automated SFTP Transfers - Guidance.docx)
