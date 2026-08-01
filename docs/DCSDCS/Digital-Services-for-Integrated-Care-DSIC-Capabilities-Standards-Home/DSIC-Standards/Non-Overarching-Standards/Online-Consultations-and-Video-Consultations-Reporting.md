---
page_id: "12526223418"
space: "DCSDCS"
title: "Online Consultations and Video Consultations Reporting"
version: 11
updated: "2026-07-22T13:10:40.849Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12526223418/Online+Consultations+and+Video+Consultations+Reporting"
labels: ["standard"]
---

# Online Consultations and Video Consultations Reporting

|  |  |
| --- | --- |
| **ID** | S97 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 05 May 2026 |
| **Contracting Vehicle(s)** | - [DFOCVC](https://nhse-dsic.atlassian.net/wiki/spaces/DFOCVCL) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

# Description {#OnlineConsultationsandVideoConsultationsReporting-Description}

The Online Consultations and Video Consultations Reporting Standard enables the collection and submission of data to the Authority inline with the Online Consultation / Video Consultation (OC/VC) extended data collection.

The Online Consultation / Video Consultation (OC/VC) extended data collection goal is to support understanding of demand and activity in general practice Accurate and timely capture of this data supports GP practices and local commissioners to plan and provide implementation support, as well as make more informed procurement decisions. Moreover, nationally it will help with understanding usage and shaping future policy.

# Requirements {#OnlineConsultationsandVideoConsultationsReporting-Requirements}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Applicable Contracting Vehicles** | **Requirement ID** | **Requirement Title** | **Requirement Text** | **Level** |
| All | **OCVCR1** | Submit Online Consultation and Online Patient/Patient Representatives Requests data | The Solution to submit Online Consultation and Online Patient Request data to the Authority, including the required data items specified in the Data Items Specification section, as per [Online and video consultation undertaken in general practice data collection](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/online-and-video-consultation-undertaken-in-general-practice). | MUST |
| All | **OCVCR2** | Submit Video Consultation data | The Solution to submit Video Consultation data to the Authority, including the required data items specified in the Data Items Specification section, as per [Online and video consultation undertaken in general practice data collection](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/online-and-video-consultation-undertaken-in-general-practice). | MUST |

## Data Items Specification {#OnlineConsultationsandVideoConsultationsReporting-DataItemsSpecification}

The [Online Consultation and Video Consultation data specification](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/online-and-video-consultation-undertaken-in-general-practice#data-specification) defines the data items in full, however Suppliers only need to submit the data items defined below.

### Online Patient Consultation and Online Patient Requests {#OnlineConsultationsandVideoConsultationsReporting-OnlinePatientConsultationandOnlinePatientRequests}

If the Supplier is offering the [Online Patient Consultation](../../DSIC-Capabilities/Online-Patient-Consultation.md) and [Online Patient Request](../../DSIC-Capabilities/Online-Patient-Request.md) Capabilities the data items below are required from Suppliers as part of the Online Consultation extended data collection.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Table** | **Field ID** | **Data Item** | **Description** | **Level** |
| Header | OCH\_VCH-001 | primary\_data\_collection\_supplier\_in\_use | Name of online consultation Supplier returning the data. | MUST |
| Header | OCH\_VCH-002 | reporting\_period\_start\_date | The reporting period start date to which this file refers. | MUST |
| Header | OCH\_VCH-003 | reporting\_period\_end\_date | The reporting period end date to which this file refers. | MUST |
| Header | OCH\_VCH-004 | date\_and\_time\_data\_set\_created | Date and time of VC submission start | MUST |
| Header | OCH\_VCH-005 | data\_set\_version\_number | The version number of a Data Set. | MUST |
| Header | OCH\_VCH-006 | organisation\_identifier\_submitting\_organisation | Organisation code for the system supplier submitting data. | MUST |
| OC Record | OCR-001 | oc\_record\_id | Reference number that is unique to this data entry record. This uniquely identifies the event rather than the patient | MUST |
| OC Record | OCR-002 | oc\_general\_medical\_practice\_patient\_registration | The GP Practice ODS code for the   - GP Practice for which data is being returned - the Hub for which data is being returned | MUST |
| OC Record | OCR-006 | oc\_submission\_successful\_to\_general\_practice | Note: A submission is defined as a successful and secure transmission of a patient’s entry into an OC system to their registered GP practice or virtual hub | MUST |
| OC Record | OCR-007 | oc\_access\_method | Method used to access online consultation system: | SHOULD |
| OC Record | OCR-008 | oc\_submission\_source | Person who completed the online submission: | SHOULD |
| OC Record | OCR-009 | oc\_patient\_age | Age (in years) of patient at date of OC submission | SHOULD |
| OC Record | OCR-010 | oc\_person\_stated\_gender\_code | Patient gender: | SHOULD |
| OC Record | OCR-011 | oc\_ethnic\_category\_code\_2001 | Patient ethnicity: | SHOULD |
| OC Record | OCR-012 | oc\_language\_code | The language used by a PERSON.  LANGUAGE CODE  is based on the ISO 639-1 two character language codes (see the  ISO Registration Authority website) plus five communication method extensions: | SHOULD |
| OC Record | OCR-013 | oc\_disability\_recorded | Submissions where patient entering into OC triage system were recorded as having a disability. Read/CTV3/SNOMED mapping | SHOULD |
| OC Record | OCR-014 | oc\_accessibility\_requirements | Patient submitted accessibility requirements  Read/CTV3/SNOMED mapping | SHOULD |
| OC Record | OCR-015 | oc\_submission\_start | Date and time of OC submission start | SHOULD |
| OC Record | OCR-016 | oc\_submission\_end | Date and time of OC submission end | MUST |
| OC Record | OCR-017 | oc\_submission\_type | Type of consultation as classified by the OC system | MUST |
| OC Record | OCR-018 | oc\_consultation\_mechanism | Method used to respond/ close OC encounter by general practice: | SHOULD |
| OC Record | OCR-019 | oc\_clinical\_problem\_type | Type of clinical problem as categorised by the online system: | SHOULD |
| OC Record | OCR-020 | oc\_clinical\_submission\_priority\_type | Urgency of the clinical problem as categorised by the online system [by types of clinical pathway]: The clinical response priority of a SERVICE REQUEST. | SHOULD |
| OC Record | OCR-021 | oc\_admin\_activity\_type | Type of admin activity as categorised by the online system: | SHOULD |
| OC Record | OCR-024 | oc\_initial\_response\_date\_time | Date and time initial response was received by the patient | SHOULD |
| OC Record | OCR-028 | oc\_response\_preference | Patient submitted their preferred method for response to their OC request: | SHOULD |
| OC Record | OCR-030 | oc\_clinician\_preference | Patient submitted their preferred clinician within online consultation system | SHOULD |
| OC Practice | OCP-001 | oc\_general\_medical\_practice\_patient\_registration | The GP Practice ODS code for:   - the GP Practice for which data is being returned - the ‘Hub’ for which data is being returned | MUST |
| OC Practice | OCP-005 | oc\_procurement\_route | Route of procurement for online consultation solution. | MUST |
| OC Practice | OCP-007 | oc\_video\_consultation\_enabled | Video consultation functionality enablement status in the online consultation Solution as at reporting period end date. | MUST |
| OC Practice | OCP-008 | oc\_two\_way\_communication\_enabled | Two-way communication (between patient and GP practice) functionality enablement status in the online consultation Solution as at report period end date. | MUST |
| OC Practice | OCP-009 | oc\_photo\_upload\_patient\_enabled | Patient photo upload functionality enablement status in the online consultation Solution at the Practice as at report period end date. | MUST |
| OC Practice | OCP-010 | oc\_triage\_enabled | If OC triage is enabled. | MUST |
| OC Practice | OCP-011 | oc\_switch\_off\_start | The date and time that the system was switched off. | SHOULD |
| OC Practice | OCP-012 | oc\_switch\_off\_end | The date and time that the system was switched back on. | SHOULD |

### Video Consultation {#OnlineConsultationsandVideoConsultationsReporting-VideoConsultation}

If the Supplier is offering the [Video Consultation](../../DSIC-Capabilities/Video-Consultation.md) Capability the data items below are required from Suppliers as part of the Video Consultation extended data collection.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Table** | **Field ID** | **Data Item** | **Description** | **Level** |
| Header | OCH\_VCH-001 | primary\_data\_collection\_supplier\_in\_use | Name of online consultation Supplier returning the data. | MUST |
| Header | OCH\_VCH-002 | reporting\_period\_start\_date | The reporting period start date to which this file refers. | MUST |
| Header | OCH\_VCH-003 | reporting\_period\_end\_date | The reporting period end date to which this file refers. | MUST |
| Header | OCH\_VCH-004 | date\_and\_time\_data\_set\_created | Date and time of VC submission start | MUST |
| Header | OCH\_VCH-005 | data\_set\_version\_number | The version number of a Data Set. | MUST |
| Header | OCH\_VCH-006 | organisation\_identifier\_submitting\_organisation | Organisation code for the system supplier submitting data. | MUST |
| VC Record | VCR-001 | vc\_record\_id | Reference number that is unique to this data entry record | MUST |
| VC Record | VCR-002 | vc\_general\_medical\_practice\_patient\_registration | The GP Practice ODS code for the   - GP Practice for which data is being returned - the Hub for which data is being returned | MUST |
| VC Record | VCR-003 | vc\_start | Date and time of VC start. | MUST |
| VC Record | VCR-004 | vc\_end | Date and time of VC end. | MUST |
| VC Record | VCR-013 | vc\_consultation\_type | Type of consultation as classified by the VC system | MUST |
| VC Record | VCR-014 | vc\_patient\_age | Age (in years) of patient at date of video consultation | SHOULD |
| VC Record | VCR-015 | vc\_person\_stated\_gender\_code | Patient gender: | SHOULD |
| VC Record | VCR-016 | vc\_ethnic\_category\_code\_2001 | Patient ethnicity: | SHOULD |
| VC Record | VCR-017 | vc\_language\_code | The language used by a PERSON.  LANGUAGE CODE  is based on the ISO 639-1 two character language codes (see the  ISO Registration Authority website) plus five communication method extensions: | SHOULD |
| VC Record | VCR-018 | vc\_disability\_recorded | Submissions where patient entering into VC triage system were recorded as having a disability.  Read/CTV3/SNOMED mapping | SHOULD |
| VC Record | VCR-019 | vc\_accessibility\_requirements | Patient submitted accessibility requirements  Read/CTV3/SNOMED mapping | SHOULD |
| VC Practice | VCP-001 | vc\_general\_medical\_practice\_patient\_registration | The GP Practice ODS code for the   - GP Practice for which data is being returned - the Hub for which data is being returned | MUST |
| VC Practice | VCP-005 | vc\_procurement\_route | Route of procurement for online consultation solution. | MUST |
| VC Practice | VCP-008 | vc\_switch\_off\_start | The date and time that the system was switched off. | SHOULD |
| VC Practice | VCP-009 | vc\_switch\_off\_end | The date and time that the system was switched back on. | SHOULD |

### Incident Data {#OnlineConsultationsandVideoConsultationsReporting-IncidentData}

If the Supplier is offering the [Online Patient Consultation](../../DSIC-Capabilities/Online-Patient-Consultation.md), [Online Patient Request](../../DSIC-Capabilities/Online-Patient-Request.md) or [Video Consultation](../../DSIC-Capabilities/Video-Consultation.md) Capability the data items below are required from Suppliers as part of the Online Consultation and Video Consultation extended data collection.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Table** | **Field ID** | **Data Item** | **Description** | **Level** |
| Header | OCH\_VCH-001 | primary\_data\_collection\_supplier\_in\_use | Name of online consultation Supplier returning the data. | MUST |
| Header | OCH\_VCH-002 | reporting\_period\_start\_date | The reporting period start date to which this file refers. | MUST |
| Header | OCH\_VCH-003 | reporting\_period\_end\_date | The reporting period end date to which this file refers. | MUST |
| Header | OCH\_VCH-004 | date\_and\_time\_data\_set\_created | Date and time of VC submission start | MUST |
| Header | OCH\_VCH-005 | data\_set\_version\_number | The version number of a Data Set. | MUST |
| Header | OCH\_VCH-006 | organisation\_identifier\_submitting\_organisation | Organisation code for the system supplier submitting data. | MUST |
| Incident data | ICP-001 | record\_id | Reference number that is unique to this data entry record | SHOULD |
| Incident data | ICP-002 | general\_medical\_practice\_patient\_registration | The GP Practice ODS code for the   - GP Practice for which data is being returned - the Hub for which data is being returned | SHOULD |
| Incident data | ICP-003 | OC\_VC\_type | Was the incident relating to OC or VC | SHOULD |
| Incident data | ICP-004 | incident\_type | An incident is any unintended or unexpected incident that could have or did lead to harm for one or more patients receiving healthcare. Note: This definition incorporates all terms such as 'adverse incidents', 'adverse events', and 'near misses'. Not a substitute for formal incident reporting - this is for incident data capturing only. Any incidents need to be reported to the Authority through the agreed processes as part of the DFOCVC Contracting Vehicle. Suppliers are required to provide information for all incidents or issues | SHOULD |
| Incident data | ICP-005 | non\_incident\_type | A non incident could be described as a lower grade issue which has not lead to an adverse incident, event or near miss. Not a substitute for formal incident reporting - this is for incident data capturing only. Any incidents need to be reported to the Authority through the agreed processes as part of the DFOCVC Contracting Vehicle. Suppliers are required to provide information for all incidents or issues | SHOULD |
| Incident data | ICP-006 | incident\_severity | The severity of the incident | SHOULD |
| Incident data | ICP-007 | incident\_cause | The cause of the incident | SHOULD |
| Incident data | ICP-008 | high\_severity\_service\_incident\_indicator | An indication of whether the incident is considered to be a high severity. | SHOULD |
| Incident data | ICP-012 | incident\_date\_time | Date and time that incident occurred | SHOULD |

# Roadmap {#OnlineConsultationsandVideoConsultationsReporting-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |