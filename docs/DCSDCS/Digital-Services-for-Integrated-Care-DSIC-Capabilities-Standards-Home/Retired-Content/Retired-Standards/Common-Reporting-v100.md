---
page_id: "10612277445"
space: "DCSDCS"
title: "Common Reporting v1.0.0"
version: 1
updated: "2020-12-31T11:17:19.935Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/10612277445/Common+Reporting+v1.0.0"
labels: ["context_specific_retired"]
---

# Common Reporting v1.0.0

|  |  |
| --- | --- |
| ID | S22 |
| Version | 1.0.0 |
| Type | Context Specific Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

# Description

Supports the reporting needs that are common to General Practices and includes searchable report templates.

Common Reporting functionality allows an Organisation to collate and organise data to support the monitoring of activity and produce inputs into other processes, such as producing targeted communications for a Patient list. The Common Reporting Standard will allow any structured data within Solutions to be extractable and reportable, supporting all of an Organisations' local, regional and national Reporting requirements.

Search Criteria functionality is required to be flexible, allowing it to be used in support of both the ad-hoc identification of information and Patient Records, and the creation of regular reports and inputs into other processes. After Search Criteria are defined this can be saved for future use to create further reports and defined reports can be scheduled to run at predefined times and repeat at user defined intervals. Search Results are the data items/records that meet a particular Search Criteria when a Search is performed. Search Results will be able to be saved for future use, including as input into other processes .

A report can be a summary view of Search Results, that can include aggregate information such as numbers or percentages calculated from the Search Results, or the detailed list of Search Results that would likely include Patient identifiable information.

Reporting functionality will be used to report on the clinical care, performance and activity of individual Patients. It will provide Organisations with the ability to define and manage locally defined reports. This includes Supplier defined reports to support known standard Reporting requirements; as well as reacting to evolving Reporting Requirements to support public health directives and initiatives as defined by NHS England.

# Requirements

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| GP-11.1-01 | **Define Search Criteria**  Use all/any combination of coded or structured data held within or linked to the Patient Record as Search Criteria.   - Enter future and/or historical dates into Search Criteria e.g. allowing ability to search for future Appointments or Patients born in a certain year - Enter Defined time periods to report on (hours, days, weeks, months) - Allow Users to explicitly indicate that they wish to include deceased and/or Inactive Patients within Search Results where the Patient Record meets Search Criteria. Where the output can include sensitive data for Patients with whom a User has no Legitimate Relationship, the reason selected for accessing these records (as specified in Information Governance standard) shall be applied to all affected Patients in a single step - Allow Users to enter data as Search Criteria that is deemed to be inactive and possibly prevented from ongoing data entry into a Patient record i.e. search on a previously active term | MUST |
| **CR-01** | **Synthetic Patients**  Allow Users to explicitly indicate that they wish to include synthetic Patients within search results where the Patient Record meets Search Criteria (default to exclude synthetic records).  Where a patient or data about a synthetic patient is included, this will be clearly indicated in search results. | MAY |
| **GP-11.3-06** | **Reporting by Age/Sex**  Ability to generate Patient-based reports on Age/Sex analysis (number of Patients falling within User-definable age/Sex bands) | MUST |
| GP-11.1-02 | **Save Search Criteria**  Save Search Criteria, allocating a User-defined name   - Allow saved search criteria to be re-used/re-run | MUST |
| **GP-11.1-04** | **SNOMED CT Reporting**   All searching and reporting functionality will be specified in the SNOMED CT hierarchy where appropriate. Existing reports will need to provide correct results after the introduction of new content  captured using SNOMED CT, and new reports need to operate correctly over historic data even when specified in SNOMED CT. This will include but is not limited to:   - eMed3 - QOF - Practice reports - National audits - National screening   See Data Standards and SNOMED CT for further information | MUST |
| **GP-11.3-07** | **Temporary/local Clinical Terms Reporting**  Ability to generate a Patient-based report on Temporary/local Clinical Terms as per SNOMED CT (list of Patients who have an active temporary or local term within their Patient Record, by Clinical Term)  See Data Standards for Temporary/local Clinical terms definition. | MUST |
| GP-11.2-01 | **Generate Search Results**  Generate Search Results by applying a Search Criteria to Patient Records   - Display these results in a list containing a subset of data items from the Patient Record – Practice to define this subset from all structured data items | MUST |
| GP-11.2-02 | **Save Search Results**  Save Search Results, allocating a User-defined name   - Allow saved search results to be re-used/re-accessed | MUST |
| GP-11.2-04 | **Use Search Results**  Use Search Results   - Access/view selected Patient Record - Produce communication – individual and/or batch | MUST |
| GP-11.3-01 | **Report Templates**  Define, amend and delete report templates. Each template will need to have as a minimum:   - Unique identifier and/or name - Version | MUST |
| GP-11.3-02 | **Generate Report**  Create/generate a report by applying a locally defined report template to the results of Search Criteria – a report can be a summary view of Search Results or detailed Search Results list.  Users will have the ability to:   - Preview report - Navigate to Search Results i.e. see individual Patient Records that contribute to report content - Save report allocating a User-defined name, for future reference - Re-run report (for same or different date ranges) - Run a report adhoc - Print report - Schedule the automated running of reports at a specified date/time | MUST |
| GP-11.3-05 | **Create/Save report from default template**  Modify/customise standard reports and save as own report template | MUST |
| **GP-11.3-08** | **Identify where Patient is included/excluded for each criteria **in a report****  Ability for Users to identify at what point of the specified report criteria a Patient has been included or excluded (even if they are excluded from the overall report results).  For example, for a report with three specified criteria, indicate for a Patient the reason why they were included or excluded for each criterion. | MAY |
| **GP-11.3-09** | **Identify why Patient is included **for each criteria**in a report**  Ability for Users to identify the reason why a Patient has been included based on the specified report criteria (e.g. the relevant SNOMED code was recorded).  For example, for a report with three specified criteria, indicate for a Patient the reason why they were included or excluded for each criterion. | MAY |
| **GP-11.3-10** | **Show results using most up to date Patient Record data**  For GP-11.3-08, depending on the reporting mechanism, the data used for reporting might not match the data in the Patient Record at the time of running a report. In this case, Users will have the ability to see the results of GP-11.3-08 using the most up to date data from the Patient Record. | MAY |
| **GP-AP-4.6-05** | **Reporting - Export**  Export reports to formats which can be opened in:   - Microsoft Excel - Microsoft Word - PDF | MUST |
| **GP-DS-2.2-4** | **Report Access**  The service will allow Users to create reports to be accessed by and used across a group of Users | MUST |
| **GP-DS-2.2-5** | **Sharing of Reports**  The service will allow Users to share reports and report criteria within and across external organisations with the ability to anonymise the reports where appropriate. | MUST |
| **GP-DS-2.2-6** | **Provide Analytics**  Provide ability to perform analytics or be capable of providing data to other systems that perform analysis. | MUST |
| **RAVE-APU-PR-009** | ******Practice Reporting - Interrogate data******  Have the ability to interrogate data to analyse Patient trends by:   - Viewing a list of Patients who meet defined criteria ([GP-11.1-01](Common-Reporting-v100.md)) - Drilling down to a Patient level data | MUST |
| **RAVE-APU-PR-010** | ******Practice Reporting - Interrogate data - Clinician level******  Have the ability to interrogate data to analyse professional/clinician trends by:   - Drilling down to an individual Staff Member level AND/OR Health and Care Professional type level - Health and Care Professional type to be as defined in the Solution (see Healthcare Professional Types) | MUST |
| **RAVE-APU-PR-015** | ******Practice Reporting - View trends******  Have the ability to compare performance by:   - Viewing results for a day, week, month and year - AND/OR selecting a specific date/time period - This will include the ability to view historic and future data - The User can compare data over a time period e.g. the number of DNA’s each day over a week. | MUST |
| **RAVE-APU-PR-017** | ******Practice Reporting - Individual/combined data items******  Identify and analyse trends by reporting on information items individually and in any specified combination | MAY |
| **RAVE-APU-PR-018** | ******Practice Reporting - Select/sort/filter report information******  Have the ability to select, filter and sort the information items included in a report to assist in analysis of data | MAY |
| **GP-11.3-11** | **Access Patient Record**  Access a Patient Record where a Patient has been successfully identified, linked, listed or otherwise presented to the user. | MUST |

# Capabilities

**Applicable Capabilities**

All supplier Solutions delivering one or more of the of the following Capabilities will need to meet this Standard:

##### Filter by label

There are no items with the selected labels at this time.

# Roadmap

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |