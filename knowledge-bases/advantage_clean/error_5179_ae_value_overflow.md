---
title: Error 5179 Ae Value Overflow
slug: error_5179_ae_value_overflow
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5179_ae_value_overflow.htm
source: Advantage CHM
tags:
  - error
checksum: 9eed688dab4c363615210e23bb79dde2d4fec686
---

# Error 5179 Ae Value Overflow

5179 AE\_VALUE\_OVERFLOW

5179 AE\_VALUE\_OVERFLOW

Advantage Error Guide

| 5179 AE\_VALUE\_OVERFLOW  Advantage Error Guide |  |  |  |  |

Problem: The value cannot be stored in the designated column. For example: this error will be returned when attempting to store into an Integer column a numeric value that is outside the range -2,147,483,647 to 2,147,483,647. See [ADT Field Types and Specification](master_adt_field_types_and_specifications.md).

Solution: Ensure the numeric value to be stored in a column is within the supported range or restructure (i.e., ALTER) the table to ensure that the column can stored the expected values.
