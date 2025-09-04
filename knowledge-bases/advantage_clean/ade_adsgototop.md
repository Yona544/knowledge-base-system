---
title: Ade Adsgototop
slug: ade_adsgototop
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgototop.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 11b175421667b66bef60e432ea8355c716f18ef2
---

# Ade Adsgototop

AdsGotoTop

TAdsTable.AdsGotoTop

Advantage TDataSet Descendant

| TAdsTable.AdsGotoTop  Advantage TDataSet Descendant |  |  |  |  |

Positions the given table to the first record.

Syntax

procedure AdsGotoTop;

Description

If no index has been set, the table is positioned at the top of its natural order. The record on which it positions is the first record starting from record 1 that satisfies current filter conditions. If an index is set, the table is positioned at the top of the current logical order, obeying both current filters and scopes.

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsGotoTop;

{ note that this method is identical to the native Delphi method First }

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.md)

[AdsGotoBottom](ade_adsgotobottom.md)

[AdsGotoRecord](ade_adsgotorecord.md)

[AdsSkip](ade_adsskip.md)
