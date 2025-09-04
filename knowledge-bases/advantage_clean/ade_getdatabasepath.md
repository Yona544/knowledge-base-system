---
title: Ade Getdatabasepath
slug: ade_getdatabasepath
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getdatabasepath.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 31db6fe9a84ef37e9045df6fa6cef1765cd7b8d6
---

# Ade Getdatabasepath

GetDatabasePath

TAdsDataSet.GetDatabasePath

Advantage TDataSet Descendant

| TAdsDataSet.GetDatabasePath  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md) [TAdsStoredProc](ade_tadsstoredproc.md)

Retrieves the path the TAdsDataSet instance is using.

Syntax

function GetDatabasePath : String;

Description

GetDatabasePath will return the path the TAdsDataSet instance is using, regardless of what method has been used to assign the databasename property.

If the TAdsDataSet instance is using an alias, the alias path will be returned. If the TAdsDataSet is using a simple path in the databasename property, that path will be returned. If the TAdsDataSet instance is using a TAdsConnection, the TAdsConnection path will be returned, etc.

See Also

[DatabaseName](ade_databasename.md)
