---
page_id: "2454978655"
space: "DCSDCS"
title: "National Data Opt-Out v1.0.0"
version: 1
updated: "2020-09-17T14:58:09.832Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/2454978655/National+Data+Opt-Out+v1.0.0"
labels: ["interop_standard_retired"]
---

# National Data Opt-Out v1.0.0

|  |  |
| --- | --- |
| ID | S73 |
| Version | 1.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 30 Sep 2020 |

- [Introduction](#NationalDataOpt-Outv1.0.0-Introduction)
- [Compliance and Assurance](#NationalDataOpt-Outv1.0.0-ComplianceandAssurance)
- [Requirements](#NationalDataOpt-Outv1.0.0-Requirements)
- [Dependencies](#NationalDataOpt-Outv1.0.0-Dependencies)
- [Roadmap](#NationalDataOpt-Outv1.0.0-Roadmap)

# Introduction

The National Data Opt-Out Programme has been established to ensure that a mechanism is developed and available for Health and Social Care organisations to use that will enable a Patient’s preference to be honoured accordingly, e.g. if a Patient’s preference is to opt-out then their data is to be withheld from being shared from appropriate disclosures – this is known as the ‘Upholding’ of an opt-out.

# Compliance and Assurance

At a high-level, Compliance, Assurance and Testing of the National Data Opt-Out will align with the following steps:

1. A GP System Supplier will provide NHS Digital Solution Assurance with their full list of data extractions/ data disseminations impacted for NDOP, for reference.
2. A GP System Supplier will provide NHS Digital Solution Assurance with their detailed user stories and their associated acceptance criteria, for each NDOP requirements in scope, for reference and any feedback.
3. A GP System Supplier will provide NHS Digital Solution Assurance with their test cases against each of their user stories and the pass/fail test results against each test case. Evidence of associated test criteria for supplier test cases may be additionally requested by NHS Digital Solution Assurance.
4. A GP System Supplier Testing to include but not limited to:
   1. Retrieval and upholding of Patient National Data Opt-Out preference for a single Patient data dissemination(s)
   2. Retrieval and upholding of Patient National Data Opt-Out preference for multiple Patients data dissemination(s)
   3. Patient changes their National Data Opt-Out choice and its’ effect on data dissemination(s) from the GP System
   4. Testing that any Type 1 opt-out preferences recorded in the GP system for Patients, continue to be respected
   5. Testing that the GP system is able to report with the required report data attributes on whether Patient data was included or removed from a dataset along with the reason for inclusion/exclusion
   6. Audit logging for retrieval of Patient’s National Data Opt-Out preference
5. NHS Digital Solutions Assurance to sample a set of Supplier test cases for witness testing in a witness test session lasting not exceeding more than one day
6. FOT (First of Type) DevMAC to be awarded to the GP System Supplier at the end of the successful assurance
7. FRA (Full Rollout Approval) DevMAC post successful FOT

# Requirements

Standards for confirming the Patient preferences: 

Supplier Solutions need to retrieve the National Data Opt-Out Status before using or disclosing data, which can be done over Message Exchange for Social Care and Health (MESH). Technical information below describes, how to access and use MESH to check for national data opt-outs:

Check for National Data Opt-outs Service

DCB3058 Compliance with National Data Opt-Outs contains further information on the Standard and information on the legal, strategic and policy context behind the requirements.

The final set of National Data Opt-Out requirements, v2.0 published April 2019, can be accessed below:

[NDOP GP IT Change requir…](National-Data-Opt-Out-v100.md)

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standard:

- Messaging Exchange for Social Care and Health (MESH)

# Roadmap

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NDOP GP IT Change requirements v2.0 29Apr2019.docx](../../../../.raw/DCSDCS/attachments/2454978655/att2454978658-NDOP GP IT Change requirements v2.0 29Apr2019.docx)
