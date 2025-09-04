---
title: Ade Adslookupkey
slug: ade_adslookupkey
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adslookupkey.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3eb9edb88c3226839b463e1bda18f7ff1eefad00
---

# Ade Adslookupkey

AdsLookupKey

TAdsTable.AdsLookupKey

Advantage TDataSet Descendant

| TAdsTable.AdsLookupKey  Advantage TDataSet Descendant |  |  |  |  |

Performs an indexed search on the given table using the given index order to determine if a key exists in the index. Scopes and filters are ignored.

Syntax

function AdsLookupKey( const strTag, strKey : string ) : boolean;

Parameters

| strTag | Name of tag to search. |
| strKey | Search key. |

Description

AdsLookupKey determines if a key exists in the index. It does not perform any record movement. This function may be used to determine if a key value can be added to a unique index. See [AdsCreateIndex](ade_adscreateindex.md) for information about unique indexes.

Example

AdsTable1.IndexName := FirstName;

bFound := AdsTable1.AdsLookupKey( 'LastName', 'Smith' );

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsSeek](ade_adsseek.md)
