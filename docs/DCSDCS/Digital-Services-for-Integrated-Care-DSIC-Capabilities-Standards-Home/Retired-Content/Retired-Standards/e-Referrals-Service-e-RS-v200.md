---
page_id: "11910348809"
space: "DCSDCS"
title: "e-Referrals Service (e-RS) v2.0.0"
version: 5
updated: "2022-06-10T11:06:31.860Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/11910348809/e-Referrals+Service+e-RS+v2.0.0"
labels: []
---

# e-Referrals Service (e-RS) v2.0.0

|  |  |
| --- | --- |
| ID | S35 |
| Version | 2.0.0 |
| Type | Interoperability Standard |
| Status | Published |
| Effective Date | 30 Jun 2022 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") |

- [Introduction](#e-ReferralsService(e-RS)v2.0.0-Introduction)
- [Compliance and Assurance](#e-ReferralsService(e-RS)v2.0.0-ComplianceandAssurance)
- [Testing](#e-ReferralsService(e-RS)v2.0.0-Testing)
- [Requirements](#e-ReferralsService(e-RS)v2.0.0-Requirements)
- [Documentation](#e-ReferralsService(e-RS)v2.0.0-Documentation)
- [Dependencies](#e-ReferralsService(e-RS)v2.0.0-Dependencies)
- [Roadmap](#e-ReferralsService(e-RS)v2.0.0-Roadmap)

# Introduction

The NHS e-Referral Service (NHS e-RS) combines electronic booking with a choice of place, date and time for first hospital or clinic Appointments. Patients can choose their initial hospital or clinic Appointment, book it in the GP surgery at the point of referral, or later at home on the phone or online.

Service integration is presently supported through the Health and Social Care Network (HSCN) -based HL7 message interactions from the NHS Connecting for [Health Message Implementation Manual (MiM)](../../DSIC-Standards/Non-Overarching-Standards/NHS-Messaging-Implementation-Manual-MIM.md).

# Compliance and Assurance

To gain access to e-RS suppliers follow the Common Assurance Process (CAP). CAP is an end-to-end assurance process, which involves a tailored (CAP) approach being developed which states what deliverable and activities are conducted.

As part of the CAP suppliers will be asked to demonstrate adherence to the following specifications:

- CAP Information Governance Compliance Requirements
- [External Interface Specification](../../DSIC-Standards/Non-Overarching-Standards/External-Interface-Specification-EIS.md)
- [NHS Messaging Implementation Manual](../../DSIC-Standards/Non-Overarching-Standards/NHS-Messaging-Implementation-Manual-MIM.md)
- [Personal Demographics Service Integration Requirements](../../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md)
- e-Referrals Service Integration Requirements

These specifications contain a set of generic requirements applicable to all systems seeking compliance to a business domain. Compliance with these specifications is mandatory and established through the CAP.

For advice, access to the documentation, and support from the NHS Business Partners programme, please contact [businesspartners@nhs.net](mailto:businesspartners@nhs.net)or visit <https://digital.nhs.uk/services/nhs-business-partners>

# Testing

The design and testing of Supplier Solutions are based upon the NHS Connecting for Health MIM version 2.3 and 3.1.09.

System Suppliers can access the updated data dictionary for the NHS e-RS. Other technical messaging documents can be found on the archived [Choose and Book site.](https://webarchive.nationalarchives.gov.uk/20160921151419/http://digital.nhs.uk/referrals)

# Requirements

Please see requirements in the document below.

[NHS e-Referrals Service …](e-Referrals-Service-e-RS-v200.md)

# Documentation

Developer resources are available on the official [e-Referral Service landing page](https://digital.nhs.uk/services/nhs-e-referral-service) on NHS Digital's website; the [Document Library](https://digital.nhs.uk/services/nhs-e-referral-service/document-library) is a component part of e-RS' requirements for suppliers seeking guidance and any implementation documentation.

If you are interested in learning more about the NHS e-RS APIs, please visit the [NHS Digital Developer Network website](https://developer.nhs.uk/apis/).

# Dependencies

Creating a compliant implementation requires implementing the following dependent interface standards:

- [Personal Demographics Service (PDS)](../../DSIC-Standards/Non-Overarching-Standards/Personal-Demographics-Service-PDS.md) \*
- [External Interface Specification (EIS)](../../DSIC-Standards/Non-Overarching-Standards/External-Interface-Specification-EIS.md)
- [NHS Messaging Implementation Manual (MIM)](../../DSIC-Standards/Non-Overarching-Standards/NHS-Messaging-Implementation-Manual-MIM.md)

\*May be sourced indirectly by existing PDS interface provided by PIM Solution, either via API to PIM Solution, or as a shared application resource if delivered as part of the same Solution.

# Roadmap

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [NHS e-Referrals Service - Referrer Compliance Document v1.1.docx](../../../../.raw/DCSDCS/attachments/11910348809/att11910348829-NHS e-Referrals Service - Referrer Compliance Document v1.1.docx)
- [NHS e-Referrals Service - Referrer Compliance Document v1.docx](../../../../.raw/DCSDCS/attachments/11910348809/att11910348832-NHS e-Referrals Service - Referrer Compliance Document v1.docx)
