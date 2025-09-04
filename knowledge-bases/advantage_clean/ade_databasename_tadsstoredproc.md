---
title: Ade Databasename Tadsstoredproc
slug: ade_databasename_tadsstoredproc
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_databasename_tadsstoredproc.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d948150f8ed6eb2f6b004f0c6390c4dcb97ffbd0
---

# Ade Databasename Tadsstoredproc

DatabaseName

TAdsStoredProc.DatabaseName

Advantage TDataSet Descendant

| TAdsStoredProc.DatabaseName  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.md)

Specifies the name of the TAdsConnection component to associate with this TAdsStoredProc component.

Syntax

property DatabaseName: string;

Description

Use DatabaseName to specify the TAdsConnection component to associate with this TAdsStoredProc component. TAdsStoredProc components can not directly access Advantage alias names or connection paths, they must reference a TAdsConnection component. All Advantage Database Dictionary access is accomplished through a TAdsConnection component. See [Accessing an Advantage Data Dictionary](master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.md) for more information.

See Also

[GetDatabasePath](ade_getdatabasepath.md)
