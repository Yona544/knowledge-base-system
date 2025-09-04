---
title: Error 5143 Ae Ri Failed
slug: error_5143_ae_ri_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5143_ae_ri_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 3b7dcfdcede456854bf85bc755adb209d30bd8bb
---

# Error 5143 Ae Ri Failed

5143 AE\_RI\_FAILED

5143 AE\_RI\_FAILED

Advantage Error Guide

| 5143 AE\_RI\_FAILED  Advantage Error Guide |  |  |  |  |

Problem: The new referential integrity rule could not be added to the Advantage Data Dictionary.

Solution: When this error occurs, retrieve the text error message that accompanies the error code. That text will include the specific reason that the new rule failed to be added. Some causes are:

- The primary key name supplied is not the primary index for the table.

- The primary key and foreign key are not the same length.

- The primary key and foreign key do not consist of the same number of fields.

- A field in the primary key has a different length than the corresponding field in the foreign key.

- A field in the primary key has a different type than the corresponding field in the foreign key.
