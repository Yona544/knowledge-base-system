---
title: Ade Closecachedtables
slug: ade_closecachedtables
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_closecachedtables.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: b782579da5b9d1b1f2f9022ee5da7f10327e9a7e
---

# Ade Closecachedtables

CloseCachedTables

TAdsConnection.CloseCachedTables

| TAdsConnection.CloseCachedTables |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Advantage TDataset Descendant

Close all cached tables on the connection.

Syntax

procedure CloseCachedTables;

Description

CloseCachedTables can be used to close all cached tables on a given connection. All cached closed tables on the client will be closed, as well as all cache closed tables on the server that might have been used when executing SQL statements.

This method can be useful if you know another application (or some other instance of the same application) will require exclusive access to a table that has been used by the existing application, or if you want tables used by some server-side functionality (like an extended procedure, or a trigger) to be available for exclusive use by the client at some later time.

Note If using this function you must still call [TAdsQuery.AdsCloseSQLStatement](ade_adsclosesqlstatement.md) to force queries to completely close all files they have used. If you wish to close all tables used by all queries you can use the [TAdsConnection.DataSets](ade_datasets.md) property to iterate through all queries and call AdsCloseSQLStatement on each one before calling CloseCachedTables.

See Also

[NumCachedCursors](ade_numcachedcursors.md)
