---
title: Master Replace
slug: master_replace
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_replace.htm
source: Advantage CHM
tags:
  - master
checksum: 0652bd00b95f6282ccfea4dead7ea926d55d84d5
---

# Master Replace

REPLACE()

REPLACE()

Advantage Concepts

| REPLACE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that replaces substrings in one string with another.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

REPLACE( <cTarget>, <cSearch>, <cReplace> ) à cResult

Parameters

| <cTarget> | The string to be searched |
| <cSearch> | The substring to search for |
| <cReplace> | The replacement string. |

Return Value

A copy of <cTarget> where all instances of the substring <cSearch> have been replaced with <cReplace>

Remarks

This function replaces all occurrences of <cSearch> in <cTarget> with <cReplace>.

Example

 

SELECT REPLACE( 'abcdefabc', 'abc', '12345' ) FROM system.iota;   // returns 12345def12345

See Also

[AT()](master_at.md)

[SUBSTR()](master_substr.md)
