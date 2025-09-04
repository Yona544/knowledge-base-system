---
title: Error 5142 Ae Ri Cascade
slug: error_5142_ae_ri_cascade
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5142_ae_ri_cascade.htm
source: Advantage CHM
tags:
  - error
checksum: d0ba64c187c769ab23c8d9639a06e1e4817f22f9
---

# Error 5142 Ae Ri Cascade

5142 AE\_RI\_CASCADE

5142 AE\_RI\_CASCADE

Advantage Error Guide

| 5142 AE\_RI\_CASCADE  Advantage Error Guide |  |  |  |  |

Problem: The record update or delete failed because an existing referential integrity rule caused cascaded updates, and subsequent updates failed. The row that failed to update is a child in a different referential integrity rule. The updates produced a foreign key from the data in this row that does not have a corresponding key in the parent table. Note that these RI rules may cause cascaded updates: ADS\_DD\_RI\_CASCADE, ADS\_DD\_RI\_SETNULL, and ADS\_DD\_RI\_SET\_DEFAULT.

Solution: When this error occurs, retrieve the text error message that accompanies the error code. That text will include information about the row and RI rule that caused the failure.
