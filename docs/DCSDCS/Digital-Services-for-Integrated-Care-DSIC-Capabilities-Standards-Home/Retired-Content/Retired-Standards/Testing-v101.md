---
page_id: "12375457800"
space: "DCSDCS"
title: "Testing v1.0.1"
version: 1
updated: "2023-04-11T13:53:50.113Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/12375457800/Testing+v1.0.1"
labels: ["overarching_standard_retired"]
---

# Testing v1.0.1

|  |  |
| --- | --- |
| ID | S69 |
| Version | 1.0.1 |
| Type | Overarching Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |
| Framework(s) | - [GP IT Futures](https://gpitbjss.atlassian.net/wiki/spaces/GPITF "/wiki/spaces/GPITF") - [Tech Innovation](https://gpitbjss.atlassian.net/wiki/spaces/GIFTIF "/wiki/spaces/GIFTIF") - [DFOCVC](https://gpitbjss.atlassian.net/wiki/spaces/DFOCVCL) - [Vaccinations - Local/PCN Delivery](https://gpitbjss.atlassian.net/wiki/spaces/CVPDR) |

# Description

Ensures that Suppliers' software delivery test processes are of sufficient quality and rigour.

It is essential that Solutions delivered under the Catalogue demonstrate a high-quality approach to software development and testing. Within the area of software testing, there are various established standards and many good industry practices in place.

This standard does not seek to mandate adherence to a particular standard, it does however through compliance evidence look to establish that an appropriate level of quality and rigour are in place with respect to software testing, with ISO/IEC/IEEE 29119 providing a reference point.

According to ISO, Standards are "Guideline documentation that reflects agreements on products, practices, or operations by nationally or internationally recognised industrial, professional, trade associations or governmental bodies". They are guideline documents, therefore not compulsory unless mandated. The standards and external references within provide a clear benchmark for good industry practices which NHS Digital would expect a supplier to follow. As such, they provide a guide to suppliers on what level of quality NHS Digital expects from software development testing.

## The International Software Testing Standard - ISO/IEC/IEEE 29119

An internationally agreed set of standards for software testing that can be used within any software development life cycle or organisation:

- ISO/IEC/IEEE 29119-1: Concepts & Definitions, published in September 2013
- ISO/IEC/IEEE 29119-2: Test Processes, published in September 2013
- ISO/IEC/IEEE 29119-3: Test Documentation, published in September 2013
- ISO/IEC/IEEE 29119-4: Test Techniques, published in December 2015
- ISO/IEC/IEEE 29119-5: Keyword-Driven Testing, published in November 2016

Within the context of the Catalogue, ISO/IEC/IEEE 29119 is used to provide a guidance checklist, used to establish suppliers entering a Framework demonstrate quality within their software testing. Context and Risk-based Approach ISO/IEC/IEEE 29119 part 1 states "Software testing is performed as a context-managed process.". It also states "A key premise of this standard is the idea of performing the optimal testing within the given constraints and context using a risk-based approach". These statements stand true for almost any testing approach.

## Further Guidance

http://context-driven-testing.com/

http://softwaretestingstandard.org/

http://www.satisfice.com/tools/htsm.pdf

# Requirements

## Testing Requirements

| Requirement ID | Requirement Text | Level |
| --- | --- | --- |
| **TEST-1** | There will be organisational and project specific test processes underpinned by appropriate artefacts.  Example evidence could include:   - Test Policy - Test Strategy - Test Plans - Test Specifications - Risk identification process as applied to Solution testing - How is testing within development phases established, such as;   - Unit,   - Module   - System   - System Integration   - Integration   - System Integration   - User Acceptance Testing - How testing automation is incorporated into the software build and distribution process, such as continuous build integration - Testing Qualifications within supplier organisation - Retrospective process improvement | MUST |
| ****TEST**-2** | There will be Test Management Processes covering test planning and design.  Example evidence could include:   - Test Automation (automated scope as opposed to manual testing automated) - Test Regression and process for establishing coverage scope during a specific and subsequent Solution releases - Covering both Functional and non-Functional Testing - Techniques used - Risk-based, static/dynamic testing, testing heuristics, exploratory testing, smoke testing,... | MUST |
| **TEST-3** | There will be Test Management Processes covering test execution and management.  Example evidence could include:   - Tooling used, explaining how results are captured, - Test Execution Management - Repeatability - Defect/Incident Management - Test Environment Management | MUST |
| **TEST-4** | There will be Test Management Processes covering test completion and Reporting.  Example evidence could include:   - Comprehensive test results captured within test tooling - Incident management on completion - Quality Criteria for exiting testing | MUST |

## Test Environments Requirements

The Test Environment requirements detail the test environment(s) requested by NHS Digital to support testing and assurance of central services, to aid interoperability testing, and the assurance of connecting supplier Solutions.

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Requirements** | **Level** |
| **TEST-ENV-1** | A Digital Care Services supplier whose Solution interoperates with NHS Digital national services (such as PDS, ePS, SCR, eRS, NHAIS, GPES, etc), or provides IM1 or GP Connect APIs, shall provide access to instances of production versions of their Solution(s), such as a Virtual Machine (VM) image, to be installed and maintained in the NHS Digital test laboratory. Or alternatively, provide access to supplier data centre hosted, or cloud-hosted versions, which allow multiple concurrency of connecting systems, such as API consumers for testing.  In this context, the production version means a version of the Solution which is reflective of the supplier’s LIVE estate for that Solution. Where a supplier has multiple instances and version, the supplier will provide access to the majority installed version. | MUST |
| **TEST-ENV-2** | The Supplier must make access available to the latest version 5 days after release in live. If it is provisioned for installation by NHS Digital, then the software installation package must be accompanied with appropriate instructions for installation and the release notes for the release being installed. | MUST |
| **TEST-ENV-3** | The Supplier shall provide access or provision installation any additional requested versions of its Solution(s) within 10 working days of the NHS Digital’s request. These versions could either be compliant or versions for which compliance are being sought. | MUST |
| **TEST-ENV-4** | The Supplier shall ensure that an up to date version of each Supplier Release of its Compliant Solution (including Live APIs) in the suppliers’ LIVE estate is installed, maintained in their own test environment and connected to NHS Digitals’ Path to Live environments (DEV and INT) as required to support the Suppliers’ own testing of a Supplier Release or where required, to support the testing of another Supplier Release and for NHS Digitals’ assurance of the release. | MUST |
| **TEST-ENV-5** | The Supplier must ensure that a non-functional test environment is available to do Volumetrics and Performance testing for their Solution. | MUST |
| **TEST-ENV-6** | The Supplier shall support end-user organisations to aid training of their users on the supplier Solution(s) with Spine connectivity, including all Core Messaging and CIS services, enabled through integration with the SPINE Training environments. | MUST |
| **TEST-ENV-7** | The Supplier must ensure that their test environments support robust access controls (security features) both at Solution level and Infrastructure level so that only authorised users and authorised external connecting supplier Solutions can access the test environment. | MUST |
| **TEST-ENV-8** | The Supplier must ensure that the test environment(s) availability times and any scheduled downtimes for maintenance activities are made known to all the external connecting Solution suppliers and NHS Digital accessing the supplier hosted test environment. Any changes to the known availability times or scheduled downtimes should be communicated to the suppliers and NHS Digital at least two working days in advance. It is acknowledged that there might be compelling reasons in certain circumstances to perform maintenance activities outside the scheduled slots. | MUST |
| **TEST-ENV-9** | The Supplier must either provide appropriate Solution test data (including patient clinical data) in their test environment(s) to aid testing of the external connecting Solution suppliers and for NHS Digital to do assurance activities, or when provided by NHS Digital, the supplier must preload any provided test data (such as PDS test patients). If specified by NHS Digital, the supplier must ensure patient test data meets a minimum set of clinical data.  The test data must contain Synthetic Data only. It must not contain any sensitive or personally identifiable patient data.  The Supplier must ensure that any maintenance releases / emergency patches deployed to their test environment does NOT erase any of the existing test data as this might adversely impact any ongoing testing. | MUST |
| **TEST-ENV-10** | The Supplier shall ensure that the test environment is able to support concurrent testing by multiple external connecting Solution suppliers. The Solution test data must be discrete for each external connecting Solution supplier such that they can test independently of others. | MUST |
| **TEST-ENV-11** | The Supplier shall support backup and restore functions, to allow restoration of the test environment(s) back to the original clean state or a previously backed-up state. | MUST |
| **TEST-ENV-12** | The Supplier shall ensure that the performance of the test Solution is comparable to the LIVE service levels for the restricted volumes in the Test environment, in order to provide a realistic expectation of performance behaviour in the LIVE estate | MUST |
| **TEST-ENV-13** | The Supplier must provide any necessary documentation pertaining to external interfaces to allow the integration of connecting systems. | MUST |
| **TEST-ENV-14** | The Supplier must provide the necessary guidance and access privileges to NHS Digital for interrogating Audit Trail records, system logs and API messaging logs which might aid in early identification of any integration issues. This is applicable where the Supplier has provided the Virtual Machine (VM) images for NHS Digital to host. Where the Supplier is hosting their own system in their own test environment, the Supplier must provide all the necessary support to identify and resolve any integration issues. | MUST |

## Live Environments Requirements

The Live Environment requirements detail the live environment(s) requested by NHS Digital to support testing and assurance of central services, to aid interoperability testing, and the assurance of connecting supplier Solutions.

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Requirements** | **Level** |
| LIVE-ENV-1 | The Supplier must support use of appropriate Solution test data (including patient clinical data) in their live environment(s). That support will ensure that test data can be used and exist in live environments in accordance with NHS Digital guidance on the Use of Synthetic Data in Live Environments which is published as part of Training for Providers. | MUST |

# Capabilities

**Applicable Capabilities**

All suppliers Solutions delivering any Capabilities will need to meet this Standard.

# Roadmap

**Items on the Roadmap which impact or relate to this Standard**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |