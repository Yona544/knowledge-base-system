---
title: Ade Adsisindexunique
slug: ade_adsisindexunique
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsisindexunique.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 5ae0b7c4274f197180f453b0a794e9db9adb1860
---

# Ade Adsisindexunique

AdsIsIndexUnique

TAdsTable.AdsIsIndexUnique

Advantage TDataSet Descendant

| TAdsTable.AdsIsIndexUnique  Advantage TDataSet Descendant |  |  |  |  |

Determines if the given index order is unique.

Syntax

function AdsIsIndexUnique : Boolean;

Description

A unique index will have no repeated key values.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'FirstName', '', '', [ optUNIQUE ] );

AdsTable1.IndexName := Tag1;

 

bIsUnique := AdsTable1.AdsIsIndexUnique;

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsOpenIndex](ade_adsopenindex.md)
