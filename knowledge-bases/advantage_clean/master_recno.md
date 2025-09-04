---
title: Master Recno
slug: master_recno
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_recno.htm
source: Advantage CHM
tags:
  - master
checksum: 2bf41a7b8df2faee506c2f1d0bff8f568797b56c
---

# Master Recno

RECNO()

RECNO()

Advantage Concepts

| RECNO()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the identity at the position of the record pointer.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

RECNO( [<tablealias>] )à Identity

Return Values

RECNO()  Returns the identity found at the position of the record pointer.

Remarks

RECNO() is a database function that returns the identity found at the current position of the record pointer. Identity is a unique value guaranteed by the structure of the data file to reference a specific record of a data file. In an Xbase table this value is the record number.

In SQL usage, the RECNO() scalar function accepts an optional table alias that can be used when the table reference is ambiguous (e.g., in the case of a join where multiple tables are involved).

Example

SELECT \* FROM mytable WHERE RECNO() = 100;

SELECT \* FROM table1, table2 WHERE RECNO(table1) = RECNO(table2);

See Also

None.
