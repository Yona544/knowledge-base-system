---
title: Error 7151 Invalid Table Type
slug: error_7151_invalid_table_type
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7151_invalid_table_type.htm
source: Advantage CHM
tags:
  - error
checksum: 5a67cd351624478314bd6e50f951cfbad19bc338
---

# Error 7151 Invalid Table Type

7151 Invalid Table Type

7151 Invalid Table Type

Advantage Error Guide

| 7151 Invalid Table Type  Advantage Error Guide |  |  |  |  |

Problem: A Visual FoxPro DBF table was opened with either the ADS\_CDX or ADS\_NTX table type. This error occurs if the table contains field types (e.g., currency, datetime, etc.) that are not supported by the ADS\_NTX and ADS\_CDX table types.

Solution: Use the ADS\_VFP table type when opening Visual FoxPro tables.
