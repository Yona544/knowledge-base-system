---
title: Master Abs
slug: master_abs
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_abs.htm
source: Advantage CHM
tags:
  - master
checksum: 578d6a1f318e139c4b16e795eac741c07e1e0c0e
---

# Master Abs

ABS()

ABS()

Advantage Concepts

| ABS()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the absolute value of a numeric expression.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

ABS(<nExp>) à nPositive

Parameters

<nExp>  The numeric expression to be evaluated.

Returns

ABS() returns a number representing the absolute value of its argument. The return value is a positive number or zero.

Description

ABS() is a numeric function that determines the magnitude of a numeric value independent of its sign. It lets you, for example, obtain the difference between two numbers as a positive value without knowing in advance which of the two is larger.

As a formalism, ABS(x) is defined in terms of its argument, x, as follows: if x >= 0, ABS(x) returns x; otherwise, ABS(x) returns the negation of x.

Examples

The following examples show typical results from ABS():

ABS(100 - 50) // Result: 50

ABS(50 - 100) // Result: 50

ABS(-12) // Result: 12

ABS(0) // Result: 0

See Also

None.
