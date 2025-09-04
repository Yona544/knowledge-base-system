---
title: Master Sys
slug: master_sys
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sys.htm
source: Advantage CHM
tags:
  - master
checksum: 390e3e755270029a40b6d6a14e2a8ef721b29812
---

# Master Sys

SYS()

SYS()

Advantage Concepts

| SYS()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that provides compatibility with Microsoft Visual Foxpro.

| Supported in SQL: | No |
| Supported in Navigational: | Yes |

Syntax

SYS(<nNumber>, <Value> ) à cNumber

Parameters

<nNumber> The system function to perform, currently only function 11 is supported.

<Value> An argument to the function.

Return Values

SYS( 11 ) returns the Julian day of a date value as a character string.

Remarks

SYS( 11 ) converts a date value to a Julian date and returns the value as a string.

Note Binary, memo, and image fields are not supported by this function.
