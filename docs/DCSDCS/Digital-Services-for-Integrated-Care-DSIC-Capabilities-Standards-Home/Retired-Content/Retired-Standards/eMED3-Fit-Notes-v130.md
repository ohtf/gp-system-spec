---
page_id: "12288688132"
space: "DCSDCS"
title: "eMED3 (Fit Notes) v1.3.0"
version: 3
updated: "2023-01-31T10:42:18.456Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12288688132/eMED3+Fit+Notes+v1.3.0"
labels: ["capability_specific_retired"]
---

# eMED3 (Fit Notes) v1.3.0

|  |  |
| --- | --- |
| ID | S39 |
| Version | 1.3.0 |
| Type | Capability Specific Standard |
| Status | Retired |
| Effective Date | 01 Jul 2022 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

# Description

Supports the creation of eMED3 data, its integration into the Patient Record, printing or issuing of MED3 fit note certificates and extraction of data to NHS Digital.

The Statement of Fitness for Work (known as a Med 3 form or ‘fit note’) is used throughout Great Britain. Fit notes are issued by doctors, nurses, physiotherapists, occupational therapists and pharmacists for Statutory Sick Pay or Social Security purposes. As a part of a medical consultation a doctor, nurse, physiotherapist, occupational therapist or pharmacist may assess a patient’s medical condition to determine its impact on their fitness for work.  The fit note provides return to work advice for the patient and their employer and can also be used to support a claim to health related benefits.

The roll out of the computer generated fit note project ‘eMed3’ which was completed in 2014 provided a simple tool for the provision of fit note forms, reducing effort, retaining details and allowing the extraction of fit note data which has been published quarterly since August 2017. Access to the eMED3 has been restricted to doctors but is extended to nurses, physiotherapists, occupational therapists and pharmacists.

This document specifies the requirements in respect of the computer generation, record retention and printing of a fit note and the extraction of data. It ensures the retention of existing processes through consistent implementation across all Solutions covered by GP IT Futures.

### **Data extraction and publication**

Since 2017, NHS Digital has published quarterly anonymous, aggregated data on behalf of the Department for Work and Pensions (DWP) derived from the issue of fit notes saved in the electronic patient record.  The data is extracted from GP IT Solutions via XML-based eMED3 Activity Files from practices on a weekly basis via Messaging Exchange for Social Care and Health (MESH). The periodic transfer of data will be instigated by the supplier’s Solution and automatically submitted to NHS Digital. 

# Requirements

|  |  |  |
| --- | --- | --- |
| eMED3 Data Recording and Printing | | |
| Requirement ID | Requirement Text | Level |
| eMED3-01 | Capture and edit New eMED3 data in accordance with Copy of eMED3 (Fit Notes)#eMED3 Data Entry | MUST |
| eMED3-02 | Ability to cancel the transaction at any time during the data entry process.  Upon cancelling, Practice User to be informed that by cancelling no record of the eMED3 transaction will be kept and the form, if printed, is to be destroyed. Practice User is to be asked if they wish to continue with cancelling. If NO, the user to be returned to the data entry form. | MUST |
| eMED3-03 | Create eMED3 forms (as per eMED3 Template (2022))  in an unalterable format (compatible with GP2GP transfer) populated with the eMED3 data recorded in Copy of eMED3 (Fit Notes)#eMED3-01  and as defined in eMED3 Data Items Usage.  eMED3 forms only to be created when all mandatory data items  as defined in Copy of eMED3 (Fit Notes)#eMED3 Data Entry have been recorded. | MUST |
| eMED3-04 | Preview unprinted eMED3 forms created as per Copy of eMED3 (Fit Notes)#eMED3-03. | MUST |
| eMED3-05 | Print eMED3 forms created as per Copy of eMED3 (Fit Notes)#eMED3-03**.**The form to be printed in the format specified by eMED3 Template (2022) with data populating the appropriate fields as defined in eMED3 Data Items Usage, in the eMED3 Data Entry table and in Copy of eMED3 (Fit Notes)#eMED3 Template (2022) with Mappings.  For <Patient.title>, suppliers can choose to display the title by striking through the appropriate alternative titles on the form (Mr, Mrs, Ms, Miss) or by simply printing only the relevant title as held on the Patient Record.  This can include titles other than those listed on the form (e.g. ‘Dr.’, ‘Prof’, ‘Lord’).  eMED3 forms only to be printed when all mandatory data items  as defined in Copy of eMED3 (Fit Notes)#eMED3 Data Entry have been recorded. | MUST |
| eMED3-06 | Printed eMED3 statement to contain a 2D Barcode positioned on the form as shown on Copy of eMED3 (Fit Notes)#eMED3 Template (2022).   - Each field to be delimited by a ‘|’ character ('pipe symbol') - To avoid delimiter collision, escape characters to be used (i.e.’\|’) - Only data which is printed on the form will be encoded as per the 2D Barcode Data elements table - Data to be included in the order listed as per the 2D Barcode Data elements table - Information to be stored on the barcode to be truncated if required in order to fit within the maximum characters the barcode can allow    Click here to view the 2D Barcode Data elements table2D Barcode Data elements  | Order | Field | Max Size (Characters) | | --- | --- | --- | | 1 | <AssessmentDate> | 8 | | 2 | <StatementDateTime> | 8 | | 3 | <Patient.title> | 3 | | 4 | <Patient.first.name> | 20 | | 5 | <Patient.second.name> | 1 | | 6 | <Patient.surname> | 30 | | 7 | <Patient.Address1> | 15 | | 8 | <Patient.Postcode> | 8 | | 9 | <Patient.DOB> | 8 | | 10 | <Diag.Printed.Text> | 42 | | 11 | <NFWFlag> | 1 | | 12 | <MFWFlag> | 1 | | 13 | <MFWPhaseRtn> | 1 | | 14 | <MFWAlteredHrs> | 1 | | 15 | <MFWAmendDuties> | 1 | | 16 | <MFWAdaptWorkplace> | 1 | | 17 | <ValidPeriodDays>, <ValidPeriodWeeks>, <ValidPeriodMonths> OR “INDEF” (i.e. <ValidPeriodIndefinite>) | 5 | | 18 | <ValidPeriodStartDate> | 8 | | 19 | <ValidPeriodEndDate> | 8 | | 20 | <FollowUpAssessment> | 1 | | 21 | <UniqueID> | 20 | | 22 | <DuplicatePrinted> | 1 | | 23 | <Practice.name> | 20 | | 24 | <Practice.address1> | 15 | | 25 | <Practice.postcode> | 8 | | 26 | <Practice.phone.number> | 12 |   For Standards relating to barcode implementation, see:   - ISB1077 - AIDC for Patient Identification - ISB0108 - AIDC: Automatic Identification and Data Capture | MUST |
| eMED3-07 | If the eMED3 Statement has been printed, but not yet saved to the Patient Record, the Practice User to have the option to amend the data and reprint. An audit of this activity will be captured. | MUST |
| eMED3-08 | All eMED3 data and created eMED3 forms to be saved to the patient record as per eMED3 Data Items Usage.  Data can be saved before printing, after printing or (to the user) simultaneously as long as the requirements are met. | MUST |
| eMED3-09 | Record that eMED3 form was 'issued by hand' (e.g. when retroactively capturing data for a paper-based MED3 form). This function to adhere to requirements eMED3- 01, eMED3-08 and to Copy of eMED3 (Fit Notes)#eMED3 Data Entry, with the following exceptions:   1. - Admin Code to be recorded as one of:      - 751751000000104 - MED3 (2010) issued by hand, may be fit for work (finding)      - 751731000000106 - MED3 (2010) issued by hand, not fit for work (finding)    - Printing is not mandatory, but Practice User to be offered the option to print the statement       - If they choose to print Copy of eMED3 (Fit Notes)#eMED3 Data Entry to be adhered to (also see eMED3-10 and Copy of eMED3 (Fit Notes)#eMED3-05) | MUST |
| eMED3-10 | When printing eMED3 forms (see Copy of eMED3 (Fit Notes)#eMED3-05) which are recorded as 'issued by hand', the words “ISSUED BY HAND” to be included overlaid in grey scale format and in the background on the printed form. | MUST |
| eMED3-11 | View all saved eMED3 forms and associated data (see Copy of eMED3 (Fit Notes)#eMED3-01 and Copy of eMED3 (Fit Notes)#eMED3-03). | MUST |
| eMED3-12 | Create Duplicate of saved eMED3 form. | MUST |
| eMED3-13 | Print Duplicate of saved eMED3 form (see Copy of eMED3 (Fit Notes)#eMED3-03) ensuring the word “DUPLICATE” is included overlaid in grey scale format and in the background on the printed form. | MUST |
| eMED3-14 | Duplicates can only be printed of previously issued New statements, i.e. Not statements Issued by Hand or Duplicates previously printed | MUST |
| eMED3-15 | For all Duplicate eMED3 forms created, update the Patient record by saving the following data items:   - Depending on whether the original statement was Not Fit for Work (NFW) or May Be Fit for work (MFW), record the applicable <AdminCode> and its <AdminText> for Duplicate:   - 751641000000105 - eMED3 (2010) duplicate issued, may be fit for work (finding)   - 751621000000103 - eMED3 (2010) duplicate issued, not fit for work (finding) - Record <DuplicatePrinted> flag and ensure the <PrintedFlag> is NOT recorded. - Save all other structured data associated with the original statement (using all the original dates) | MUST |
| eMED3-16 | Solution to generate a <LinkingID> to be used as a linking identifier allowing DWP to identify all data relating to the same Patient without identifying him or her.  The <LinkingID> to be in the form of a DCE UUID and stored with each eMED3 transaction in the Patient’s record. | MUST |
| eMED3-17 | Solution to ensure that only doctors, nurses, physiotherapists, occupational therapists and pharmacists can capture and edit New eMED3 data and forms (i.e. forms that are not recorded as Issued by hand or Duplicate). | MUST |
| eMED3-18 | Creation and printing of Duplicate and Issued by hand eMED3 forms to be possible by both doctors, nurses, physiotherapists, occupational therapists and pharmacists as well as GP Practice admin users | MUST |
| eMED3-28 | Solution to automatically populate the Name and Profession of the Authorised Health or Care Professional issuing the form; data to be populated in the Copy of eMED3 (Fit Notes)#eMED3 Template (2022) in the two new data fields. | MUST |
| eMED3 Data Extraction | | |
| eMED3-19 | Ability to extract eMED3 activity data manually and automatically at a specified time. | MUST |
| eMED3-20 | Format extracted eMED3 activity data into one XML-based eMED3 Activity File adhering to the data elements defined and the record layout indicated in eMED3 Data Items Usage. | MUST |
| eMED3-21 | The structure and enveloping of the extracted content to be consistent with the following eMED3 Activity File XML Schema:   - [EMED3-v2-7 SCHEMA Rev 1](https://nhse-dsic.atlassian.net/wiki/download/attachments/12288688132/EMED3-v2-7%20SCHEMA%20Rev%201.txt?version=1&modificationDate=1675160494345&cacheVersion=1&api=v2) | MUST |
| eMED3-22 | XML-based eMED3 Activity Files will be transferred to NHS Digital on a weekly basis via Messaging Exchange for Social Care and Health (MESH). | MUST |
| eMED3-23 | The weekly extraction and transfer to occur every Sunday | MUST |
| eMED3-24 | Scheduled extracts to commence from the first Sunday following the eMED3 service going live and weekly thereafter | MUST |
| eMED3-25 | Each new submission to be an extract of all eMED3 transaction activity which has occurred since the last extract (unless this is the first extract being taken).  Suppliers to not populate extracts with data any older than is covered by the standard extract cycle defined in Copy of eMED3 (Fit Notes)#eMED3-23**.** | MUST |
| eMED3-26 | Each eMED3 Activity File Construction to comprise an *envelope* and a *payload*.  The payload to be the extracted statistical content as defined in Copy of eMED3 (Fit Notes)#eMED3 Activity File Payload.  Where there are no eMED3 transaction records i.e. a null return as detailed in the schema, an eMED3 Activity File to still be provided.  The practice envelope to contain the data itemised in Copy of eMED3 (Fit Notes)#eMED3 Activity File Envelope. | MUST |
| eMED3-27 | Data about patients who have registered a Type 1 opt-out (as per National data opt-out programme) will not be included in the eMED3 data extract, unless the patient has withdrawn this at a later date.  Opt-out is recorded in the Patient Record currently using the following (Type 1) patient objection code (in SNOMED CT):  827241000000103 - Dissent from secondary use of GP patient identifiable data  Withdrawal of this opt-out is recorded on the patient record currently using the following (Type 1) patient objection code (in SNOMED CT):  827261000000102 - Withdraw dissent from secondary use of GP patient identifiable data  The date of the most recent (Type 1) patient objection code i.e. the event data associated with the (Type 1) patient objection code, will be used to determine if data is to be included. | MUST |

eMED3 Data Entry: Fields and Data Definition 

This table defines the mapping between data items and the form (see Copy of eMED3 (Fit Notes)#eMED3 Template (2022) with Mappings), the minimum data to be captured, the rules to be applied to this data and the preconditions for enabling and disabling the ability to record data on the form:

| Field # | Form Field Title | Type | Data Item Saved | Field Contents Displayed | Rule(s) |
| --- | --- | --- | --- | --- | --- |
| 3 | Date of assessment | Date  Flag | <AssessmentDate> <AssessmentSixMonthFlag> | Date in dd/month/yyyy format | - Mandatory field   This is the date the authorised professional (doctor, nurse, physiotherapist, occupational therapist, or pharmacist) assessed or examined the Patient, or the date he/she considered a report from another healthcare professional.    - Default to <StatementDateTime> - Can be the same date the statement is issued or it can be any date preceding the issued date. - It cannot be a future date. - If date is 26 weeks or more before the date of issue, prompt the user to confirm that the correct Assessment Date has been entered. If confirmed, the <AssessmentSixMonthFlag> field to be set. |
| N/A | Admin Term | Code  Text  Code | <AdminCode>  <AdminText>  <CodingSystem> | Admin Code Description | - <AdminCode> selected to be one of:   - 751601000000107 - eMED3 (2010) new statement issued, may be fit for work (finding)   - 751481000000104 - eMED3 (2010) new statement issued, not fit for work (finding) - Mandatory field - Only <AdminText> to be displayed (on-screen and on form) which is the term for the selected <AdminCode> for the new statement being issued - Text not to exceed number of characters that can be printed within the box in Arial pt.8.5 |
| 4 | Diagnosis | Code  Code  Text | <DiagCode>  <DiagCodeText>  <Diag.Printed.Text> | Text from SNOMED CT Dictionary including a coded diagnosis with additional Free Text where applicable | - This field is the principal diagnosis causing the statement to be issued - <DiagCode>, <DiagCodeText> and <Diag.Printed.Text> are all MANDATORY data items - <Diag.Printed.Text> defaults to <DiagCodeText>, but can be amended - Text not to exceed number of characters that can be printed within the box in Arial pt.8.5 |
| 5 | Not Fit for Work (NFW) | Flag | <NFWFlag> | Tick in the box | - Tick box to be offered for the authorised professional (doctor, nurse, physiotherapist, occupational therapist, or pharmacist) to indicate the Patient is NOT fit for work (<NFWFlag>) - Mandatory to select one of NFW or MFW tick boxes, and only one is to be ticked by the user and then the appropriate flag set - If not ticked, this to be indicated on the form for both the box and its title (e.g. by changing it to background grey scale, over-writing with a double strikethrough) |
| 6 | May Be Fit for work (MFW) | Flag | <MFWFlag> | Tick in the box | - Tick box to be offered for the authorised professional (doctor, nurse, physiotherapist, occupational therapist, or pharmacist) to indicate the Patient MAY be fit for work (<MFWFlag>) - Mandatory to select one of NFW or MFW tick boxes, and only one is to be ticked by the user and then the appropriate flag set - If not ticked, this to be indicated on the form for both the box and its title (e.g. by changing it to background grey scale, over-writing with a double strikethrough) |
| 7, 8 | Comments | Text  Text | <NFW.Remarks>  Or  <MFW.Comments> | Free text as entered | If <NFWFlag> is set:    - Comments are OPTIONAL; - <MFWPhaseRtn>, <MFWAlteredHrs>, <MFWAmendDuties> and <MFWAdaptWorkplace> tick boxes to be DISABLED - Free text entered to be saved as <NFW.Remarks> - Text not to exceed number of characters that can be printed within the box in Arial pt.8.5   If <MFW.flag> is set:    - Comments are MANDATORY; - <MFWPhaseRtn>, <MFWAlteredHrs>, <MFWAmendDuties> and <MFWAdaptWorkplace> tick boxes to be ENABLED - Free text entered to be saved as <MFW.Comments> - Text not to exceed number of characters that can be printed within the box in Arial pt.8.5 |
| 9 | Phased return | Flag | <MFWPhaseRtn> | Tick in the box | - If <NFWFlag> is set, then box to be DISABLED - If <MFWFlag> is set, then box to be ENABLED    - Tick box is optional.   - Can be ticked in combination with other MFW boxes or left unticked  - If not ticked, this to be indicated on the form for both the box and its title (e.g. by changing it to background grey scale, over-writing with a double strikethrough) |
| 10 | Altered hours Flag | Flag | <MFWAlteredHrs> | Tick in the box | - If <NFWFlag> is set, then box to be DISABLED - If <MFWFlag> is set, then box to be ENABLED    - Tick box is optional.   - Can be ticked in combination with other MFW boxes or left unticked  - If not ticked, this to be indicated on the form for both the box and its title (e.g. by changing it to background grey scale, over-writing with a double strikethrough) |
| 11 | Amended duties Flag | Flag | <MFWAmendDuties> | Tick in the box | - If <NFWFlag> is set, then box to be DISABLED - If <MFWFlag> is set, then box to be ENABLED    - Tick box is optional.   - Can be ticked in combination with other MFW boxes or left unticked  - If not ticked, this to be indicated on the form for both the box and its title (e.g. by changing it to background grey scale, over-writing with a double strikethrough) |
| 12 | Adaptations Flag | Flag | <MFWAdaptWorkplace> | Tick in the box | - If <NFWFlag> is set, then box to be DISABLED - If <MFWFlag> is set, then box to be ENABLED    - Tick box is optional.   - Can be ticked in combination with other MFW boxes or left unticked  - If not ticked, this to be indicated on the form for both the box and its title (e.g. by changing it to background grey scale, over-writing with a double strikethrough) |
| 13, 14, 15,  16 | This will be the case for: | Number  Number  Number  Flag  Flag | <ValidPeriodDays>  <ValidPeriodWeeks>  <ValidPeriodMonths>  <ValidPeriodIndefinite>  <NFWSixMonthFlag> | Days, weeks, months, or “Indefinite Period’ for which statement is valid | - Enables the user to define the period of time for which the statement is valid from the <AssessmentDate> - Mandatory to record this field or record <ValidPeriodStartDate> and <ValidPeriodEndDate> - Options are:   - No. of Days   - No. of Weeks   - No. of Months   - Indefinite  - Duration to be stored as appropriate data item: <ValidPeriodDays>, <ValidPeriodWeeks>, <ValidPeriodMonths> or <ValidPeriodIndefinite> - If Duration >= 13 weeks or 3 months, or value = indefinite, then prompt user to confirm the Patient has been unfit for work for at least 6 months preceding the <AssessmentDate>.   - If confirmed, the specified extended period to be allowed and the <NFWSixMonthFlag> set   - If not confirmed, the Solution to allow the authorised professional (doctor, nurse, physiotherapist, occupational therapist, or pharmacist) to re-enter the date range subject to all the same rules defined for this field - If the Duration <= 14 days, this field to be left blank and the Solution to automatically fill in the <ValidPeriodStartDate> and <ValidPeriodEndDate> fields as per defined rules for these fields |
| 17, 18 | Or from:  <> TO : <> | Date  Date  Flag | <ValidPeriodStartDate>  <ValidPeriodEndDate>  <NFWSixMonthFlag> | Date range for which statement is valid | - User can enter both <ValidPeriodStartDate> and <ValidPeriodEndDate> or they can specify just <ValidPeriodEndDate>. - If they enter only <ValidPeriodEndDate>, then <ValidPeriodStartDate> to default <AssessmentDate> - If Duration >= 13 weeks or 3 months, or value = indefinite, then prompt user to confirm the Patient has been unfit for work for at least 6 months preceding the <AssessmentDate>   - If confirmed, the specified extended period to be allowed and the <NFWSixMonthFlag> set   - If not confirmed, the Solution to allow the authorised professional (doctor, nurse, physiotherapist, occupational therapist, or pharmacist) to re-enter the date range subject to all the same rules defined for this field |
| 19 | Follow-up assessment required | Flag  Date | <FollowUpAssessment>  <Follow.up.date> | Tick in the box | - Ticked if a follow-up assessment is required at the end of the period.     - If ticked <FollowUpAssessment> flag to be set   - <Follow.up.date> to be recorded although this date is not printed, but can be used for future reference  - As per eMED3 form layout as shown in Copy of eMED3 (Fit Notes)#eMED3 Template (2022) with Mappings, one of the following lines of text to be printed, as appropriate:   *I will/will not need to assess your fitness for work again at the end of this period.*  *I will/will not need to assess your fitness for work again at the end of this period.* |
| 34, 20 | PRINT | Calculated  Date  Time | <UniqueID>  <StatementDate  <StatementTime> |  | - Printing only to be allowed once all Mandatory data items have been recorded - If PRINT clicked:   - <UniqueID> is generated by the Solution and recorded     - There is no requirement for the unique ID to hold any linking or identifiable information and therefore a standard GUID (DCE UUID, provided in dash-separated print format) is acceptable for this requirement   - <StatementDate> automatically recorded by Solution as today’s system date in MMDDYY format   - <StatementTime> automatically recorded by Solution as system time in HHMM format (24 hour)   - Form is printed as per Copy of eMED3 (Fit Notes)#eMED3-05   - Data items are generated and all data saved as per Copy of eMED3 (Fit Notes)#eMED3-08 - If the printing fails   - A failed print will be recorded   - User to have ability to print again (to reprint the eMED3 in its original format – i.e. not as a Duplicate) |
| N/A | SAVE or OK | Flag | <PrintedFlag> |  | - Signifies end of transaction - Option enabled after PRINT option has been selected for the user to confirm the statement printed successfully - Once clicked, <PrintedFlag> is recorded - If not already saved, data items are generated and all data saved as per Copy of eMED3 (Fit Notes)#eMED3-08 |

## eMED3 Data Items Usage

The eMED3 Data Items table details all eMED3 data elements, their name, form, and source, and their use as follows: 

- Display - the data item is displayed for the user while doing the transaction
- Saved - the data item is saved to the Patient Record
- Printed - the data item is printed on the statement perCopy of eMED3 (Fit Notes)#eMED3 Template (2022) with Mappings
- Xfr - the data item is transferred to NHS Digital

The 'Source' column represents the likely origin of the data:

- Sys files - reference data expected to be already held in the Solution, but user selected
- Patient Record - data expected to be already held in the Patient Record
- User - new data entered by the user when completing the form
- Solution - data generated by the Solution in the completion of the form (either newly generated or using existing reference data)

Where the source is 'Sys files' or 'Patient Record', there is not a requirement for this information to be saved in duplicate to the Patient Record.

### eMED3 Data Items

| Name | Form | Source | Display | Saved | Printed | Xfr |
| --- | --- | --- | --- | --- | --- | --- |
| <AdminCode> |  | Sys files | Y | Y | N | Y |
| <AdminText> |  | Sys files | Y | Y | N | Y |
| <CodingSystem> |  | Solution | N | Y | N | Y |
| <Patient.title> | As per Copy of eMED3 (Fit Notes)#eMED3-05 | Patient Record | Y | Y | Y | N |
| <Patient.surname> |  | Patient Record | Y | Y | Y | N |
| <Health.or.Care.Professional-ID> |  | Solution | N | Y | N | N |
| <AssessmentDate> | dd/mm/yyyy | User | Y | Y | Y | Y |
| <AssessmentSixMonthFlag> | flag | User | N | Y | N | Y |
| <DiagCode> |  | Sys files | N | Y | N | Y |
| <DiagCodeText> |  | Sys files | Y | Y | N | Y |
| <Diag.Printed.Text> | Free text | User | Y | Y | Y | N |
| <NFWFlag> | flag | User | Y | Y | Y | Y |
| <MFWFlag> | flag | User | Y | Y | Y | Y |
| <NFW.Remarks> | Free text | User | Y | Y | Y | N |
| <MFW.Comments> | Free text | User | Y | Y | Y | N |
| <MFWPhaseRtn> | flag | User | Y | Y | Y | Y |
| <MFWAlteredHrs> | flag | User | Y | Y | Y | Y |
| <MFWAmendDuties> | flag | User | Y | Y | Y | Y |
| <MFWAdaptWorkplace> | flag | User | Y | Y | Y | Y |
| <ValidPeriodDays> | nnnn | User | Y | Y | Y | Y |
| <ValidPeriodWeeks> | nnn | User | Y | Y | Y | Y |
| <ValidPeriodMonths> | nn | User | Y | Y | Y | Y |
| <ValidPeriodIndefinite> | flag | User | Y | Y | Y | Y |
| <ValidPeriodStartDate> | dd/mm/yyyy | User | Y | Y | Y | Y |
| <ValidPeriodEndDate> | dd/mm/yyyy | User | Y | Y | Y | Y |
| <NFWSixMonthFlag> | flag | User | N | Y | N | Y |
| <FollowUpAssessment> | flag | User | Y | Y | Y | Y |
| <Follow.up.date> | dd/mm/yyyy | Solution | N | Y | N | N |
| <PrintedFlag> | flag | Solution | N | Y | N | Y |
| <DuplicatePrinted> | flag | Solution | N | Y | N | Y |
| <StatementDate> | dd/mm/yyyy | Solution | N | Y | Y | Y |
| <StatementTime> | hhmmss | Solution | N | Y | N | Y |
| <Issuer's.name> |  | Solution | Y | Y | Y | N |
| <Issuer's.profession> |  | Solution | Y | Y | Y | N |
| <Practice.name> |  | Solution | N | N | Y | N |
| <Practice.address1> |  | Solution | N | N | Y | N |
| <Practice.address2> |  | Solution | N | N | Y | N |
| <Practice.address3> |  | Solution | N | N | Y | N |
| <PracticePostCode> | AADD Snn | Solution | N | N | Y | Y |
| <PracticeCode> |  | Solution | N | N | N | Y |
| <Practice.phone.number> |  | Solution | N | N | Y | N |
| <Patient.first.name> |  | Patient Record | N | N | Y | N |
| <Patient.second.name> |  | Patient Record | N | N | Y | N |
| <Patient.Address1> |  | Patient Record | N | N | Y | N |
| <Patient.Address2> |  | Patient Record | N | N | Y | N |
| <Patient.Address3> |  | Patient Record | N | N | Y | N |
| <Patient.DOB> | dd/mm/yyyy | Patient Record | N | N | Y | N |
| <Sex> |  | Patient Record | N | N | N | Y |
| <LinkingID> | See Copy of eMED3 (Fit Notes)#eMED3-16 | Solution | N | Y | N | Y |
| <UniqueID> |  | Solution | N | Y | Y | Y |

## eMED3 Activity File Construction

The eMED3 Activity File will comprise an envelope and a payload as defined in Copy of eMED3 (Fit Notes)#eMED3 Activity File Envelope and Copy of eMED3 (Fit Notes)#eMED3 Activity Record data items tables.

### eMED3 Activity File Envelope

|  |  |
| --- | --- |
| <RecordCount> | A count of the number of records extracted and contained in the payload |
| <ExtractReference> | A GUID assigned by the supplier on extraction and stored for future reference; used for manual diagnostic transaction identification/correlation |
| <ExtractDateTime> | The date and time of eMED3 activity extraction |
| <SubmissionDateTime> | It is expected that transmission will occur immediately after extraction so this will be the same timestamp as above |
| <PracticeCode> | The practice ODS code |
| <PracticePostCode> | The full Post Code of the practice |
| <SystemCode> | A code to identify the Solution (suppliers can choose how to populate this) |
| <VersionRelease> | The Version and Release number of the Solution doing the extract (suppliers can choose how to populate this) |
| <EmailReceiptAck> | OPTIONAL: nominated email address for receipt acknowledgement by NHS Digital |
| <EmailProcessAck> | OPTIONAL: nominated email address for process acknowledgement by NHS Digital |
| <EmailErrorNotification> | OPTIONAL: nominated email address for any error notification by NHS Digital |

### eMED3 Activity File Payload

The payload will comprise of the data items in the Copy of eMED3 (Fit Notes)#eMED3 Activity Record data items.

The separately-supplied schema provides the type for each data item.

### eMED3 Activity Record data items

| **Schema Element Name** |
| --- |
| <AdminCode> |
| <AdminText> |
| <CodingSystem> |
| <AssessmentDate> |
| <AssessmentSixMonthFlag> |
| <DiagCode> |
| <DiagCodeText> |
| <NFWFlag> |
| <MFWFlag> |
| <MFWPhaseRtn> |
| <MFWAlteredHrs> |
| <MFWAmendDuties> |
| <MFWAdaptWorkplace> |
| <ValidPeriodDays> |
| <ValidPeriodWeeks> |
| <ValidPeriodMonths> |
| <ValidPeriodIndefinite> |
| <ValidPeriodStartDate> |
| <ValidPeriodEndDate> |
| <NFWSixMonthFlag> |
| <FollowUpAssessment> |
| <PrintedFlag> |
| <DuplicatePrinted> |
| <StatementDateTime> |
| <Sex> |
| <LinkingID> |
| <UniqueID> |

### eMED3 Template (2022)

[eMED3 Template (2022).pdf](eMED3-Fit-Notes-v130.md)

### eMED3 Template (2022) with Mappings

This template defines the mappings between the printed form and the eMED3 data items. This can be used with the eMED3 Data Entry: Fields and Data Definition table to establish where data recorded is to be printed on the form.

The eMED3 Template Mappings -all printed data items shows this for all data items.

[eMED3 Template (2022) wi…](eMED3-Fit-Notes-v130.md)

### eMED3 Template Mappings - all printed data items

![](https://nhse-dsic.atlassian.net/wiki/images/icons/grey_arrow_down.png)Click here to view table of mappings for all printed eMED3 data items to the form

| **#** | **Name** |
| --- | --- |
| 1 | <Patient.title> |
| 2 | <Patient.surname> |
| 3 | <AssessmentDate> |
| 3d | - |
| 3m | - |
| 3y | - |
| 4 | <Diag.Printed.Text> |
| 5 | <NFWFlag> |
| 6 | <MFWFlag> |
| 7 | <NFW.Remarks> |
| 8 | <MFW.Comments> |
| 9 | <MFWPhaseRtn> |
| 10 | <MFWAlteredHrs> |
| 11 | <MFWAmendDuties> |
| 12 | <MFWAdaptWorkplace> |
| 13 | <ValidPeriodDays> |
| 14 | <ValidPeriodWeeks> |
| 15 | <ValidPeriodMonths> |
| 16 | <ValidPeriodIndefinite> |
| 17 | <ValidPeriodStartDate> |
| 17d | - |
| 17m | - |
| 17y | - |
| 18 | <ValidPeriodEndDate> |
| 18d | - |
| 18m | - |
| 18y | - |
| 19 | <FollowUpAssessment> |
| 20 | <StatementDate> |
| 20d | - |
| 20m | - |
| 20y | - |
| 21 | <Practice.name> |
| 22 | <Practice.address1> |
| 23 | <Practice.address2> |
| 24 | <Practice.address3> |
| 25 | <PracticePostCode> |
| 26 | <Practice.phone.number> |
| 27 | <Patient.first.name> |
| 28 | <Patient.second.name> |
| 29 | <Patient.Address1> |
| 30 | <Patient.Address2> |
| 31 | <Patient.Address3> |
| 32 | <Patient.Postcode> |
| 33 | <Patient.DOB> |
| 33d | - |
| 33m | - |
| 33y | - |
| 34 | <UniqueID> |
| 35 | <Issuer's.name> |
| 36 | <Issuer's.profession> |

## Documentation

- Data Provision Notice
- Information Standard Notification (SCCI2118 Amd 65/2015)
- Updated GP guidance (March 2013) Getting the most out of the fit note – a guide for GP

# Capability

**Applicable Capability**

All supplier Solutions will need to meet this Standard if they are delivering the Recording Consultations - GP Capability.

# Roadmap

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [EMED3-v2-7 - Rev 2.txt](../../../../.raw/DCSDCS/attachments/12288688132/att12288262247-EMED3-v2-7 - Rev 2.txt)
- [EMED3-v2-7 SCHEMA Rev 1.txt](../../../../.raw/DCSDCS/attachments/12288688132/att12288688155-EMED3-v2-7 SCHEMA Rev 1.txt)
- [eMED3 Template (2022) with Mappings.pdf](../../../../.raw/DCSDCS/attachments/12288688132/att12288688158-eMED3 Template (2022) with Mappings.pdf)
- [eMED3 Template (2022).pdf](../../../../.raw/DCSDCS/attachments/12288688132/att12288688161-eMED3 Template (2022).pdf)
- [eMED3 - Templatewithmapping.pdf](../../../../.raw/DCSDCS/attachments/12288688132/att12288688164-eMED3 - Templatewithmapping.pdf)
- [Annex 1 Med3 Master Final 080317.pdf](../../../../.raw/DCSDCS/attachments/12288688132/att12288688167-Annex 1 Med3 Master Final 080317.pdf)
- [eMED3-v2-4 SCHEMA.txt](../../../../.raw/DCSDCS/attachments/12288688132/att12288688170-eMED3-v2-4 SCHEMA.txt)
