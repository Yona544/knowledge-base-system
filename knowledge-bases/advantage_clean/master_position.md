---
title: Master Position
slug: master_position
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_position.htm
source: Advantage CHM
tags:
  - master
checksum: 11cd783eea69d463091eb35b3f739afb6a7b7c7d
---

# Master Position

POSITION()

POSITION()

Advantage Concepts

| POSITION()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that searches for one string in another.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

POSITION( <cSearch> IN <cTarget> ) à nPos

Parameters

| <cSearch> | The string to search for |
| <cTarget> | The string to be searched |

Return Value

POSITION() returns the position of the first instance of <cSearch> within <cTarget> as an integer numeric value. If <cSearch> is not found, POSITION() returns zero.

See Also

[AT()](master_at.md)
