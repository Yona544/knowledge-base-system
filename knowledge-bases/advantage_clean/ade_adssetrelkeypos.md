---
title: Ade Adssetrelkeypos
slug: ade_adssetrelkeypos
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetrelkeypos.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 89a27c77bdaf476070c87ff0d9d10ab1ebc9de99
---

# Ade Adssetrelkeypos

AdsSetRelKeyPos

TAdsTable/TAdsQuery.AdsSetRelKeyPos

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsSetRelKeyPos  Advantage TDataSet Descendant |  |  |  |  |

Sets the current record to the given relative position in the given index order.

Syntax

procedure AdsSetRelKeyPos( dPos : Double );

Parameter

| dPos | Set relative key positions. The value specified in the dPos parameter must be in the range from 0.0 to 1.0, where 0.0 would indicate the top of the index and 1.0 refers to the bottom. |

Description

AdsSetRelKeyPos approximates the position in the index order based on the given value. If there is a scope set, AdsSetRelKeyPos calculates and sets the relative position relative to the current scope.

Example

AdsTable1.Active := TRUE;

{ go to the approximate center of the current index }

AdsTable1.AdsSetRelKeyPos( 0.50 );

See Also

[AdsGetKeyCount](ade_adsgetkeycount.md)

[AdsGetRelKeyPos](ade_adsgetrelkeypos.md)

[AdsGotoRecord](ade_adsgotorecord.md)
