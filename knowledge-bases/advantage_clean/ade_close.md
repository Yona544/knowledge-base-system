---
title: Ade Close
slug: ade_close
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_close.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6aab3abfef506db11a0af7bf22897e5fa73acc16
---

# Ade Close

Close

TAdsQuery.Close

Advantage TDataSet Descendant

| TAdsQuery.Close  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

Closes the dataset.

Syntax

procedure Close;

Description

The close method changes the datasets active property to False. This method is identical to the Delphi TQuery method, except for performance reasons the tables involved in the query are cache-closed, and remain open on the server for the life of the query statement, or until the [AdsCloseSQLStatement](ade_adsclosesqlstatement.md) method is called.

Note If the TAdsSettings.NumCachedCursors property is set to zero (not recommended), then cursors will not be cache-closed.

See Also

[NumCachedCursors](ade_numcachedcursors.md)

[NumCachedTables](ade_numcachedtables.md)

[CloseCachedTables](ade_closecachedtables.md)
