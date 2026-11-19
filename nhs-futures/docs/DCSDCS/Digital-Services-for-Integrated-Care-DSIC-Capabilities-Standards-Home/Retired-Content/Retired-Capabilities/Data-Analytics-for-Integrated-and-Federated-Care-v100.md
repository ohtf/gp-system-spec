---
page_id: "1695613032"
space: "DCSDCS"
title: "Data Analytics for Integrated and Federated Care v1.0.0"
version: 2
updated: "2020-01-15T16:28:44.366Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1695613032/Data+Analytics+for+Integrated+and+Federated+Care+v1.0.0"
labels: ["capability_retired"]
---

# Data Analytics for Integrated and Federated Care v1.0.0

|  |  |
| --- | --- |
| ID | C26 |
| Version | 1.0.0 |
| Type | Capability |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Description}

Data Analytics for Integrated and Federated Care delivers the ability to combine, or link, and then report against structured datasets and then present the results to underpin (secondary uses of the data such as) service and performance management, decision-making around services and resource usage, action planning, alerting / issue management and forecasting.

Subject to the correct data sharing agreements being in place, the Data Analytics Capability enables reporting against datasets from systems within the Integrated/Federated Care Setting (e.g. GP clinical systems or systems holding information relating to budgets, spend, drug costs, etc.) It also allows reporting on data from other sources: national (e.g. HES, ePACT2, QOF, GPES); and local (e.g. other care providers in the area).

Users can run existing or create new reports as required, creating output at different levels (e.g. Practice, Integrated/Federated Care Setting, CCG or postcode area) and presenting the results according to the needs of the audience (e.g. as reports, aggregated figures or via dashboards).

The Data Analytics Capability supports analysis of data from different systems or sources (e.g. Patient, prescribing, Appointments, financial, workforce). Practices and Integrated/Federated Care Setting (Federations) can use this data, for example, to:

- Maximise the use of current resources
- Assess future resource needs
- Plan and manage Patient care
- Benchmark and track performance
- Underpin decision-making

# Outcomes {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Outcomes}

|  |  |
| --- | --- |
| Patients/Service Users | - Confident that, where they are happy with its use, their data contributes to improved Patient care, better use of resources and issue identification |
| Managers | - Can use data analysis to support decision making relating to Patient care as well as resource utilisation based on accurate and comprehensive reporting - Can access more powerful analysis of their data through combination of data from multiple sources - Can access new and more complex analyses of their data |
| Integrated and Federated Care Settings | Integrated and Federated groups of Practices have the ability to track and optimise resource usage for example:   - Appointment utilisation (e.g. unused slots) and - where data is available - utilisation type - The relationship between Practice spend (e.g. on particular drugs or drug groups) and outcomes (e.g. hospital admissions) - Data integrity and identify data quality issues - Inconsistencies in clinical coding or the recording of data - Effectiveness of screening programmes   In addition, they can:   - Gain efficiencies relating to provision of data for national returns to national Organisations - Understand the performance of the Federation (and its constituent Practices) - Gain efficiencies from being able to report at Federation level rather than multiple reporting streams at Practice level - Grow expertise in analysis and reporting at Federation level that can be propagated to or shared with Practices |
| CCGs | - Have the ability to track performance in their area against local and national benchmarks |
| Authorised Research Organisations | - Have access to large pseudonymised or anonymised datasets for research and population health management, subject to the correct controls and data sharing agreements being in place |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### EpicDA1 - analyse data across multiple organisations within the Integrated/Federated Care Setting (Federation) {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-EpicDA1-analysedataacrossmultipleorganisationswithintheIntegrated/FederatedCareSetting(Federation)}

As an Analyst

I want to combine or link equivalent, structured data from multiple Organisations within the Federation

So that I can identify trends and track performance across the Federation

#### Acceptance criterion 1: report across Practices within the Federation {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion1:reportacrossPracticeswithintheFederation}

Given that structured data of a type (e.g. Appointment attendance data) is available from multiple Practices within the Federation

And a report has been configured to meet the reporting need (e.g. analysis of Appointment Did Not Attend by Practice)

When the report is run

Then data relating to each Practice will be output

And data can be aggregated or summarised by Practice

And the data for a Practice can be compared to data from other Practices

---

### EpicDA2 - analyse data across different datasets {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-EpicDA2-analysedataacrossdifferentdatasets}

As an Analyst

I want to combine or link structured data relating to different types of activity within the Federation (e.g. Patient, prescribing, Appointments, financial, workforce)

So that I can create richer or more complex metrics against which to track performance across the Federation

#### Acceptance criterion 1: report across Practices within the Federation {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion1:reportacrossPracticeswithintheFederation.1}

Given that structured data of different types is available from Practices within the Federation or Organisations external to the Federation

And a report has been configured to meet the reporting need (e.g. to identify trends such as the relationship between the timing of home visits and subsequent A&E attendance)

And there is a means to link datasets

When the report is run

Then data across the datasets will be linked

And data will be output according to the design of the report

---

### EpicDA3 - create new or update existing reports  {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-EpicDA3-createneworupdateexistingreports}

As an Analyst

I want to be able to create or update reports

So that I can respond to new or updated reporting requirements

#### Acceptance criterion 1: create report in response to new reporting requirement {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion1:createreportinresponsetonewreportingrequirement}

Given access permissions allow the creation of new reports

When a new reporting requirement is identified

Then a new report can be created to meet the requirement

And the new report be can saved for future use with a name or identifier defined by the Analyst

#### Acceptance criterion 2: update report in response to new reporting requirement {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion2:updatereportinresponsetonewreportingrequirement}

Given there is a library of existing reports

And access permissions allow the update of existing reports

When a new reporting requirement is identified

Then an existing report can be updated to meet the requirement

And the new report be can saved for future use with a name or identifier defined by the Analyst

---

### EpicDA4 - run existing reports {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-EpicDA4-runexistingreports}

As an Analyst

I want to be able to access and run an existing report

So that I can perform regular reporting and analysis in the most efficient way

#### Acceptance criterion 1: run existing report {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion1:runexistingreport}

Given there is a library of existing reports

When reporting is triggered (e.g. receipt of new data)

Then the Analyst can access and run the existing report

And output the results according to the existing report design

#### Acceptance criterion 2: report template shared by report creator with another user {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion2:reporttemplatesharedbyreportcreatorwithanotheruser}

Given there is a library of existing reports

And the security model defines the functions and data that are allowed to each user

And access permissions allow the sharing of report templates by the report template creator

And the other user is an authorised user of the tool and data

When the report template is shared with a user

Then the report template can be run by the other user

And the results are output

And the results are constrained to the data allowed by the security model

#### Acceptance criterion 3: schedule report to run {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion3:schedulereporttorun}

Given there is a library of existing reports

And a reporting schedule is defined for the report (e.g. regular reporting cycle such as month end)

When the Analyst defines the times and intervals at which the report will be run

Then the report is run at the defined times and intervals

And the results can be output according to the existing report design

---

### EpicDA5 - present output {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-EpicDA5-presentoutput}

As an Analyst

I want to be able to present the output of reporting and analysis in a variety of ways

So that I can best tailor the output to the audience and purpose of the reporting

#### Acceptance criterion 1: create detailed report {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion1:createdetailedreport}

Given that the audience requires access to the report detail (e.g. list of Patients with a condition to enable planning, report of referrals and test requests)

And access to the detail of the report is appropriate for the audience

When the report is run

Then the detail output is retrieved according to the design of the report

And the detailed output can be presented to the audience (e.g. as a list, table or other)

#### Acceptance criterion 2: create aggregated report {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion2:createaggregatedreport}

Given the audience for the report require aggregated information (e.g. counts of Patients with a condition across the Federation or counts of Appointment 'Did Not Attend' by Practice)

And a report has been previously created and configured to meet the reporting requirement

When the report is run

Then the output is aggregated or summarised according to the design of the report

And the aggregated output can be presented to the audience (e.g. as a table)

#### Acceptance criterion 3: output to dashboard or similar visual representation of the data {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion3:outputtodashboardorsimilarvisualrepresentationofthedata}

Given that the audience want to receive to receive multiple types of data presented visually (e.g. to track performance over time and receive alerts)

And a report or set of reports have been previously created and configured to meet the reporting requirement

And the layout of the dashboard has been designed

When the report or set of reports is run

Then the data is output to the dashboard

And is presented to the audience according to the design of the dashboard

#### Acceptance criterion 4: output in a format allowing the data to be shared {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion4:outputinaformatallowingthedatatobeshared}

Given that the audience want to receive to receive the output of queries in a variety of shareable formats

And a report has been previously created and configured to meet the reporting requirement

When the report is run

Then the report output or results can be exported in the format defined by the user

And the results can be saved to a location defined by the user, external to the Data Analytics Capability

---

### EpicDA6 - define selection rules on reports {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-EpicDA6-defineselectionrulesonreports}

As an Analyst

I want to define selection criteria for my reports

So that I can fine-tune my reports to identify only those records that positively or negatively match the selection criteria (e.g. Patients, Appointments, prescriptions, activity during particular time periods, etc.)

#### Acceptance criterion 1: identify activity or conditions on records {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion1:identifyactivityorconditionsonrecords}

Given a report has been configured to identify values on a record (e.g. referral activity, a particular condition or diagnosis, missing NHS number or activity that occurs within or outside particular date ranges)

When the report is run

Then only those records with matching values are displayed

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### EpicDA7 - create and run performance-based reports {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-EpicDA7-createandrunperformance-basedreports}

As an Analyst

I want to define and report against performance targets (e.g. profit-analysis per Practice, A&E attendances per 1000 population, % medicines review completed)

So that I can track performance across the Federation

#### Acceptance criterion 1: bench-marking {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion1:bench-marking}

Given that performance data of a type (e.g. Patient/Service User feedback metrics) is available from multiple Practices within the Federation

And a benchmark performance level (e.g. target feedback ratings) has been defined across the Federation

And a report has been configured to meet the reporting need

When the report is run

Then performance data for each Practice will be output compared to the benchmark level for the Federation

---

### EpicDA8 - drill down to detailed information {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-EpicDA8-drilldowntodetailedinformation}

As a Clinician or Clinical Lead

I want to be able to drill-down from summary information to detailed Patient/Service User records

So that I can identify Patients/Service Users requiring a follow-up or intervention (e.g. book a follow-up Appointments or test)

#### Acceptance criterion 1: drill-down to detail held in an integrated Patient-record system {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion1:drill-downtodetailheldinanintegratedPatient-recordsystem}

Given that a summary level report has been run (e.g. list of Patients with test results)

And the Data Analytics Capability has been integrated with or linked to the Patient-record system

And the security model allows the user access to Patient-level information within the Patient-record system

When Patients/Service Users requiring a follow-up or intervention are identified (e.g. Patients/Service Users with test results outside a normal range)

Then the Clinician can drill-down to view the underlying detailed data (e.g. Patient record) in the integrated Patient-record system

---

### EpicDA9 - forecasting {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-EpicDA9-forecasting}

As an Analyst

I want to use past or current data to forecast or model future demand

So that I can use this to support effective decision-making and planning

#### Acceptance criterion 1: model future demand {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion1:modelfuturedemand}

Given that past or current data is available (e.g. in relation to Appointment use)

And parameters or rules can be defined regarding future use

When the report is run

Then future demand is modelled

---

### EpicDA10  - enable reporting at different levels {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-EpicDA10-enablereportingatdifferentlevels}

As an Analyst

I want to determine the level of Organisational or geographical reporting (e.g. Practice, CCG or Federation level; postcode sector)

So that I can report flexibly according to perspectives on the data

#### Acceptance criterion 1: determine organisation level for reporting {#DataAnalyticsforIntegratedandFederatedCarev1.0.0-Acceptancecriterion1:determineorganisationlevelforreporting}

Given that data of a type is available from multiple Practices within the Federation

And there are audiences wanting output at different Organisational levels

And the data allows the identification of different reporting levels

And the report has been configured to determine the reporting level

When the report is run

Then data is output at the reporting level (e.g. Practice or CCG) according to the report design

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