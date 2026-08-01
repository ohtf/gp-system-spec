---
page_id: "1391134857"
space: "DCSDCS"
title: "National Medicines Verification System v1.0.0"
version: 10
updated: "2022-08-15T10:15:13.137Z"
source_url: "https://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391134857/National+Medicines+Verification+System+v1.0.0"
labels: ["interop_standard_retired"]
---

# National Medicines Verification System v1.0.0

|  |  |
| --- | --- |
| ID | S71 |
| Version | 1.0.0 |
| Type | Interoperability Standard |
| Status | Retired |
| Effective Date | 01 Apr 2019 |
| Framework(s) | GP IT Futures |

- [Introduction](#NationalMedicinesVerificationSystemv1.0.0-Introduction)
  - [Resources](#NationalMedicinesVerificationSystemv1.0.0-Resources)
- [Compliance and Assurance](#NationalMedicinesVerificationSystemv1.0.0-ComplianceandAssurance)
- [Testing](#NationalMedicinesVerificationSystemv1.0.0-Testing)
- [Environments](#NationalMedicinesVerificationSystemv1.0.0-Environments)
- [Requirements](#NationalMedicinesVerificationSystemv1.0.0-Requirements)
- [Documentation](#NationalMedicinesVerificationSystemv1.0.0-Documentation)
- [Dependencies](#NationalMedicinesVerificationSystemv1.0.0-Dependencies)
- [Roadmap](#NationalMedicinesVerificationSystemv1.0.0-Roadmap)

# Introduction {#NationalMedicinesVerificationSystemv1.0.0-Introduction}

The Falsified Medicines Directive is an EU directive (EU legislation EU/2011/62) that will become UK law (regardless of Brexit) on 9th February 2019. Any prescribed medicines dispensed beyond that date will require a 2D barcode to be scanned to "decommission" the medicine from the supply chain. This ruling applies to *all* events where a medicine is dispensed.  This will particularly impact dispensing doctors but also clinicians providing vaccinations etc.  GP practices will therefore be subject to the same processes as pharmacists.  Failure to comply with this law beyond the effective date will be a criminal offence and so GP practices are required to have a Solution in place to support this process.

A central European "Hub" will store data of all medicines to be supplied throughout Europe and there will be National Hubs in each of the EU member states.  A Solution compliant with this Standard is required to connect to the UK hub of the National Medicines Verification System (NMVS).

National Hubs are provided by a third-party non-profit organisation called SecurMed. The NMVS has been developed by a sub-contractor called Arvato Systems Healthcare and it is important to note that the infrastructure, interface specifications and testing processes are controlled by this company not NHS Digital.

A Solution compliant with FMD may be standalone or integrated with the GP system(s) and may use dedicated hand-held scanners or apps on mobile phones.

Integration with the National Medicine Verification System (NMVS) is via a web services API compliant with the following web standards:

- Simple Object Access Protocol (SOAP) 1.2
- Web Services Definition Language (WSDL) 1.1
- eXtensible Markup Language (XML)
- WS-I Basic Profile 1.1.1

The NMVS API allows clients to verify the status of medicines and decommission medicines from the supply chain via single or bulk operations and supports synchronous and asynchonous connection modes.

## Resources {#NationalMedicinesVerificationSystemv1.0.0-Resources}

https://www.securmed.org.uk/what-is-fmd/

https://www.securmed.org.uk/wp-content/uploads/2018/09/arvato\_it\_ssp\_workshop\_presentation.pdf

https://ukfmdworkinggroup.wordpress.com/faqs/

# Compliance and Assurance {#NationalMedicinesVerificationSystemv1.0.0-ComplianceandAssurance}

Suppliers need to register on the NMVS portal and undertake the baseline testing process as described.

# Testing {#NationalMedicinesVerificationSystemv1.0.0-Testing}

For interface testing details please refer to the NMVS portal (registration required).

The broad stages are:

- Generate a test pack set
- Connect to the NMVS sandbox environment
- Test interface
- Undergo Baseline Testing

# Environments {#NationalMedicinesVerificationSystemv1.0.0-Environments}

The "NMVS Sandbox" has web services endpoints for testing connected applications.

For details please refer to the NMVS portal (registration required).

# Requirements {#NationalMedicinesVerificationSystemv1.0.0-Requirements}

| ID | Description | Level |
| --- | --- | --- |
| NMV-01 | Solutions which implement the Medicines Verification capability must be compliant with the National Medicines Verification System. | MUST |

# Documentation {#NationalMedicinesVerificationSystemv1.0.0-Documentation}

Implementation Guide and testing documentation available on the NMVS portal (registration required).

# Dependencies {#NationalMedicinesVerificationSystemv1.0.0-Dependencies}

# Roadmap {#NationalMedicinesVerificationSystemv1.0.0-Roadmap}

| Title |
| --- |
| No content found. |