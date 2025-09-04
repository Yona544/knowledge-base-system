---
title: Master Space
slug: master_space
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_space.htm
source: Advantage CHM
tags:
  - master
checksum: a9a2fc650abae60ca575297ef8f13b221d7d1c02
---

# Master Space

SPACE()

SPACE()

Advantage Concepts

| SPACE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns a string of spaces.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

SPACE(<nCount>) à cSpaces

Parameters

<nCount> The number of spaces to be returned, up to a maximum of 65,535 (64K) in navigational usage and up to 1024 in SQL usage.

Return Values

SPACE() returns a character string. If <nCount> is zero, SPACE() returns an empty string ("").

Remarks

SPACE() is a character function that returns a specified number of spaces. SPACE() can pad strings with leading or trailing spaces.

See Also

[PAD()](master_pad.md)

[REPEAT()](master_repeat.md)
