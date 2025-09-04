---
title: Ade Adsisindexcompound
slug: ade_adsisindexcompound
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsisindexcompound.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 862259f1be2d9aeec45c865725d7d5986faf4cba
---

# Ade Adsisindexcompound

AdsIsIndexCompound

TAdsTable.AdsIsIndexCompound

Advantage TDataSet Descendant

| TAdsTable.AdsIsIndexCompound  Advantage TDataSet Descendant |  |  |  |  |

Determines if the given index order is from a compound index file.

Syntax

function AdsIsIndexCompound : Boolean;

Description

AdsIsIndexCompound will return True only if the index order specified is in a compound index file (a Foxpro-compatible CDX file or Advantage proprietary ADI file). Indexes built with NTX and FoxPro-compatible IDX files are not compound indexes.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'FirstName', '', '', [ optCOMPOUND ] );

AdsTable1.IndexName := Tag1;

bIsCompound := AdsTable1.AdsIsIndexCompound;

{ bIsCompound equals True since within a compound index }

 

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsOpenIndex](ade_adsopenindex.md)
