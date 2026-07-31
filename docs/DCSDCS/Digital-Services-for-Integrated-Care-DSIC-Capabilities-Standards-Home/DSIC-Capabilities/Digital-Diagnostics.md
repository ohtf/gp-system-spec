---
page_id: "1391133770"
space: "DCSDCS"
title: "Digital Diagnostics"
version: 16
updated: "2026-07-17T10:35:57.532Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133770/Digital+Diagnostics"
labels: ["capability"]
---

# Digital Diagnostics

|  |  |
| --- | --- |
| **ID** | C8 |
| **Version** | 1.0.2 |
| **Type** | Capability |
| **Category** | Care coordination |
| **Status** | Effective |
| **Effective Date** | 22 May 2023 |
| **Contracting Vehicle(s)** | - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

# Description

Supports the recording of Requests for Investigations information for Patients. Investigation results can also be received, reviewed and stored against the Electronic Patient Record (EPR).

# Outcomes

|  |  |
| --- | --- |
| For a Patient: | Improving the accuracy and speed of test requests and results between care settings leading to accurate diagnosis, shorter waiting times for Appointments and access to appropriate treatment. |
| For Healthcare Organisations: | Able to record, update and view details of all requests. Investigation results can be received, reviewed and stored against the Electronic Patient Record (EPR) ensuring up to date and relevant information is available to appropriate staff to support timely Patient care. |

|  |
| --- |
| **MUST Epics - Describes the minimum functionality required to deliver a Capability. Solutions MUST be successfully evaluated against each Epic and Acceptance Criteria via Capability Assessment in order to be associated with this Capability** |
| E00432 - manage Requests for Investigations information for Patients As a Health or Care Professional  I want to manage Requests for Investigations information for Patients  So that information relating to Requests for Investigations for Patients is managed Acceptance criterion 1: create Requests for Investigations information in the Patient’s Electronic Patient Record (EPR) Given the Health or Care Professional is permitted to manage Requests for Investigations information  When the Health or Care Professional selects to create a Request for Investigations information for a Patient  Then the Request for Investigations information is created in the Patient’s Electronic Patient Record (EPR)  And the date of the Request for Investigations is recorded  And the requestor is recorded  And the request type is recorded as a coded clinical term  And the reason for the request is recorded  And the sample type is recorded  And the laboratory name is recorded Acceptance criterion 2: view Request for Investigations information Given the Health or Care Professional is permitted to manage Requests for Investigations information  When the Health or Care Professional selects to view Request for Investigations information for a Patient  Then the Request for Investigations information is displayed Acceptance criterion 3: amend Request for Investigations information Given the Health or Care Professional is permitted to manage Requests for Investigations information  When the Health or Care Professional selects to amend Request for Investigations information for a Patient  Then the Request for Investigations information is amended Acceptance criterion 4: delete Request for Investigations information Given the Health or Care Professional is permitted to manage Requests for Investigations information  When the Health or Care Professional selects to delete Request for Investigations information for a Patient  Then the Request for Investigations information is deleted E00432 - Supporting Information  - Requests for Investigations are typically made using a separate Solution, but information about the request and that it has happened, needs to be recorded in the Patient’s Electronic Patient Record (EPR) - Examples of Requests for Investigations MAY include, but are not limited to:    - Pathology requests   - Radiology requests   - Electrocardiogram (ECG) requests   - Electroencephalogram (EEG) requests   - Echocardiogram (Echo) requests   - Lung Function requests - See [**Data Standards**](../DSIC-Standards/Overarching-Standards/Data-Standards.md) for further information on Clinical Codes and terms  ---  E00433 - Digital Diagnostics & Pathology Messaging As a Health or Care Professional  I want to view Investigation Results that have been received  So that the Investigation Results can support the delivery of Patient care Acceptance criterion 1: view Investigation Results Given that an Investigation Result has been received into the Healthcare Organisation  When the Health or Care Professional selects to view the Investigation Result  Then the Investigation Result is displayed E00433 - Additional Implementation Details Solutions MUST comply with the following when implementing this Epic:   - [**Digital Diagnostics & Pathology Messaging**](../DSIC-Standards/Non-Overarching-Standards/Digital-Diagnostics-Pathology-Messaging.md) Standard - [**Screening messaging**](../DSIC-Standards/Non-Overarching-Standards/Screening-Messaging.md) Standard |

|  |
| --- |
| **MAY Epics - Describes additional functionality associated with the Capability. Suppliers should consider all MAY Epics as part of their User Research. Suppliers can choose to map their Solutions to these Epics and they will be evaluated via Capability Assessment. Contracting Authorities or purchasing organisations may require these Epics as product qualification or requirements criteria** |
| E00434 - reconcile Investigation Results with Requests for Investigations information As a Health or Care Professional  I want to reconcile received Investigation Results with existing Requests for Investigations information  So that I can identify outstanding Requests for Investigations for Patients Acceptance criterion 1: reconcile Requests for Investigations with Investigation Results Given the Health or Care Professional is permitted to reconcile Investigation Results with Requests for Investigations information  And Investigation Results have been received for a Patient  When the Health or Care Professional selects to reconcile the Investigation Results with a Request for Investigations for the Patient  Then the Request for Investigations is reconciled with the Investigation Results E00434 - Supporting Information  - The data items available when reconciling Investigation Results with Request for Investigations information MAY include, but are not limited to:    - Date of request   - Requestor   - Request type, as a coded clinical term   - Reason for the request   - Sample type   - Laboratory name  - See [**Data Standards**](../DSIC-Standards/Overarching-Standards/Data-Standards.md) for further information on coded clinical terms  ---  E00435 - view Requests for Investigations information reports As a Health or Care Professional  I want to view Requests for Investigations information reports  So that I can see Request for Investigations activity Acceptance criterion 1: view Requests for Investigations information reports Given a Health or Care Professional is permitted to view Requests for Investigations information reports  When the Health or Care Professional selects to view a Requests for Investigations information report  Then the report results are displayed E00435 - Supporting Information  - Reports MAY be based on, but not limited to:    - Patients   - Health or Care Professionals   - Health or Care Organisations - The data included in reports MAY include, but is not limited to:    - Status   - Requestor   - Recipient Target (e.g. Service, Organisation and/or Individual)   - Date range  ---  E00436 - create Request for Investigations information for multiple Patients in a single action As a Health or Care Professional  I want to create Request for Investigations information for multiple Patients in a single action  So that I can create Request for Investigations information for multiple Patients more efficiently Acceptance criterion 1: create Request for Investigations information for multiple Patients in a single action Given a Health or Care Professional is permitted to manage Request for Investigations information for Patients  When the Health or Care Professional selects to create Request for Investigations information for multiple Patients in a single action  Then Request for Investigations information for multiple Patients is created   ---  E00437 - receive external Requests for Investigations information for Patients As a Health or Care Professional  I want to receive external Requests for Investigations information for Patients  So that Requests for Investigations information can be received from an external source Acceptance criterion 1: view external Requests for Investigations information for a Patient Given a Health or Care Professional is permitted to manage Request for Investigations information for Patients  And external Request for Investigations information has been received  When the Health or Care Professional selects to view the external Request for Investigations information  Then the external Request for Investigations information is displayed |

## Roadmap

Items on the Roadmap which impact or relate to this Capability

| Roadmap Item |
| --- |
| No content found. |