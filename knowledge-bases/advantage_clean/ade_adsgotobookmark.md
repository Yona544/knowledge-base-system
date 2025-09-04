---
title: Ade Adsgotobookmark
slug: ade_adsgotobookmark
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgotobookmark.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 67b52f3df62f8221a2a4f6d4c2b3ffceedbdb208
---

# Ade Adsgotobookmark

AdsGotoBookmark

TAdsTable.AdsGotoBookmark

Advantage TDataSet Descendant

| TAdsTable.AdsGotoBookmark  Advantage TDataSet Descendant |  |  |  |  |

Positions the given table to the given bookmark.

Syntax

procedure AdsGotoBookmark( hBookmark : Longint );

Parameter

| hBookmark | Bookmark from a call to AdsGetBookmark. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: GotoBookmark. See your Delphi documentation for more information about this native Delphi method.

Description

This function is equivalent to AdsGotoRecord. Currently, hBookmark as returned from AdsGetBookmark is the record number.

Note Explicitly moving to a deleted record when using the Advantage proprietary table format (ADT) is an illegal operation and will return the error 5022 (AE\_INVALID\_RECORD\_NUMBER), invalid record number.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

Example

AdsTable1.FindKey( [Smith] );

oBookMark := AdsTable1.GetBookmark;

AdsTable1.Next;

 

AdsTable1.GotoBookmark( oBookMark );

See Also

[AdsGetBookmark](ade_adsgetbookmark.md)

[AdsGotoRecord](ade_adsgotorecord.md)
