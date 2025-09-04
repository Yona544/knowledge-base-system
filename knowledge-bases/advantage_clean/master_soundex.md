---
title: Master Soundex
slug: master_soundex
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_soundex.htm
source: Advantage CHM
tags:
  - master
checksum: 254fc0eb0a44abfc25990d977d7b4feda91f18a3
---

# Master Soundex

SOUNDEX()

SOUNDEX()

Advantage Concepts

| SOUNDEX()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the Soundex value for a string.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

SOUNDEX( <cStr> ) à cSoundex

Parameters

| <cStr> | The string to compute a Soundex value for. |

Return Value

A string in the form <letter><digit><digit><digit>

Remarks

The soundex function returns a four-digit phonetic encoding of the given string.

See Also

[DIFFERENCE()](master_difference.md)
