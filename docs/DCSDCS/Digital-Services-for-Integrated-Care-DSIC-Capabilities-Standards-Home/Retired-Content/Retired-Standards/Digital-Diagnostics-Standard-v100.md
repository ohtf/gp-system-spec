---
page_id: "1680048864"
space: "DCSDCS"
title: "Digital Diagnostics - Standard v1.0.0"
version: 3
updated: "2020-01-15T15:00:30.262Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1680048864/Digital+Diagnostics+-+Standard+v1.0.0"
labels: ["capability_specific_retired"]
---

# Digital Diagnostics - Standard v1.0.0

|  |  |
| --- | --- |
| ID | S8 |
| Version | 1.0.0 |
| Type | Capability Specific Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |

# Requirements

| Epic Mapping | Requirement ID | Requirement Text | Level |
| --- | --- | --- | --- |
| Epic 1 | **GP-08.3-01A** | **External services**  Support requests for investigation including:   - Pathology requesting - Radiology requesting | MUST |
| Epic 1 | **GP-08.3-01B** | **Further external services**  Support requests for investigation including:   - Electrocardiogram (ECG) - Electroencephalogram (EEG) - Echocardiogram (Echo) - Lung Function | MAY |
| Epic 1 | **GP-08.3-02A** | **External Services - Record request information within Patient Record**  Record the following request information within the Patient Record:   - Unique identifier - Date of request - Requestor – Staff Member detail   - This will include the ability to specify an alternative Staff Member requesting on behalf of a Clinician - Type/request item (as a coded clinical term) - Reason for the request - Sample type - Status - Laboratory identifier/code - Laboratory name   Auto populate data wherever possible (e.g. from data received via the Pathology/Radiology requesting Solution).  Where multiple request items are included within a single request e.g. a number of blood tests, the Solution will record the overall request and the individual detail within. | MUST |
| Epic 3 | **GP-08.3-02B** | **Record request for multiple Patients**  Have the ability to record a request (see GP-08.3-02A for request information) for multiple Patients. | MAY |
| Epic 4 | **GP-DIAG-05** | **External Services - Receive external request information - Pathology/Radiology requesting Solution**  Receive external request information from a Pathology/Radiology requesting Solution and consume all the data items provided.  Where a request includes multiple items, the Solution to receive and record the overall request and the individual detail within. | MAY |
| Epic 1 | **GP-DIAG-04** | **Reconcile results with requests**  Provide ability to reconcile request messages with the resulting reports to update the status of the request to indicate that results are available. Pathology/Radiology Request data items to be available when reconciling are:   - Unique identifier - Date of request - Requestor – Staff Member detail - Type/request item (as a coded clinical term) - Reason for the request - Sample type - Status - Laboratory identifier/code - Laboratory name | MUST |
| Epic 2 | **GP-DIAG-01** | **Service Requests Reporting**  Ability to generate a report based on Patient, Clinician or Practice for Service Requests.  This will be a list of service requests with associated status, by Requestor, by Recipient Target (Service, Organisation and/or Individual) within a date range. | MUST |

# Capability

**Applicable Capability**

All supplier Solutions will need to meet this Standard if they are delivering the Digital Diagnostics Capability

# Roadmap

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |