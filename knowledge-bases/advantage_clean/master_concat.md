---
title: Master Concat
slug: master_concat
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_concat.htm
source: Advantage CHM
tags:
  - master
checksum: c8cdb67fe11730327edf3210f72e46e3a6cb3415
---

# Master Concat

CONCAT()

CONCAT()

Advantage Concepts

| CONCAT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that concatenates two strings together.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

CONCAT( <cString1>, <cString2> ) -> <cString>

 

Parameters

| <cString1>, <cString2> | The two strings to be concatenated. |

Return Values

CONCAT returns a string consisting of the concatenation of the two input strings.

Remarks

The result is the same as using the + operator on the two strings.

Note Binary and image fields are not supported by this function.
