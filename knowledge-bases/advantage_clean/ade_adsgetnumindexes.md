---
title: Ade Adsgetnumindexes
slug: ade_adsgetnumindexes
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetnumindexes.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9ff55b2444b0c81867a373d8a65c23ae96783684
---

# Ade Adsgetnumindexes

AdsGetNumIndexes

TAdsTable.AdsGetNumIndexes

Advantage TDataSet Descendant

| TAdsTable.AdsGetNumIndexes  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the total number of open index orders associated with the given table.

Syntax

function AdsGetNumIndexes : Word;

Description

Return number of index orders. For example, if the user opened a CDX file with five tags and an IDX, then this function would return the total 6. The number of indexes returned does not necessarily correspond to the number of index files opened for the table. A compound index may contain multiple index orders. Calling this function before calling [AdsGetAllIndexes](ade_adsgetallindexes.md) will provide the number of index orders that will be returned. AdsGetNumIndexes does not return information for full text search indexes.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

AdsTable1.AdsCreateIndex( '', 'Tag2', 'DeptNum', '', '', [] );

wIndexCount := AdsTable1.AdsGetNumIndexes;

{ wIndexCount equals 2 }

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsGetAllIndexes](ade_adsgetallindexes.md)

[AdsOpenIndex](ade_adsopenindex.md)
