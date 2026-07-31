---
page_id: "1391133974"
space: "DCSDCS"
title: "National Record Locator Service (NRLS)"
version: 3
updated: "2019-04-04T12:50:32.624Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391133974/National+Record+Locator+Service+NRLS"
labels: ["reference_page"]
---

# National Record Locator Service (NRLS)

|  |  |
| --- | --- |
| ID | R6 |
| Version | 1.0.0 |
| Type | Reference |

# Summary

The National Record Locator Service (NRLS) aims to provide a national capability for locating and, ultimately, sharing patient records across health and care systems. A one-stop demonstrator of the NRLS capability can also be [accessed here](https://nrls.digital.nhs.uk/), detailing what the capability is, how it works, the benefits it might bring in the context of their phase 1 sites (ambulance trusts and mental health trusts). The site also directs interested parties to the more technical side of NRLS where the API / code can be accessed.

Further information is available at the [NRLS web site](https://developer.nhs.uk/apis/nrls/).

The current timetable is in the following phases:

- Phase 1: Record Location.  Use of the NRLS to finding where the record for a patient is located.  This is in demo now with 5 Mental Health Trusts and Ambulance Trusts and will be live at end of November 2018.
- Phase 2: Record Retrieval.  Intended for delivery around Q2 2019. Specifications including defined record types and other metadata are currently being finalised.
- Phase 3: Social Care rollout
- Phase 4: full uptake across Health and Social care by Q1 2020

Record location is supported by the NRLS API and the Summary Care Record application (SCRa).

While not currently mandated, GP system suppliers are encouraged to start building phase 1 access via the API.  This will provide clinicians with the ability to locate records such as mental health crisis plans for their patients.

In the near future, specific use cases around Digital Child Health and Digital Maternity will require GP systems to integrate with the NRLS API.

# Documentation

| **Resource** | **Intended Audience** | **Location** |
| --- | --- | --- |
| Interactive Guide   - *What the NRLS is* - *What the index information within the NRLS looks like* - *How the NRLS could feature within your work routine* - *The benefits of the NRLS* | Clinical | <https://nrls.digital.nhs.uk/> |
| API specification  *Describes to developers how to integrate with NRLS* | Technical | <https://developer.nhs.uk/apis/nrls/> |
| API client implementation guide  *The guide complements the API specification by showing developers one way that an NRS client application can be built* | Technical | <https://github.com/nhsconnect/nrls-reference-implementation/wiki> |
| NRLS Reference implementation  *An implementation of the NRLS service. This service gives people a means to test their**client implementations. Crucially this service is publicly accessible over the internet thus lowering the barrier to adoption.* | Technical | <https://data.developer.nhs.uk/nrls-ri> |
| Consumer User Guide  *Describes how to perform an NRLS query via SCRa and helps the end user to interpret the results* | Clinical | Will be sent direct to those Organisations wishing to integrate with NRLS |
| Provider User Guide  *Advice for Provider organisations around how to manage the lifecycle of their Pointers such when to creation of a new Pointer, when to replace an existing Pointer and when deletion is appropriate* | Clinical and Technical | Will be sent direct to those Organisations wishing to integrate with NRLS |