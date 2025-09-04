---
title: Master Full Text Search Column Permissions
slug: master_full_text_search_column_permissions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_full_text_search_column_permissions.htm
source: Advantage CHM
tags:
  - master
checksum: 7ec5d52b2577a9667786d7f2c3ef97703446d1c4
---

# Master Full Text Search Column Permissions

Full Text Search Column Permissions

Full Text Search Column Permissions

Advantage Concepts

| Full Text Search Column Permissions  Advantage Concepts |  |  |  |  |

In general, the CONTAINS, SCORE, and SCOREDISTINCT scalar functions obey column level permissions the same as other functions. In one case, however, they are stricter. Normally with level 1 permissions (ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_1), it is possible to search columns that do not have read permissions. When using the form of the FTS scalar functions with the asterisk (\*) as the first parameter, only fields with read permissions will be searched.
