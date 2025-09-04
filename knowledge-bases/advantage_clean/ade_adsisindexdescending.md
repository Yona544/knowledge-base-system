---
title: Ade Adsisindexdescending
slug: ade_adsisindexdescending
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsisindexdescending.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2aa8752a5d59077a933d2aeee98fb81245e19884
---

# Ade Adsisindexdescending

AdsIsIndexDescending

TAdsTable.AdsIsIndexDescending

Advantage TDataSet Descendant

| TAdsTable.AdsIsIndexDescending  Advantage TDataSet Descendant |  |  |  |  |

Determines if the given index order is descending.

Syntax

function AdsIsIndexDescending : Boolean;

Description

A descending index has keys sorted in the order of largest to smallest. The default is an ascending index. An AdsGotoTop on a descending order will position at the largest key in the index. An AdsGotoBottom will position at the smallest key in the index order.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'FirstName', '', '', [ optDESCENDING ] );

AdsTable1.IndexName := Tag1;

 

bIsDescending := AdsTable1.AdsIsIndexCustom;

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsOpenIndex](ade_adsopenindex.md)
