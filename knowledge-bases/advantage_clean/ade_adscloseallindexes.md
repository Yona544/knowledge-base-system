---
title: Ade Adscloseallindexes
slug: ade_adscloseallindexes
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adscloseallindexes.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 4820e54fffb1520c419b52f84baec82e0923d5e5
---

# Ade Adscloseallindexes

AdsCloseAllIndexes

TAdsTable.AdsCloseAllIndexes

Advantage TDataSet Descendant

| TAdsTable.AdsCloseAllIndexes  Advantage TDataSet Descendant |  |  |  |  |

Closes all index orders for a given table.

Syntax

procedure AdsCloseAllIndexes;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: CloseIndexFile. See your Delphi documentation for more information about this native Delphi method.

Description

It is not possible to close an AutoOpen index. If the table has an AutoOpen index, AdsCloseAllIndexes will not raise an exception, but index order handles from the AutoOpen index will still be valid.

Note Updating data in a table without all associated indexes being opened can result in index corruption. If such corruption occurs, it can be repaired by calling AdsReindex on the table handle.

Example

While AdsTable1.IndexFiles.Count > 0

AdsTable1.CloseIndexFile( AdsTable1.IndexFiles.Strings[0] );

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsOpenIndex](ade_adsopenindex.md)

[AdsReindex](ade_adsreindex.md)
