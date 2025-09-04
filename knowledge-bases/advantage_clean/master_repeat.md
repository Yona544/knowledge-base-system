---
title: Master Repeat
slug: master_repeat
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_repeat.htm
source: Advantage CHM
tags:
  - master
checksum: 5ebd07899e3fadbd70386151d7a17d7fea57e01e
---

# Master Repeat

REPEAT()

REPEAT()

Advantage Concepts

| REPEAT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns a string with given characters duplicated 1 or more times.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

REPEAT(<cString>, <nCnt>) à cRepeatedString

Parameters

<cString> The character string to repeat.

<nCnt> The number of times to duplicate <cString>.

Return Values

REPEAT() returns a string consisting of <cString> repeated <nCnt> times.

Remarks

<nCnt> must be greater or equal to zero. If nCnt is zero, an empty string is returned.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[SPACE()](master_space.md)
