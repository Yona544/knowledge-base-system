---
title: Ade Adsgotobottom
slug: ade_adsgotobottom
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgotobottom.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: c242acec87b999ac8e4b40e15e9aa49436edfb7c
---

# Ade Adsgotobottom

AdsGotoBottom

TAdsTable.AdsGotoBottom

Advantage TDataSet Descendant

| TAdsTable.AdsGotoBottom  Advantage TDataSet Descendant |  |  |  |  |

Positions the given table to the last record.

Syntax

procedure AdsGotoBottom;

Description

If no index has been set, the table is positioned at the last record in natural order, obeying the current filter. If an index is set, the table is positioned at the last logical record in the order that passes both filters or scopes that are set.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsGotoBottom;

{ this function is identical to AdsTable1.Last }

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.md)

[AdsGotoRecord](ade_adsgotorecord.md)

[AdsGotoTop](ade_adsgototop.md)

[AdsSkip](ade_adsskip.md)
