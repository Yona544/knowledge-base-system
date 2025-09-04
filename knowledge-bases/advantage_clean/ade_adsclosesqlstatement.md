---
title: Ade Adsclosesqlstatement
slug: ade_adsclosesqlstatement
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsclosesqlstatement.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 09bdac211592283f15e6caf50d53e1bca83b59b4
---

# Ade Adsclosesqlstatement

AdsCloseSQLStatement

TAdsQuery.AdsCloseSQLStatement

Advantage TDataSet Descendant

| TAdsQuery.AdsCloseSQLStatement  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

Completely closes all files associated with any TAdsQuery instance.

Syntax

procedure TAdsQuery.AdsCloseSQLStatement();

Description

When an SQL statement is executed, the Advantage Client Engine and the Advantage Database Server open any tables and indexes necessary to produce the rowset. Even if the TAdsQuery.Close method is called, these files remain opened for performance reasons. After the Close method is called, the CloseSQLStatement method will close all files and destroy all pertinent information within the Advantage Database Server and the Advantage Client Engine.

Note The [TAdsSettings.NumCachedCursors](ade_numcachedcursors.md) property must be set to zero in conjunction with the AdsCloseSQLStatement. Use these functions only when necessary due to performance loss. To close all cached tables without modifying NumCachedCursors, see the [TAdsConnection.CloseCachedTables](ade_closecachedtables.md) method.
