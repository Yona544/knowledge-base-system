---
title: Ade Lastautoincval Tadstable
slug: ade_lastautoincval_tadstable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_lastautoincval_tadstable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2b26f0fe563f72703c8481120253bde62850f8ee
---

# Ade Lastautoincval Tadstable

LastAutoincVal

TAdsTable.LastAutoincVal

Advantage TDataSet Descendant

| TAdsTable.LastAutoincVal  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md)

Indicates the last AutoIncrement field value that was inserted into the table.

Syntax

property LastAutoincVal : Integer;

Description

Use LastAutoincVal after a record has been appended to the table. If the table contains an AutoIncrement field, this property will store the last value inserted into that field. If the table does not contain an AutoIncrement field, or no record has been inserted, then this property will be set to 0. The LastAutoincVal property is read-only.

With TAdsQuery the LastAutoincVal is available immediately after execution of the INSERT statement.

Note This behavior differs from [TAdsQuery.LastAutoincVal](ade_lastautoincval_tadsquery.md).

 

Note The autoinc value returned is client-specific, and because of concurrent database access, is not guaranteed to be the absolute last autoinc value in the table.
