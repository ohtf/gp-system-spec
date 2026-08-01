---
page_id: "1391133583"
space: "DCSDCS"
title: "Testing"
version: 25
updated: "2026-07-20T10:34:06.117Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133583/Testing"
labels: ["overarching_standard"]
---

# Testing

|  |  |
| --- | --- |
| **ID** | S69 |
| **Version** | 1.0.11 |
| **Type** | Overarching Standard |
| **Status** | Effective |
| **Effective Date** | 20 Jul 2026 |
| **Contracting Vehicle(s)** | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) - [DFOCVC](https://nhse-dsic.atlassian.net/wiki/spaces/DFOCVCL) - [Community Pharmacy Clinical Services](https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH) - [Digital Pathways Solution Registry](https://nhse-dsic.atlassian.net/wiki/spaces/DPSR) - [Digital Primary Care](https://nhse-dsic.atlassian.net/wiki/spaces/DPC) |

- [Introduction](#Testing-Introduction)
  - [The International Software Testing Standard - ISO/IEC/IEEE 29119](#Testing-TheInternationalSoftwareTestingStandard-ISO/IEC/IEEE29119)
  - [Further Guidance](#Testing-FurtherGuidance)
- [Baseline Assurance Standard Requirements](#Testing-BaselineAssuranceStandardRequirements)
- [Further Requirements](#Testing-FurtherRequirements)
- [Roadmap](#Testing-Roadmap)

# Introduction {#Testing-Introduction}

Ensures that Suppliers' software delivery test processes are of sufficient quality and rigour.

It is essential that Solutions delivered under the Catalogue demonstrate a high-quality approach to software development and testing. Within the area of software testing, there are various established Standards and many good industry practices in place.

This Standard does not seek to mandate adherence to a particular Standard, it does however, through compliance evidence, look to establish that an appropriate level of quality and rigour are in place with respect to software testing, with ISO/IEC/IEEE 29119 providing a reference point.

According to ISO, Standards are "Guideline documentation that reflects agreements on products, practices, or operations by nationally or internationally recognised industrial, professional, trade associations or governmental bodies". They are guideline documents, therefore not compulsory unless mandated. The Standards and external references within provide a clear benchmark for good industry practices which The Authority would expect a Supplier to follow. As such, they provide a guide to Suppliers on what level of quality The Authority expects from software development testing.

## The International Software Testing Standard - ISO/IEC/IEEE 29119 {#Testing-TheInternationalSoftwareTestingStandard-ISO/IEC/IEEE29119}

An internationally agreed set of Standards for software testing that can be used within any software development life cycle or organisation:

- ISO/IEC/IEEE 29119-1: Concepts & Definitions, published in September 2013
- ISO/IEC/IEEE 29119-2: Test Processes, published in September 2013
- ISO/IEC/IEEE 29119-3: Test Documentation, published in September 2013
- ISO/IEC/IEEE 29119-4: Test Techniques, published in December 2015
- ISO/IEC/IEEE 29119-5: Keyword-Driven Testing, published in November 2016

Within the context of the Catalogue, ISO/IEC/IEEE 29119 is used to provide a guidance checklist, used to establish Suppliers entering a Contracting Vehicle demonstrate quality within their software testing. Context and Risk-based Approach ISO/IEC/IEEE 29119 part 1 states "Software testing is performed as a context-managed process". It also states "A key premise of this Standard is the idea of performing the optimal testing within the given constraints and context using a risk-based approach". These statements stand true for almost any testing approach.

## Further Guidance  {#Testing-FurtherGuidance}

- [Context Driven Testing](http://context-driven-testing.com/)
- [Software Testing Standards](http://softwaretestingStandard.org)
- [Heuristic Test Strategy Model](http://www.satisfice.com/tools/htsm.pdf)

# Baseline Assurance Standard Requirements {#Testing-BaselineAssuranceStandardRequirements}

The Baseline Assurance Standard (BAS) provides a proportionate, risk-based assurance approach for Solutions; balancing safety against efficiency by combining a minimum set of essential Requirements from the [DSIC Overarching](index.md) Standards. Completing the BAS is the first step to achieving full assurance with the Overarching Standards allowing Supplier Solutions to be published on the Buying Catalogue. Upon meeting this Standard, Solutions are required to meet any remaining Further Requirements in the Overarching Standards in the timeframe applicable to the Contracting Vehicle.

All Baseline Assurance Requirements can be found [here.](Baseline-Assurance-Standard.md) Each Solution will be assigned a category of A, B or C that determines the level of assurance applied to that Solution. See the relevant category column to understand the assurance required for each Requirement. For information on Solution Categories see [Solution Categories for Assurance in DSIC](../../Reference-Pages/Baseline-Assurance-Standard-and-Solution-Categories-for-Assurance-in-DSIC-Guidance.md).

The following table of Requirements are the Requirements in the Baseline Assurance Standard related to the Testing Standard.

| **Applicable Contracting Vehicle(s)** | **ID** | **Requirement** | **Level** | **Category A** | **Category B** | **Category C** |
| --- | --- | --- | --- | --- | --- | --- |
| **Testing Requirements** | | | |  |  |  |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-1 | Irrespective of the Software Development Life Cycle (SDLC) implemented (traditional Waterfall to Agile), there will be organisational and project specific test processes underpinned by appropriate artefacts.  Example evidence could include but not constrained to:   - Test Policy - Test Strategy - Test Plans - Risk identification process as applied to Solution testing   How are different types of testing either within a traditional SDLC or within Agile iterative-incremental development established, such as:   - Unit - Module or Component - System or Functional - Integration (including APIs) - Performance and Load Testing - Scalability, Resilience and Recovery Testing - Security Testing - User Acceptance Testing - Usability Testing - Accessibility Testing   How testing automation is incorporated into the software build and distribution process, such as continuous build integration:   - Testing Qualifications within Supplier organisation - Retrospective process improvement | MUST | **Full Assessment**  Supporting evidence to include:   - Documentation that covers all aspects listed within the Requirement. - Demonstration of the Supplier’s software testing approach and processes, types of testing and test tools via a Live Witness Assessment. | **Self-certification** | **Self-certification** |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-2 | There will be Test Management Processes covering test planning and design.  Example evidence could include:   - Test Automation (automated scope as opposed to manual testing automated) - Test Regression and process for establishing coverage scope during a specific and subsequent Solution releases - Covering both Functional and Non-Functional Testing - Techniques used - Risk-based, static/dynamic testing, testing heuristics, exploratory testing, smoke testing | MUST | **Full Assessment**  Supporting evidence to include:   - Documentation that covers all aspects listed within the Requirement. - Demonstration of the Supplier’s software testing approach and processes, types of testing and test tools via a Live Witness Assessment. | **Self-certification** | **Self-certification** |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-3 | There will be Test Management Processes covering test execution and management.  Example evidence could include:   - Tooling used, explaining how results are captured - Test Execution Management - Repeatability - Defect/Incident Management - Test Environment Management | MUST | **Full Assessment**  Supporting evidence to include:   - Documentation that covers all aspects listed within the Requirement. - Demonstration of the Supplier’s software testing approach and processes, types of testing and test tools via a Live Witness Assessment. | **Self-certification** | **Self-certification** |
| - GP IT Futures - Tech Innovation - DFOCVC - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-4 | There will be Test Management Processes covering test completion and Reporting.  Example evidence could include:   - Comprehensive test results captured within test tooling - Incident management on completion - Quality Criteria for exiting testing | MUST | **Full Assessment**  Supporting evidence to include:   - Documentation that covers all aspects listed within the Requirement. - Demonstration of the Supplier’s software testing approach and processes, types of testing and test tools via a Live Witness Assessment. | **Self-certification** | **Self-certification** |
| **Test Environments Requirements** | | | | | | |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-1 | The Supplier whose solution interoperates with the NHS national services and the applicable Non-Overarching Standards will provide the Authority with access to their system test instance(s), for assurance of the Capabilities and Non-Overarching Standards under the Contracting Vehicle. | MUST | **Full Assessment**  Supporting evidence to include:   - Access details of the test environment(s) hosting the system software test instance(s), integrated to the Authority’s 'Path to Live' test environment enabled with the national services. - Details of available test data. - Any supporting system software usage guidance or training documentation. - Walkthrough of the provisioned test environment(s)/system test instances in an online session.   **Note**: The system software test instance(s) should be separate from the system software development instances, to support the testing and assurance activities of the Authority and other third party consumer Suppliers who would need to interoperate with the system software test instance(s) using the Non-Overarching Standards APIs. | **N/A** | **N/A** |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-2 | The Supplier will make access available to the requested version(s) of system test instance(s) within two weeks of the date of request by the Authority.  These versions could either be compliant or versions for which compliance is being sought. | MUST | **Self-certification** | **N/A** | **N/A** |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-5 | The Supplier will ensure that a non-functional test environment is available to do Volumetric and Performance testing for their Solution. | MUST | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Documentation of the test environment details confirming a non-functional test environment to support Volumetric and Performance testing. | **N/A** | **N/A** |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-6 | The Supplier will provision and support system test instances for User Acceptance Testing (UAT) and for training of End Users, enabled with all the Capabilities and national service integrations as per the Non-Overarching Standards under the Contracting Vehicle. Such instances shall be separate from the system test instance(s) provisioned to the Authority. | MUST | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Documentation of test environment(s) details for supporting User Acceptance Testing(UAT) and for supporting training of End Users of the Supplier system. - Any user training materials. | **N/A** | **N/A** |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-7 | The Supplier will ensure that their test environment(s) and system test instance(s) support robust access and security controls both at Solution level and Infrastructure level, so that only authorised users can access the test environment(s) and system test instance(s). | MUST | **Self-certification with Supporting Evidence**  Supporting evidence to include:   - Documentation of the access and security controls in place. - Alternatively, demonstrate the access and security controls in place in an online walkthrough session | **N/A** | **N/A** |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-8 | The Supplier will ensure that the test environment is, as a minimum, available on all the working days of a week between 8 am to 6 pm.  Any scheduled downtimes for undertaking maintenance activities should preferably be slotted outside the working hours and be notified to the Authority a couple of weeks in advance, to minimise the impact on ongoing or scheduled testing and assurance activities either being undertaken by the Authority or the connecting system suppliers.  Any downtime required for deployment of emergency patch releases, should be notified to the Authority prior to the deployment. | MUST | **Self-certification** | **N/A** | **N/A** |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-9 | The Supplier will provide at least a minimum test data set (such as admin users, reference data such as user roles and access privileges, clinical reference dataset and any other applicable reference data sets etc.)  for the Authority to be able to perform testing and assurance activities and to perform any basic admin tasks on the system test instance(s).  The test data will contain Synthetic Data only. It will not contain any sensitive or personally identifiable Patient data.  The Supplier will ensure that any maintenance releases/emergency patches deployed to their test environment does NOT erase any of the existing test data created by the Authority as this might adversely impact any ongoing testing and assurance. | MUST | **Full Assessment**  Supporting evidence to include:   - Details of the test data setup in the system test instance(s) | **N/A** | **N/A** |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-10 | The Supplier will ensure that the system test instance(s) are capable of supporting concurrent testing by multiple external connecting system suppliers, where applicable under the Contracting Vehicle, allowing each to test independently of the others. | MUST | **Full Assessment**  Walkthrough of the provisioned test environment(s)/system test instance(s) in an online session | **N/A** | **N/A** |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-11 | The Supplier will support backup and restore functions, to allow restoration of their system test instances(s) back to the original clean state or a previously backed-up state, if required. | MUST | **Self-certification** | **N/A** | **N/A** |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-12 | The Supplier will ensure that the performance of their system test instance(s) is comparable to the production system instance, albeit for the restricted volumes in the Test environment, in order to provide a realistic expectation of performance behaviour in the LIVE estate. | MUST | **Self-certification** | **N/A** | **N/A** |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-13 | The Supplier will provide all the necessary technical documentation for their provisioned API interfaces or bulk data interfaces to allow integration testing with external connecting supplier systems, where applicable to the Contracting Vehicle. | MUST | **Full Assessment**  Supporting evidence to include:   - Documentation of any API and access/connection details e.g. for testing IM1 interfaces for integration. | **N/A** | **N/A** |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | TEST-ENV-14 | The Supplier will provide the necessary guidance and access privileges to the Authority for interrogating Audit Trail records, system logs and API messaging logs which might aid the Authority in independent identification of any technical integration issues to minimise reliance on the Supplier.  The Supplier will provide all the necessary support to the Authority in identifying and resolving any technical integration issues encountered during the testing and assurance activities. | MUST | **Self-certification with Supporting Evidence**   - Documentation that covers all aspects listed within the Requirement. - Alternatively, walkthrough of the evidence in an online session. | **N/A** | **N/A** |
| - Community Pharmacy Clinical Services - Digital Pathways Solution Registry | TEST-ENV-15 | The Supplier will provide contact details of their system help desk or the team who are accountable for logging and resolution of any test environments(s) or system test instance(s) issues or incidents.  The Supplier should advise the Authority of the process for logging the issues or incidents, and the expected timescales for resolution based on severity/criticality. | MUST | **Self-certification** | **N/A** | **N/A** |
| **Live Environments Requirements** | | | | | | |
| - GP IT Futures - Tech Innovation - Community Pharmacy Clinical Services - Digital Pathways Solution Registry - Digital Primary Care | LIVE-ENV-1 | The Supplier will support use of appropriate and limited Synthetic Data in their production (live) environment to support any smoke testing of the software build in the production (live) environment.  It will be possible for the synthetic test patients to be clearly demarcated from the real patients. | MUST | **Self-certification** | **N/A** | **N/A** |

# Further Requirements {#Testing-FurtherRequirements}

Suppliers will not be required to meet any Further Requirements to achieve full compliance with the Testing Standard.

# Roadmap {#Testing-Roadmap}

Items on the Roadmap which impact or relate to this Standard

| Roadmap Item |
| --- |
| No content found. |