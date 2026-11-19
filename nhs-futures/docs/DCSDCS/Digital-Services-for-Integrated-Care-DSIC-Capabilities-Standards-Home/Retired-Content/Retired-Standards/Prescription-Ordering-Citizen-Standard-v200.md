---
page_id: "1754333540"
space: "DCSDCS"
title: "Prescription Ordering - Citizen - Standard v2.0.0"
version: 2
updated: "2021-08-03T12:43:00.312Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1754333540/Prescription+Ordering+-+Citizen+-+Standard+v2.0.0"
labels: ["capability_specific_retired"]
---

# Prescription Ordering - Citizen - Standard v2.0.0

|  |  |
| --- | --- |
| ID | S3 |
| Version | 2.0.0 |
| Type | Capability Specific Standard |
| Status {#PrescriptionOrdering-Citizen-Standardv2.0.0-Status} | Retired |
| Effective Date {#PrescriptionOrdering-Citizen-Standardv2.0.0-EffectiveDate} | 31 Jul 2020 |

# Requirements {#PrescriptionOrdering-Citizen-Standardv2.0.0-Requirements}

| Epic Mapping | Requirement ID | Requirement Text | Level |
| --- | --- | --- | --- |
| C3E1 | **GP-SPFS-5.2.2-02A** | **Prescription Management - Repeat Prescription Requests - Patient**  Allow Patients to view, request, and cancel outstanding (unactioned) requests for repeat Prescription medications (including repeat dispensing). Patients to have the ability to:   - View all medications currently available for a repeat Prescription or repeat dispensing Prescription including:   - Name, Strength (where applicable), Form (e.g. tablets), Dose (where applicable), Most recent issue date, duration, suggested date of next issue (if applicable)   - Date & status of last request including associated free text (free text to display only when the request originated from Citizen Services)   - Which medications are due for a review, including the expected review date, if applicable - Select and request one or multiple Prescription medications - Cancel unactioned requests   See Prescribing - Standard for information on recording medication | MUST |
| C3E6 | **GP-ORPR-4** | **Prescription Management - Repeat Prescription Requests - Proxy**  Allow Proxies to view, request, and cancel outstanding (unactioned) requests for repeat Prescription medications (including repeat dispensing) for the Patient. Proxies to have the ability to:   - View all medications currently available for a repeat Prescription or repeat dispensing Prescription including:   - Name, Strength (where applicable), Form (e.g. tablets), Most recent issue date, duration, suggested date of next issue (if applicable)   - Date & status of last request including associated free text (free text to display only when the request originated from Citizen Services)   - Which medications are due for a review, including the expected review date, if applicable - Select and request one or multiple Prescription medications - Cancel unactioned requests   See Prescribing - Standard for information on recording medication | MUST |
| C3E1 | **GP-SPFS-5.2.2-02B** | **Prescription Management - Repeat Prescription Requests - Free Text - Patient**  Allow Patients to optionally add 'free text' to accompany   - Each Prescription medication item being requested - The overall Repeat Prescription request - The cancellation of a Prescription medication item - The cancellation of the overall Prescription request | MUST |
| C3E6 | **GP-ORPR-5** | **Prescription Management - Repeat Prescription Requests - Free Text - Proxy**  Allow Proxies to optionally add 'free text' to accompany   - Each Prescription medication item being requested - The overall Repeat Prescription request - The cancellation of a Prescription medication item - The cancellation of the overall Prescription request | MUST |
| C3E1 | **GP-ORPR-2.01** | **Prescription Management - Unable to request pre-authorised repeats - Patient**  Patients will not be able to request repeat Prescription medications which have outstanding pre-authorised future issues (e.g. a repeatable Prescription - see GP-07.10-011) | MUST |
| C3E6 | **GP-ORPR-6** | **Prescription Management - Unable to request pre-authorised repeats - Proxy**  Proxies will not be able to request repeat Prescription medications which have outstanding pre-authorised future issues (e.g. a repeatable Prescription - see GP-07.10-011) | MUST |
| C3E4 | **GP-SPFS-5.2.2-03A** | **Prescription Management - Acute Prescription Requests -Patient**  Allow Patients to view, request, amend and cancel outstanding requests for Acute Prescription medications. (see GP-07.23-05). | MAY |
| C3E9 | **GP-ORPR-7** | **Prescription Management - Acute Prescription Requests - Proxy**  Allow Proxies to view, request, amend and cancel outstanding requests for Acute Prescription medications for the Patient (see GP-07.23-05). | MAY |
| C3E4 | **GP-SPFS-5.2.2-03B** | **Prescription Management - Acute Prescription Requests - Free Text - Patient**  Allow Patients to optionally add 'free text' to accompany   - Each Acute Prescription medication item being requested - The overall Acute Prescription request - The cancellation of a Prescription medication item - The cancellation of the overall Acute Prescription request | MAY |
| C3E9 | **GP-ORPR-8** | **Prescription Management - Acute Prescription Requests - Free Text -Proxy**  Allow Proxies to optionally add 'free text' to accompany   - Each Acute Prescription medication item being requested - The overall Acute Prescription request - The cancellation of a Prescription medication item - The cancellation of the overall Acute Prescription request | MAY |
| C3E1, C3E4 | **GP-SPFS-5.2.2-04** | **Prescription Management - Request Notification - Patient**  Upon successful submission of the Prescription request, Patients will be informed of the collection approach for their request. For example,   - Where the Patient is participating in EPS, Patients to be notified that the requested Prescription will be sent to the Patient's nominated pharmacy.   - If the Prescription medication being requested is not available via EPS, Patients will be informed that the Prescription will need to be collected. | MUST |
| C3E6, C3E9 | **GP-ORPR-9** | **Prescription Management - Request Notification - Patient**  Upon successful submission of the Prescription request, Proxies will be informed of the collection approach for their request. For example,   - Where the Patient is participating in EPS, Proxies to be notified that the requested Prescription will be sent to the Patient's nominated pharmacy.   - If the Prescription medication being requested is not available via EPS, Patients will be informed that the Prescription will need to be collected. | MUST |
| C3E2 | **GP-SPFS-5.2.2-05A** | **Prescription Management - EPS Nominated Pharmacy - View - Patient**  Allow Patients to view their EPS nominated pharmacy where the Patient is already participating in EPS. | MUST |
| C3E7 | **GP-ORPR-10** | **Prescription Management - EPS Nominated Pharmacy - View - Proxy**  Allow Proxies to view the Patient's EPS nominated pharmacy where the Patient is already participating in EPS. | MUST |
| C3E2 | **GP-SPFS-5.2.2-05B** | **Prescription Management - EPS Nominated Pharmacy - Amend/Cancel -Patient**  Allow Patients to:   - Amend the Patient's EPS nominated pharmacy, by selecting from a list of all pharmacies participating in EPS   - Immediately notify the Citizen that future Prescriptions will be sent to the Patient's new EPS nominated pharmacy. Citizens can select to:     - Continue to amend. Update Patient's nominated Pharmacy on the NHS Spine and indicate to the Practice that the Patient's EPS nominated pharmacy has been amended - Cancel the request at this point. EPS nominated pharmacy to continue as before. Remove/delete the Patient's EPS nominated pharmacy,   - Immediately notify the Citizen that Prescriptions will no longer be sent to the Patient's EPS nominated pharmacy.   A Patient will be able to change EPS nominated pharmacy without requiring any action by the Practice.  Any such selection to result in the Patient being automatically notified via their preferred Verified Contact Details. | MUST |
| C3E7 | **GP-ORPR-11** | **Prescription Management - EPS Nominated Pharmacy - Amend/Cancel**  Allow Proxies to:   - Amend the Patient's EPS nominated pharmacy, by selecting from a list of all pharmacies participating in EPS   - Immediately notify the Citizen that future Prescriptions will be sent to the Patient's new EPS nominated pharmacy. Citizens can select to:     - Continue to amend. Update Patient's nominated Pharmacy on the NHS Spine and indicate to the Practice that the Patient's EPS nominated pharmacy has been amended - Cancel the request at this point. EPS nominated pharmacy to continue as before. Remove/delete the Patient's EPS nominated pharmacy,   - Immediately notify the Citizen that Prescriptions will no longer be sent to the Patient's EPS nominated pharmacy.   A Proxy will be able to change EPS nominated pharmacy without requiring any action by the Practice.  Any such selection to result in the Proxy being automatically notified via their preferred Verified Contact Details. | MUST |
| C3E3 | **GP-ORPR-3.01** | **Prescription Management - **Preferred** Pharmacy - View - Patient**  Allow Patients to view their Preferred Pharmacy where the Patient is NOT participating in EPS.  See GP-07.3-06 for recording Preferred Pharmacy | MAY |
| C3E8 | **GP-ORPR-12** | **Prescription Management - **Preferred** Pharmacy - View - Proxy**  Allow Proxies to view the Patient's Preferred Pharmacy where the Patient is NOT participating in EPS.  See GP-07.3-06 for recording Preferred Pharmacy | MAY |
| C3E3 | **GP-ORPR-3.02** | **Prescription Management - Preferred Pharmacy - Amend/Cancel - Patient**  Allow Patients to amend their Preferred Pharmacy, by selecting from a list of pharmacies (sourced from ODS and as defined by the Practice - See GP-07.3-06).  Option will only be available if the Patient is NOT participating in EPS and will not change the Patient’s Nominated Pharmacy. | MAY |
| C3E8 | **GP-ORPR-13** | **Prescription Management - Preferred Pharmacy - Amend/Cancel - Proxy**  Allow Proxies to amend the Patient's Preferred Pharmacy, by selecting from a list of pharmacies (sourced from ODS and as defined by the Practice - See GP-07.3-06).  Option will only be available if the Patient is NOT participating in EPS and will not change the Patient’s Nominated Pharmacy. | MAY |

# Capability {#PrescriptionOrdering-Citizen-Standardv2.0.0-Capability}

**Applicable Capability**

All supplier Solutions will need to meet this Standard if they are delivering the Prescription Ordering – Citizen Capability

# Roadmap {#PrescriptionOrdering-Citizen-Standardv2.0.0-Roadmap}

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |