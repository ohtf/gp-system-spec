---
page_id: "1693188278"
space: "DCSDCS"
title: "GP Extracts Verification - Standard v1.0.0"
version: 3
updated: "2020-01-15T15:06:50.896Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1693188278/GP+Extracts+Verification+-+Standard+v1.0.0"
labels: ["capability_specific"]
---

# GP Extracts Verification - Standard v1.0.0

|  |  |
| --- | --- |
| ID {#GPExtractsVerification-Standardv1.0.0-ID} | S10 |
| Version {#GPExtractsVerification-Standardv1.0.0-Version} | 1.0.0 |
| Type {#GPExtractsVerification-Standardv1.0.0-Type} | Capability Specific Standard |
| Status {#GPExtractsVerification-Standardv1.0.0-Status} | Retired |
| Effective Date | 01 Apr 2019 |

# Requirements {#GPExtractsVerification-Standardv1.0.0-Requirements}

| Epic Mapping | Requirement ID | Requirement Text | Level |
| --- | --- | --- | --- |
| Epic 1 | **GP-PF-5** | **Report for Future Extraction**  Suppliers to provide reports which detail the Patients who are to be included in an upcoming national extraction. This enables the GP Practice Users to see which Patients will be included in the counts for national extractions.  Upcoming extracts are extracts which have been certified by GPES and have an associated set of Run Time Parameters. It is the responsibility of the GPES team to provide correct Run Time Parameters to Suppliers.  For more information on 'upcoming extracts' and those that have 'extract parameter' values, see GPES Data Extraction | MUST |
| Epic 1 | **GP-PF-5.1** | **National Extraction Reports**  A report to be produced for each extract supported by the Solution which is extracted by the GPES Data Extraction service and sent to the Calculating Quality Reporting Service (CQRS).  See Current Live Extract Specifications section for information on current live extracts. | MUST |
| Epic 1 | **GP-PF-5.2** | ****National Extraction Reports -**Exact Logic**  The logic for the reports in GP-PF-5.1 to match exactly the extraction logic which is being used to generate the national extraction. | MUST |
| Epic 1 | **GP-PF-5.2.1** | ******National Extraction Reports -****Inclusion Reason**  Practice Users to be able to identify for included Patients exactly which logical conditions have been met, how they have been met and how this has led the Patient to be included at each stage, according to the extraction logic.  See MenACWY\_v3.0 Business Rules for example logic. | MUST |
| Epic 1 | **GP-PF-5.2.2** | ********National Extraction Reports -******Identifier and Relevant Information**  The report to identify the Patients by their NHS Number and should provide other information relevant to the extraction and the logical steps of the 'Business Rules'. Click here to see High level User Story for definition of 'other information'**As a** GP Practice User, **I want** to see the data that has led a Patient to be selected into the report, **So that** I can determine why a Patient has been included in an extract.**Given** that a set of parameters, which are defined in the business rules, must be met **When** a Patient is successfully selected and included in an extract **Then** the parameters and the associated data that have been met should be available in the report.For example:Rule 1: Patient must be registered at the practiceRule 2: patient must be over 65Rule 3: patient must be maleRule 4: patient must have either code x y or z between date a and b The report should contain:  - the registration status - the Patient's age - the Patient's gender - the code and the date which has led to selection | MUST |
| Epic 1 | **GP-PF-5.2.3** | **********National Extraction Reports -********Plain English Description**  Information to include a plain English description of why the Patient has been included in the extract. NHS Digital will provide these in the ‘Business Rules’ and the plain English description to reflect these where appropriate.  See MenACWY\_v3.0 Business Rules for example descriptions | MUST |
| Epic 1 | **GP-PF-5.3** | **Time Period Matching**  Each report to be executed for a specific period which matches the period for which data is to be extracted for the national extract.  See Section 3 in MenACWY\_v3.0 Business Rules for example time periods  See GPES Data Extraction for time period 'extract parameters'. | MUST |
| Epic 1 | **GP-PF-6** | **Report for Previous Extractions**  An additional version of the reports defined in GP-PF-5.2, GP-PF-5.2.1, GP-PF-5.2.2 and GP-PF-5.2.3 to be made available which meets the same requirements so that Practice Users can see precisely which Patients have been included or not in the extractions which have been executed.  These reports need to be accessible throughout the duration of the service and then for 6 years from the end of the service. The duration of the service is defined in the appropriate service specification or via the GMS contract (GMS Statement of Financial Entitlements 2013, section 25.12)  See the Pneumococcal vaccination specification - Paragraph 2.2 states that the Service is valid from 01 April 2017 to 31 March 2018 and Paragraph 7.6 part iv. states that there is a maximal 6 month claim window.  See Current Live Extract Specifications section for information on current live extracts and which are defined as payment extracts. | MUST |
| Epic 1 | **GP-PF-6.1** | **Exact Logic - Previous Extractions**  The reports in GP-PF-6 to match exactly the data which has been sent to the national extraction system. Reports also to match exactly the inclusion and exclusion criteria specified within the 'Business Rules'. | MUST |
| Epic 1 | **GP-PF-6.2** | **Report for Ad-hoc Extractions**  If data is re-sent to the national extraction system, the report in GP-PF-6 to be provided for each successful attempt. | MAY |
| Epic 1 | **GP-PF-7** | **Search for Inclusion/Exclusion Reason**  Practice Users to have ability to search against individual Patient Records to identify the reason for that Patient being included or excluded in/from a national extract. | MUST |
| Epic 1 | **GP-PF-7.1** | **Search Before and After Extraction**  Practice Users to be able to conduct the search prior to an extract being run and identify if a Patient is included or excluded and the reason why.  After a national extraction has been run the Practice User to be able to search the record and identify why a Patient was excluded or included in a specific extract for a specific period. | MUST |
| Epic 1 | **GP-PF-7.1.1** | **Search Result Updated**  If the Patient Record is updated, the result of the search to reflect the change if:  - The national extract has not yet been run - The national extract is due to be re-run  If data has been re-sent via the national extraction system, the result of the search to reflect the data that was originally sent and the data that was re-sent.  As per requirement GP-11.3-10 in the Common Reporting standards, changes made to the Patient Record will be reflected in the associated reports/searches.  See [GPIT Futures Detailed Requirements Requirement 7.1.1 Supporting Diagram v2.0.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1693188278/GPIT%20Futures%20Detailed%20Requirements%20Requirement%207.1.1%20Supporting%20Diagram%20v2.0.pdf?version=1&modificationDate=1578324550130&cacheVersion=1&api=v2) which shows how search results should be stored. | MUST |
| Epic 1 | **GP-PF-7.1.2** | **Search Result Storage**  Where a result for a search is stored and available historically the result to be available for the lifetime of the service and claim window.  See the Pneumococcal vaccination specification - Paragraph 2.2 states that the Service is valid from 01 April 2017 to 31 March 2018 and Paragraph 7.6 part iv. states that there is a maximal 6 month claim window.  See [GPIT Futures Detailed Requirements Requirement 7.1.1 Supporting Diagram v2.0.pdf](https://nhse-dsic.atlassian.net/wiki/download/attachments/1693188278/GPIT%20Futures%20Detailed%20Requirements%20Requirement%207.1.1%20Supporting%20Diagram%20v2.0.pdf?version=1&modificationDate=1578324550130&cacheVersion=1&api=v2) which shows how search results should be stored. | MUST |
| Epic 1 | **GP-PF-7.2** | **Search Result Content**  When conducting the search in GP-PF-7.1.2:  - The Search and associated Reason to match exactly the extraction logic as set out in the 'Business Rules' (as per requirement GP-PF-5.2) - The Search and associated Reason to identify the stage in the extraction logic and the reason for the Patient being excluded or included (related to requirement GP-PF-5.2.1) - The Search and associated Reason to provide additional relevant information to the logical steps which identifies why the Patient has been excluded or included (as per requirement GP-PF-5.2.2) -The Reason to be provided as a plain English description of why the Patient has been excluded or included (as per requirement GP-PF-5.2.3) | MUST |
| Epic 2 | **GP-PF-9** | **Non-Payment National Extracts**  Implement all requirements within this Capability for non-payment national extracts.  See Current Live Extract Specifications section for information on current live extracts and which are defined as non-payment extracts. | MAY |

# Capability {#GPExtractsVerification-Standardv1.0.0-Capability}

**Applicable Capability**

All supplier Solutions will need to meet this Standard if they are delivering the GP Extracts Verification Capability

# Roadmap {#GPExtractsVerification-Standardv1.0.0-Roadmap}

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |

## Attachments

- [GPIT Futures Detailed Requirements Requirement 7.1.1 Supporting Diagram v2.0.pdf](../../../../attachments/DCSDCS/1693188278/att1693188281-GPIT Futures Detailed Requirements Requirement 7.1.1 Supporting Diagram v2.0.pdf)
- [MenACWY_v3.0 Business Rules.pdf](../../../../attachments/DCSDCS/1693188278/att1693188284-MenACWY_v3.0 Business Rules.pdf)
- [GPIT Futures MENACWY Report Example.xlsx](../../../../attachments/DCSDCS/1693188278/att1693188287-GPIT Futures MENACWY Report Example.xlsx)
