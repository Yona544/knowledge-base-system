---
title: Ade Adsdeleteindex
slug: ade_adsdeleteindex
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsdeleteindex.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 82898c6924a71f7a713e77d84e981b2de55cabe6
---

# Ade Adsdeleteindex

AdsDeleteIndex

TAdsTable.AdsDeleteIndex

Advantage TDataSet Descendant

| TAdsTable.AdsDeleteIndex  Advantage TDataSet Descendant |  |  |  |  |

Deletes the given index order.

Syntax

procedure AdsDeleteIndex( strTag : String );

Parameter

| strTag | Tag of index order to delete. If it is the only index order (tag) in a compound index file or if it is an index order in a non-compound index file, the file will be deleted as well. |

Description

If the index order is a tag in a CDX or ADI, it will be removed. If it is the last tag in the index, the file will be deleted. If the index order is an IDX or NTX, the file will be deleted.

Note It is illegal to delete an index order during a transaction.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', '', '', [] );

 

{. . . your code here . . .}

 

AdsTable1.AdsDeleteIndex( 'Tag1' );

 

See Also

[AdsCloseIndex](ade_adscloseindex.md)

[AdsCreateIndex](ade_adscreateindex.md)

[AdsOpenIndex](ade_adsopenindex.md)
