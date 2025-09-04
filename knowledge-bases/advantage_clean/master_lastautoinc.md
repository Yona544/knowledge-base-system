---
title: Master Lastautoinc
slug: master_lastautoinc
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_lastautoinc.htm
source: Advantage CHM
tags:
  - master
checksum: f9141433d7e1c95b936c80c1ebabe661e0101231
---

# Master Lastautoinc

LASTAUTOINC()

LASTAUTOINC()

Advantage Concepts

| LASTAUTOINC()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that retrieves the last autoinc value generated.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

LASTAUTOINC( CONNECTION | STATEMENT ) à nAutoinc

Parameters

| CONNECTION | Indicates that the last autoinc value generated for the current connection will be returned. |
| STATEMENT | Indicates that the last autoinc value generated on the current SQL statement handle will be returned. |

Return Value

The last generated autoinc value as specified by the parameter.

Remarks

LASTAUTOINC returns the last used autoinc value from an insert or append statement. If no autoinc value has been updated yet, a NULL value is returned.

Note Triggers that operate on tables with autoinc fields may affect the last autoinc value. SQL script triggers run on their own SQL statement. Therefore, calling LASTAUTOINC( STATEMENT ) inside an SQL script trigger would return the lastautoinc value used by the trigger's SQL statement, not the original SQL statement which caused the trigger to fire. To obtain the original SQL statement's lastautoinc value, use LASTAUTOINC( CONNECTION ) instead.

Example

 

SELECT LASTAUTOINC( STATEMENT ) FROM system.iota;

See Also

[LASTROWID()](master_rowid.md)

[LASTROWVERSION()](master_lastrowversion.md)
