---
title: Master System Views
slug: master_system_views
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_views.htm
source: Advantage CHM
tags:
  - master
checksum: 53675283cfe478fe471e8620b007f04e98432e43
---

# Master System Views

system.views

system.views

Advantage SQL Engine

| system.views  Advantage SQL Engine |  |  |  |  |

Contains one row for each view in the database.

| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | View name. |
| View\_Stmt\_Len | ShortInt | 2 | The length of the SQL statement used to generate the view. |
| View\_Stmt | Memo | variable | The SQL statement used to generate the view. |
| Comment | Memo | variable | The description of the view. |
