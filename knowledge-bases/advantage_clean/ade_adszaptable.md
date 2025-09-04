---
title: Ade Adszaptable
slug: ade_adszaptable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adszaptable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6acd8c925e10efa7f808a000418c820e0be12888
---

# Ade Adszaptable

AdsZapTable

TAdsTable.AdsZapTable

Advantage TDataSet Descendant

| TAdsTable.AdsZapTable  Advantage TDataSet Descendant |  |  |  |  |

Removes all records from the table and rebuilds indexes associated with the table.

Syntax

procedure AdsZapTable;

Description

AdsZapTable will remove all records from the table; then the Advantage Client Engine will reindex the table. The indexes must be opened during the empty or they will become invalid. This operation requires exclusive access to the table, which is specified during the open.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsZapTable;

See Also

[AdsPackTable](ade_adspacktable.md)
