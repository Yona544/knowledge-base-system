---
title: Master Inlist
slug: master_inlist
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_inlist.htm
source: Advantage CHM
tags:
  - master
checksum: 180268a2752664b0531d52836f5e11d489df3453
---

# Master Inlist

INLIST()

INLIST()

Advantage Concepts

| INLIST()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function to determine if one expression matches another expression in a set of expressions.

| Supported in SQL: | No |
| Supported in Navigational: | Yes |

Syntax

INLIST(<Expression>, <Expression2>, [ Expression3,]) à lFound

Parameters

<Expression>  Expression to search for in the set of expressions.

<Expression2> The first of up to 25 expressions to be searched.

Return Values

Logical or NULL

Remarks

Returns true if the expression is found in the list. False if the expression is not found in the set and NULL if the expression was not found and one or more values in the expression set was NULL.

See Also
