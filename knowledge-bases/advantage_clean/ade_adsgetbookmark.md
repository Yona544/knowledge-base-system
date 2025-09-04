---
title: Ade Adsgetbookmark
slug: ade_adsgetbookmark
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetbookmark.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: caccf550bc8189ce73f050bb9769c49f98aad0fd
---

# Ade Adsgetbookmark

AdsGetBookmark

TAdsTable.AdsGetBookmark

Advantage TDataSet Descendant

| TAdsTable.AdsGetBookmark  Advantage TDataSet Descendant |  |  |  |  |

Retrieves a bookmark for a later call to AdsGotoBookmark.

Syntax

function AdsGetBookmark : Longint;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: GetBookmark. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetBookmark returns the physical record number. It is the equivalent of AdsGetRecordNum called with IGNORE \_WHEN\_COUNTING.

Example

AdsTable1.FindKey( [Smith] );

oBookMark := AdsTable1.GetBookmark;

AdsTable1.Next;

 

AdsTable1.GotoBookmark( oBookMark );

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.md)

[AdsGotoBookmark](ade_adsgotobookmark.md)

[AdsGotoRecord](ade_adsgotorecord.md)
