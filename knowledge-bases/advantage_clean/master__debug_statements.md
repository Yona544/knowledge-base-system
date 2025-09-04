---
title: Master Debug Statements
slug: master__debug_statements
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master__debug_statements.htm
source: Advantage CHM
tags:
  - master
checksum: 579c4e97bc8f98e2e1c2d51a0a9378e5c9e1bbfc
---

# Master Debug Statements

::DEBUG\_STATEMENTS

::DEBUG\_STATEMENTS

| ::DEBUG\_STATEMENTS |  |  |  |  |

The ::DEBUG\_STATEMENTS table holds information about the query handles currently being debugged.

Definition

| Field Name | Field Type | Field Size | Description |
| user\_id | Integer | 4 | Foreign key into the ::DEBUG\_CONNECTIONS table. |
| query\_id | Integer | 4 | Primary key of the table. |
| stmt\_name | Char | 32 | Name of the query handle. The value of this column may be used in DEBUG commands where a statement\_name value is required.  This value can also be obtained from ::stmt.name system variable. |
