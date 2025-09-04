---
title: Master Debug Breaks
slug: master__debug_breaks
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master__debug_breaks.htm
source: Advantage CHM
tags:
  - master
checksum: e4c42fdffd064465632c37182d2bc58e969a4b78
---

# Master Debug Breaks

::DEBUG\_BREAKS

::DEBUG\_BREAKS

| ::DEBUG\_BREAKS |  |  |  |  |

The ::DEBUG\_BREAKS table holds information about all break points defined for the current debugger session.

Definition

| Field Name | Field Type | Field Size | Description |
| break\_name | CiChar | 43 | Name of the break point. The value in this column may be null. |
| user\_id | Integer | 4 | Non-zero if the break point should only apply to the specific user. The value in this column may be null. |
| query\_id | Integer | 4 | Non-zero if the break point should only apply to the specific query handle. The value in this column may be null. |
| object\_id | Integer | 4 | Non-zero if the break point is set for an object in the database. Otherwise the break point if for the base script. |
| Offset | Integer | 4 | Location in the source script where the break point is set. |
| ObjectType | Short | 2 | Non-zero if the object\_id is non-zero. Identifies the type of the object in the database. Possible values are ADS\_DD\_FUNCTION\_OBJECT, ADS\_DD\_PROCEDURE\_OBJECT or ADS\_DD\_TRIGGER\_OBJECT. These constants are defined in the header file ace.h. |

Remark

When an SQL script is executed in debug mode, the ::DEBUG\_BREAKS table is consulted by the query engine to determine whether execution should be suspended. If a break point matching the current executing script is found, the execution is suspended and the [::DEBUG\_CONNECTIONS](master__debug_connections.md) table is updated.

See [DEBUG BREAK POINT](master_debug_break_point.md) statement for additional information.
