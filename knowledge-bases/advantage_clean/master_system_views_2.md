---
title: Master System Views 2
slug: master_system_views_2
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_views_2.htm
source: Advantage CHM
tags:
  - master
checksum: a77345d773198e0ed71dcc607fdd26ad73f202c6
---

# Master System Views 2

system.ansi\_views

system.ansi\_views

Advantage SQL Engine

| system.ansi\_views  Advantage SQL Engine |  |  |  |  |

Contains one row for each view in the database.

| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | View name. |
| View\_Stmt\_Len | ShortInt | 2 | The length of the SQL statement used to generate the view. |
| View\_Stmt | Memo | variable | The SQL statement used to generate the view. |
| Comment | Memo | variable | The description of the view. |
