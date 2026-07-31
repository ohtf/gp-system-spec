---
page_id: "12417400882"
space: "DCSDCS"
title: "GP Extracts Verification v1.0.1"
version: 1
updated: "2023-05-22T11:23:32.923Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12417400882/GP+Extracts+Verification+v1.0.1"
labels: ["capability_retired"]
---

# GP Extracts Verification v1.0.1

|  |  |
| --- | --- |
| ID | C10 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - GP IT Futures - Tech Innovation |

Full Capability status only. For this Capability, Solutions are required to meet all MUST EPICs and associated acceptance criteria.

# Description

Aggregated data is extracted from GP Practices via the General Practice Extraction Service (GPES) and sent to the Calculating Quality Reporting Service (CQRS), both operated by NHS Digital. Calculations performed by the CQRS determine how much money a GP Practice should be paid for National Services.

The data extracted in this process is based on information recorded in individual Patient Records. The GP Extracts Verification Capability provides Practices with reports and search tools to establish which Patients will be or have/have not been included in these payment extracts and calculations. These reports and tools will ultimately support data quality investigations and improvements.

# Outcomes

|  |  |
| --- | --- |
| For General Practice: | Staff can verify that the information to be extracted or that was extracted to support payment is accurate. This helps the Practice ensure that the data used for calculations is correct and that they receive the correct payments. |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C10E1 - view GPES payment extract reports

As a Practice User

I want to view reports for national GPES payment extractions

So that I can identify included and excluded patients

#### Acceptance criterion 1: view future GPES payment extract reports

Given the Practice User is permitted to view GPES payment extract reports

When the Practice User chooses to view a future GPES payment extract report

Then the GPES payment extract report is displayed

#### Acceptance criterion 2: view previous GPES payment extract reports

Given the Practice User is permitted to view GPES payment extract reports

When the Practice User chooses to view a previous GPES payment extract report

Then the GPES payment extract report is displayed

#### Acceptance criterion 3: view a GPES payment extract reports for a Patient

Given the Practice User is permitted to view GPES payment extract reports

When the Practice User chooses to view a GPES payment extract report for a Patient

Then the reason for inclusion or exclusion is displayed

**MAY Epics - All May Epics and Acceptance Criteria will be evaluated during the Capability Assessment Stage of On-boarding. However, these Epics are not mandatory and will not be used as part of the overall assessment of whether the Capability is fully met. Any May Epics that are assessed as met will be available to buyers via the Buying Catalogue.**

### C10E2 - view national GPES non-payment extract reports

As a Practice User

I want to view reports for national GPES non-payment extractions

So that I can identify included and excluded patients

#### Acceptance criterion 1: view future GPES non-payment extract reports

Given the Practice User is permitted to view GPES non-payment extract reports

When the Practice User chooses to view a future GPES non-payment extract report

Then the GPES non-payment extract report is displayed

#### Acceptance criterion 2: view previous GPES non-payment extract reports

Given the Practice User is permitted to view GPES non-payment extract reports

When the Practice User chooses to view a GPES non-payment extract report

Then the GPES non-payment extract report is displayed

#### Acceptance criterion 3: view a GPES non-payment extract reports for a Patient

Given the Practice User is permitted to view GPES non-payment extract reports

When the Practice User chooses to view a GPES non-payment extract report for a Patient

Then the reason for inclusion or exclusion is displayed

**Capability Specific Standards**

Suppliers will have to attain compliance with this Standard during the compliance stage before they can be live on a framework with this Capability:

- GP Extracts Verification - Standard v1.0.2
**Other Applicable Standards**

Suppliers will also have to attain compliance with these additional standards during the compliance stage before they can be live on a framework with this capability:

- Interoperability Standard
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |