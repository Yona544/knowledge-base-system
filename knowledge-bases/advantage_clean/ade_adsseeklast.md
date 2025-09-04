---
title: Ade Adsseeklast
slug: ade_adsseeklast
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsseeklast.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f1615cc1c3103e008f49649523deda968b26c23d
---

# Ade Adsseeklast

AdsSeekLast

TAdsTable.AdsSeekLast

Advantage TDataSet Descendant

| TAdsTable.AdsSeekLast  Advantage TDataSet Descendant |  |  |  |  |

Seeks for the last value in an index.

Syntax

function AdsSeekLast( strKey : String ) : Boolean;

Parameter

| strKey | Search key. |

Description

AdsSeekLast will perform a seek for the last key in the indicated index order that matches the passed in search key. If the key is not in the index, the function will position the table at EOF and set the found flag to False.

Example

AdsTable1.IndexName := LastName;

bFound := AdsTable1.AdsSeekLast( Smith );

See Also

[AdsSeek](ade_adsseek.md)
