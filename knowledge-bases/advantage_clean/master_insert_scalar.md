---
title: Master Insert Scalar
slug: master_insert_scalar
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_insert_scalar.htm
source: Advantage CHM
tags:
  - master
checksum: 63232cbc4387886ff7caccdd23b91339dbba4b3b
---

# Master Insert Scalar

INSERT()

INSERT()

Advantage Concepts

| INSERT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function to replace a substring of one string with another.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

INSERT(<cStr1>, <nStart>, <nLength>, <cStr2>) à cString

Parameters

| <cStr1> | The string in which characters are to be replaced |
| <nStart> | The starting position in <cStr1> |
| <nLength> | The number of characters to replace in <cStr1> |
| <cStr2> | The string to place into <cStr1> |

Return Value

A copy of <cStr1> where the substring defined by <nStart> and <nLength> has been replaced by <cStr2>

Remarks

If either string in the INSERT() call is Unicode, the result will be Unicode.

See Also

REPLACE()
