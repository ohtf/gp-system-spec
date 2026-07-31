---
page_id: "1391134283"
space: "DCSDCS"
title: "Primary Care Clinical Terminology Usage Report"
version: 15
updated: "2026-07-22T13:12:03.612Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391134283/Primary+Care+Clinical+Terminology+Usage+Report"
labels: ["standard"]
---

# Primary Care Clinical Terminology Usage Report

|  |  |
| --- | --- |
| **ID** | S70 |
| **Version** | 1.0.1 |
| **Type** | Standard |
| **Status** | Effective |
| **Effective Date** | 04 Dec 2025 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

/\*<![CDATA[\*/
div.rbtoc1785498411560 {padding: 0px;}
div.rbtoc1785498411560 ul {list-style: disc;margin-left: 0px;}
div.rbtoc1785498411560 li {margin-left: 0px;padding-left: 0px;}
/\*]]>\*/

- [Introduction](#PrimaryCareClinicalTerminologyUsageReport-Introduction)
- [Requirements](#PrimaryCareClinicalTerminologyUsageReport-Requirements)
- [Compliance, Assurance and Testing](#PrimaryCareClinicalTerminologyUsageReport-Compliance,AssuranceandTesting)
- [Dependencies](#PrimaryCareClinicalTerminologyUsageReport-Dependencies)
- [Roadmap](#PrimaryCareClinicalTerminologyUsageReport-Roadmap)

# Introduction

The purpose of this report is to collect data from each GP IT System Supplier on the frequency of use of clinical coded terms, both terminology (SNOMED CT, Read v2, CTV3) and local codes, recorded through their System for fully registered Patients over a 12 month period for all entries which are part of the GP record, aggregated across the selected Practices.

This data on the frequency of usage of clinical terms is to inform which codes are in actual use to:

- support the clinical assurance process with respect to data migration and GP2GP
- support the production, maintenance and clinical assurance of the cross maps for primary care
- facilitate the development of guidance with respect to terminology codes and local codes

Elements of the data submitted will be published and made publicly available once processed to protect any Patient and commercially sensitive data.

# Requirements

|  |  |  |
| --- | --- | --- |
| **General** | | |
| **ID** | **Requirement** | **Level** |
| **PCTUR01** | Data is to be provided where the Solution is hosted either via Public or Private Cloud, or in a Co located or Provider data centre | MUST |
| **PCTUR02** | Data can be provided where the Solution is locally hosted | MAY |
| **GP-BI.2-02** | Report will be provided on an annual basis | MUST |
| **GP-BI.2-03** | Report will cover the period from 00:00 on 1st August to 23:59 on 31st July of the following year  i.e. a report produced in August 2017 would cover the period from 1st August 2016 to 31st July 2017 | MUST |
| **GP-BI.2-04** | Report will be provided by the end of September of the year in which the reporting period ends  i.e. a report for the period 1st August 2016 to 31st July 2017 will be submitted by the end of September 2017 | MUST |
| **Practices** | | |
| **GP-BI.2-06** | Report to include aggregated data on code usage across all Practices in the Supplier estate | MUST |
| **GP-BI.2-07** | Report will only include aggregated data on code usage for Practices which went live with the Supplier System at least 2 months prior to the start of the reporting period  i.e. for a report for the period 1st August 2016 to 31st July 2017, the Supplier System will have gone live in the Practice prior to 1st June 2016 | MUST |
| **Patients** | | |
| **GP-BI.2-08a** | Report to include aggregated data on code usage for Patients who were fully registered with a Practice as at the end of the reporting period | MUST |
| **GP-BI.2-08b** | Report to include aggregated data on code usage for Patients who were fully registered with a Practice but died during the reporting period | MUST |
| **GP-BI.2-09** | Report will include codes entered during the reporting period via a different System e.g. where a Patient has moved to a new Practice and their record has been transferred via GP2GP | MUST |
| **Codes** | | |
| **GP-BI.2-10** | Report will only include coded data recorded during the reporting period  NB. this is to be determined by the System audit date | MUST |
| **GP-BI.2-11** | Report to exclude codes not normally used by or visible to users i.e. those inserted by the System (e.g. metadata codes to identify record component types) | MUST |
| **GP-BI.2-12** | Report to include all codes visible to the user as part of the Patient Record, including:   - codes entered directly by users into the System - codes received via pathology laboratory links - codes received from other feeder Systems | MUST |
| **GP-BI.2-13** | Report to include all coded items newly entered within the reporting period, including where identical entries have been added prior to the reporting period | MUST |
| **GP-BI.2-14** | Where dual coding is in place, report will include the code from the primary coding scheme which was actually selected by the user | MUST |
| **Format** | | |
| **GP-BI.2-16** | Suppliers will provide the **Terminology Usage Report** and the associated **Metadata Report** | MUST |
| **GP-BI.2-17** | Reports will be provided in a TAB-delimited UTF8-MB3 text file (NOT comma separated, quote delimited or Excel spreadsheet). | MUST |
| **GP-BI.2-18** | The first row of the reports will contain the column names as specified in [Primary Care Clinical Terminology Metadata Report GP-BI.2-21](Primary-Care-Clinical-Terminology-Usage-Report.md) and [Primary Care Clinical Terminology Usage Report GP-BI.2-22](Primary-Care-Clinical-Terminology-Usage-Report.md) | MUST |
| **GP-BI.2-19** | Report columns will always be submitted in the order as specified in [Primary Care Clinical Terminology Metadata Report GP-BI.2-21](Primary-Care-Clinical-Terminology-Usage-Report.md) and [Primary Care Clinical Terminology Usage Report GP-BI.2-22](Primary-Care-Clinical-Terminology-Usage-Report.md) | MUST |
| **GP-BI.2-20** | Reports will be submitted via [Secure Electronic File Transfer (SEFT)](Secure-Electronic-File-Transfer-SEFT.md) | MUST |
| **GP-BI.2-21** | The **Metadata Report** to be formatted as follows:  **Column 1: PracticeCount**. Number of Practices included in the report as per [Primary Care Clinical Terminology Usage Report GP-BI.2-06](Primary-Care-Clinical-Terminology-Usage-Report.md) and [Primary Care Clinical Terminology Usage Report GP-BI.2-07](Primary-Care-Clinical-Terminology-Usage-Report.md)  **Column 2: PatientCount**. Number of Patients included in the report as per [Primary Care Clinical Terminology Usage Report GP-BI.2-08a](Primary-Care-Clinical-Terminology-Usage-Report.md) and [Primary Care Clinical Terminology Usage Report GP-BI.2-22](Primary-Care-Clinical-Terminology-Usage-Report.md) | MUST |
| **GP-BI.2-22** | The **Terminology Usage Report** to be formatted as follows:  **Column 1: CodeID**.  5 character READ/CTV3 code, 18 digit SNOMED ConceptID or local code identifier that uniquely identifies the local OR national terminology concept e.g. N2450, XM1NJ, 18876004, EGTON460, Y7121  **Column 2: TermID**. 2 character READ termcode, 5 character CTV3 termcode, SNOMED DescriptionID or local term identifier for the actual description text selected by the user e.g. 12, YaYBJ, 31828016, 99  **Column 3: TermDescription**. Longest available preferred display term string encoded for by ConceptID+TermID e.g. 'Finger Pain', 'Vertigo', 'Herpetic Stomatitis'  **Column 4: EPREntryCount**. Aggregate count of the number of discrete new entries made using ConceptID+TermID across the selected Patients and Practices during the reporting period | MUST |
| **GP-BI.2-23** | For the **Terminology Usage Report**, the following pseudo code to be used:  For all Patients fully registered with a Practice on **<end date> AND** those who were fully registered but died during the reporting period (**"<start date>"-"<end date>"**) as per [Primary Care Clinical Terminology Metadata Report GP-BI.2-21](Primary-Care-Clinical-Terminology-Usage-Report.md) and [Primary Care Clinical Terminology Usage Report GP-BI.2-08b](Primary-Care-Clinical-Terminology-Usage-Report.md)  **ANALYSE**  **GROUPED\_BY** CodeID **AND** TermID **AND** TermDescription  **FROM JOURNALS (ALL)**  **WHERE RECORD\_DATE IN ("<start date>"-"<end date>") AND CODE IN ("%")**  Where **<start date> = 1st August <YYYY>** and **<end date> = 31st July <YYYY+1>** | MAY |
| **GP-BI.2-24** | The actual query used for the **Terminology Usage Report** will NOT:   - Double count - Sample different fragments of the same full coded Electronic Patient Record content - Include codes attached to 'System' tables   Where the TermID does not exist or is not persisted, no data (an empty field) will be returned for the TermID column | MUST |

# Compliance, Assurance and Testing

See the Primary Care Clinical Terminology Usage Report section on [Onboarding Overview of the Digital Care Services Interoperability Standards and Requirements](../../Reference-Pages/Onboarding-Overview-of-the-Digital-Services-for-Integrated-Care-DSIC-Non-Overarching-Standards-and-Requirements.md).

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface Standards:

- [Secure Electronic File Transfer (SEFT)](Secure-Electronic-File-Transfer-SEFT.md)

# Roadmap

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |