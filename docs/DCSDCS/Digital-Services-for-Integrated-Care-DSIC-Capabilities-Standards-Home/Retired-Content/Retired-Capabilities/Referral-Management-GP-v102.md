---
page_id: "13020594177"
space: "DCSDCS"
title: "Referral Management - GP v1.0.2"
version: 1
updated: "2024-05-31T08:32:45.412Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/13020594177/Referral+Management+-+GP+v1.0.2"
labels: ["capability_retired"]
---

# Referral Management - GP v1.0.2

|  |  |
| --- | --- |
| ID {#ReferralManagement-GPv1.0.2-ID} | C11 |
| Version {#ReferralManagement-GPv1.0.2-Version} | 1.0.2 |
| Type {#ReferralManagement-GPv1.0.2-Type} | Capability |
| Category {#ReferralManagement-GPv1.0.2-Category} | Care coordination |
| Status {#ReferralManagement-GPv1.0.2-Status} | Retired |
| Effective Date {#ReferralManagement-GPv1.0.2-EffectiveDate} | 28 Apr 2022 |
| Framework(s) {#ReferralManagement-GPv1.0.2-Framework(s)} | - [GP IT Futures](https://nhse-dsic.atlassian.net/wiki/spaces/GPITF) - [Tech Innovation](https://nhse-dsic.atlassian.net/wiki/spaces/GIFTIF) |

# Description {#ReferralManagement-GPv1.0.2-Description}

Supports the creation of Referral information for Patients and sending referral requests to the e-Referrals Service (e-RS).

# Outcomes {#ReferralManagement-GPv1.0.2-Outcomes}

|  |  |
| --- | --- |
| For a Patient: | Requests to relevant Health and Care Organisations for advice or handover of care that is efficiently managed, in turn providing better quality of care for the Patient. |
| For GP Practice: | Management of Referrals with technology to provide better efficiency to the Organisation, by using mechanisms to create Referral information. |

| **MUST Epics - Describes the minimum functionality required to deliver a Capability. Solutions MUST be successfully evaluated against each Epic and Acceptance Criteria via Capability Assessment in order to be associated with this Capability** |
| --- |
| E00148 - create Referral information for Patients {#ReferralManagement-GPv1.0.2-E00148-createReferralinformationforPatients} As a Health or Care Professional  I want to create Referral information for Patients  So that Referral information is created for Patients when they are referred to other Healthcare Organisations Acceptance Criterion 1: create Referral information for Patients {#ReferralManagement-GPv1.0.2-AcceptanceCriterion1:createReferralinformationforPatients} Given the Health or Care Professional is permitted to create Referral information for Patients  When the Health or Care Professional selects to create Referral information for a Patient  Then the Recipient Healthcare Organisation is recorded  And the Recipient Health or Care Professional is recorded  And the reason for the Referral is recorded  And the referring Staff Member’s information is recorded  And the date of the Referral is recorded  And the type of Referral is recorded as a coded clinical term  And the Referral information is created for the Patient E00148 - Supporting Information {#ReferralManagement-GPv1.0.2-E00148-SupportingInformation}  - Other examples of Referral information MAY include, but are not limited to:    - Unique identifier (this can be the Unique Booking Reference Number (UBRN) used for e-Referrals)   - Status   - Priority   - Specialty   - Service type (e.g. outpatient, direct access service, day case, inpatient) - For coded clinical terms, see Data Standards for requirements  ---  E00149 - e-Referrals Service (e-RS) {#ReferralManagement-GPv1.0.2-E00149-e-ReferralsService(e-RS)} As a Health or Care Professional  I want to send Referral requests to the e-Referrals Service (e-RS) for Patients  So that Referral requests can be made to the e-Referrals Service (e-RS) Acceptance criterion 1: send Referral requests to the e-Referrals Service (e-RS) {#ReferralManagement-GPv1.0.2-Acceptancecriterion1:sendReferralrequeststothee-ReferralsService(e-RS)} Given the Health or Care Professional is permitted to send Referral requests to the e-Referrals Service (e-RS)  When the Health or Care Professional selects to send the Referral request for a Patient  Then the Referral request is sent to the e-Referrals Service (e-RS) E00149 - Additional Implementation Details {#ReferralManagement-GPv1.0.2-E00149-AdditionalImplementationDetails} Solutions MUST comply with the following when implementing this Epic:   - e-Referrals Service (e-RS) Standard |

| **MAY Epics - Describes additional functionality associated with the Capability. Suppliers should consider all MAY Epics as part of their User Research. Suppliers can choose to map their Solutions to these Epics and they will be evaluated via Capability Assessment. Framework Authorities or purchasing organisations may require these Epics as product qualification or requirements criteria** |
| --- |
| E00150 - manage e-Referrals {#ReferralManagement-GPv1.0.2-E00150-managee-Referrals} As a Health or Care Professional  I want to manage e-Referrals  So that electronic Referrals can be made to other Health or Care Professionals for Patients Acceptance criterion 1: create an e-Referral {#ReferralManagement-GPv1.0.2-Acceptancecriterion1:createane-Referral} Given the Health or Care Professional is permitted to manage e-Referrals  When the Health or Care Professional selects to create an e-Referral  Then the e-Referral is created Acceptance criterion 2: view an e-Referral {#ReferralManagement-GPv1.0.2-Acceptancecriterion2:viewane-Referral} Given the Health or Care Professional is permitted to manage e-Referrals  When the Health or Care Professional selects to view an e-Referral  Then the e-Referral is displayed Acceptance criterion 3: amend an e-Referral {#ReferralManagement-GPv1.0.2-Acceptancecriterion3:amendane-Referral} Given the Health or Care Professional is permitted to manage e-Referrals  When the Health or Care Professional selects to amend an e-Referral  Then the e-Referral is amended Acceptance criterion 4: delete an e-Referral {#ReferralManagement-GPv1.0.2-Acceptancecriterion4:deleteane-Referral} Given the Health or Care Professional is permitted to manage e-Referrals  When the Health or Care Professional selects to delete an e-Referral  Then the e-Referral is deleted   ---  E00151 - manage manual Referrals {#ReferralManagement-GPv1.0.2-E00151-managemanualReferrals} As a Health or Care Professional  I want to manage manual Referrals  So that the process of manually referring Patients to other Healthcare Organisation is supported Acceptance criterion 1: create a manual Referral {#ReferralManagement-GPv1.0.2-Acceptancecriterion1:createamanualReferral} Given the Health or Care Professional is permitted to manage manual Referrals  When the Health or Care Professional selects to create a manual Referral  Then the manual Referral is created Acceptance criterion 2: view a manual Referral {#ReferralManagement-GPv1.0.2-Acceptancecriterion2:viewamanualReferral} Given the Health or Care Professional is permitted to manage manual Referrals  When the Health or Care Professional selects to view a manual Referral  Then the manual Referral is displayed Acceptance criterion 3: amend a manual Referral {#ReferralManagement-GPv1.0.2-Acceptancecriterion3:amendamanualReferral} Given the Health or Care Professional is permitted to manage manual Referrals  When the Health or Care Professional selects to amend a manual Referral  Then the manual Referral is amended Acceptance criterion 4: delete a manual Referral {#ReferralManagement-GPv1.0.2-Acceptancecriterion4:deleteamanualReferral} Given the Health or Care Professional is permitted to manage manual Referrals  When the Health or Care Professional selects to delete a manual Referral  Then the manual Referral is deleted E00151 - Supporting Information {#ReferralManagement-GPv1.0.2-E00151-SupportingInformation}  - An example of a manual Referral is producing a Referral letter that automatically contains Referral and clinical information from the Electronic Patient Record (EPR)  ---  E00152 - Referral reports {#ReferralManagement-GPv1.0.2-E00152-Referralreports} As a Health or Care Professional  I want to view Referral reports  So that reports relating to Referrals for Patients can be viewed Acceptance criterion 1: view a Referral report {#ReferralManagement-GPv1.0.2-Acceptancecriterion1:viewaReferralreport} Given the Health or Care Professional is permitted to view Referral reports  When the Health or Care Professional selects to view a Referral report  Then the report is displayed E00152 - Supporting Information {#ReferralManagement-GPv1.0.2-E00152-SupportingInformation}  - Types of Referral reports MAY include, but are not limited to:    - Reporting by Referrer   - Reporting by Recipient e.g.      - Service     - Healthcare Organisation     - Individual Health or Care Professional |

| **Other Applicable Standards** |
| --- |
| Suppliers will have to attain compliance with this Standard during the compliance stage before they can be live on a framework with this Capability:   - Interoperability Standard - Overarching Standards |

| **Items on the Roadmap which impact or relate to this Capability** |
| --- |
| | Roadmap Item | | --- | | No content found. | |