---
title: Ade Create Or Alter Table Editor
slug: ade_create_or_alter_table_editor
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_create_or_alter_table_editor.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3d805b293f44d35e488a8d0dd0924c7eb855f561
---

# Ade Create Or Alter Table Editor

Create or Alter Table Editor

Create or ALTER Table Editor

Advantage TDataSet Descendant

Advanced Property Editors

| Create or ALTER Table Editor  Advantage TDataSet Descendant  Advanced Property Editors |  |  |  |  |

You can create a new table from inside the Delphi IDE by right-clicking on a [TAdsTable](ade_tadstable_7.md) instance and selecting "Create New Table...". Note you will need to have either the [DatabaseName](ade_databasename.md) property or the [AdsConnection](ade_adsconnection.md) property set before creating a new table.

Menu option to create a new table

You can ALTER an existing table from inside the Delphi IDE by right-clicking on a TAdsTable instance and selecting "ALTER/Restructure Table...". In addition to having either the [DatabaseName](ade_databasename.md) or [AdsConnection](ade_adsconnection.md) property set, you will also need to have the TableName property pointing to an existing table.

Menu option to ALTER an existing table

Note that the "Create New Table..." menu option is also available on [TAdsQuery](ade_tadsquery.md) instances. This allows you to quickly create tables and then write SQL statements to query them.

Menu option to create a new table also available from TAdsQuery instances
