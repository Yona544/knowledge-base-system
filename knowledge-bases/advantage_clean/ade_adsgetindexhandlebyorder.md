---
title: Ade Adsgetindexhandlebyorder
slug: ade_adsgetindexhandlebyorder
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetindexhandlebyorder.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9b3e9b37cb92672f6cfd16a304a6378c5b97c871
---

# Ade Adsgetindexhandlebyorder

AdsGetIndexHandleByOrder

TAdsTable.AdsGetIndexHandleByOrder

Advantage TDataSet Descendant

| TAdsTable.AdsGetIndexHandleByOrder  Advantage TDataSet Descendant |  |  |  |  |

Returns the index handle indicated by an order number.

Syntax

function AdsGetIndexHandleByOrder( usOrderNum : Word ) : ADSHANDLE;

Parameter

| usOrderNum | Order number to retrieve index handle for. |

Description

This function returns the index handle corresponding to the indicated order number. The index order number is a number from 1 to the number of index orders currently open. The index orders are arranged by the order they are opened. If an index file is closed, the index orders in it are no longer available, and index orders opened after it are moved down so there is a continuous list of index orders. Note that if an AutoOpen index exits, the index orders in it are always the first ones in the order list.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

AdsTable1.AdsCreateIndex( '', 'Tag2', 'DeptNum', '', '', [] );

 

hIndex := AdsTable1.AdsGetIndexHandleByOrder( 1 );

{ hIndex is the Advantage Client Engine handle for Tag1 }

See Also

[AdsCloseIndex](ade_adscloseindex.md)

[AdsGetIndexHandle](ade_adsgetindexhandle.md)

[AdsGetIndexName](ade_adsgetindexname.md)

[AdsOpenIndex](ade_adsopenindex.md)
