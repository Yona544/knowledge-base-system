---
title: Error 5228 Invalid Data
slug: error_5228_invalid_data
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5228_invalid_data.htm
source: Advantage CHM
tags:
  - error
checksum: 4d1d34b11b7a77f6c089b49d107ff6ed2dbebe2a
---

# Error 5228 Invalid Data

5228 Invalid Data

5228 Invalid Data

Advantage Error Guide

| 5228 Invalid Data  Advantage Error Guide |  |  |  |  |

Problem: The data supplied is not valid for the given field type.

Solution:

When providing data to integer, numeric, double or long integer field as string data, make sure the string contain valid integer or numeric data. The valid data must only contain decimal digits, '.' as decimal point, and '+' or '-' sign.

When providing data to GUID field as string data, the data must be in either the registry format "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" or the same format without the '-' characters.
