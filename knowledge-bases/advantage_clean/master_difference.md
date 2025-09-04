---
title: Master Difference
slug: master_difference
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_difference.htm
source: Advantage CHM
tags:
  - master
checksum: cfc2448a0f172e30731424dfc8565de63ba8fcd7
---

# Master Difference

DIFFERENCE()

DIFFERENCE()

Advantage Concepts

| DIFFERENCE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that computes the difference of the SOUNDEX values of two strings.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DIFFERENCE( <cStr1>, <cStr2> ) à nResult

Parameters

| <cStr1>, <cStr2> | Character values. |

Return Value

A value measuring the SOUNDEX difference between <cStr1> and <cStr2>.

Remarks

DIFFERENCE() returns an integer value that indicates the difference between the values returned by the SOUNDEX() function for <cStr1> and <cStr2>. The value returned will be in the range 0 to 4. The value 4 indicates the closest match (it means that the soundex encoding of str1 and str2 are identical). The value 0 indicates the lowest possible phonetic match, with the values 1, 2, and 3 indicating increasing degrees of phonetic matching.

See Also

[SOUNDEX()](master_soundex.md)
