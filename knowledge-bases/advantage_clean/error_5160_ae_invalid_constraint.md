---
title: Error 5160 Ae Invalid Constraint
slug: error_5160_ae_invalid_constraint
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5160_ae_invalid_constraint.htm
source: Advantage CHM
tags:
  - error
checksum: 049ef1ad41eea448ced62d348fc326e12def72f7
---

# Error 5160 Ae Invalid Constraint

5160 AE\_INVALID\_CONSTRAINT

5160 AE\_INVALID\_CONSTRAINT

Advantage Error Guide

| 5160 AE\_INVALID\_CONSTRAINT  Advantage Error Guide |  |  |  |  |

One of the following conditions is true:

- The field-level or record-level constraint is invalid. It is either of the wrong data type or invalid syntax.

- Cannot set a default field value to NULL when a field constraint exists that does not allow NULL values to exist in the column.

- The default field value must be set to a non-NULL value before setting the field constraint that does not allow NULL values to exist in the column.

- An invalid date, time, or timestamp value or syntax was specified for the field constraint.
