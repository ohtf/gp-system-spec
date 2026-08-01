---
page_id: "12375359510"
space: "DCSDCS"
title: "Data Migration v2.0.1"
version: 1
updated: "2023-04-11T11:47:23.407Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12375359510/Data+Migration+v2.0.1"
labels: ["overarching_standard_retired"]
---

# Data Migration v2.0.1

|  |  |
| --- | --- |
| ID | S26 |
| Version | 2.0.1 |
| Type | Overarching Standard |
| Status | Retired |
| Effective Date | 30 Sep 2022 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") - [DFOCVC](https://gpitbjss.atlassian.net/wiki/spaces/DFOCVCL) - [Vaccinations - Local/PCN Delivery](https://gpitbjss.atlassian.net/wiki/spaces/CVPDR) |

# Description {#DataMigrationv2.0.1-Description}

Data Migration is a mandatory Overarching Standard which applies to all Suppliers. This Standard should be read in conjunction with the Catalogue Solution Migration Process ancillary document which describes the principles, key features, roles and responsibilities and the process applicable to the migration between Catalogue Solutions. The Catalogue Solution Migration process also sets out a number of SLAs with which Suppliers will need to be compliant.

If a Supplier is offering a Solution which does not store any data which would need to be migrated during a Data Migration process, they will need to provide evidence to that effect as part of the Compliance phase of the onboarding process. However it is expected that all Suppliers will have in place and will submit a generic, high level Data Migration Approach to cover the scenario where they are acting both as Source and Target Solution Supplier, and a Documented Data Extract (DDE) to NHS Digital for assessment during the Standards Compliance phase of onboarding. This can then be used and tailored to the specific needs of a Data Migration event when required.

The Data Migration Standard supports the safe and effective migration of data between Catalogue Solutions when a Practice (or other buying organisation such as a CCG, hub, Federation etc.) opts to change from one Catalogue Solution to another. Data Migration refers to the actions performed on multiple records stored in a Catalogue Solution, as opposed to the transfer of individual Patient records e.g. via GP2GP, or the separate transfer of part of a Patient record. This Standard covers the requirements for when a health and care organisation is moving from one Catalogue Solution to another, whether that be a complete switch of Foundation Solution(s) or of one or more specific Capabilities. In the scenario where one or more of the Solutions involved in the migration activity is not a Solution registered on the Catalogue or on the Framework, then this Standard and process will not apply. This does not however relieve Suppliers who wish to onboard a Catalogue Solution from their obligations to achieve full compliance with this Standard.

Suppliers shall provide a Data Migration Service, to support the safe and effective transfer of all data required to replicate each Patient’s Record in the Target Solution as it was recorded in the Source Solution at the time of migration. This includes the full set of Patient records and audit trails, including documents and attached images as well as other clinical and administrative information such as tasks and appointments where applicable to the individual migration event and will be in a human readable format without any undue degradation (i.e. flattening from structured data to plain text) or the need for access to the legacy Solution to be available. A successful and efficient Data Migration involves activities and responsibilities from several parties:

- The Source Solution Supplier
- The Target Solution Supplier
- Service Recipient (i.e. the organisation initiating the switch of Catalogue Solutions and responsible for overseeing the process)
- NHS Digital as the Catalogue Authority and Service Management Agent

As the Catalogue Solution Migration Process and Data Migration activities inevitably involve several parties, it is essential that all parties work together and collaborate to ensure that the process of switching Catalogue Solutions is completed as efficiently and securely as possible to ensure alignment with the SLAs and in particular to ensure that any disruption to the provision of health and care services is minimised to the extent possible. This includes ensuring that the Cut-Over period from when the final data extract is taken to Business Go-Live, where manual and duplicate data entry is likely to be required, is completed within 72 hours and outside core working hours wherever possible.

The need to migrate data from one Solution to another is normally triggered by the decision of a Service Recipient (such as a Practice, CCG, CSU, STP etc.) to use a different Catalogue Solution, whether from the same Supplier or a different one. However the need may also arise as a result of the merging or splitting of one or more Practices or the formation/closure of other health and care organisations providing primary care which involves the replacement or consolidation of existing IT systems.

Data Migration exercises inevitably involve access to, and processing of, significant amounts of sensitive personal information. Therefore all parties taking part in such activities, or providing any degree of service or support to such activities, must be conscious of the risks involved, and of their responsibilities to safeguard the confidentiality of all the data being migrated. All parties involved are required to be compliant with all UK legislation and in particular the following laws, policies, standards and guidelines in respect of Information Governance:

- Access to Medical Reports Act (1988)
- Access to Health Records Act (1990)
- NHS Act 2006 (Section 251) (previously Section 60 of the Health and Social Care Act 2001)
- General Data Protection Regulation (GDPR) (see General Data Protection Regulation (GDPR) - information - NHS Digital)
- NHS (Venereal Diseases) Regulations (1974)
- NHS Data Dictionary
- Records Management - NHS Code of Practice (DHSC)
- NIST Cryptography Standards

See Information Governance Standard for further information

It is the Service Recipient as Data Controller that has ultimate responsibility for validating and signing-off a Data Migration, however they cannot do this effectively without support from Suppliers.  To ensure a consistent understanding of responsibilities, this Standard, along with the associated Ancillary Document and the Processes set out within them, Suppliers should also make reference to Chapter 8c of the General Practice GPG, which provides guidance to organisations undertaking a Data Migration.

# Requirements {#DataMigrationv2.0.1-Requirements}

| Requirement ID | Requirement Text | Applies to | Level |
| --- | --- | --- | --- |
| **ALL Solution Suppliers** | | | |
| DMI01 {#DataMigrationv2.0.1-DMI01} | Provide a Data Migration Approach document which details their approach to a Data Migration when acting both as Source and Target Solution Supplier  *Note: This is a high level, generic document to be provided to NHS Digital as part of Standards Compliance and then to be tailored according to the needs of each Data Migration undertaken* | All | MUST |
| DMI02 {#DataMigrationv2.0.1-DMI02} | Provide a Documented Data Extract (DDE) that allows a Target Solution Supplier to understand and interpret the form and structure of the extracted data. This will include, but is not limited to:   1. A description of the physical data included in the extract 2. A logical model explaining the relationships between the data in the extract, and any physical primary/compound/foreign key information required to be able to understand and process the extract 3. A mapping between the physical and logical models 4. Details of units of measure for numeric fields where these are not clearly identified in the extract itself 5. Full descriptions of the meaning of any coded values included in the extract 6. Details of any business rules/logic that the Target Solution Supplier would have to understand to successfully import the extract 7. Details of any exceptional or specific handling required for the Target Solution Supplier to successfully import the extract, e.g. where handling of certain data has to be treated differently if it was created between certain dates 8. Rules for any data which the Source Solution derives from the extracted data but which is not included 9. Any excluded data 10. Any checks or validations (e.g. integrity checks) which the Target Solution Supplier needs to undertake to ensure the accuracy of the imported data 11. Any documentation which would be required to support Solution reconstitution 12. The format of the data extract to be provided   *Note: This is an overarching DDE to be provided to NHS Digital as part of Standards Compliance and then tailored according to the specifics of each Data Migration undertaken* | All | MUST |
| DMI03 {#DataMigrationv2.0.1-DMI03} | Provide the DDE to NHS Digital:   - at the request of NHS Digital (e.g. for Standards Compliance) or in the case of significant changes to the DDE | All | MUST |
| DMI04 {#DataMigrationv2.0.1-DMI04} | Support, and/or provide mechanisms to support, the migration and/or re-integration of data which is stored solely in a Solution which is not the Source Solution where such a Solution is in use | All | MUST |
| DMI27 {#DataMigrationv2.0.1-DMI27} | Perform a migration of data from a source supplier to target supplier over the internet.   - Internet-based transfers must conform to the Cross Function Requirements outlined within the DMS Data Transfer - Cross Functional Requirements Document - If, under the circumstance that a bandwidth of >= 70 Mbps and a latency of <200ms cannot be achieved, then a fall back to physical media transfer can be used. - If, under the circumstance that physical media is deemed necessary, and the target supplier is primarily cloud-based, then a solution supported by the target supplier’s cloud provider must be used, for example AWS Snow Cone or Azure Data Box. - If, under the circumstance that both Suppliers are primarily cloud-based, then an internet-based transfer must be used. This is due to the potential number of additional transfers steps when using physical media between two alternative cloud providers. | All | MUST |
| **Source Solution Suppliers only** | | | |
| DMI05 {#DataMigrationv2.0.1-DMI05} | Support the Service Recipient with improving the data quality in the Source Solution up to the minimum standard agreed by all parties in preparation for the data extracts    See documents available here for guidance regarding data cleansing and preparation of data for a migration | Source | MUST |
| DMI06 {#DataMigrationv2.0.1-DMI06} | Provide a minimum of two separate data extracts to the Target Solution Supplier and/or the Service Recipient to include:   - an initial sample data extract - a final data extract for data loading   *NB. The provision of additional extracts may be required to facilitate the data transformation and data migration activities as detailed in the Data Migration Process set out in the Catalogue Solution Migration Process Ancillary Document* | Source | MUST |
| DMI07 {#DataMigrationv2.0.1-DMI07} | All data extracts will:   - be in an encrypted electronic format - be in conformance with the DDE provided - be provided to the Target Solution Supplier and/or the Service Recipient as instructed by the Service Recipient (as Data Controller) - employ cryptographic techniques which conform to NIST Cryptogrophy Standards - contain the full set of Patient records, including documents and attached images as well as other clinical and administrative information such as tasks and appointments where applicable to the individual migration event - be in a human readable format without any undue degradation (i.e. flattening from structured data to plain text) or the need for access to the legacy Solution to be available | Source | MUST |
| DMI26 {#DataMigrationv2.0.1-DMI26} | All data extracts to contain the full set of audit trails where applicable to the individual migration event. | Source | SHOULD |
| DMI08 {#DataMigrationv2.0.1-DMI08} | Provide a document and reports detailing any irregularities regarding the way in which data has been entered into the Source Solution (i.e. variances on the DDE), including reference to any dependencies on other Solutions and Suppliers | Source | MUST |
| DMI09 {#DataMigrationv2.0.1-DMI09} | Provide access to the Source Solution, including data and audit trails in human readable format, and support services for the duration of the agreed Run-Off period as a minimum, according to the terms of the applicable contracts and agreements for that Data Migration and/or at the request of the Service Recipient.  *Note: Reference access to the Source Solution may be required for some time after completion of the Data Migration activities* | Source | MUST |
| DMI10 {#DataMigrationv2.0.1-DMI10} | Where a third party Supplier is used during the Data Migration process, provide an automated mechanism for the third party Supplier to access and extract the data from the Source Solution | Source | SHOULD |
| **Target Solution Suppliers only** | | | |
| DMI11 {#DataMigrationv2.0.1-DMI11} | Undertake the data transformation and mapping of data from the extracts provided by the Source Solution Supplier to a format which can be loaded into the Target Solution | Target | MUST |
| DMI12 {#DataMigrationv2.0.1-DMI12} | Undertake the data transformation and mapping of data using the latest version of the approved mapping tables published by UK Terminology Centre (UKTC) | Target | MUST |
| DMI13 {#DataMigrationv2.0.1-DMI13} | Where mapping cannot be completed using the UKTC mapping tables, provide and describe the mapping tables used during the data transformation activities | Target | SHOULD |
| DMI14 {#DataMigrationv2.0.1-DMI14} | Provide tables detailing any specific mappings between the Source Solution data and the Target Solution | Target | MUST |
| DMI15 {#DataMigrationv2.0.1-DMI15} | Facilitate as many iterations of the data transformation and mapping as required to address all errors, omissions, and irregularities to the satisfaction of the Service Recipient  *Note: If greater than five iterations of the data extract and transformation process are required, this will need to be reported to NHS Digital* | Target | MUST |
| DMI16 {#DataMigrationv2.0.1-DMI16} | Provide tools to enable the Service Recipient to undertake the mapping of non-standard, local codes where necessary | Target | SHOULD |
| DMI17 {#DataMigrationv2.0.1-DMI17} | Provide the Service Recipient with the transformed data and a trial environment to enable the validation of the integrity, accuracy and completeness of the data | Target | MUST |
| DMI18 {#DataMigrationv2.0.1-DMI18} | Maintain an Issues Log of all issues encountered during the data transformation, including how and when each was resolved | Target | MUST |
| DMI19 {#DataMigrationv2.0.1-DMI19} | Undertake any corrective action necessary to address issues raised regarding the data transformation and document this in the Issues Log | Target | MUST |
| DMI20 {#DataMigrationv2.0.1-DMI20} | Provide comprehensive aggregated reports to enable the Service Recipient to verify the integrity, accuracy and completeness of the transformed data. As a minimum these will include:   - counts of all coded data items from both Source and Target Solutions - comparisons of data in the Source Solution with data in the Target Solution (e.g. number of current Active Patients, active medications, results of routine QOF searches) - any variances | Target | MUST |
| DMI21 {#DataMigrationv2.0.1-DMI21} | Reports will be available at all times from the live and/or trial Environments (as applicable) from the moment the corresponding environment is made available | Target | MUST |
| DMI22 {#DataMigrationv2.0.1-DMI22} | Reports to be refreshed every time data is re-loaded | Target | MUST |
| DMI23 {#DataMigrationv2.0.1-DMI23} | Load the transformed data into the Target Solution once approved by the Service Recipient | Target | MUST |
| DMI24 {#DataMigrationv2.0.1-DMI24} | Ensure staff, facilities, tools, training and support services, including floor-walking staff, are in place to support the Service Recipient in use of the Target Solution and to ensure that any obligations and responsibilities can continue to be met effectively | Target | MUST |
| DMI25 {#DataMigrationv2.0.1-DMI25} | Support additional training needs and requests post Business Go-Live as requested by the Service Recipient | Target | SHOULD |

# Capabilities {#DataMigrationv2.0.1-Capabilities}

**Applicable Capabilities**

All Suppliers Solutions delivering any Capabilities will need to meet this Standard.

# Roadmap {#DataMigrationv2.0.1-Roadmap}

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item | Standards and Capabilities | Status | Effective Date | Description | Change Type | Change Route |
| --- | --- | --- | --- | --- | --- | --- |
| [Uplift Catalogue Solution Migration Process document](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/15319465997/Uplift+Catalogue+Solution+Migration+Process+document) | [Data Migration](../../DSIC-Standards/Overarching-Standards/Data-Migration.md) | Draft | 24 Aug 2026 | Periodic Update to Improve the Catalogue Solution Migration Process document | Uplift | Managed Capacity - Minor/Patch uplifts |
| [Data Migration Standard - Mandating Out of Hours Cutover](https://nhse-dsic.atlassian.net/wiki/spaces/DCSDR/pages/14523203585/Data+Migration+Standard+-+Mandating+Out+of+Hours+Cutover) | [Data Migration](../../DSIC-Standards/Overarching-Standards/Data-Migration.md), [Baseline Assurance Standard](../../DSIC-Standards/Overarching-Standards/Baseline-Assurance-Standard.md) | Draft | TBC | Requirements uplifted to support the mandating of an out of hours cutover as part of the overall Data Migration process | Uplift | Managed Capacity - Other |

## Attachments

- [DMSDataTransfer-CrossFunctionalRequirements-100622-0930.pdf](../../../../.raw/DCSDCS/attachments/12375359510/att12374180075-DMSDataTransfer-CrossFunctionalRequirements-100622-0930.pdf)
- [Catalogue Solution Migration Process.docx](../../../../.raw/DCSDCS/attachments/12375359510/att12375359538-Catalogue Solution Migration Process.docx)
