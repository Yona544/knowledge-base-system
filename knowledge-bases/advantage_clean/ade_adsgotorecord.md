---
title: Ade Adsgotorecord
slug: ade_adsgotorecord
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgotorecord.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: e29f01140c2f04f58e22e43c0afd765b54bf3ab6
---

# Ade Adsgotorecord

AdsGotoRecord

TAdsTable.AdsGotoRecord

Advantage TDataSet Descendant

| TAdsTable.AdsGotoRecord  Advantage TDataSet Descendant |  |  |  |  |

Positions the given table to the given record number.

Syntax

procedure AdsGotoRecord( ulRecNum : Longint );

Parameter

| ulRecNum | Record number to goto. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TTable.GotoBookmark. See your Delphi documentation for more information about this native Delphi method.

 

Note Explicitly moving to a deleted record when using the Advantage proprietary table format (ADT) is an illegal operation and will return the error 5022 (AE\_INVALID\_RECORD\_NUMBER), invalid record number.

Description

AdsGotoRecord ignores filters, relations, and scopes. If ulRec is zero, the client will be unpositioned (EOF and BOF will be set), and the current record number will be set to 0. If ulRec is greater than the number of records in the table, the client will be unpositioned (EOF and BOF will be set), and the current record number will be set to the number of records in the table + 1.

Example

SavePlace := AdsTable1.GetBookmark;

AdsTable1.FindKey( ['Smith'] );

 

{. . .your code here. . .}

 

Adstable1.GotoBookmark( SavePlace );

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.md)

[AdsGotoBottom](ade_adsgotobottom.md)

[AdsGotoTop](ade_adsgototop.md)

[AdsSkip](ade_adsskip.md)

[AdsWriteRecord](ade_adswriterecord.md)
