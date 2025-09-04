---
title: Master Descend
slug: master_descend
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_descend.htm
source: Advantage CHM
tags:
  - master
checksum: f459fe226aabfb1d0aefe2ec8180dec9f2950b20
---

# Master Descend

DESCEND()

DESCEND()

Advantage Concepts

| DESCEND()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that creates a descending index key value.

| Supported in SQL: | No (The descending option can be controlled via the DESC keyword in CREATE INDEX statements and ORDER BY clauses.) |
| Supported in Navigational: | Yes |

Syntax

DESCEND(<exp>) à ValueInverted

Parameters

| <exp> | Any valid expression of any data type other than memo, binary, or image. Valid Advantage expressions can consist of field names, literal values, supported operators, and supported functions. |

Return Values

DESCEND() returns an inverted expression of the same data type as the <exp>, except for dates that return a numeric value. A DESCEND() of CHR(0) always returns CHR(0).

Remarks

DESCEND() is a conversion function that returns the inverted form of the specified expression to be used when creating multi-segmented indexes where one or more segments should be in descending order. Specify the segment of the index expression you want to be descending as the DESCEND() argument.

To subsequently perform a lookup with a seek operation, you must first evaluate it using the Advantage Client Engine AdsInitRawKey and AdsBuildRawKey APIs.

Only use this function to create a certain segment(s) of a multi-segmented index in descending order. If the entire index expression is to be in descending order, create the index with the "descending" option rather than use the DESCEND() function. If you create an index using the "descending" option, you will not need to perform any special operations before performing a seek. "Descending" is an attribute of the index file where it is stored and used for reindexing purposes.

Note Memo, binary, and image fields are not supported in this Advantage Expression Engine function. If memo, binary, or image fields are used with this expression engine function, the Advantage Expression Engine will be unable to evaluate the expression.

See Also

Advantage TDataSet Descendant

AdsCreateIndex

AdsSeek

Advantage Client Engine API

AdsCreateIndex

AdsInitRawKey

AdsBuildRawKey

AdsSeek
