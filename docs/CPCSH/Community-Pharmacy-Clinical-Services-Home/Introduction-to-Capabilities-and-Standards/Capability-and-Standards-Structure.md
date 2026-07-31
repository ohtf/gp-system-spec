---
page_id: "14449082371"
space: "CPCSH"
title: "Capability and Standards Structure"
version: 1
updated: "2025-11-03T15:34:32.346Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/CPCSH/pages/14449082371/Capability+and+Standards+Structure"
labels: []
---

# Capability and Standards Structure

Capabilities and Standards will each have the content detailed in the attributes table below:

|  |  |
| --- | --- |
| **ID** | Each Capability and Standard has a unique alphanumeric identifier. The letter "C" indicates a Capability, an "S" indicates a Standard and “SCS” indicates a Supplementary Care Standard. The number is arbitrary and does not have any additional meaning such as priority, sequence or inter-relationships. This allows for the identification of Capabilities and Standards in a consistent manner. |
| **Version** | Each Capability and Standard has a version number. Each Capability and Standard can change independently and it's version number will change accordingly. Version numbers are subject to change depending on the nature of the change (e.g. major, minor, patch). There is no relationship between the version numbers of different Capabilities and Standards. |
| **Type** | Indicates a Capability or a Standard and where applicable, defines the type of Standard:   - Capability - Describes the business needs at the highest level. - Non-Overarching Standard - Express technical and non-functional requirements for a specific interface or integration. - Overarching Standard - Expresses overarching technical and non-functional requirements. - Supplementary Care Standard - Describes the functional, technical and/or operating conditions required to deliver a specific service within a health and care setting. |
| **Category** | Only Capabilities have the Category field. Category is used to group related Capabilities on the Buying Catalogue. |
| **Status** | Each Capability and Standard will have one of five statuses:   - Draft - Whilst in Draft status, Suppliers can provide feedback about the content of the Capability or Standard, which is subject to change at this stage. - Published - When this status is reached, it is expected that the contents of the Capability or Standard are fully defined, agreed, signed off and are not expected to change. - Effective - Used to indicate that Suppliers should now be compliant with the Capability or Standard. - Deprecated - The content is still visible to Suppliers but is Deprecated for a period of time before it is Retired. Suppliers will no longer be able to be assessed against Deprecated content however compliant Solutions must remain compliant until the Capability or Standard is Retired. - Retired - The content is now Retired and located under [“Retired Content”](../../../DCSDCS/Digital-Services-for-Integrated-Care-DSIC-Capabilities-Standards-Home/Retired-Content/index.md) for reference. |
| **Effective Date** | Capabilities and Standards will have an Effective Date by which Suppliers must comply with the Capability or Standard.  Suppliers will need to have achieved compliance against relevant Effective Capabilities and Standards (see Status above) in order to onboard on to the Buying Catalogue. There may be other Capabilities and Standards that Suppliers need to achieve compliance with in order to be awarded a place on a Contracting Vehicle. |
| **Contracting Vehicle(s)** | Indicates the commercial Contracting Vehicle a Capability or Standard is applicable to. |

### Structure of Capabilities

Describes the business needs at the highest level.

|  |  |
| --- | --- |
| **Description** | A concise description of the purpose of the Capability covering the mandatory scope. |
| **Outcomes** | Describes the main users of the Capability and the outcomes they want to achieve from using a Solution that meets the Capability based on the mandatory scope. |
| **Epics and Acceptance Criteria** | Epics are individual high level business requirements and describes features relevant to the Capabilities they belong to. All Epics together define the full scope of a Capability.  The Acceptance Criteria associated with an Epic defines the minimum expected functions a Supplier’s Solution must deliver, and are test scenarios that will be used during the Capability Assessment stage of Onboarding to establish whether a Supplier’s Solution meets the Epic or not. In order to pass any Epic, all associated Acceptance Criteria for that Epic must pass the assessment.  Epics are classified as either MUST or MAY Epics and all Epics will be assessed during the Capability Assessment stage of Onboarding. It is recommended that Suppliers consider all Epics as part of User Research to understand what the Minimal Viable Product (MVP) is for their users. MUST Epics MUST Epics are mandatory and used to confirm during the Capability Assessment stage of Onboarding that a Solution delivers the minimum required for a Capability. A Supplier Solution needs to meet all MUST Epics in order to Pass Capability Assessment for a Capability. MAY Epics Describes additional functionality associated with the Capability. These Epics are not mandatory, unless mandated by the Contracting Vehicle or Supplementary Care Standard. Suppliers should consider all MAY Epics as part of their User Research. Suppliers can choose to map their Solutions to these Epics and they will be evaluated via Capability Assessment. Contracting Authorities or purchasing organisations may require these Epics as product qualification or requirements criteria. |
| **Additional Implementation Details** | Additional Implementation Details are mandatory details related to a specific Epic and are assessed during the Assurance stage of Onboarding.  These details can include references to other Standards and Suppliers will need to complete any separate assurance activities related to those Standards. Additional Implementation Details can also include information of how any functionality should be implemented. |
| **Supporting Information** | This information may be useful to Suppliers when implementing the related Epic, but is not mandatory and is for guidance only. |
| **Roadmap** | The Roadmap section summarises future changes and opportunities for Suppliers in relation to the Capability or Standard. These are links to the individual Roadmap pages which provide further information on the Roadmap Item. |

### Structure of Overarching Standards

Expresses technical and non-functional requirements.

|  |  |
| --- | --- |
| **Description** | A concise description of the purpose of the Standard covering the mandatory scope. |
| **Baseline Assurance Standard Requirements** | The Baseline Assurance Standard Requirements have the following attributes:   - **Applicable Contracting Vehicle -**Specifies which Contracting Vehicle(s) the requirement applies to (some requirements may only apply to certain Contracting Vehicles and not all). - **ID -** Each requirement within a Standard will have a unique ID so it can be recognised during compliance. - **Requirement -** The description of each requirement within a Standard that will be used to determine compliance of a Solution with the Standard. - **Level** - Each requirement within a Standard will have a level as defined in the [RFC 2119.1](https://tools.ietf.org/html/rfc2119) and Ancillary Document (Change Management Process and Roadmap Content). - **Category A/ Category B/ Category C-** Solutions are categorised as A/B/C to specify the level of assurance that a Supplier will complete as part of the Baseline Assurance Standard Requirement. |
| **Further Requirements** | The Further Requirements have the following attributes:   - **Applicable Contracting Vehicle -**Specifies which Contracting Vehicle(s) the requirement applies to (some requirements may only apply to certain Contracting Vehicles and not all). - **ID -** Each requirement within a Standard will have a unique ID so it can be recognised during compliance. - **Requirement -** The description of each requirement within a Standard that will be used to determine compliance of a Solution with the Standard. - **Level** - Each requirement within a Standard will have a level as defined in the [RFC 2119.1](https://tools.ietf.org/html/rfc2119) and Ancillary Document (Change Management Process and Roadmap Content). - **Category A/ Category B/ Category C-** Solutions are categorised as A/B/C to specify the level of assurance that a Supplier will complete as part of the Further Requirement. |
| **Roadmap** | The Roadmap section summarises future changes and opportunities for Suppliers in relation to the Overarching Standard. These are links to the individual Roadmap pages which provide further information on the Roadmap Item. |

### Structure of Non-Overarching Standards

Technical and non-functional requirements for a specific interface or integration.

|  |  |
| --- | --- |
| **Introduction** | A concise description of the purpose of the Standard covering the mandatory scope. |
| **Requirements** | The Requirements have the following attributes:   - **Applicable Suppliers** - Specifies which Supplier type the requirement applies to. - **ID** - Each requirement within a Standard will have a unique ID so it can be recognised during compliance. - **Requirement -** The description of each requirement within a Standard that will be used to determine compliance of a Solution with the Standard. - **Level** - Each requirement within a Standard will have a level as defined in the [RFC 2119.1](https://tools.ietf.org/html/rfc2119) and Ancillary Document (Change Management Process and Roadmap Content). |
| **Compliance, Assurance & Testing** | The guidance on Assurance requirements that need to be met in order to comply with the requirements of the Standard. |
| **Documentation** | Any relevant documentation to assist with the development of the Standard |
| **Dependencies** | Any relevant dependencies for implementing this Standard including any non-overarching Standards within the Capabilities and Standards model that are dependents. |
| **Roadmap** | The Roadmap section summarises future changes and opportunities for Suppliers in relation to the non-overarching Standard. These are links to the individual Roadmap pages which provide further information on the Roadmap Item. |

### Structure of Supplementary Care Standards

Describes the functional, technical and/or operating conditions required to deliver a specific service within a health and care setting.

|  |  |
| --- | --- |
| **Description** | A concise description of the purpose of the Supplementary Care Standard covering the broad scope. |
| **Functional Requirements** | The functional requirements that need to be met in order to comply with the Supplementary Care Standard. |
| **Secondary Artefacts** | Non-functional and overarching requirements that need to be met in order to comply with the Supplementary Care Standard. |
| **Requirement ID** | Each requirement within a Supplementary Care Standard will have a unique ID so it can be recognised during compliance. |
| **Requirement** | The description of each requirement within a Supplementary Care Standard that will be used to determine compliance of a Solution with the Standard. |
| **Level** | Each requirement within a Standard will have a level as defined in the [RFC 2119.1](https://tools.ietf.org/html/rfc2119) and Ancillary Document (Change Management Process and Roadmap Content). |
| **Theme** | For Secondary Artefact requirements only, categorises similar or related requirements. |
| **Roadmap** | The Roadmap section summarises future changes and opportunities for Suppliers in relation to the Supplementary Care Standard. These are links to the individual Roadmap pages which provide further information on the Roadmap Item. |