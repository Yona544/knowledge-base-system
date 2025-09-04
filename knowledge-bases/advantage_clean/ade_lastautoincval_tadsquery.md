---
title: Ade Lastautoincval Tadsquery
slug: ade_lastautoincval_tadsquery
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_lastautoincval_tadsquery.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: b255292ccc5132c8af2526cb46603046809453f8
---

# Ade Lastautoincval Tadsquery

LastAutoincVal

TAdsQuery.LastAutoincVal

Advantage TDataSet Descendant

| TAdsQuery.LastAutoincVal  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

Indicates the last AutoIncrement field value that was inserted into the table.

Syntax

property LastAutoincVal : Integer;

Description

Use LastAutoincVal after executing an SQL INSERT statement. If the table contains an AutoIncrement field, this property will store the last value inserted into that field. If the table does not contain an AutoIncrement field, or no record has been inserted, then this property will be set to 0. The LastAutoincVal property is read-only.

With TAdsQuery the LastAutoincVal is available immediately after execution of the INSERT statement.

Note This behavior differs from [TAdsTable.LastAutoincVal](ade_lastautoincval_tadstable.md).

 

Note The autoinc value returned is client-specific, and because of concurrent database access, is not guaranteed to be the absolute last autoinc value in the table.
