---
title: Ade Adsisindexcustom
slug: ade_adsisindexcustom
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsisindexcustom.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2a7a16fbf313de58bd1ba9d5975b841141521cbe
---

# Ade Adsisindexcustom

AdsIsIndexCustom

TAdsTable.AdsIsIndexCustom

Advantage TDataSet Descendant

| TAdsTable.AdsIsIndexCustom  Advantage TDataSet Descendant |  |  |  |  |

Determines if the given index order was built as a custom index.

Syntax

function AdsIsIndexCustom : Boolean;

Description

A custom index is built without keys. Keys are added to the custom index explicitly by calls to AdsAddCustomKey and AdsDeleteCustomKey. This allows a user to build a very small and specific index.

Custom indexes can only be built on tables opened with the ttAdsCDX or ttAdsADT option.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'FirstName', '', '', [ optCUSTOM ] );

AdsTable1.IndexName := Tag1;

 

bIsCustom := AdsTable1.AdsIsIndexCustom;

See Also

[AdsAddCustomKey](ade_adsaddcustomkey.md)

[AdsCreateIndex](ade_adscreateindex.md)

[AdsDeleteCustomKey](ade_adsdeletecustomkey.md)

[AdsOpenIndex](ade_adsopenindex.md)
