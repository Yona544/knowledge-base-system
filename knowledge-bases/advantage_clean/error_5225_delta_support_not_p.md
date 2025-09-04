---
title: Error 5225 Delta Support Not P
slug: error_5225_delta_support_not_p
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5225_delta_support_not_p.htm
source: Advantage CHM
tags:
  - error
checksum: 7c47dc7456850afef83b7b5b36060fdcaeea7bca
---

# Error 5225 Delta Support Not P

5225 Delta Support Not Possible

5225 Delta Support Not Possible

Advantage Error Guide

| 5225 Delta Support Not Possible  Advantage Error Guide |  |  |  |  |

Problem: Cannot enable oData server Delta functionality for the table because requirements are not met.

Solution: To support the Delta functional, the table must meet the following requirements:

| 1. | The table must have a ROWVERSION column. |

| 2. | The table must have a Unique Index, Primary Key or Autoinc field. |

Additionally, the data dictionary must be allowed to create a table named "GetTombstones". If there is an object with this name already exists in the data dictionary, and it does not have the right fields to support the delta functionality, then this error may be returned. If that is the case, removing the "GetTombstones" object and re-enabling the Delta support for the table should solve the problem.
