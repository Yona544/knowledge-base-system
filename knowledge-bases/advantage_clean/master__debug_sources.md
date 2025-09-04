---
title: Master Debug Sources
slug: master__debug_sources
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master__debug_sources.htm
source: Advantage CHM
tags:
  - master
checksum: 45d70ecf6209819d611f679ff08f1604626c3047
---

# Master Debug Sources

::DEBUG\_SOURCES

::DEBUG\_SOURCES

| ::DEBUG\_SOURCES |  |  |  |  |

The ::DEBUG\_SOURCES table holds source code referenced by the ::DEBUG\_STACK table.

Definition

| Field Name | Field Type | Field Size | Description |
| source\_id | Autoinc | 4 | Primary key of the table |
| object\_id | Integer | 4 | Non-zero if the source code is from a database object such as a trigger, stored procedure or user defined function. |
| parent\_name | CiChar | 200 | Parent name of the object. This column may contain null values. For triggers, the parent name is the table name. For user defined functions, the parent name is the package name. |
| object\_name | CiChar | 200 | Name of the object. May be null if the source code is not from a database object |
| Source | Memo |  | SQL script. It only contains the body of the function or stored procedure. This column may be null if the source is not available or if the user does not have permission to view the source. |
| ref\_count | Integer | 4 | The number of times this object is referenced. It is not used at the moment. |
| object\_type | Short | 2 | Non-zero if the source script is from a database object. Possible values are ADS\_DD\_FUNCTION\_OBJECT, ADS\_DD\_PROCEDURE\_OBJECT, or ADS\_DD\_TRIGGER\_OBJECT. These constants are defined in the header file ace.h. |

Remark

The ::DEBUG\_SOURCES table is referenced by the [::DEBUG\_STACK](master__debug_stack.md) table. The value in the "source" column contains the actual source code of the SQL script being executed.
