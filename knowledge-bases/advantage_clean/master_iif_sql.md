---
title: Master Iif Sql
slug: master_iif_sql
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_iif_sql.htm
source: Advantage CHM
tags:
  - master
checksum: 3597ba27731e9fb9492a4a1134a55fa0411055c2
---

# Master Iif Sql

IIF

IIF

Advantage SQL Engine

| IIF  Advantage SQL Engine |  |  |  |  |

The IIF scalar evaluates a boolean expression and returns one of two possible result expressions. The IIF lets you use IF ... THEN ... ELSE logic in SQL statements.

Syntax

IIF ( <boolean\_expression> , <true\_expression> , <false\_expression> )

Parameters

| <boolean\_expression> | A boolean expression that evaluates to true or false. |
| <true\_expression> | An expression or value to be returned when <boolean\_expression> is true. |
| <false\_expression> | An expression or value to be returned when <boolean\_expression> is false. |

Return Values

When <boolean\_expression> evaluates to true then the evaluation of <true\_expression> is returned. Conversely, when <boolean\_expression> evaluates to false then the evaluation of <false\_expression> is returned.

Remarks

IIF() is a logical conversion function. It provides a mechanism to evaluate a condition within an SQL statement. With this ability you can convert a logical expression to another data type. The true and false expressions must be of compatible types. Similarly the IIF return value must be compatible within the encompassing SQL statement.

Examples

A. Simple data type conversion using IIF

SELECT name, IIF ( married = TRUE, 'Married', 'Not Married' ) FROM employees

B. Calculate the difference between the number of married persons and the number of unmarried persons.

SELECT SUM( IIF( married = TRUE, 1, -1 )) FROM employees

See Also

[CASE()](master_case.md)
