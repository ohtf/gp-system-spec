---
page_id: "1391134046"
space: "DCSDCS"
title: "NHS Cloud Hosting Standards & Guidance"
version: 3
updated: "2020-10-29T16:17:27.706Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391134046/NHS+Cloud+Hosting+Standards+Guidance"
labels: []
---

# NHS Cloud Hosting Standards & Guidance

The following is a summary of the "NHS and social care data: off-shoring and the use of public cloud services" gathered from cloud guidance information published by NHS Digital. It makes clear what evidence is to be sought from a supplier, where it is deemed necessary to assure compliance with the 4 step process.

Some key points of note:

- All decisions in relation to the security of data are the responsibility of the data controller(s). Also, in many cases organisations will have a SIRO responsible for data and cyber security.
- Where a professional body exists, there is certainly merit in seeking their approval for the migration of data to cloud, but ultimately the data controller remains the key approver.
- Data Controllers need to understand the risks of moving to cloud, and any impact.
- Data controllers must take into account the standard CIA triad (confidentiality, Integrity, Availability), and also other relevant factors, including, but not limited to, cost, security, resilience, capability and funding.

The 4 steps to inform the data controller on a risk based decision are detailed below.

## Step 1 - Understand the data {#NHSCloudHostingStandards&Guidance-Step1-Understandthedata}

All data managed by NHS and social care organisations should be treated as OFFICIAL or OFFICIAL-SENSITIVE data, in line with the Government Security Classification Policy.

NHS Digital has further elaborated the very broad classifications. The Health and Social Care Cloud Risk Model is more granular than the Government Security Classification Policy.

### EVIDENCE requested for step 1: {#NHSCloudHostingStandards&Guidance-EVIDENCErequestedforstep1:}

1. The supplier needs to provide evidence that they have identified all data, data types, and attributes, and assessed it against the model.
2. Binary objects identified within the data set, such as JPEG, PDF, etc, can still be classified by their content. The supplier needs to evidence an understanding of the percentage splits between data types, which may alter the overall the classification.

## Step 2- Assess the Risks {#NHSCloudHostingStandards&Guidance-Step2-AssesstheRisks}

The NHS Digital Health and Social Care data risk framework (cloud\_risk\_framework\_document\_final.pdf) and associated risk tool (health\_and\_social\_care\_data\_risk\_model.xlsx) are both used to establish the risk level of the data. Typically Personally Identifiable Data (PID) would be Level 5.

### EVIDENCE requested for step 2: {#NHSCloudHostingStandards&Guidance-EVIDENCErequestedforstep2:}

1. Completed risk model indicating the risk level established from the data detailed in step 1.
2. The Health and Social Care Cloud Risk Model also considers service classification (Bronze/Silver/Gold/Platinum), and suppliers will need a statement to back-up their selection of the classification.

## Step 3 - Implement the appropriate controls {#NHSCloudHostingStandards&Guidance-Step3-Implementtheappropriatecontrols}

Care organisations, such as GPs, retain the data controller responsibilities and they are therefore ultimately responsible for ensuring that proportionate controls are put in place to mitigate all risks. The data controllers may rightly request to see these controls (proposed by the supplier) before considering any migration to cloud.

### EVIDENCE requested for step 3: {#NHSCloudHostingStandards&Guidance-EVIDENCErequestedforstep3:}

1. The supplier will provide a completed table from the "cloud\_security\_good\_practice\_guide\_final1", with a statement (or linked evidence) against each guidance line item which is applicable for the data classification level identified at step 2.
2. Prior to implementation - where there are many data controllers using a Solution (such as a GP system), NHS Digital would request evidence of the comms strategy to inform all data controllers, seeking any dissent based on the identified risk.
3. Prior to implementation - consideration around GDPR: The supplier should state they have completed and provide if requested to the Catalogue Authority, a Data Protection Impact Assessment (DPIA), plus confirm adherence to the relevant data protection legislation.

## Step 4 - Monitoring the Implementation {#NHSCloudHostingStandards&Guidance-Step4-MonitoringtheImplementation}

All cloud providers take on data processor responsibilities, with Care organisations (e.g. GP practices) retaining the data controller responsibilities, and they must ensure the selected cloud provider remains fit for purpose.

Clearly where compliance is being undertaken by NHS Digital, the data controllers will likely be relying on NHS Digital's ongoing involvement e.g. NHS Digital Security team are working annually with cloud providers to validate their industry standards compliance, including areas such as penetration testing.

### EVIDENCE requested for step 4: {#NHSCloudHostingStandards&Guidance-EVIDENCErequestedforstep4:}

1. Within a contractual framework, such as GP IT Futures, suppliers will be obliged to evidence any external accreditations at the point of renewal. This will include those external standards evidenced during step 3.

## NHS Digital Associated Cloud Guidance Links: {#NHSCloudHostingStandards&Guidance-NHSDigitalAssociatedCloudGuidanceLinks:}

|  |
| --- |
| NHS and social care data: off-shoring and the use of public cloud services |
| NHS and social care data: off-shoring and the use of public cloud services guidance |
| Health and social care cloud risk framework |
| Health and social care data risk model |
| Health and social care cloud security one page overview |