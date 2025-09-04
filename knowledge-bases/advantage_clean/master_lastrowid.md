---
title: Master Lastrowid
slug: master_lastrowid
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_lastrowid.htm
source: Advantage CHM
tags:
  - master
checksum: bc08a5803812178acc56a6448d8bc7ebd78a29e2
---

# Master Lastrowid

LASTROWID()

LASTROWID()

Advantage Concepts

| LASTROWID()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that retrieves the ROWID of the last row inserted into the table.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

LASTROWID() à cRowid

Parameters

| None |  |

Return Value

A [ROWID](master_rowid.md) value

Remarks

Returns the ROWID of the last row inserted into the table. This value can be used to identify a newly inserted row without prior knowledge of that row's key value, and without requiring the table to have an autoinc column.

See Also

[LASTAUTOINC()](master_lastautoinc.md)

[LASTROWVERSION()](master_lastrowversion.md)
