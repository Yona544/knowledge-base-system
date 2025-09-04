---
title: Ade Adssetindexbyorder
slug: ade_adssetindexbyorder
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetindexbyorder.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 23fa26ef98f487258cd1c3c1e2a2ab6022392a47
---

# Ade Adssetindexbyorder

AdsSetIndexByOrder

TAdsTable.AdsSetIndexByOrder

Advantage TDataSet Descendant

| TAdsTable.AdsSetIndexByOrder  Advantage TDataSet Descendant |  |  |  |  |

Set the active index via an order number.

Syntax

procedure TAdsTable.AdsSetIndexByOrder( usOrderNum: Word );

Parameter

| usOrderNum | The order number. 0 means natural order. |

Description

This function sets the IndexName property of TAdsTable to the name of the index indicated by the order number. If usOrderNum is zero, no index is active. The index order number is a number from 1 to the number of index orders currently open. The index orders are arranged by the order they are opened. If an index file is closed, the index orders in it are no longer available, and index orders opened after it are moved down so there is a continuous list of index orders.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

AdsTable1.AdsCreateIndex( '', 'Tag2', 'DeptNum', '', '', [] );

 

AdsTAble1.AdsSetIndexByOrder( 2 );

{ tag2 is now the current index }

See Also

[AdsCloseIndex](ade_adscloseindex.md)

[AdsGetIndexHandle](ade_adsgetindexhandle.md)

[AdsGetIndexName](ade_adsgetindexname.md)

[AdsOpenIndex](ade_adsopenindex.md)
