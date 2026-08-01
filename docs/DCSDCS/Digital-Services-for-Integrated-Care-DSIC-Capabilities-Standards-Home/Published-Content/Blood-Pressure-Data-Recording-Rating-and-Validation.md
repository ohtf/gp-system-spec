---
page_id: "15179644969"
space: "DCSDCS"
title: "Blood Pressure - Data Recording, Rating and Validation"
version: 4
updated: "2026-07-06T13:23:13.739Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/15179644969/Blood+Pressure+-+Data+Recording+Rating+and+Validation"
labels: ["reference_page"]
---

# Blood Pressure - Data Recording, Rating and Validation

|  |  |
| --- | --- |
| ID {#BloodPressure-DataRecording,RatingandValidation-ID} | R18 |
| Version {#BloodPressure-DataRecording,RatingandValidation-Version} | 1.0.1 |
| Type {#BloodPressure-DataRecording,RatingandValidation-Type} | Reference |

# Introduction {#BloodPressure-DataRecording,RatingandValidation-Introduction}

This page defines the data recording requirements, validation rules, and rating criteria for blood pressure readings. Its purpose is to ensure that recorded values are clinically plausible and that all transmitted data is accurate and reliable.

The following sections are included:

- **Ambulatory Blood Pressure Measurement (ABPM) SNOMED Codes** – Details the SNOMED codes that are to be used for an Ambulatory Blood Pressure Measurement (ABPM) reading.
- **Clinic Blood Pressure SNOMED Codes** – Details the SNOMED codes that are to be used for a clinic blood pressure reading.
- **Blood Pressure Reading Validation** – Defines the validation rules and expected actions for blood pressure readings.
- **Clinic Blood Pressure Rating Values** – Specifies the parameters used to determine blood pressure ratings based on clinic blood pressure readings.
- **Ambulatory Blood Pressure Measurement (ABPM) Rating Values** – Specifies the parameters used to determine blood pressure ratings based on Ambulatory Blood Pressure Measurement (ABPM) readings.

## Ambulatory Blood Pressure Measurement (ABPM) SNOMED Codes {#BloodPressure-DataRecording,RatingandValidation-AmbulatoryBloodPressureMeasurement(ABPM)SNOMEDCodes}

Where Ambulatory Blood Pressure Measurement (ABPM) readings are recorded they are to be recorded using:

- [Average ambulatory day interval blood pressure](https://simplifier.net/guide/gp-connect--update-record--itk3/Home/Build/Handling-observations?version=1.2.1-public-beta)
- [Average ambulatory night interval blood pressure](https://simplifier.net/guide/gp-connect--update-record--itk3/Home/Build/Handling-observations?version=1.2.1-public-beta)
- [Average 24 hour blood pressure](https://simplifier.net/guide/gp-connect--update-record--itk3/Home/Build/Handling-observations?version=1.2.1-public-beta)
- [Average ambulatory blood pressure](https://simplifier.net/guide/gp-connect--update-record--itk3/Home/Build/Handling-observations?version=1.2.1-public-beta)

## Clinic Blood Pressure SNOMED Codes {#BloodPressure-DataRecording,RatingandValidation-ClinicBloodPressureSNOMEDCodes}

Clinic Blood Pressure readings to be recorded using:

- [On examination - blood pressure reading](https://simplifier.net/guide/gp-connect--update-record--itk3/Home/Build/Handling-observations?version=1.2.1-public-beta)

---

## Blood Pressure Reading Validation {#BloodPressure-DataRecording,RatingandValidation-BloodPressureReadingValidation}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Parameter** | **Threshold** | **Outcome** | **Action** | **Message (Example)** |
| Systolic BP | <71mmHg | Warning Message | Warning can be bypassed but with a reason | Unusual reading. Please re-check the measurement. |
| Systolic BP | >199 mmHg | Warning Message | Warning can be bypassed but with a reason | Unusual reading. Please re-check the measurement. |
| Systolic BP | >299 mmHg | Error Message | Consultation information cannot be submitted. | The value you have entered is clinically impossible. Please re-check the measurement. |
| Diastolic BP | <41 mmHg | Warning Message | Warning can be bypassed but with a reason | Unusual reading. Please re-check the measurement. |
| Diastolic BP | >119 mmHg | Warning Message | Warning can be bypassed but with a reason | Unusual reading. Please re-check the measurement. |
| Systolic > diastolic | Systolic value must be greater than diastolic value | Error Message | Consultation information cannot be submitted. | The value you have entered is clinically impossible. Please re-check the measurement. |
| Pulse rate | <50bpm | Warning Message | Warning can be bypassed but with a reason | Unusual reading. Please re-check the measurement. |
| Pulse rate | >115bpm | Warning Message | Warning can be bypassed but with a reason | Unusual reading. Please re-check the measurement. |
| Pulse pressure (difference between systolic and diastolic values) | >40mmHg | Warning Message | Warning can be bypassed but with a reason | Unusual reading. Please re-check the measurement. |
| Negative values | No negative values | Error Message | Consultation information cannot be submitted. | The value you have entered is clinically impossible. Please re-check the measurement. |

---

## Clinic Blood Pressure Rating Values {#BloodPressure-DataRecording,RatingandValidation-ClinicBloodPressureRatingValues}

When determining the rating use the highest value from the diastolic or systolic value. For example, if Diastolic is 70 mmHg and Systolic is 145 mmHg, the rating should be suggested as “High”.

| **Diastolic Clinic Blood Pressure Reading** | **Systolic Clinic Blood Pressure Reading** | **Blood Pressure Rating** |
| --- | --- | --- |
| <60mmHg | <90mmHg | Low |
| >=60mmHg and <=89mmHg | >=90mmHg and <=139mmHg | Normal |
| >=90mmHg and <=119mmHg | >=140mmHg and <=179mmHg | High |
| >=120mmHg | >=180mmHg | Very High |

## Ambulatory Blood Pressure Measurement (ABPM) Blood Pressure Rating Values {#BloodPressure-DataRecording,RatingandValidation-AmbulatoryBloodPressureMeasurement(ABPM)BloodPressureRatingValues}

When determining the rating use the highest value from the diastolic or systolic value. For example, if Diastolic is 70 mmHg and Systolic is 145 mmHg, the rating should be suggested as “Stage 1 Hypertension”.

| **Diastolic ABPM Blood Pressure Reading** | **Systolic ABPM Blood Pressure Reading** | **ABPM Blood Pressure Rating - use the highest rating for either the diastolic or systolic value** |
| --- | --- | --- |
| >=60mmHg and <=84mmHg | >=90mmHg and <=134mmHg | Normal |
| >=85mmHg and <=94mmHg | >=135mmHg and <=149mmHg | Stage 1 Hypertension |
| >=95mmHg and <=114mmHg | >=150mmHg and <=169mmHg | Stage 2 Hypertension |
| >=115mmHg | >=170mmHg | Stage 2 Hypertension (Very High Blood Pressure) |