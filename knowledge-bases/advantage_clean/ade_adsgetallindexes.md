---
title: Ade Adsgetallindexes
slug: ade_adsgetallindexes
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetallindexes.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f1b00b8e84db240861707029bb7268659713611b
---

# Ade Adsgetallindexes

AdsGetAllIndexes

TAdsTable.AdsGetAllIndexes

Advantage TDataSet Descendant

| TAdsTable.AdsGetAllIndexes  Advantage TDataSet Descendant |  |  |  |  |

Returns an array of open index order handles for the given table.

Syntax

function AdsGetAllIndexes( ahIndexes : Array of ADSHANDLE ) : Word;

Parameter

| ahIndexes | Return index order handles in the given array. |

Description

The index order handles are returned in the order they were opened. For CDX or ADI indexes, the index order handles are returned in the order in which they were created within the index file. Return value is the number of returned entries on output. AdsGetAllIndexes does not return information for full text search indexes.

Example

var

ahIndexes : Array [0 .. 10] of AdsHandle;

wIndexHandleCount : Word;

 

begin

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

AdsTable1.AdsCreateIndex( '', 'Tag2', 'DeptNum', '', '', [] );

 

wIndexHandleCount := AdsTable1.AdsGetAllIndexes( ahIndexes );

{ wIndexHandleCount equals 2 and ahIndexes contains two values }

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsGetIndexHandle](ade_adsgetindexhandle.md)

[AdsGetNumIndexes](ade_adsgetnumindexes.md)

[AdsOpenIndex](ade_adsopenindex.md)
