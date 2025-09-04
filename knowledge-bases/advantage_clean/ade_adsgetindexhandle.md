---
title: Ade Adsgetindexhandle
slug: ade_adsgetindexhandle
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetindexhandle.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8b3f9efab40fe1c00a4368ce4bf71869a1ef7710
---

# Ade Adsgetindexhandle

AdsGetIndexHandle

TAdsTable.AdsGetIndexHandle

Advantage TDataSet Descendant

| TAdsTable.AdsGetIndexHandle  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the handle of an index order given the index order name.

Syntax

function AdsGetIndexHandle( strIndexOrder : String ) : ADSHANDLE;

Parameter

| strIndexOrder | Name of index order for which to search. |

Description

For non-compound indexes, the index order name is the base of the file name (up to 8 characters). For compound indexes, the index order name is the tag name (up to 10 characters for CDXs, IDXs, and NTXs and up to 128 characters for ADIs).

If there is more than one index order open with the same name, the Advantage Client Engine will return the first one it finds.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', 'Empid>50', '', [] );

 

hHandle := AdsTable1.AdsGetIndexHandle( Tag1 );

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsGetIndexName](ade_adsgetindexname.md)

[AdsOpenIndex](ade_adsopenindex.md)
