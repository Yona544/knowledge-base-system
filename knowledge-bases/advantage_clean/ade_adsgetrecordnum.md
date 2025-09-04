---
title: Ade Adsgetrecordnum
slug: ade_adsgetrecordnum
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetrecordnum.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f189d7af7e48f2e3a19a69684f3bccc9844a09ef
---

# Ade Adsgetrecordnum

AdsGetRecordNum

TAdsTable.AdsGetRecordNum

Advantage TDataSet Descendant

| TAdsTable.AdsGetRecordNum  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the current record number.

Syntax

function AdsGetRecordNum : Longint;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TTable.GotoBookmark. See your Delphi documentation for more information about this native Delphi method.

Description

Each physical record in a table has a record number. The first physical record is number 1. All records, even deleted ones, have record numbers. The only way to change record numbers in a table is to perform an [AdsPackTable](ade_adspacktable.md).

If AdsTableOptions.AdsFilterOptions is IGNORE\_WHEN\_COUNTING, this function is very fast; the physical record number in the table is simply returned.

If AdsTableOptions.AdsFilterOptions is RESPECT\_WHEN\_COUNTING, this function will go to the first record in the table, skip through records that pass the filter, and count the records until the current record is reached. Thus, with large tables, this operation can be very slow. It is not recommended to use this function when AdsTableOptions.AdsFilterOptions is set to RESPECT\_WHEN\_COUNTING except on very small tables.

See [AdsGetKeyNum](ade_adsgetkeynum.md) to retrieve logical record numbers based on index orders.

Example

SavePlace := AdsTable1.GetBookmark;

AdsTable1.FindKey( ['Smith'] );

 

{. . .your code here. . .}

 

Adstable1.GotoBookmark( SavePlace );

See Also

[AdsGetKeyNum](ade_adsgetkeynum.md)

[AdsGotoRecord](ade_adsgotorecord.md)
