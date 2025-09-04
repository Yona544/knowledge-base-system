---
title: Master Trim
slug: master_trim
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_trim.htm
source: Advantage CHM
tags:
  - master
checksum: d3fca47c35b9cd9dcc4162e5ff836c59f748df24
---

# Master Trim

TRIM()

TRIM()

Advantage Concepts

| TRIM()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that removes trailing spaces from a character string. The [SQL version](master_trim_sql_scalar.md) can optionally trim a specific string from another string.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

Navigational:

 TRIM(<cString>) à cTrimString

 

SQL:

 TRIM( [[ LEADING | TRAILING | BOTH [ str1 ] FROM ] | [ str1 FROM ]] cString )

 

Parameters

| <cString> | The character string to be copied without trailing spaces. |
| <str1> | Optional string to trim from cString (as opposed to space characters). |

Return Values

A copy of the given string with characters trimmed.

Remarks

The navigational version of TRIM and the SQL version differ in semantics.

Navigational:

When TRIM() is used in a navigational environment (e.g., when setting filters directly on a table), it behaves the same as RTRIM().  It removes trailing spaces from the string.

SQL:

When TRIM() is used in SQL statements, it can be used in a number of different forms.  An important difference from the navigational version is that the default behavior of TRIM() with SQL is to remove both leading and trailing spaces like ALLTRIM(). The behavior can be controlled with the alternative forms of the syntax.

Note If trim functions are used in an index expression for the purposes of optimizing SQL statements, the LTRIM, RTRIM, and ALLTRIM scalars should be used.  When TRIM() is used in SQL statements, it will not be optimized by indexes.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[PAD()](master_pad.md)

[RTRIM()](master_rtrim.md)

[LTRIM()](master_ltrim.md)

[ALLTRIM()](master_alltrim.md)

[SUBSTR()](master_substr.md)

[SQL TRIM()](master_trim_sql_scalar.md)
