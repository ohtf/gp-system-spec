---
page_id: "1391133668"
space: "DCSDCS"
title: "Unstructured Data Extraction v1.0.1"
version: 9
updated: "2023-05-22T11:12:32.854Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133668/Unstructured+Data+Extraction+v1.0.1"
labels: ["capability_retired"]
---

# Unstructured Data Extraction v1.0.1

|  |  |
| --- | --- |
| ID | C19 |
| Version | 1.0.1 |
| Type | Capability |
| Status | Retired |
| Effective Date | 31 Dec 2019 |
| Framework(s) | - GP IT Futures - Tech Innovation |

Full or Partial Capability status. For this Capability, Solutions are required to meet a minimum of one MUST EPIC and associated acceptance criteria but not all MUST EPICs (where there are multiple MUST EPICS) to achieve Partial Capability Status, or; to meet all MUST EPICs and their associated acceptance criteria to achieve Full Capability Status.

# Description

Enables automated and manual interpretation and extraction of structured data from paper documents and unstructured electronic documents to support their classification and matching with Patient Records.

# Outcomes

|  |  |
| --- | --- |
| For General Practice: | Automated classification and data population from documents to Patient Records resulting in reduction in administrative overheads. |

**MUST Epics - Epics and acceptance criteria will be evaluated during the Capability Assessment Stage of Onboarding**

### C19E1 - document classification

As a Practice User

I want Document classification

So that Documents are classified

#### Acceptance criterion 1: view document classification

Given the Practice User is permitted to view document classifications

When the Practice User chooses to view a document classification

Then the document properties are displayed

And the document attributes are displayed

And the document classification is displayed

And the document coded entries are displayed

#### Acceptance criterion 2: automated document classification

Given automated document classification is enabled

When there are documents to be classified

Then automated document classification occurs

#### Acceptance criterion 3: approve automated document classification

Given the Practice User is permitted to classify documents

And there are documents that have been classified automatically

When the Practice User chooses to approve the automated document classification

Then the automated document classification is retained

#### Acceptance criterion 4: reject automated document classification

Given the Practice User is permitted to classify documents

And there are documents that have been classified automatically

When the Practice User chooses to reject the automated document classification

Then the automated document classification is removed

#### Acceptance criterion 5: classify a document

Given the Practice User is permitted to classify documents

When the Practice User chooses to classify a document

Then the document is classified

#### Acceptance criterion 6: amend document classification

Given the Practice User is permitted to classify documents

When the Practice User chooses to amend a document classification

Then the document classification is amended

---

### C19E2 - manage Document Classification rules

As a Practice User

I want to manage Document Classification rules

So that there are Document Classification rules

#### Acceptance criterion 1: create Document Classification rules

Given the Practice User is permitted to create Document Classification rules

When the Practice User chooses to create a Document Classification rule

Then the Document Classification rule is created

#### Acceptance criterion 2: amend Document Classification rules

Given the Practice User is permitted to amend Document Classification rules

When the Practice User chooses to amend a Document Classification rule

Then the Document Classification rule is amended

#### Acceptance criterion 3: enable Document Classification rules

Given the Practice User is permitted to enable Document Classification rules

When the Practice User chooses to enable a Document Classification rule

Then the Document Classification rule is enabled

#### Acceptance criterion 4: disable Document Classification rules

Given the Practice User is permitted to disable Document Classification rules

When the Practice User chooses to disable a Document Classification rule

Then the Document Classification rule is disabled

#### Acceptance criterion 5: delete Document Classification rules

Given the Practice User is permitted to delete Document Classification rules

When the Practice User chooses to delete a Document Classification rule

Then the Document Classification rule is deleted

---

### C19E3 - document and Patient matching

As a Practice User

I want Documents to be matched with Patients

So that Documents are matched with Patients

#### Acceptance criterion 1: view Patient matching

Given the Practice User is permitted to view the matched Patient for a document

When the document is matched to a Patient

Then the Practice User can see the matched Patient

#### Acceptance criterion 2: automated document and Patient matching

Given automated document and Patient matching is enabled

When there are documents to be matched with Patients

Then the documents are automatically matched with Patients

#### Acceptance criterion 3: approve automated document and Patient matching

Given the Practice User is permitted to match documents with Patients

And there are documents that have been automatically matched with Patients

When the Practice User chooses to approve an automated document and Patient match

Then the document is matched with the Patient

#### Acceptance criterion 4: reject automated document and Patient matching

Given the Practice User is permitted to match documents with Patients

And there are documents that have been automatically matched with Patients

When the Practice User chooses to reject an automated document and Patient match

Then the document is no longer matched to the Patient

#### Acceptance criterion 5: match documents to Patients

Given the Practice User is permitted to match documents with Patients

When the Practice User chooses to match a document with a Patient

Then the document is matched with the Patient

#### Acceptance criterion 6: remove document and Patient matching

Given the Practice User is permitted to match documents with Patients

When the Practice User chooses to remove the match of a document with a Patient

Then the document is not matched with the Patient

**Capability Specific Standard**

Suppliers will have to attain compliance with this Standard during the compliance stage before they can be live on a framework with this Capability:

- Unstructured Data Extraction - Standard v1.0.1
**Other Applicable Standards**

Suppliers will also have to attain compliance with these additional Standards during the compliance stage before they can be live on a framework with this Capability:

- Interoperability Standard
- Overarching Standards
**Items on the Roadmap which impact or relate to this Capability**

Suppliers will not be assessed or assured on these Roadmap Items as part of Onboarding

| Roadmap Item |
| --- |
| No content found. |