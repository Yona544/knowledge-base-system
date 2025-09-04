---
title: Master Lastrowversion
slug: master_lastrowversion
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_lastrowversion.htm
source: Advantage CHM
tags:
  - master
checksum: 076bcc41690733006fac6e9dc897374a9eca4cfd
---

# Master Lastrowversion

LASTROWVERSION()

LASTROWVERSION()

Advantage Concepts

| LASTROWVERSION()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that retrieves the ROWVERSION of the most recent table update.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

LASTROWVERSION() à iRowversion

Parameters

| None |  |

Return Value

A ROWVERSION value (a 64-bit integer).

Remarks

Returns the ROWVERSION from the most recent update of a table having a ROWVERSION field for the current statement handle.

See Also

[LASTAUTOINC()](master_lastautoinc.md)

[LASTROWID()](master_lastrowid.md)
