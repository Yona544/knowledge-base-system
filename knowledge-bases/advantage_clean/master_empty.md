---
title: Master Empty
slug: master_empty
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_empty.htm
source: Advantage CHM
tags:
  - master
checksum: 7ac282b2e3b5aef4e6d2458f34b536c1b0e4b5f2
---

# Master Empty

EMPTY()

EMPTY()

Advantage Concepts

| EMPTY()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that determines if the result of an expression is empty for DBFs or NULL for ADTs.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

EMPTY(<exp>) à lEmpty

Parameters

<exp>  An expression of any data type.

Return Values

When using DBF tables, EMPTY() returns True if the expression results in an empty value; otherwise, it returns False. When using ADT tables, EMPTY() returns True if the expression results in a NULL value; otherwise, it returns False. With Visual FoxPro (VFP) tables, this function returns False for NULL column values. Empty and NULL are not equivalent when using VFP tables.

The criteria for determining whether a value is considered NULL when using ADT tables depends on the data type of <exp>. Advantage internally stores a special data type dependent value that indicates to the Advantage application the value is NULL. Any time a record is inserted, appended, or cleared, all column values will be set to their NULL value.

The criteria for determining whether a value is considered empty when using DBF tables depends on the data type of <exp> according to the following rules:

List of DBF Empty Values:

| DBF Data Type | Contents |
| Character | Spaces, tabs, CR/LF, or an empty string ("") |
| Numeric, Integer, Double | 0 |
| Date, ShortDate | CTOD("") or STOD("") |
| Logical | False (.F.) |

Remarks

When using DBF tables, the EMPTY() function treats carriage returns, line feeds, and tabs as space characters and removes these as well. When <exp> is a DBF memo field, the EMPTY function returns True if the memo field does not contain any data.

See Also

[LEN()](master_len.md)

[ISNULL()](master_isnull.md)
